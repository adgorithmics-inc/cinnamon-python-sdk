import time
import pydash
import json
import requests
import copy
from typing import Union, List, Any, Iterable
from enum import Enum
from requests import Response

from .constants import (
    CinnamonUndefined,
    VENDOR_TOKEN_LENGTH,
    GraphQLCodes,
    GraphQLRetryableCodes,
    CONNECTION_EXCEPTIONS,
    FilterInput,
)
from .exceptions import CinnamonException


class BaseCinnamonScalar:
    type_hint: str

    @staticmethod
    def decode(api_value: Any) -> Any:
        raise NotImplementedError

    @staticmethod
    def encode(python_value: Any) -> Any:
        raise NotImplementedError


class BaseCinnamonObject:
    class _API_FIELDS:
        pass

    def __init__(self, api_object: dict) -> None:
        for api_key, api_value in api_object.items():
            field = getattr(self._API_FIELDS, api_key, None)
            if not field:
                continue
            setattr(self, field.python_name, field.get_python_value(api_value))

    def __str__(self) -> str:
        s = self.__class__.__name__
        if getattr(self, "id", None):
            s += f" {self.id}"
        if getattr(self, "name", None):
            s += f": {self.name}"
        return s


class BaseCinnamonField:
    api_name: str
    api_kind: str
    api_kind_name: str
    not_null: bool
    python_iterable: Any
    python_name: str
    python_default_value: Any
    scalar: Union[BaseCinnamonScalar, None] = None
    obj: Union[BaseCinnamonObject, None] = None

    @classmethod
    def __str__(cls) -> str:
        return (
            f"<{cls.__name__} - {cls.api_name} - {cls.api_kind} - {cls.api_kind_name}>"
        )

    @classmethod
    def __repr__(cls) -> str:
        return str(cls)

    @classmethod
    def _get_core_value(cls, value: Any) -> Any:
        if cls.scalar:
            return cls.scalar.decode(value)
        elif cls.obj:
            return cls.obj(value)
        else:
            return value

    @classmethod
    def get_python_value(cls, api_value: Any) -> Any:
        if cls.python_iterable and api_value is not None:
            return cls.python_iterable(
                cls._get_core_value(value) for value in api_value
            )
        return cls._get_core_value(api_value)


class BaseCinnamonFieldsEnum:
    @classmethod
    def _default_fields(cls) -> List[str]:
        return [
            getattr(cls, field)
            for field in dir(cls)
            if isinstance(getattr(cls, field), str) and not field.startswith("_")
        ]


class BaseCinnamonInput:
    class _PYTHON_ARGS:
        pass

    _api_dict: dict

    def __init__(self, **kwargs) -> None:
        self._api_dict = {}
        for python_key, value in kwargs.items():
            if python_key == "self" or python_key.startswith("_"):
                continue
            if value == CinnamonUndefined:
                continue
            if isinstance(value, Enum):
                value = value.value
            api_field = getattr(self._FIELDS, python_key, None)
            if not api_field:
                continue
            self._api_dict[api_field.api_name] = value
            setattr(self, python_key, value)

    @property
    def api_dict(self) -> dict:
        return copy.deepcopy(self._api_dict)


class BaseCinnamon:
    url = None
    max_retry = None
    retry_sleep_time = None
    refresh_token = None
    token = None
    retry_count = 0

    def __init__(
        self,
        url: str,
        max_retry: int = 3,
        retry_sleep_time: float = 0.5,
        token: str = None,
        refresh_token: str = None,
    ) -> None:
        self.url = url
        self.max_retry = max_retry
        self.retry_sleep_time = retry_sleep_time
        self.token = token
        self.refresh_token = refresh_token
        self.retry_count = 0

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.url}>"

    @staticmethod
    def is_vendor_token(token: str) -> bool:
        return len(token) == VENDOR_TOKEN_LENGTH

    def _network_request(self, url: str, headers: dict, body: str) -> Response:
        raise NotImplementedError

    def _refresh_login(self) -> None:
        result = self._api(
            """
            mutation($input: RefreshTokenInput!) {
                refreshLogin(input: $input) {
                    token
                    refreshToken
                }
            }
            """
        )["data"]["refreshLogin"]

        if result["token"] and result["refreshToken"]:
            self.token = result.token
            self.refresh_token = result.refresh_token

        return result

    def _api(
        self,
        query: str,
        variables: Union[dict, None] = None,
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> dict:
        try:
            send_headers = {
                "authorization": f"Bearer {token or self.token}"
                if token or self.token
                else "",
                "accept": "application/json",
                "content-type": "application/json",
            }
            if headers:
                send_headers.update(headers)
            data = {
                "query": query,
            }
            if variables:
                data["variables"] = variables
            response = self._network_request(
                url=self.url, headers=send_headers, data=json.dumps(data),
            )

            try:
                json_response = response.json()
            except ValueError:
                raise CinnamonException(
                    message=f"Invalid server response: {response.text}",
                    query=query,
                    variables=variables,
                    headers=headers,
                    token=token,
                    response=response,
                )

            if json_response.get("errors"):
                if any(
                    pydash.get(error, "extensions.code") == GraphQLCodes.TOKEN_EXPIRED
                    for error in json_response["errors"]
                ):
                    self._refresh_login()
                    return self._api(query, variables, headers, token)

                raise CinnamonException(
                    message="\n".join(
                        f"{err['message']}" for err in json_response["errors"]
                    ),
                    query=query,
                    variables=variables,
                    headers=headers,
                    token=token,
                    response=response,
                )

            return json_response
        except CinnamonException as error:
            if self.retry_count >= self.max_retry:
                raise
            if error.response_json and any(
                GraphQLRetryableCodes.is_retryable(pydash.get(error, "extensions.code"))
                for error in error.response_json.get("errors")
            ):
                return self._retry(query, variables, headers, token, error)
            raise
        except CONNECTION_EXCEPTIONS as error:
            if self.retry_count >= self.max_retry:
                raise
            return self._retry(query, variables, headers, token, error)

    def _retry(
        self,
        query: str,
        variables: dict,
        headers: dict,
        token: str,
        exception: Exception,
    ) -> Response:
        raise NotImplementedError

    def _query_builder(
        self,
        query_type: str,
        api_call: str,
        fields: list,
        arguments: dict,
        argument_legend: Any,
        is_paged: bool,
    ) -> dict:
        fields_str = ""
        for field in fields:
            if isinstance(field, Enum):
                fields_str += field.value + " "
            elif isinstance(field, str):
                fields_str += field + " "
            else:
                raise ValueError(f"Invalid field: {field}")

        query_vars = []
        call_vars = []
        encoded_args = {}
        for arg_name, arg_value in arguments.items():
            if arg_value == CinnamonUndefined:
                continue
            arg_type = getattr(argument_legend, arg_name)
            query_vars.append(f"${arg_type.api_name}: {arg_type.api_kind_name}!")
            call_vars.append(f"{arg_type.api_name}: ${arg_type.api_name}")
            if isinstance(arg_value, (BaseCinnamonInput, FilterInput)):
                encoded_args[arg_name] = arg_value.api_dict
            else:
                encoded_args[arg_name] = arg_value

        if is_paged:
            fields_str += "pageInfo{endCursor hasNextPage} "
            query_vars.append("$after: String")
            call_vars.append("after: $after")

        return {
            "query": f"{query_type}({','.join(query_vars)}) {{ {api_call}({','.join(call_vars)}) {{ {fields_str} }} }}",
            "variables": encoded_args,
        }

    def api(
        self,
        query: str,
        variables: dict = None,
        headers: dict = None,
        token: str = None,
    ) -> Response:
        self.retry_count = 0
        return self._api(query, variables, headers, token)

    def login(self, email, password) -> dict:
        result = self.api(
            query=str(
                "mutation($input: UserLoginInput!) {"
                "   login(input: $input) {"
                "       token, refreshToken"
                "   }"
                "}"
            ),
            variables={"input": {"email": email, "password": password}},
        )["data"]["login"]
        self.token = result["token"]
        self.refresh_token = result["refreshToken"]
        return result

    def iterate_edges(
        self,
        base_obj: BaseCinnamonObject,
        query_args: dict,
        headers: dict,
        token: str,
        query_name: str,
    ) -> Iterable:
        page = base_obj(
            self.api(headers=headers, token=token, **query_args)["data"][query_name]
        )
        for edge in page.edges:
            yield edge.node
        if hasattr(page, "page_info") and page.page_info.has_next_page:
            while page.page_info.has_next_page:
                query_args["variables"]["after"] = page.page_info.end_cursor
                page = base_obj(
                    self.api(headers=headers, token=token, **query_args)["data"][
                        query_name
                    ]
                )
                for edge in page.edges:
                    yield edge.node


class BaseSyncCinnamon(BaseCinnamon):
    def _network_request(self, url: str, headers: dict, data: str) -> Response:
        return requests.post(url=url, data=data, headers=headers)

    def _retry(
        self,
        query: str,
        variables: dict,
        headers: dict,
        token: str,
        exception: Exception,
    ) -> dict:
        time.sleep(self.retry_sleep_time)
        self.retry_count += 1
        return self._api(query, variables, headers, token)

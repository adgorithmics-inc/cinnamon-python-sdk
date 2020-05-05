import time
import pydash
import json
import requests
import copy
from typing import Union, Any, Iterable
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
from .json_codecs import CinnamonJSONEncoder


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

    def _to_dict(self, assign_key: str) -> dict:
        to_return = {}
        for key in dir(self._API_FIELDS):
            if key.startswith("__"):
                continue

            field = getattr(self._API_FIELDS, key)
            value = getattr(self, field.python_name, None)
            write_value = None
            if isinstance(value, BaseCinnamonObject):
                write_value = value.to_dict()
            elif isinstance(value, (str, int, float)):
                write_value = value
            if write_value:
                to_return[getattr(field, assign_key)] = write_value
        return to_return

    def to_dict(self) -> dict:
        return self._to_dict("python_name")

    def to_api_dict(self) -> dict:
        return self._to_dict("api_name")


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

    def _network_request(self, url: str, headers: dict, data: str) -> Response:
        raise NotImplementedError

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
                url=self.url,
                headers=send_headers,
                data=json.dumps(data, cls=CinnamonJSONEncoder),
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
                    self.refresh_login()
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

    def _field_tree_recursion(self, branch_name: str, branch: dict) -> str:
        fields = []
        for leaf_name, leaf in branch.items():
            if isinstance(leaf, dict):
                fields.append(self._field_tree_recursion(leaf_name, leaf))
            else:
                fields.append(leaf_name)
        fields_str = " ".join(fields)
        if branch_name:
            return f"{branch_name}{{{fields_str}}}"
        return fields_str + " "

    def _query_builder(
        self,
        query_type: str,
        api_call: str,
        fields: list,
        arguments: dict,
        argument_legend: Any,
        is_paged: bool,
    ) -> dict:
        fields_list = []
        fields_tree = {}
        for field in fields:
            if isinstance(field, Enum):
                fields_list.append(field.value)
            elif isinstance(field, QueryField):
                pydash.set_(fields_tree, str(field), field)
            elif isinstance(field, QueryFieldSet):
                for default_field in field._sdk_default_fields:
                    pydash.set_(fields_tree, str(field), field)
            elif isinstance(field, str):
                fields_list.append(field)
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
                encoded_args[arg_type.api_name] = arg_value.api_dict
            else:
                encoded_args[arg_type.api_name] = arg_value

        if is_paged:
            pydash.set_(fields_tree, "pageInfo.endCursor", QueryField("endCursor"))
            pydash.set_(fields_tree, "pageInfo.hasNextPage", QueryField("hasNextPage"))
            query_vars.append("$after: String")
            call_vars.append("after: $after")

        if fields_tree:
            fields_list.append(self._field_tree_recursion("", fields_tree))

        fields_str = " ".join(fields_list)

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

    def login(self, email: str, password: str) -> dict:
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

    def refresh_login(self, refresh_token: str = None) -> dict:
        result = self._api(
            """
            mutation($input: RefreshTokenInput!) {
                refreshLogin(input: $input) {
                    token
                    refreshToken
                }
            }
            """,
            variables={"input": {"refreshToken": refresh_token or self.refresh_token}},
        )["data"]["refreshLogin"]

        if result["token"] and result["refreshToken"]:
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


class QueryField:
    def __init__(self, api_name, prefix=""):
        self.api_name = api_name
        self.prefix = prefix

    def __str__(self):
        return f"{self.prefix}{self.api_name}"


class QueryFieldSet:
    _sdk_prefix: str
    _sdk_is_paged: bool
    _sdk_default_fields: list
    _sdk_default_field_names: list

    def __init__(self, prefix: str = "") -> None:
        self._sdk_prefix = prefix
        self._sdk_is_paged = prefix.endswith("edges.node.")
        if self.__class__ != QueryFieldSet:
            self._sdk_default_fields = [
                getattr(self, field) for field in self._sdk_default_field_names
            ]

    def __getattribute__(self, name: str) -> Any:
        attrib = super().__getattribute__(name)
        if isinstance(attrib, QueryField):
            return QueryField(attrib.api_name, self._sdk_prefix)
        return attrib

    def _sdk_embed(self, child_class: "QueryFieldSet", prefix: str) -> "QueryFieldSet":
        return child_class(
            prefix=f"{self._sdk_prefix}{prefix}" if self._sdk_prefix else prefix
        )

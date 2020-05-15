import pydash
import re
import json
from requests import Response
from typing import List

from .json_codecs import CinnamonJSONEncoder

PRETTY_JSON_INDENT = 2


class CinnamonException(Exception):
    message: str = ""
    query: str = ""
    variables: dict = {}
    headers: dict = {}
    token: str = ""
    response: Response = Response()
    response_json: dict = {}
    error_codes: List[str] = []

    def __init__(
        self,
        message: str,
        query: str,
        variables: dict,
        headers: dict,
        token: str,
        response: Response,
    ) -> None:
        self.message = message
        self.query = query
        self.variables = variables
        self.headers = headers
        self.token = token
        self.response = response
        self.response_json = None
        self.error_codes = []
        try:
            self.response_json = response.json() if response else None
            if isinstance(self.response_json, dict) and isinstance(self.response_json.get("errors"), list):
                for error in self.response_json["errors"]:
                    code = pydash.get(error, "extensions.code", None)
                    if code is not None:
                        self.error_codes.append(code)
        except ValueError:
            pass

    def __str__(self) -> str:
        return self.debug_message()

    @classmethod
    def _pretty_indent(cls, lines: str) -> str:
        if not lines:
            return ""
        return "\n".join(f"  {line}" for line in lines.split("\n"))

    @classmethod
    def _pretty_json(cls, dct: dict) -> str:
        if not dct:
            return ""
        return cls._pretty_indent(
            json.dumps(
                dct,
                sort_keys=True,
                indent=PRETTY_JSON_INDENT,
                ensure_ascii=False,
                cls=CinnamonJSONEncoder,
            )
        )

    def debug_message(self) -> str:
        s = str(
            f"Cinnamon Exception: {self.message}\n"
            "--------------------" + ("-" * len(self.message)) + "\n"
        )
        if self.query:
            query = self._pretty_indent(re.sub(r"\s+", " ", self.query))
            s += str("Query:\n" f"{query}\n" "\n")
        if self.variables:
            variables = self._pretty_json(self.variables)
            s += str("Variables:\n" f"{variables}\n" "\n")
        if self.headers:
            headers = self._pretty_json(self.headers)
            s += str("Headers:\n" f"{headers}\n" "\n")
        if self.response:
            response = (
                self._pretty_json(self.response_json)
                if self.response_json
                else self._pretty_indent(self.response.text if self.response else None)
            )
            s += str("Response:\n" f"{response}\n" "\n")
        return s

import datetime
import dateutil.parser

from .base_classes import BaseCinnamonScalar
from .json_codecs import datetime_encoder


class ObjectId(BaseCinnamonScalar):
    type_hint = "str"

    @staticmethod
    def decode(api_value: str) -> str:
        return api_value

    @staticmethod
    def encode(python_value: str) -> str:
        return python_value


class DateISO(BaseCinnamonScalar):
    type_hint = "datetime"

    @staticmethod
    def decode(api_value: str) -> datetime.datetime:
        if api_value:
            return dateutil.parser.parse(api_value)
        return None

    @staticmethod
    def encode(python_value: datetime.datetime) -> str:
        return datetime_encoder(python_value)


class NonEmptyString(BaseCinnamonScalar):
    type_hint = "str"

    @staticmethod
    def decode(api_value: str) -> str:
        return api_value

    @staticmethod
    def encode(python_value: str) -> str:
        return python_value


class JSONObject(BaseCinnamonScalar):
    type_hint = "dict"

    @staticmethod
    def decode(api_value: dict) -> dict:
        return api_value

    @staticmethod
    def encode(python_value: dict) -> dict:
        return python_value


class FilterInput(BaseCinnamonScalar, dict):
    type_hint = "dict"

    @staticmethod
    def decode(api_value: dict) -> dict:
        return api_value

    @staticmethod
    def encode(python_value: dict) -> dict:
        return python_value


class String(BaseCinnamonScalar):
    type_hint = "str"

    @staticmethod
    def decode(api_value: str) -> str:
        return api_value

    @staticmethod
    def encode(python_value: str) -> str:
        return python_value


class Int(BaseCinnamonScalar):
    type_hint = "int"

    @staticmethod
    def decode(api_value: int) -> int:
        return api_value

    @staticmethod
    def encode(python_value: int) -> int:
        return python_value


class Boolean(BaseCinnamonScalar):
    type_hint = "bool"

    @staticmethod
    def decode(api_value: bool) -> bool:
        return api_value

    @staticmethod
    def encode(python_value: bool) -> bool:
        return python_value


class Float(BaseCinnamonScalar):
    type_hint = "float"

    @staticmethod
    def decode(api_value: float) -> float:
        return api_value

    @staticmethod
    def encode(python_value: float) -> float:
        return python_value

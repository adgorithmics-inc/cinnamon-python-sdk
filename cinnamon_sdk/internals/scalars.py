import datetime
import pytz
import dateutil.parser
import enum

from .base_classes import BaseCinnamonScalar


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
        return dateutil.parser.parse(api_value)

    @staticmethod
    def encode(python_value: datetime.datetime) -> str:
        return python_value.astimezone(pytz.UTC).isoformat()


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


class FilterOperator(enum.Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    ICONTAINS = "ICONTAINS"
    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"
    IN = "IN"
    IS_NULL = "IS NULL"


class FilterInput(BaseCinnamonScalar, dict):
    type_hint = "dict"

    @staticmethod
    def decode(api_value: dict) -> dict:
        return api_value

    @staticmethod
    def encode(python_value: dict) -> dict:
        return python_value

    def __init__(self, field: str, operator: FilterOperator, value: any):
        self["field"] = field
        self["operator"] = operator.value
        self["value"] = value


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

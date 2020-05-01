import typing
import requests
from enum import Enum

VENDOR_TOKEN_LENGTH = 60

CONNECTION_EXCEPTIONS = (
    requests.exceptions.SSLError,
    requests.exceptions.Timeout,
    requests.exceptions.ConnectTimeout,
    requests.exceptions.ReadTimeout,
    requests.exceptions.ChunkedEncodingError,
    requests.exceptions.ConnectionError,
    ConnectionError,
)


class GraphQLCodes(Enum):
    OBJECT_DUPLICATE = ("OBJECT_DUPLICATE",)
    OBJECT_NOT_FOUND = ("OBJECT_NOT_FOUND",)
    OBJECT_IMMUTABLE = ("OBJECT_IMMUTABLE",)
    TOKEN_EXPIRED = ("TOKEN_EXPIRED",)
    TOKEN_MALFORMED = ("TOKEN_MALFORMED",)
    INVALID_REFRESH_TOKEN = ("INVALID_REFRESH_TOKEN",)
    TOKEN_MISSING = ("TOKEN_MISSING",)
    ACCESS_DENIED = ("ACCESS_DENIED",)
    INVALID_CREDENTIALS = ("INVALID_CREDENTIALS",)
    QUERY_DEPTH_EXCEEDED = ("QUERY_DEPTH_EXCEEDED",)
    QUERY_COMPLEXITY_EXCEEDED = ("QUERY_COMPLEXITY_EXCEEDED",)
    QUERY_BREADTH_EXCEEDED = ("QUERY_BREADTH_EXCEEDED",)
    INPUT_LIST_EMPTY = ("INPUT_LIST_EMPTY",)
    INPUT_LIST_MIN = ("INPUT_LIST_MIN",)
    INPUT_LIST_MAX = ("INPUT_LIST_MAX",)
    INPUT_INVALID = ("INPUT_INVALID",)
    UNKNOWN_ERROR = ("UNKNOWN_ERROR",)
    MAX_PAYLOAD_EXCEEDED = ("MAX_PAYLOAD_EXCEEDED",)
    UNDER_MAINTENANCE = "UNDER_MAINTENANCE"


class GraphQLRetryableCodes(Enum):
    @classmethod
    def is_retryable(cls, code: str) -> bool:
        try:
            cls(code)
            return True
        except ValueError:
            return False


class CinnamonUndefined:
    @classmethod
    def __nonzero__(cls) -> bool:
        return False

    @classmethod
    def __bool__(cls) -> bool:
        return False

    @classmethod
    def __str__(cls) -> bool:
        return cls.__name__

    @classmethod
    def __repr__(cls) -> bool:
        return cls.__name__


class FilterOperator(Enum):
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


class FilterInput:
    field: str
    operator: FilterOperator
    value: typing.Any

    def __init__(self, field: str, operator: FilterOperator, value: any) -> None:
        self.field = field
        self.operator = operator
        self.value = value

    @property
    def api_dict(self) -> dict:
        return {
            "field": self.field,
            "operator": self.operator.value,
            "value": self.value,
        }

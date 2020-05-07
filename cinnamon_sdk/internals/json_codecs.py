import json
import datetime
import pytz
from enum import Enum


def datetime_encoder(dt: datetime.datetime) -> str:
    if isinstance(dt, datetime.datetime):
        return dt.astimezone(pytz.UTC).replace(tzinfo=None).isoformat() + "Z"
    return dt


class CinnamonJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return datetime_encoder(obj)
        if isinstance(obj, Enum):
            return obj.value
        return json.JSONEncoder.default(self, obj)

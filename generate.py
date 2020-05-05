# flake8: noqa

import os

from cinnamon_sdk.internals.generate import PythonCodeGenerator, get_schema

print("Collecting schema...")
generator = PythonCodeGenerator(
    get_schema(
        url=os.environ.get("CINNAMON_PYTHON_SDK_URL"),
        email=os.environ.get("CINNAMON_PYTHON_SDK_EMAIL"),
        password=os.environ.get("CINNAMON_PYTHON_SDK_PASSWORD"),
    )
)

print("Updating objects.py...")
objects_filename = os.path.join("cinnamon_sdk", "objects.py")
with open(objects_filename, mode="w") as f:
    f.write("from typing import Union, List, Any\n")
    f.write("from datetime import datetime\n")
    f.write(
        "from .internals.base_classes import BaseCinnamonObject, BaseCinnamonEdgesObject, BaseCinnamonField\n"
    )
    f.write("from .internals.constants import CinnamonUndefined\n")
    f.write("from .internals import scalars\n")
    f.write("from . import enums\n\n")
    f.write(generator.object_classes())

print("Updating fields.py...")
fields_filename = os.path.join("cinnamon_sdk", "fields.py")
with open(fields_filename, mode="w") as f:
    f.write("from functools import lru_cache\n")
    f.write("from .internals.base_classes import QueryFieldSet, QueryField\n\n")
    f.write(generator.fields_classes())

print("Updating inputs.py...")
inputs_filename = os.path.join("cinnamon_sdk", "inputs.py")
with open(inputs_filename, mode="w") as f:
    f.write("from typing import Union, List\n\n")
    f.write(
        "from .internals.base_classes import BaseCinnamonInput, BaseCinnamonField\n"
    )
    f.write("from .internals.constants import CinnamonUndefined\n")
    f.write("from .internals import scalars\n")
    f.write("from . import enums\n\n")
    f.write(generator.input_object_classes())

print("Updating enums.py...")
enums_filename = os.path.join("cinnamon_sdk", "enums.py")
with open(enums_filename, mode="w") as f:
    f.write("from enum import Enum\n\n")
    f.write(generator.enums())

print("Updating cinnamon.py...")
functions_filename = os.path.join("cinnamon_sdk", "cinnamon.py")
with open(functions_filename, mode="w") as f:
    f.write("from typing import Union, List, Iterable\n")
    f.write("from datetime import datetime\n")
    f.write(
        "from .internals.base_classes import BaseSyncCinnamon, BaseCinnamonField, QueryFieldSet, QueryField\n"
    )
    f.write("from .internals.constants import CinnamonUndefined\n")
    f.write("from .internals import scalars\n")
    f.write("from . import fields as fields_module\n")
    f.write("from . import objects\n")
    f.write("from . import inputs\n\n")
    f.write(generator.api_class("Cinnamon"))
    f.write("\n\n")
    f.write("__all__ = ['Cinnamon']\n")

print("Done.\n")

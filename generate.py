# flake8: noqa

import os
import black

BLACK_MODE = black.FileMode()

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
    objects_code = "from typing import Union, List, Any\n"
    objects_code += "from datetime import datetime\n"
    objects_code += "from .internals.base_classes import BaseCinnamonObject, BaseCinnamonEdgesObject, BaseCinnamonField\n"

    objects_code += "from .internals.constants import CinnamonUndefined\n"
    objects_code += "from .internals import scalars\n"
    objects_code += "from . import enums\n\n"
    objects_code += generator.object_classes()
    f.write(black.format_str(objects_code, mode=BLACK_MODE))

print("Updating fields.py...")
fields_filename = os.path.join("cinnamon_sdk", "fields.py")
with open(fields_filename, mode="w") as f:
    fields_code = "from functools import lru_cache\n"
    fields_code += "from .internals.base_classes import QueryFieldSet, QueryField\n\n"
    fields_code += generator.fields_classes()
    f.write(black.format_str(fields_code, mode=BLACK_MODE))

print("Updating inputs.py...")
inputs_filename = os.path.join("cinnamon_sdk", "inputs.py")
with open(inputs_filename, mode="w") as f:
    inputs_code = "from typing import Union, List\n\n"
    inputs_code += (
        "from .internals.base_classes import BaseCinnamonInput, BaseCinnamonField\n"
    )
    inputs_code += "from .internals.constants import CinnamonUndefined\n"
    inputs_code += "from .internals import scalars\n"
    inputs_code += "from . import enums\n\n"
    inputs_code += generator.input_object_classes()
    f.write(black.format_str(inputs_code, mode=BLACK_MODE))

print("Updating enums.py...")
enums_filename = os.path.join("cinnamon_sdk", "enums.py")
with open(enums_filename, mode="w") as f:
    enums_code = "from enum import Enum\n\n"
    enums_code += generator.enums()
    f.write(black.format_str(enums_code, mode=BLACK_MODE))

print("Updating cinnamon.py...")
functions_filename = os.path.join("cinnamon_sdk", "cinnamon.py")
with open(functions_filename, mode="w") as f:
    cinna_code = "from typing import Union, List, Iterable\n"
    cinna_code += "from datetime import datetime\n"
    cinna_code += "from .internals.base_classes import BaseSyncCinnamon, BaseCinnamonField, QueryFieldSet, QueryField\n"
    cinna_code += "from .internals.constants import CinnamonUndefined\n"
    cinna_code += "from .internals import scalars\n"
    cinna_code += "from . import fields as fields_module\n"
    cinna_code += "from . import objects\n"
    cinna_code += "from . import inputs\n\n"
    cinna_code += generator.api_class("Cinnamon")
    cinna_code += "\n\n"
    cinna_code += "__all__ = ['Cinnamon']\n"
    f.write(black.format_str(cinna_code, mode=BLACK_MODE))

print("Done.\n")

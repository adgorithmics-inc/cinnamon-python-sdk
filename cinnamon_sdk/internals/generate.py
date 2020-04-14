import re
import typing
import itertools
import black
from enum import Enum
from typing import List

from .base_classes import BaseSyncCinnamon, BaseCinnamonField
from . import scalars


QUERY_NAMES = ["Query", "Mutation"]
PRE_CAMEL_REPLACEMENTS = [("GCPX", "Gcpx")]
ITERABLE_TO_TYPE_HINT = {
    list: "List",
}
BLACK_MODE = black.FileMode()
MAX_COMPLEXITY = 3
EXCLUDE_QUERIES = ["login"]
PAGING_ARGUMENTS = ["first", "last", "after", "before"]


def camel_to_snake(label: str) -> str:
    if label is None:
        return None
    s = label
    for (replace_what, replace_with) in PRE_CAMEL_REPLACEMENTS:
        s = s.replace(replace_what, replace_with)
    return "_".join(part.lower() for part in re.findall("[_a-zA-Z][^A-Z]*", s))


class CinnamonToPythonType(BaseCinnamonField):
    CINNAMON_TO_PYTHON_TYPE_CONVERSION = {
        "api_name": lambda t: t.get("name"),
        "api_kind": lambda t: t.get("kind"),
        "api_kind_name": lambda t: t.get("name"),
        "not_null": lambda t: False,
        "python_name": lambda t: camel_to_snake(t.get("name")),
        "python_iterable": lambda t: None,
        "python_default_value": lambda t: None,
    }

    python_iterable: typing.Any
    root: dict

    @classmethod
    def solve(cls, root: dict = None, gql_type: typing.Any = None):
        if root is None and gql_type is None:
            raise ValueError("Must initialize a CinnamonToPythonType with data.")

        if root is None:
            root = {}

        if gql_type is None:
            gql_type = cls(**root)

        if "name" in root and "type" in root:
            return cls.solve(root["type"], gql_type)

        if "defaultValue" in root:
            if root["defaultValue"] == "false":
                gql_type.default_value = False
            elif root["defaultValue"] == "true":
                gql_type.default_value = True
            elif root["defaultValue"] is None:
                gql_type.default_value = "None"
            elif root["defaultValue"]:
                gql_type.default_value = root["defaultValue"]
            elif not gql_type.not_null:
                raise ValueError(
                    f"Function {gql_type.name} does not know how to assign default value for argument {gql_type.name}: {repr(root['defaultValue'])}"
                )

        if root.get("kind") == "LIST":
            gql_type.python_iterable = list
        elif root.get("kind") == "NON_NULL":
            gql_type.not_null = True
        elif root.get("kind"):
            gql_type.api_kind = root.get("kind")
            gql_type.api_kind_name = root.get("name")

        if root.get("ofType"):
            return cls.solve(root["ofType"], gql_type)

        gql_type.python_name = camel_to_snake(gql_type.api_name)

        return gql_type

    def __init__(self, **gql_schema) -> None:
        self.root = gql_schema
        for key, getter in self.CINNAMON_TO_PYTHON_TYPE_CONVERSION.items():
            setattr(self, key, getter(gql_schema))

    def __str__(self) -> str:
        return f"<GQL {self.api_name} - {self.api_kind_name} - {self.api_kind}>"

    def __repr__(self) -> str:
        return str(self)

    def get_python_type_hint(self, repr_objects=False, objects_prefix="") -> str:
        type_hint = self.api_kind_name
        if self.api_kind == "INTERFACE":
            # TODO: improve interfaces
            return "Any"
        elif self.api_kind == "OBJECT":
            if objects_prefix:
                type_hint += objects_prefix
            if repr_objects:
                type_hint = repr(type_hint)
        elif self.api_kind == "ENUM":
            type_hint = f"enums.{self.api_kind_name}"
        elif self.api_kind == "INPUT_OBJECT":
            type_hint = f"inputs.{self.api_kind_name}"
        elif hasattr(scalars, self.api_kind_name):
            scalar = getattr(scalars, self.api_kind_name)
            type_hint = scalar.type_hint
        else:
            raise ValueError(
                f"Don't know what to type hint {repr(self.python_iterable)} {self.api_kind} {self.api_kind_name} {self.api_name}"
            )

        all_hints = (
            [type_hint] if self.not_null else [type_hint, "None", "CinnamonUndefined"]
        )
        if len(all_hints) > 1:
            unioned_hints = ", ".join(all_hints)
            type_hint = f"Union[{unioned_hints}]"

        if self.python_iterable:
            container_type = ITERABLE_TO_TYPE_HINT[self.python_iterable]
            return f"{container_type}[{type_hint}]"

        return type_hint

    def to_class_code(
        self, class_name, include_not_null=False, include_default_value=False
    ) -> List[str]:
        python_iterable = (
            self.python_iterable.__name__ if self.python_iterable else None
        )
        class_code = [
            f"class {class_name}(BaseCinnamonField):",
            f"    api_name = {repr(self.api_name)}",
            f"    api_kind = {repr(self.api_kind)}",
            f"    api_kind_name = {repr(self.api_kind_name)}",
            f"    python_iterable = {python_iterable}",
            f"    python_name = {repr(self.python_name)}",
        ]
        if self.api_kind == "SCALAR":
            class_code.append(f"    scalar = scalars.{self.api_kind_name}")
        if include_not_null:
            class_code.append(f"    not_null = {self.not_null}")
        if include_default_value:
            class_code.append(
                f"    python_default_value = {repr(self.python_default_value)}"
            )
        return class_code

    def to_args_str(self, objects_prefix: str = "", use_undefined=False) -> str:
        type_hint = self.get_python_type_hint(objects_prefix=objects_prefix)
        arg = f"{self.python_name}: {type_hint}"
        if not self.not_null:
            if use_undefined:
                arg += " = CinnamonUndefined"
            else:
                arg += f" = {repr(self.python_default_value)}"
        return arg


class GenericSchemaObject:
    name: str
    python_name: str
    attributes: List[CinnamonToPythonType]

    def __init__(self, name: str, attributes: List[CinnamonToPythonType]) -> None:
        self.name = name
        self.python_name = camel_to_snake(name)
        self.attributes = attributes


class GraphQLQuery:
    name: str
    python_name: str
    arguments: List[CinnamonToPythonType]
    return_type: CinnamonToPythonType
    is_paged: bool
    query_type: str

    def __init__(
        self,
        name: str,
        arguments: List[CinnamonToPythonType],
        return_type: CinnamonToPythonType,
        is_paged: bool,
        query_type: str,
    ) -> None:
        self.name = name
        self.python_name = camel_to_snake(name)
        self.arguments = arguments
        self.return_type = return_type
        self.is_paged = is_paged
        self.query_type = query_type


class SchemaReader:
    objects: List[GenericSchemaObject]
    input_objects: List[GenericSchemaObject]
    enums: List[Enum]
    interfaces: list
    queries: List[GraphQLQuery]

    def __init__(self) -> None:
        self.objects = []
        self.input_objects = []
        self.enums = []
        self.interfaces = []
        self.queries = []

    def OBJECT(self, t: dict) -> None:
        self.objects.append(
            GenericSchemaObject(
                t["name"],
                [
                    CinnamonToPythonType.solve(field)
                    for field in t["fields"]
                    if not field.get("isDeprecated")
                ],
            )
        )

    def SCALAR(self, t: dict) -> None:
        if not hasattr(scalars, t["name"]):
            raise KeyError(f"Missing scalar {t['name']}")

    def INPUT_OBJECT(self, t: dict) -> None:
        self.input_objects.append(
            GenericSchemaObject(
                t["name"],
                sorted(
                    [CinnamonToPythonType.solve(field) for field in t["inputFields"]],
                    key=lambda field: not field.not_null,
                ),
            )
        )

    def ENUM(self, t: dict) -> None:
        self.enums.append(
            Enum(
                t["name"],
                [
                    (value["name"], value["name"])
                    for value in t["enumValues"]
                    if not value.get("isDeprecated")
                ],
            )
        )

    def _build_queries(self, t: dict, query_type: str) -> None:
        for query in t["fields"]:
            if query["name"] in EXCLUDE_QUERIES:
                continue
            args = sorted(
                [CinnamonToPythonType.solve(arg) for arg in query["args"]],
                key=lambda t: not t.not_null,
            )
            self.queries.append(
                GraphQLQuery(
                    name=query["name"],
                    arguments=args,
                    return_type=CinnamonToPythonType.solve(query["type"]),
                    is_paged=all(
                        any(arg.api_name == api_name for arg in args)
                        for api_name in ("first", "after")
                    ),
                    query_type=query_type,
                )
            )

    def QUERIES(self, t: dict) -> None:
        self._build_queries(t, "query")

    def MUTATIONS(self, t: dict) -> None:
        self._build_queries(t, "mutation")

    def INTERFACE(self, t: dict) -> None:
        self.OBJECT(t)


class PythonCodeGenerator:
    def __init__(self, schema: SchemaReader) -> None:
        self.schema = schema
        self.objects_by_name = {
            gql_object.name: gql_object for gql_object in schema.objects
        }

    def object_classes(self) -> str:
        all_code = ""
        for gql_object in self.schema.objects:
            fields_maps = [
                gql_field.to_class_code(gql_field.api_name)
                for gql_field in gql_object.attributes
            ]
            object_attributes = [
                f"{gql_field.python_name}: {gql_field.get_python_type_hint(repr_objects=True)}"
                for gql_field in gql_object.attributes
            ]

            fields_maps_code = "\n        ".join(itertools.chain(*fields_maps))
            object_attributes_code = "\n    ".join(object_attributes)

            object_classes = ["BaseCinnamonObject"]

            object_code = str(
                f"class {gql_object.name}({', '.join(object_classes)}):\n"
                "    class _API_FIELDS:\n"
                f"        {fields_maps_code}\n"
                ""
                f"    {object_attributes_code}\n"
            )

            all_code += object_code

        for gql_object in self.schema.objects:
            for gql_field in gql_object.attributes:
                if gql_field.api_kind == "OBJECT":
                    all_code += f"{gql_object.name}._API_FIELDS.{gql_field.api_name}.obj = {gql_field.api_kind_name}\n"

        all_object_names_list = [gql_object.name for gql_object in self.schema.objects]
        all_code += f"__all__ = {repr(all_object_names_list)}\n"

        return black.format_str(all_code, mode=BLACK_MODE)

    def _get_field_class_for_object(
        self,
        name: str,
        gql_object: GenericSchemaObject,
        prefixes: List[str] = [],
        complexity: int = 0,
    ) -> List[str]:
        hide_on_attribute = next(
            (
                gql_field
                for gql_field in gql_object.attributes
                if gql_field.api_name in ("edges", "node")
            ),
            None,
        )
        if hide_on_attribute:
            return self._get_field_class_for_object(
                name,
                self.objects_by_name[hide_on_attribute.api_kind_name],
                prefixes + [hide_on_attribute.api_name],
                complexity,
            )

        fields = []
        object_fields = []
        prefix = "{".join(prefixes)
        if prefix:
            prefix += "{"
        suffix = "}" * len(prefixes)
        for gql_field in gql_object.attributes:
            if gql_field.api_kind == "OBJECT" and complexity >= MAX_COMPLEXITY:
                continue
            elif gql_field.api_kind == "OBJECT":
                object_fields.append(
                    self._get_field_class_for_object(
                        gql_field.python_name,
                        self.objects_by_name[gql_field.api_kind_name],
                        prefixes + [gql_field.api_name],
                        complexity + 1,
                    )
                )
            else:
                fields.append(
                    f'{gql_field.python_name} = r"{prefix}{gql_field.api_name}{suffix}"'
                )

        if not fields:
            fields.append("pass")

        indent = "    " * complexity
        code = f"{indent}class {name}(BaseCinnamonFieldsEnum):\n"
        code += f"{indent}    " + f"\n{indent}    ".join(fields) + "\n"
        code += "\n".join(object_fields)
        return code

    def fields_classes(self) -> str:
        all_code = ""
        all_object_names_list = []
        for gql_object in self.schema.objects:
            all_code += self._get_field_class_for_object(
                f"{gql_object.name}Fields", gql_object
            )
            all_object_names_list.append(f"{gql_object.name}Fields")

        all_code += f"__all__ = {repr(all_object_names_list)}\n"

        return black.format_str(all_code, mode=BLACK_MODE)

    def input_object_classes(self,) -> str:
        all_code = ""
        for input_object in self.schema.input_objects:
            args = [
                arg.to_args_str("objects.", use_undefined=True)
                for arg in input_object.attributes
            ]
            attribs = [
                f"{attrib.python_name}: {attrib.get_python_type_hint('objects.')}"
                for attrib in input_object.attributes
            ]
            field_maps = [
                field.to_class_code(field.python_name)
                for field in input_object.attributes
            ]
            init_args = ", ".join(
                f"{attrib.python_name}={attrib.python_name}"
                for attrib in input_object.attributes
            )

            input_code = f"class {input_object.name}(BaseCinnamonInput):\n"

            input_code += "    class _FIELDS:\n"
            input_code += "        " + "\n        ".join(itertools.chain(*field_maps))
            input_code += "\n"

            input_code += "    " + "\n    ".join(attribs)
            input_code += "\n"

            input_code += f"    def __init__(self, {', '.join(args)}) -> None:\n"
            input_code += f"        super().__init__({init_args})\n"

            all_code += input_code

        all_object_names_list = [
            f"{input_object.name}" for input_object in self.schema.input_objects
        ]
        all_code += f"__all__ = {repr(all_object_names_list)}\n"

        return black.format_str(all_code, mode=BLACK_MODE)

    def enums(self) -> str:
        enums_code = ""
        for enm in self.schema.enums:
            enums_code += f"class {enm.__name__}(Enum):\n"
            for field in enm:
                enums_code += f"    {field.name} = {repr(field.value)}\n"
        enums_code += f"__all__ = {repr([enm.__name__ for enm in self.schema.enums])}\n"
        return black.format_str(enums_code, mode=BLACK_MODE)

    def interfaces(self, interfaces: list) -> str:
        return ""

    def api_class(self, class_name: str) -> str:
        args_legend = {}
        query_code = []
        for query in self.schema.queries:
            arguments_iterable = query.arguments
            if query.is_paged:
                arguments_iterable = [
                    arg
                    for arg in query.arguments
                    if arg.api_name not in PAGING_ARGUMENTS
                ]
            args = [
                arg.to_args_str("objects.", use_undefined=True)
                for arg in arguments_iterable
            ]
            fields_class = f"fields_module.{query.return_type.api_kind_name}Fields"
            args.extend(
                [
                    f"fields: List[{fields_class}] = {fields_class}._default_fields()",
                    "headers: Union[dict, None] = None",
                    "token: Union[str, None] = None",
                ]
            )
            args_legend[query.python_name] = [
                arg.to_class_code(arg.python_name) for arg in arguments_iterable
            ]

            query_builder_arg_dict = "{"
            for arg in arguments_iterable:
                query_builder_arg_dict += f'"{arg.python_name}": {arg.python_name},'
            query_builder_arg_dict += "}"

            function_code = [
                f"def {query.python_name}(self, {', '.join(args)}) -> objects.{query.return_type.api_kind_name}:",
                f"    query_args = self._query_builder(",
                f"        {repr(query.query_type)},",
                f"        {repr(query.name)},",
                "        fields,",
                f"        {query_builder_arg_dict},",
                f"        _ARGUMENT_LEGENDS.{query.python_name},",
                f"        {query.is_paged},",
                "    )",
            ]

            if not query.is_paged:
                function_code += [
                    f"    return objects.{query.return_type.api_kind_name}(",
                    f"        self.api(headers=headers, token=token, **query_args)['data']['{query.name}'],",
                    "    )",
                ]
            else:
                function_code += [
                    "    return self.iterate_edges(",
                    f'        objects.{query.return_type.api_kind_name}, query_args, headers, token, "{query.name}",'
                    "    )",
                ]

            query_code.append(function_code)

        all_code = "class _ARGUMENT_LEGENDS:\n"
        for name, lines in args_legend.items():
            if lines:
                all_code += f"    class {name}:\n"
                all_code += "        " + "\n        ".join(itertools.chain(*lines))
                all_code += "\n"

        all_code += f"class {class_name}(BaseSyncCinnamon):\n"
        all_code += "    " + "\n    ".join(itertools.chain(*query_code))

        return black.format_str(all_code, mode=BLACK_MODE)


def get_schema(url: str, email: str, password: str) -> SchemaReader:
    if not url:
        raise ValueError("No URL supplied.")
    if not email:
        raise ValueError("No email login provided.")
    if not password:
        raise ValueError("No password provided.")
    schema = SchemaReader()
    cinnamon = BaseSyncCinnamon(url)
    cinnamon.login(email, password)
    result = cinnamon.api(
        str(
            "{"
            "__schema {"
            "   types {"
            "       kind"
            "       name"
            "       enumValues { name, isDeprecated }"
            "       fields {"
            "           name"
            "           args { name, type { kind, name, ofType{ kind, name } }, defaultValue }"
            "           type { kind, name, ofType { kind, name, ofType { kind, name, ofType { kind, name } } } }"
            "           isDeprecated"
            "       }"
            "       inputFields { name, defaultValue, type { kind, name, ofType { kind, name, ofType { kind, name, ofType { kind, name } } } } }"
            "   }"
            "}"
            "}"
        )
    )
    types = result["data"]["__schema"]["types"]
    for t in types:
        name = t["name"]
        kind = t["kind"]
        if name.startswith("__") or name in QUERY_NAMES:
            pass
        elif kind not in ("SCALAR", "ENUM"):
            pass
        elif not hasattr(schema, kind):
            raise KeyError(f"Cannot handle kind {kind}.")
        else:
            getattr(schema, kind)(t)
    for t in types:
        name = t["name"]
        kind = t["kind"]
        if name.startswith("__") or name in QUERY_NAMES:
            pass
        elif kind in ("SCALAR", "ENUM"):
            pass
        elif not hasattr(schema, kind):
            raise KeyError(f"Cannot handle kind {kind}.")
        else:
            getattr(schema, kind)(t)
    for t in types:
        name = t["name"]
        if name == "Query":
            schema.QUERIES(t)
        elif name == "Mutation":
            schema.MUTATIONS(t)
    return schema

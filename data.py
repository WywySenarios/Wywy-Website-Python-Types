from typing import Any, Literal, NotRequired, TypeAlias, TypedDict
import datetime

DataDatatype: TypeAlias = int | float | str | bool | datetime.datetime | None
Datatype: TypeAlias = Literal[
    "int",
    "integer",
    "float",
    "number",
    "string",
    "str",
    "text",
    "bool",
    "boolean",
    "date",
    "time",
    "timestamp",
    "enum",
    "geodetic point",
    "pointer",
    "polypointer",
    "polymorphic pointer",
]
PostgresDatatype: TypeAlias = Literal[
    "integer",
    "real",
    "double precision",
    "text",
    "boolean",
    "date",
    "time",
    "timestamp",
    "interval",
    "enum",
    "ST_Point",
]


class DataColumn(TypedDict):
    name: str
    parser: NotRequired[Datatype]
    datatype: Datatype
    defaultValue: NotRequired[Any]
    entrytype: str
    invalidInputMessage: NotRequired[str]
    comments: NotRequired[bool]
    description: NotRequired[str]
    unique: NotRequired[bool]
    optional: NotRequired[bool]
    references: NotRequired[str | list[str]]


Schema: TypeAlias = list[DataColumn]
DictSchema: TypeAlias = dict[str, DataColumn]


class DescriptorInfo(TypedDict):
    name: str
    schema: Schema


class DictDescriptorInfo(TypedDict):
    name: str
    schema: DictSchema


# @TODO verify if it's descriptor or descriptors
TableType: TypeAlias = Literal[
    "data", "descriptor", "tags", "tag_names", "tag_aliases", "tag_groups"
]


class TableInfo(TypedDict):
    tableName: str
    entrytype: Literal["form", "timer"]
    read: bool
    write: bool
    comments: bool
    tagging: NotRequired[bool]
    schema: Schema
    descriptors: NotRequired[list[DescriptorInfo]]


class DictTableInfo(TypedDict):
    tableName: str
    entrytype: Literal["form", "timer"]
    read: bool
    write: bool
    comments: bool
    tagging: NotRequired[bool]
    schema: DictSchema
    descriptors: NotRequired[dict[str, DictDescriptorInfo]]


class DatabaseInfo(TypedDict):
    dbname: str
    tables: list[TableInfo]


DictDatabaseInfo: TypeAlias = dict[str, DictTableInfo]


class MainConfig(TypedDict):
    data: list[DatabaseInfo]


# User input
Entry: TypeAlias = dict[str, Any]


class FullEntry(TypedDict):
    data: Entry
    descriptors: dict[str, Any]
    tags: dict[str, Any]


class EntryTableData(TypedDict):
    columns: list[str]
    data: list[list[Any]]

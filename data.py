from typing import Any, Literal, NotRequired, TypeAlias, TypedDict

Datatype: TypeAlias = Literal["int", "integer", "float", "number", "string", "str", "text", "bool", "boolean", "date", "time", "timestamp", "enum", "geodetic point"]
PostgresDatatype: TypeAlias = Literal["integer", "real", "double precision", "text", "boolean", "date", "time", "timestamp", "interval", "enum", "ST_Point"]

class DataColumn(TypedDict):
    name: str
    parser: Datatype
    datatype: Datatype
    defaultValue: Any
    entrytype: str
    invalidInputMessage: str | None
    comments: NotRequired[bool]
    description: str | None
    unique: bool | None

Schema: TypeAlias = list[DataColumn]
DictSchema: TypeAlias = dict[str, DataColumn]

class DescriptorInfo(TypedDict):
    name: str
    schema: Schema

class DictDescriptorInfo(TypedDict):
    name: str
    schema: DictSchema

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
EntryData: TypeAlias = dict[str, Any]
Entry: TypeAlias = dict[Literal["data", "descriptors", "tags"], EntryData]

class EntryTableData(TypedDict):
    columns: list[str]
    data: list[list[Any]]
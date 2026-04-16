from typing import Iterator
from .data import TableInfo, DescriptorInfo
from config import CONFIG


def iter_tables() -> Iterator[tuple[tuple[str, str], TableInfo]]:
    """Table iterator.

    Yields:
        Iterator[tuple[tuple[str, str], TableInfo]]: The (non-lower_snake_case) ancestry and table schema.
    """
    for database_schema in CONFIG["data"]:
        database_name = database_schema["dbname"]
        for table_schema in database_schema["tables"]:
            table_name = table_schema["tableName"]
            yield (database_name, table_name), table_schema


def iter_descriptors() -> Iterator[tuple[tuple[str, str, str], DescriptorInfo]]:
    """Descriptor iterator.

    Yields:
        Iterator[tuple[tuple[str, str, str], DescriptorInfo]]: The (non-lower_snake_case) ancestry and table schema.
    """
    for database_schema in CONFIG["data"]:
        database_name = database_schema["dbname"]
        for table_schema in database_schema["tables"]:
            table_name = table_schema["tableName"]
            for descriptor_schema in table_schema.get("descriptors", []):
                descriptor_name = descriptor_schema["name"]
                yield (database_name, table_name, descriptor_name), descriptor_schema

import typing

from kuber.definitions import _abstracts
from kuber import _types


def serialize_property(value: typing.Any) -> typing.Any:
    """
    Converts a Definition property value into one compatible with the json
    and yaml configuration formats. Basic types are returned without any
    conversion, but Definition objects are converted to their dictionary
    representation and lists of non-basic types are converted down as well.

    :param value:
        Property value to be serialized for configuration file format
        compatibility.
    :return:
        Serialized version of the supplied value.
    """
    # Some falsy cases are meaningful and should be preserved.
    nulls: typing.Tuple[None, dict, list] = (None, {}, [])

    if hasattr(value, "to_dict"):
        return value.to_dict() or None

    if isinstance(value, (list, tuple)):
        raw_values = [serialize_property(v) for v in value]
        return [v for v in raw_values if v not in nulls] or None

    if isinstance(value, dict):
        raw_items = {k: serialize_property(v) for k, v in value.items()}
        return {k: v for k, v in raw_items.items() if v not in nulls} or None

    return None if value in nulls else value


def deserialize_property(value: typing.Any, data_type: tuple) -> typing.Any:
    """
    Converts the serialized configuration value into the given kuber data type.
    All Definition objects store data types internally to allow for easily
    mapping from serialized values during the loading of configuration file
    data.

    :param value:
        Serialized configuration value to be converted into the given data
        type.
    :param data_type:
        kuber data type to deserialize the given value into.
    :return:
        Deserialized form of the specified value.
    """
    if value is None:
        return None

    if data_type[0] == _types.integer_or_string:
        return _types.integer_or_string(value)

    if issubclass(data_type[0], _abstracts.Definition):
        return data_type[0]().from_dict(value)

    if data_type[0] == list:
        return [deserialize_property(v, (data_type[1], None)) for v in value]

    return data_type[0](value)


def to_camel_case(source: str) -> str:
    """Converts kebab-case or snake_case to camelCase."""
    parts = source.replace("-", "_").split("_")
    return "".join([parts[0], *[p.capitalize() for p in parts[1:]]])

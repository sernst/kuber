import typing


def integer_or_string(value: typing.Any) -> typing.Union[None, int, str]:
    """Conversion for int_or_string types."""
    if value is None:
        return None

    if isinstance(value, int):
        return value

    if isinstance(value, str):
        return value

    try:
        return int(value)
    except ValueError:
        return str(value)

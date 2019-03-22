import typing


from kuber import definitions as _kuber_definitions


class IntOrString(_kuber_definitions.Definition):
    """
    IntOrString is a type that can hold an int32 or a string.
    When used in JSON or YAML marshalling and unmarshalling, it
    produces or consumes the inner type.  This allows you to
    have, for example, a JSON field that can accept a name or
    number.
    """

    def __init__(
            self,
    ):
        """Create IntOrString instance."""
        super(IntOrString, self).__init__(
            api_version='util/intstr',
            kind='IntOrString'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IntOrString':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

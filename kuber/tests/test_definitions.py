from kuber import definitions


def test_definition_serialization():
    """Should create a Definition object and serialize as expected."""
    d = definitions.Definition('1.11', 'Deployment')
    d._properties = {'foo': 1, 'bar': None, 'baz': 'hello'}
    d._types = {'bar': (float, None), 'baz': (str, None)}

    serialized = d.to_dict()
    assert {'baz': 'hello'} == serialized
    assert d.kuber_uid is not None


def test_definition_deserialization():
    """Should create a Definition object populated from the serialized data."""
    d = definitions.Definition('1.11', 'Deployment')
    d._types = {'bar': (float, None), 'baz': (str, None)}

    d.from_dict({'foo': 1, 'bar': None, 'baz': 'hello'})
    assert {'baz': 'hello', 'bar': None} == d._properties


import kuber


def test_settings():
    """
    Should properly assign a setting that is accessible through all
    possible avenues.
    """
    s = kuber.create_bundle().settings
    s.add(a=42)
    assert s.fetch('a') == 42
    assert s.grab('a')[0] == 42
    assert s['a'] == 42
    assert s.a == 42
    assert s.to_dict() == {'a': 42}
    assert s.to_yaml().find('42') > 0
    assert list(s.values()) == [42]
    assert list(s.keys()) == ['a']
    assert list(s.items()) == [('a', 42)]

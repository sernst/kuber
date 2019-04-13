from pytest import mark

from kuber import kube_api

SCENARIOS = (
    ({'foo': None, 'fooBar': ''}, {'fooBar': ''}),
    ({'foo': False, 'foo_bar': 42}, {'foo': False, 'fooBar': 42}),
    ({'foo_bar_baz': 'a'}, {'fooBarBaz': 'a'}),
)


@mark.parametrize('source, expected', SCENARIOS)
def test_to_kuber_dict(source: dict, expected: dict):
    """Should convert to the expected value."""
    assert kube_api.to_kuber_dict(source) == expected

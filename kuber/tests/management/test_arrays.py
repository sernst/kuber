import os
import kuber

import pytest

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_resource_arrays():
    """Should access resources using dynamic arrays."""
    bundle = kuber.from_directory(MY_DIRECTORY)
    expected = bundle.get(name='first-a', kind='ConfigMap')
    assert expected == bundle.resources.config_map.first_a
    assert expected in bundle.resources.config_map
    assert expected == bundle.resources.config_map['first-a']
    assert expected == bundle.resources['config_map']['first-a']
    assert expected == bundle.resources['config-map']['first-a']
    assert expected == bundle.resources['ConfigMap']['first-a']


def test_resource_arrays_multi():
    """Should access resources using dynamic arrays."""
    bundle = kuber.from_directory(MY_DIRECTORY)
    expected = bundle.get(
        name='foo-pod',
        kind='Pod',
        namespace='first'
    )
    assert len(bundle.resources.pod) >= 3
    assert len(bundle.resources.pod.foo_pod) == 3
    assert expected in bundle.resources.pod
    assert expected == bundle.resources.pod.foo_pod[0]
    assert expected == bundle.resources.within('first').pod.foo_pod
    assert expected == bundle.resources.within('first').pod['foo-pod']


def test_resource_arrays_missing():
    """Should raise ValueError if resource does not exist."""
    bundle = kuber.from_directory(MY_DIRECTORY)

    with pytest.raises(ValueError):
        print(bundle.resources.pod.this_pod_does_not_exist)

    assert bundle.resources.pod[0] is not None


def test_resource_arrays_indexing():
    """Should retrieve the first loaded pod."""
    bundle = kuber.from_directory(MY_DIRECTORY)
    pods = bundle.get_many(kind='Pod')
    assert pods == bundle.resources.pod.to_list()
    assert pods[0] == bundle.resources.pod[0]


def test_resource_arrays_to_list():
    """Should create a list matching the contents of the array."""
    bundle = kuber.from_directory(MY_DIRECTORY)
    all_resources = bundle.resources.to_list()
    for i, r in enumerate(all_resources):
        assert bundle.resources[i] == all_resources[i]

import os
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

import kuber
from kuber import latest
from kuber.management import creation

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_initialization():
    """Should initialize bundle as expected."""
    bundle = kuber.create_bundle(
        kubernetes_version='pre',
        bundle_name='foo'
    )
    assert bundle.kubernetes_version.label == 'pre'
    assert bundle.name == 'foo'
    assert bundle.cli is not None


def test_version():
    """Should initialize bundle as expected."""
    bundle = kuber.create_bundle(
        kubernetes_version=latest.KUBERNETES_VERSION,
        bundle_name='foo'
    )
    assert bundle.kubernetes_version.label == 'latest'
    assert bundle.name == 'foo'


def test_new_resource():
    """Should create a new resource from specified arguments."""
    config_map = kuber.new_resource(
        api_version='core/v1',
        kind='ConfigMap',
        kubernetes_version=kuber.latest_kube_version.label.strip('v')
    )
    assert config_map is not None
    assert config_map.kind == 'ConfigMap'


def test_from_dict():
    """Should create a resource from a configuration dictionary."""
    version = kuber.latest_kube_version
    config_map = creation.from_dict(
        resource_definition={
            'apiVersion': 'core/v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'foo'}
        },
        kubernetes_version=f'{version.major}.{version.minor}'
    )
    assert config_map is not None
    assert config_map.kind == 'ConfigMap'


def test_add_resource():
    """Should create a new resource from specified arguments."""
    bundle = kuber.ResourceBundle()
    bundle.add(
        api_version='core/v1',
        kind='ConfigMap',
        name='foo'
    )
    assert len(bundle.resources) == 1
    assert bundle.resources[0].kind == 'ConfigMap'


def test_add_file():
    """Should add the specified YAML file to the bundle."""
    bundle = kuber.ResourceBundle()
    bundle.add_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    assert len(bundle.resources) > 0


def test_add_file_invalid():
    """Should raise an IOError for unknown file types."""
    bundle = kuber.ResourceBundle()
    with pytest.raises(IOError):
        bundle.add_file(os.path.join(MY_DIRECTORY, 'name.foo'))


def test_add_from_yaml():
    """Should add the specified YAML string to the bundle."""
    path = os.path.join(MY_DIRECTORY, 'test-get.yaml')
    with open(path) as f:
        contents = f.read()

    bundle = kuber.ResourceBundle()
    bundle.add_from_yaml(contents)
    assert len(bundle.resources) > 0


def test_remove():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    count = len(bundle.resources)
    resource = bundle.resources[1]
    bundle.remove(resource)
    assert len(bundle.resources) == count - 1
    assert resource not in bundle.resources


def test_pop():
    """Should remove the resource from the bundle."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.resources[1]
    popped_resource = bundle.pop(
        name=resource.metadata.name,
        kind=resource.kind,
        **resource.metadata.labels
    )
    assert resource == popped_resource


def test_unshift():
    """
    Should place the resource at the beginning fo the resources list.
    """
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.resources[1]
    bundle.remove(resource)
    bundle.unshift(resource)
    assert bundle.resources[0] == resource


def test_load_directory():
    """Should load all resources in the directory."""
    bundle = kuber.from_directory(MY_DIRECTORY)
    resource = bundle.get(name='loaded-from-json')
    assert resource is not None
    assert len(bundle.resources) > 1


def test_render_json():
    """Should render bundle to JSON."""
    version = latest.KUBERNETES_VERSION
    bundle = kuber.from_directory(
        directory=MY_DIRECTORY,
        kubernetes_version=f'{version.major}.{version.minor}'
    )
    results = bundle.render_json()
    assert len(bundle.resources) == len(results)


def test_render_yaml_bundle():
    """Should render bundle to a single YAML file."""
    version = latest.KUBERNETES_VERSION
    bundle = kuber.from_directory(
        directory=MY_DIRECTORY,
        kubernetes_version=f'{version.major}.{version.minor}'
    )
    assert bundle.render_yaml_bundle()


@patch('kuber.execution.create_resource')
def test_create(create_resource: MagicMock):
    """Should execute create on bundle resources."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    bundle.create()
    assert create_resource.call_count == len(bundle.resources)


@patch('kuber.execution.replace_resource')
def test_replace(replace_resource: MagicMock):
    """Should execute replace on bundle resources."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    bundle.replace()
    assert replace_resource.call_count == len(bundle.resources)


@patch('kuber.execution.get_resource_status')
def test_statuses(get_resource_status: MagicMock):
    """Should execute statuses on bundle resources."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    bundle.statuses()
    assert get_resource_status.call_count == len(bundle.resources)


@patch('kuber.execution.delete_resource')
def test_delete(delete_resource: MagicMock):
    """Should execute delete on bundle resources."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    bundle.delete()
    assert delete_resource.call_count == len(bundle.resources)

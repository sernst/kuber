import os

import kuber
from kuber import latest

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


def test_remove():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    count = len(bundle.resources)
    resource = bundle.resources[1]
    bundle.remove(resource)
    assert len(bundle.resources) == count - 1
    assert resource not in bundle.resources


def test_pop():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.resources[1]
    popped_resource = bundle.pop(
        name=resource.metadata.name,
        kind=resource.kind,
        **resource.metadata.labels
    )
    assert resource == popped_resource


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

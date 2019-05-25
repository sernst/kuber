import os

import kuber

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_new():
    """Should create new resource, add it to bundle and return it."""
    bundle = kuber.create_bundle()
    resource = bundle.new('v1', 'ConfigMap', 'foo')
    assert resource == bundle.resources[-1]
    assert resource.metadata.name == 'foo'


def test_add_directory_files():
    """Should add first resources before second resources."""
    bundle = kuber.from_directory_files(
        directory=MY_DIRECTORY,
        filenames=['test-first.yaml', 'test-second.yaml']
    )
    names = [r.metadata.name for r in bundle.resources]
    assert names == ['first-a', 'first-b', 'second-a', 'second-b']


def test_add_directory_files_reversed():
    """Should add second resources before first resources."""
    bundle = kuber.from_directory_files(
        directory=MY_DIRECTORY,
        filenames=['test-second.yaml', 'test-first.yaml']
    )
    names = [r.metadata.name for r in bundle.resources]
    assert names == ['second-a', 'second-b', 'first-a', 'first-b']

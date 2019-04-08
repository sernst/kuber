import os
import kuber

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_get_deployment():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.get(name='foo', kind='Deployment')
    assert resource.kind == 'Deployment'


def test_get_config_map():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.get(name='foo', kind='ConfigMap')
    assert resource.kind == 'ConfigMap'


def test_get_job():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.get(name='foo', kind='Job')
    assert resource.kind == 'Job'


def test_get_job_label():
    """Should return the correct resource type."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.get(kind='Job', app='bar')
    assert resource.kind == 'Job'
    assert resource.metadata.labels['app'] == 'bar'


def test_get_none():
    """Should not find a match that doesn't exist."""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resource = bundle.get(app='baz')
    assert resource is None


def test_get_many():
    """Should return all matching resources"""
    bundle = kuber.from_file(os.path.join(MY_DIRECTORY, 'test-get.yaml'))
    resources = bundle.get_many(kind='Job')
    assert len(resources) == 2
    assert set([r.kind for r in resources]) == {'Job'}

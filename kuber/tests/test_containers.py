from pytest import mark

from kuber.latest import apps_v1
from kuber.latest import batch_v1
from kuber.latest import core_v1

RESOURCES_TO_TEST = [core_v1.Pod, apps_v1.Deployment, batch_v1.Job]


@mark.parametrize('resource_class', RESOURCES_TO_TEST)
def test_container_methods(resource_class):
    """Tests auto-generated container methods."""
    resource = resource_class()
    resource.append_container(name='foo', image='foo')
    resource.append_container(name='bar', image='bar')
    assert resource.get_container('foo').name == 'foo'
    assert resource.get_container('bar').name == 'bar'
    assert len(resource.get_containers()) == 2

import os

import kuber
from kuber.latest import apps_v1


def test_zero_scale_deployment():
    """Should preserve a 0 set on the scale for a deployment."""
    d = apps_v1.Deployment()
    d.spec.replicas = 0
    result = d.to_yaml()
    assert 'replicas: 0' in result


def test_zero_replicas_from_file():
    """Should preserve a 0 replicas on a deployment loaded from yaml."""
    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        'deployment.yaml'
    ))
    bundle = kuber.from_file(path)
    assert 'replicas: 0' in bundle.render_yaml_bundle()

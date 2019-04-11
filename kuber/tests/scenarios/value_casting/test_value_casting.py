import os

import kuber
from kuber.latest import core_v1

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_target_port():
    """
    Should return target port as integer because the OpenApi v2 spec used
    by the Python Kubernetes client doesn't support multi-type validation and
    so strings cannot be used at this time as an alternative. For more details
    see the issue:
        - https://github.com/kubernetes-client/python/issues/322
    """
    path = os.path.join(MY_DIRECTORY, 'target-port.yaml')
    service: core_v1.Service = kuber.from_yaml_file(path)
    assert isinstance(service.spec.ports[0].target_port, int)

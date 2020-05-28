import os

import kuber
from kuber.latest import core_v1

directory = os.path.realpath(os.path.dirname(__file__))


def test_odd_api_versions():
    """Should serialize and deserialize odd api versions."""
    bundle = kuber.from_file(
        os.path.join(directory, 'same-names-different-resources.yaml'),
        kubernetes_version='latest'
    )

    service_account: core_v1.ServiceAccount = (
        bundle.resources.service_account.foo_bar
    )
    assert service_account.kind == 'ServiceAccount'

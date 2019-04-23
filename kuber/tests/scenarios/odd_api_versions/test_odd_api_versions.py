import os

import kuber

directory = os.path.realpath(os.path.dirname(__file__))


def test_odd_api_versions():
    """Should serialize and deserialize odd api versions."""
    bundle = kuber.from_file(
        os.path.join(directory, 'odd-resources.yaml'),
        kubernetes_version='1.11'
    )

    print(bundle.render_yaml_bundle())
    assert len(bundle.resources) == 1

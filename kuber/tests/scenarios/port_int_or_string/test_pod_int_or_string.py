import pathlib
import typing

import kuber
from kuber.latest import core_v1

directory = pathlib.Path(__file__).parent.absolute()


def test_pod_int_or_string():
    """Should handle a port string value that cannot be an integer."""
    pod = typing.cast(core_v1.Pod, kuber.from_yaml_file(directory.joinpath("pod.yaml")))
    assert pod.get_containers()[0].liveness_probe.http_get.port == "metrics"

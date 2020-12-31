import pathlib
import typing
import yaml

import kuber
from kuber.latest import custom_v1

directory = pathlib.Path(__file__).parent.absolute()


def test_custom_object_in_bundle():
    """Should load a custom object successfully."""
    bundle = kuber.create_bundle(kubernetes_version="latest").add_file(
        directory.joinpath("custom_object.yaml")
    )
    assert len(bundle.resources) == 1

    co = typing.cast(custom_v1.CustomObject, bundle.resources.workflow[0])
    assert co.api_version == "argoproj.io/v1alpha1"
    assert co.kind == "Workflow"
    assert co.to_yaml() is not None


def test_custom_object():
    """Should populate a custom object directly without error."""
    co = custom_v1.CustomObject().from_dict(
        yaml.safe_load(directory.joinpath("custom_object.yaml").read_text())
    )
    assert co.api_version == "argoproj.io/v1alpha1"
    assert co.kind == "Workflow"
    assert co.to_yaml() is not None


def test_custom_object_convenience():
    """Should populate a custom object from convenience function without error."""
    co = typing.cast(
        custom_v1.CustomObject,
        kuber.from_yaml_file(directory.joinpath("custom_object.yaml")),
    )
    assert co.api_version == "argoproj.io/v1alpha1"
    assert co.kind == "Workflow"
    assert co.to_yaml() is not None

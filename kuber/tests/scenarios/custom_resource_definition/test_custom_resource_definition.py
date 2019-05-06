import os

import kuber
from kuber.latest import apiextensions_v1beta1

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_custom_resource_definition():
    """
    Should not cause a recursion error while loading a CRD yaml definition.
    For more details on the source of this scenario see:
    https://github.com/sernst/kuber/issues/1
    """
    bundle = (
        kuber.create_bundle(kubernetes_version='latest')
        .add_file(os.path.join(MY_DIRECTORY, 'crd.yaml'))
    )
    assert len(bundle.resources) == 1

    crd: apiextensions_v1beta1.CustomResourceDefinition = bundle.resources[0]
    assert crd.spec.validation.open_apiv3_schema.not_ is None, """
        Expect the self-referential property value to be None by default.
        """

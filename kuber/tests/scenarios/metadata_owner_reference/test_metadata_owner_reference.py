import os

import kuber

directory = os.path.realpath(os.path.dirname(__file__))


def test_metadata_owner_reference():
    """
    Should load the owner references correctly. Specifically that the
    apiVersion and kind are set correctly to the reference
    """
    pod = kuber.from_yaml_file(os.path.join(directory, 'owner_metadata.yaml'))
    reference = pod.metadata.owner_references[0]
    reference_dict = pod.to_dict()['metadata']['ownerReferences'][0]
    serialized = pod.to_yaml()

    assert reference.kind == 'DaemonSet'
    assert reference_dict['kind'] == 'DaemonSet'
    assert ' kind: DaemonSet' in serialized

    assert reference.api_version == 'apps/v1'
    assert reference_dict['apiVersion'] == 'apps/v1'
    assert ' apiVersion: apps/v1' in serialized

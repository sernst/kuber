import os

import kuber
from kuber.latest import rbac_v1

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_empty_api_group():
    """Should include the empty apiGroup value."""
    path = os.path.join(MY_DIRECTORY, 'empty-api-group.yaml')
    cluster_role: rbac_v1.ClusterRole = kuber.from_yaml_file(path)
    assert cluster_role.rules[0].api_groups is not None
    assert 'apiGroups' in cluster_role.to_dict()['rules'][0]

import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.8',
    major='1',
    minor='17',
    patch='8',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='35dc4cdc26cfcb6614059c4c6e836e5f0dc61dee'
)

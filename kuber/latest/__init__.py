import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.17.4',
    major='1',
    minor='17',
    patch='4',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 3, 24),
    commit_sha='8d8aa39598534325ad77120c120a22b3a990b5ea'
)

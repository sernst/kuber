import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.13',
    version='v1.13.6',
    major='1',
    minor='13',
    patch='6',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 5, 13),
    commit_sha='abdda3f9fefa29172298a2e42f5102e777a8ec25'
)

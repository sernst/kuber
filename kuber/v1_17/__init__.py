import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.0-beta.0',
    major='1',
    minor='17',
    patch='0',
    pre_release='beta.0',
    build='',
    created_at=_datetime.datetime(2019, 10, 31),
    commit_sha='fd61642e68bdf91550a219763a78c76e18ac80bb'
)

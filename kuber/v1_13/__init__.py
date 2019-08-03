import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.13',
    version='v1.13.8',
    major='1',
    minor='13',
    patch='8',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 3),
    commit_sha='0c6d31a99f81476dfc9871ba3cf3f597bec29b58'
)

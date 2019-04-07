import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.14.0',
    major='1',
    minor='14',
    patch='0',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 4, 7),
    commit_sha='641856db18352033a0d96dbc99153fa3b27298e5'
)

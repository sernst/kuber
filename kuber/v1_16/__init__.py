import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.0-beta.1',
    major='1',
    minor='16',
    patch='0',
    pre_release='beta.1',
    build='',
    created_at=_datetime.datetime(2019, 8, 23),
    commit_sha='92639f719ee353219fa2cd19128a93409bb3a1e3'
)

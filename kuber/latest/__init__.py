import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.18.5',
    major='1',
    minor='18',
    patch='5',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='e6503f8d8f769ace2f338794c914a96fc335df0f'
)

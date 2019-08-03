import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.12',
    version='v1.12.10',
    major='1',
    minor='12',
    patch='10',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 3),
    commit_sha='e3c134023df5dea457638b614ee17ef234dc34a6'
)

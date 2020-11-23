import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.20',
    version='v1.20.0-beta.2',
    major='1',
    minor='20',
    patch='0',
    pre_release='beta.2',
    build='',
    created_at=_datetime.datetime(2020, 11, 23),
    commit_sha='3af376d3ad5009fa82c94c1ef1fed17dc1f8c29a'
)

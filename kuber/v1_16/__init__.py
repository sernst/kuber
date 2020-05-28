import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.10',
    major='1',
    minor='16',
    patch='10',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 5, 28),
    commit_sha='f3add640dbcd4f3c33a7749f38baaac0b3fe810d'
)

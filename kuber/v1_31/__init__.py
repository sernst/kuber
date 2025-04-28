import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.31",
    version="v1.31.8",
    major="1",
    minor="31",
    patch="8",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="3f46d435cd795e85aeea6b1a73742edad13b5222",
)

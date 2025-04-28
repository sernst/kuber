import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.30",
    version="v1.30.12",
    major="1",
    minor="30",
    patch="12",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="66f4b3fc7966ccf5faf8264b1fef9f63b83a8ef4",
)

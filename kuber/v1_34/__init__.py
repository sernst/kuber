import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.34",
    version="v1.34.0-alpha.0",
    major="1",
    minor="34",
    patch="0",
    pre_release="alpha.0",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="ab3e83f73424a18f298a0050440af92d2d7c4720",
)

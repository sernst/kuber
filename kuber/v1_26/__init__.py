import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.26",
    version="v1.26.14",
    major="1",
    minor="26",
    patch="14",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="6db79806d788bfb9cfc996deb7e2e178402e8b50",
)

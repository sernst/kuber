import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.20",
    version="v1.20.12",
    major="1",
    minor="20",
    patch="12",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="4bf2e32bb2b9fdeea19ff7cdc1fb51fb295ec407",
)

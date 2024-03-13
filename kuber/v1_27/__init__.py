import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.27",
    version="v1.27.11",
    major="1",
    minor="27",
    patch="11",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="b9e2ad67ad146db566be5a6db140d47e52c8adb2",
)

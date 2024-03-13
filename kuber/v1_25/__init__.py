import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.25",
    version="v1.25.8",
    major="1",
    minor="25",
    patch="8",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="0ce7342c984110dfc93657d64df5dc3b2c0d1fe9",
)

import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="pre",
    version="v1.22.0-alpha.0",
    major="1",
    minor="22",
    patch="0",
    pre_release="alpha.0",
    build="",
    created_at=_datetime.datetime(2021, 4, 26),
    commit_sha="9c9af69ea60519b610a70261fb1b8bb81a2a5d04",
)

import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.27",
    version="v1.27.0-beta.0",
    major="1",
    minor="27",
    patch="0",
    pre_release="beta.0",
    build="",
    created_at=_datetime.datetime(2023, 3, 20),
    commit_sha="a34e37c9963af5944435b736882bfcd1e81f7e09",
)

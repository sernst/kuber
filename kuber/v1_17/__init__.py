import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.17",
    version="v1.17.16",
    major="1",
    minor="17",
    patch="16",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 1, 7),
    commit_sha="d88fadbd65c5e8bde22630d251766a634c7613b0",
)

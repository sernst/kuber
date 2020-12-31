import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.20",
    version="v1.20.1",
    major="1",
    minor="20",
    patch="1",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 31),
    commit_sha="c4d752765b3bbac2237bf87cf0b1c2e307844666",
)

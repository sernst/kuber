import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="pre",
    version="v1.30.0-beta.0",
    major="1",
    minor="30",
    patch="0",
    pre_release="beta.0",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="634fc1b4836b3a500e0d715d71633ff67690526a",
)

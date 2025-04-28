import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.28",
    version="v1.28.7",
    major="1",
    minor="28",
    patch="7",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="c8dcb00be9961ec36d141d2e4103f85f92bcf291",
)

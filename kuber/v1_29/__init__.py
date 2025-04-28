import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.29",
    version="v1.29.2",
    major="1",
    minor="29",
    patch="2",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="4b8e819355d791d96b7e9d9efe4cbafae2311c88",
)

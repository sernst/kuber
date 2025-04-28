import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="latest",
    version="v1.33.0",
    major="1",
    minor="33",
    patch="0",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2025, 4, 28),
    commit_sha="60a317eadfcb839692a68eab88b2096f4d708f4f",
)

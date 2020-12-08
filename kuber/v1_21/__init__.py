import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="v1.21",
    version="v1.21.0-alpha.0",
    major="1",
    minor="21",
    patch="0",
    pre_release="alpha.0",
    build="",
    created_at=_datetime.datetime(2020, 12, 8),
    commit_sha="98bc258bf5516b6c60860e06845b899eab29825d",
)
import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="latest",
    version="v1.20.0",
    major="1",
    minor="20",
    patch="0",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 17),
    commit_sha="af46c47ce925f4c4ad5cc8d1fca46c7b77d13b38",
)

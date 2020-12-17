import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="v1.17",
    version="v1.17.15",
    major="1",
    minor="17",
    patch="15",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 17),
    commit_sha="737e2c461a2999fa242d39e77b9252d0eee7167e",
)

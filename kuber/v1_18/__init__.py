import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.18",
    version="v1.18.14",
    major="1",
    minor="18",
    patch="14",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 31),
    commit_sha="89182bdd065fbcaffefec691908a739d161efc03",
)

import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="v1.19",
    version="v1.19.5",
    major="1",
    minor="19",
    patch="5",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 17),
    commit_sha="e338cf2c6d297aa603b50ad3a301f761b4173aa6",
)

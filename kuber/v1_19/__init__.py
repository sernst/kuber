import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.19",
    version="v1.19.6",
    major="1",
    minor="19",
    patch="6",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 31),
    commit_sha="fbf646b339dc52336b55d8ec85c181981b86331a",
)

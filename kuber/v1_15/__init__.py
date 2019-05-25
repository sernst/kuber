import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.0-beta.0',
    major='1',
    minor='15',
    patch='0',
    pre_release='beta.0',
    build='',
    created_at=_datetime.datetime(2019, 5, 25),
    commit_sha='bde05a518c62656c7d368e55bb70dcf41a6ec074'
)

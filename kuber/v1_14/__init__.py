import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.14',
    version='v1.14.4',
    major='1',
    minor='14',
    patch='4',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 3),
    commit_sha='a87e9a978f65a8303aa9467537aa59c18122cbf9'
)

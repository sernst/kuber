import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.latest.meta_v1 import LabelSelector
from kuber.latest.meta_v1 import ListMeta
from kuber.latest.meta_v1 import MicroTime
from kuber.latest.meta_v1 import ObjectMeta
from kuber.latest.meta_v1 import Status
from kuber.latest.meta_v1 import StatusDetails


class AWSElasticBlockStoreVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Persistent Disk resource in AWS.

    An AWS EBS
    disk must exist before mounting to a container. The disk
    must also be in the same AWS zone as the kubelet. An AWS EBS
    disk can only be mounted as read/write once. AWS EBS volumes
    support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            partition: int = None,
            read_only: bool = None,
            volume_id: str = None,
    ):
        """Create AWSElasticBlockStoreVolumeSource instance."""
        super(AWSElasticBlockStoreVolumeSource, self).__init__(
            api_version='core/v1',
            kind='AWSElasticBlockStoreVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'partition': partition or None,
            'readOnly': read_only or None,
            'volumeID': volume_id or '',

        }
        self._types = {
            'fsType': (str, None),
            'partition': (int, None),
            'readOnly': (bool, None),
            'volumeID': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#awselast
        icblockstore
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#awselast
        icblockstore
        """
        self._properties['fsType'] = value

    @property
    def partition(self) -> int:
        """
        The partition in the volume that you want to mount. If
        omitted, the default is to mount by volume name. Examples:
        For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you
        can leave the property empty).
        """
        return self._properties.get('partition')

    @partition.setter
    def partition(self, value: int):
        """
        The partition in the volume that you want to mount. If
        omitted, the default is to mount by volume name. Examples:
        For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you
        can leave the property empty).
        """
        self._properties['partition'] = value

    @property
    def read_only(self) -> bool:
        """
        Specify "true" to force and set the ReadOnly property in
        VolumeMounts to "true". If omitted, the default is "false".
        More info: https://kubernetes.io/docs/concepts/storage/volum
        es#awselasticblockstore
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Specify "true" to force and set the ReadOnly property in
        VolumeMounts to "true". If omitted, the default is "false".
        More info: https://kubernetes.io/docs/concepts/storage/volum
        es#awselasticblockstore
        """
        self._properties['readOnly'] = value

    @property
    def volume_id(self) -> str:
        """
        Unique ID of the persistent disk resource in AWS (Amazon EBS
        volume). More info: https://kubernetes.io/docs/concepts/stor
        age/volumes#awselasticblockstore
        """
        return self._properties.get('volumeID')

    @volume_id.setter
    def volume_id(self, value: str):
        """
        Unique ID of the persistent disk resource in AWS (Amazon EBS
        volume). More info: https://kubernetes.io/docs/concepts/stor
        age/volumes#awselasticblockstore
        """
        self._properties['volumeID'] = value

    def __enter__(self) -> 'AWSElasticBlockStoreVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Affinity(_kuber_definitions.Definition):
    """
    Affinity is a group of affinity scheduling rules.
    """

    def __init__(
            self,
            node_affinity: 'NodeAffinity' = None,
            pod_affinity: 'PodAffinity' = None,
            pod_anti_affinity: 'PodAntiAffinity' = None,
    ):
        """Create Affinity instance."""
        super(Affinity, self).__init__(
            api_version='core/v1',
            kind='Affinity'
        )
        self._properties = {
            'nodeAffinity': node_affinity or NodeAffinity(),
            'podAffinity': pod_affinity or PodAffinity(),
            'podAntiAffinity': pod_anti_affinity or PodAntiAffinity(),

        }
        self._types = {
            'nodeAffinity': (NodeAffinity, None),
            'podAffinity': (PodAffinity, None),
            'podAntiAffinity': (PodAntiAffinity, None),

        }

    @property
    def node_affinity(self) -> 'NodeAffinity':
        """
        Describes node affinity scheduling rules for the pod.
        """
        return self._properties.get('nodeAffinity')

    @node_affinity.setter
    def node_affinity(self, value: typing.Union['NodeAffinity', dict]):
        """
        Describes node affinity scheduling rules for the pod.
        """
        if isinstance(value, dict):
            value = NodeAffinity().from_dict(value)
        self._properties['nodeAffinity'] = value

    @property
    def pod_affinity(self) -> 'PodAffinity':
        """
        Describes pod affinity scheduling rules (e.g. co-locate this
        pod in the same node, zone, etc. as some other pod(s)).
        """
        return self._properties.get('podAffinity')

    @pod_affinity.setter
    def pod_affinity(self, value: typing.Union['PodAffinity', dict]):
        """
        Describes pod affinity scheduling rules (e.g. co-locate this
        pod in the same node, zone, etc. as some other pod(s)).
        """
        if isinstance(value, dict):
            value = PodAffinity().from_dict(value)
        self._properties['podAffinity'] = value

    @property
    def pod_anti_affinity(self) -> 'PodAntiAffinity':
        """
        Describes pod anti-affinity scheduling rules (e.g. avoid
        putting this pod in the same node, zone, etc. as some other
        pod(s)).
        """
        return self._properties.get('podAntiAffinity')

    @pod_anti_affinity.setter
    def pod_anti_affinity(self, value: typing.Union['PodAntiAffinity', dict]):
        """
        Describes pod anti-affinity scheduling rules (e.g. avoid
        putting this pod in the same node, zone, etc. as some other
        pod(s)).
        """
        if isinstance(value, dict):
            value = PodAntiAffinity().from_dict(value)
        self._properties['podAntiAffinity'] = value

    def __enter__(self) -> 'Affinity':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AttachedVolume(_kuber_definitions.Definition):
    """
    AttachedVolume describes a volume attached to a node
    """

    def __init__(
            self,
            device_path: str = None,
            name: str = None,
    ):
        """Create AttachedVolume instance."""
        super(AttachedVolume, self).__init__(
            api_version='core/v1',
            kind='AttachedVolume'
        )
        self._properties = {
            'devicePath': device_path or '',
            'name': name or '',

        }
        self._types = {
            'devicePath': (str, None),
            'name': (str, None),

        }

    @property
    def device_path(self) -> str:
        """
        DevicePath represents the device path where the volume
        should be available
        """
        return self._properties.get('devicePath')

    @device_path.setter
    def device_path(self, value: str):
        """
        DevicePath represents the device path where the volume
        should be available
        """
        self._properties['devicePath'] = value

    @property
    def name(self) -> str:
        """
        Name of the attached volume
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the attached volume
        """
        self._properties['name'] = value

    def __enter__(self) -> 'AttachedVolume':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AzureDiskVolumeSource(_kuber_definitions.Definition):
    """
    AzureDisk represents an Azure Data Disk mount on the host
    and bind mount to the pod.
    """

    def __init__(
            self,
            caching_mode: str = None,
            disk_name: str = None,
            disk_uri: str = None,
            fs_type: str = None,
            kind: str = None,
            read_only: bool = None,
    ):
        """Create AzureDiskVolumeSource instance."""
        super(AzureDiskVolumeSource, self).__init__(
            api_version='core/v1',
            kind='AzureDiskVolumeSource'
        )
        self._properties = {
            'cachingMode': caching_mode or '',
            'diskName': disk_name or '',
            'diskURI': disk_uri or '',
            'fsType': fs_type or '',
            'kind': kind or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'cachingMode': (str, None),
            'diskName': (str, None),
            'diskURI': (str, None),
            'fsType': (str, None),
            'kind': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def caching_mode(self) -> str:
        """
        Host Caching mode: None, Read Only, Read Write.
        """
        return self._properties.get('cachingMode')

    @caching_mode.setter
    def caching_mode(self, value: str):
        """
        Host Caching mode: None, Read Only, Read Write.
        """
        self._properties['cachingMode'] = value

    @property
    def disk_name(self) -> str:
        """
        The Name of the data disk in the blob storage
        """
        return self._properties.get('diskName')

    @disk_name.setter
    def disk_name(self, value: str):
        """
        The Name of the data disk in the blob storage
        """
        self._properties['diskName'] = value

    @property
    def disk_uri(self) -> str:
        """
        The URI the data disk in the blob storage
        """
        return self._properties.get('diskURI')

    @disk_uri.setter
    def disk_uri(self, value: str):
        """
        The URI the data disk in the blob storage
        """
        self._properties['diskURI'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def kind(self) -> str:
        """
        Expected values Shared: multiple blob disks per storage
        account  Dedicated: single blob disk per storage account
        Managed: azure managed data disk (only in managed
        availability set). defaults to shared
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Expected values Shared: multiple blob disks per storage
        account  Dedicated: single blob disk per storage account
        Managed: azure managed data disk (only in managed
        availability set). defaults to shared
        """
        self._properties['kind'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'AzureDiskVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AzureFilePersistentVolumeSource(_kuber_definitions.Definition):
    """
    AzureFile represents an Azure File Service mount on the host
    and bind mount to the pod.
    """

    def __init__(
            self,
            read_only: bool = None,
            secret_name: str = None,
            secret_namespace: str = None,
            share_name: str = None,
    ):
        """Create AzureFilePersistentVolumeSource instance."""
        super(AzureFilePersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='AzureFilePersistentVolumeSource'
        )
        self._properties = {
            'readOnly': read_only or None,
            'secretName': secret_name or '',
            'secretNamespace': secret_namespace or '',
            'shareName': share_name or '',

        }
        self._types = {
            'readOnly': (bool, None),
            'secretName': (str, None),
            'secretNamespace': (str, None),
            'shareName': (str, None),

        }

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_name(self) -> str:
        """
        the name of secret that contains Azure Storage Account Name
        and Key
        """
        return self._properties.get('secretName')

    @secret_name.setter
    def secret_name(self, value: str):
        """
        the name of secret that contains Azure Storage Account Name
        and Key
        """
        self._properties['secretName'] = value

    @property
    def secret_namespace(self) -> str:
        """
        the namespace of the secret that contains Azure Storage
        Account Name and Key default is the same as the Pod
        """
        return self._properties.get('secretNamespace')

    @secret_namespace.setter
    def secret_namespace(self, value: str):
        """
        the namespace of the secret that contains Azure Storage
        Account Name and Key default is the same as the Pod
        """
        self._properties['secretNamespace'] = value

    @property
    def share_name(self) -> str:
        """
        Share Name
        """
        return self._properties.get('shareName')

    @share_name.setter
    def share_name(self, value: str):
        """
        Share Name
        """
        self._properties['shareName'] = value

    def __enter__(self) -> 'AzureFilePersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AzureFileVolumeSource(_kuber_definitions.Definition):
    """
    AzureFile represents an Azure File Service mount on the host
    and bind mount to the pod.
    """

    def __init__(
            self,
            read_only: bool = None,
            secret_name: str = None,
            share_name: str = None,
    ):
        """Create AzureFileVolumeSource instance."""
        super(AzureFileVolumeSource, self).__init__(
            api_version='core/v1',
            kind='AzureFileVolumeSource'
        )
        self._properties = {
            'readOnly': read_only or None,
            'secretName': secret_name or '',
            'shareName': share_name or '',

        }
        self._types = {
            'readOnly': (bool, None),
            'secretName': (str, None),
            'shareName': (str, None),

        }

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_name(self) -> str:
        """
        the name of secret that contains Azure Storage Account Name
        and Key
        """
        return self._properties.get('secretName')

    @secret_name.setter
    def secret_name(self, value: str):
        """
        the name of secret that contains Azure Storage Account Name
        and Key
        """
        self._properties['secretName'] = value

    @property
    def share_name(self) -> str:
        """
        Share Name
        """
        return self._properties.get('shareName')

    @share_name.setter
    def share_name(self, value: str):
        """
        Share Name
        """
        self._properties['shareName'] = value

    def __enter__(self) -> 'AzureFileVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Binding(_kuber_definitions.Resource):
    """
    Binding ties one object to another; for example, a pod is
    bound to a node by a scheduler. Deprecated in 1.7, please
    use the bindings subresource of pods instead.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            target: 'ObjectReference' = None,
    ):
        """Create Binding instance."""
        super(Binding, self).__init__(
            api_version='core/v1',
            kind='Binding'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'target': target or ObjectReference(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'target': (ObjectReference, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def target(self) -> 'ObjectReference':
        """
        The target object that you want to bind to the standard
        object.
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['ObjectReference', dict]):
        """
        The target object that you want to bind to the standard
        object.
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['target'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Binding in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_binding',
            'create_binding'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the Binding in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_binding',
            'replace_binding'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the Binding in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_binding',
            'patch_binding'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Binding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_binding',
            'read_binding'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Binding from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_binding',
            'delete_binding'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Binding':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents storage that is managed by an external CSI volume
    driver (Beta feature)
    """

    def __init__(
            self,
            controller_publish_secret_ref: 'SecretReference' = None,
            driver: str = None,
            fs_type: str = None,
            node_publish_secret_ref: 'SecretReference' = None,
            node_stage_secret_ref: 'SecretReference' = None,
            read_only: bool = None,
            volume_attributes: dict = None,
            volume_handle: str = None,
    ):
        """Create CSIPersistentVolumeSource instance."""
        super(CSIPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CSIPersistentVolumeSource'
        )
        self._properties = {
            'controllerPublishSecretRef': controller_publish_secret_ref or SecretReference(),
            'driver': driver or '',
            'fsType': fs_type or '',
            'nodePublishSecretRef': node_publish_secret_ref or SecretReference(),
            'nodeStageSecretRef': node_stage_secret_ref or SecretReference(),
            'readOnly': read_only or None,
            'volumeAttributes': volume_attributes or {},
            'volumeHandle': volume_handle or '',

        }
        self._types = {
            'controllerPublishSecretRef': (SecretReference, None),
            'driver': (str, None),
            'fsType': (str, None),
            'nodePublishSecretRef': (SecretReference, None),
            'nodeStageSecretRef': (SecretReference, None),
            'readOnly': (bool, None),
            'volumeAttributes': (dict, None),
            'volumeHandle': (str, None),

        }

    @property
    def controller_publish_secret_ref(self) -> 'SecretReference':
        """
        ControllerPublishSecretRef is a reference to the secret
        object containing sensitive information to pass to the CSI
        driver to complete the CSI ControllerPublishVolume and
        ControllerUnpublishVolume calls. This field is optional, and
        may be empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        return self._properties.get('controllerPublishSecretRef')

    @controller_publish_secret_ref.setter
    def controller_publish_secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        ControllerPublishSecretRef is a reference to the secret
        object containing sensitive information to pass to the CSI
        driver to complete the CSI ControllerPublishVolume and
        ControllerUnpublishVolume calls. This field is optional, and
        may be empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['controllerPublishSecretRef'] = value

    @property
    def driver(self) -> str:
        """
        Driver is the name of the driver to use for this volume.
        Required.
        """
        return self._properties.get('driver')

    @driver.setter
    def driver(self, value: str):
        """
        Driver is the name of the driver to use for this volume.
        Required.
        """
        self._properties['driver'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs".
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs".
        """
        self._properties['fsType'] = value

    @property
    def node_publish_secret_ref(self) -> 'SecretReference':
        """
        NodePublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodePublishVolume and
        NodeUnpublishVolume calls. This field is optional, and may
        be empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        return self._properties.get('nodePublishSecretRef')

    @node_publish_secret_ref.setter
    def node_publish_secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        NodePublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodePublishVolume and
        NodeUnpublishVolume calls. This field is optional, and may
        be empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['nodePublishSecretRef'] = value

    @property
    def node_stage_secret_ref(self) -> 'SecretReference':
        """
        NodeStageSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodeStageVolume and NodeStageVolume and
        NodeUnstageVolume calls. This field is optional, and may be
        empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        return self._properties.get('nodeStageSecretRef')

    @node_stage_secret_ref.setter
    def node_stage_secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        NodeStageSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodeStageVolume and NodeStageVolume and
        NodeUnstageVolume calls. This field is optional, and may be
        empty if no secret is required. If the secret object
        contains more than one secret, all secrets are passed.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['nodeStageSecretRef'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: The value to pass to
        ControllerPublishVolumeRequest. Defaults to false
        (read/write).
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: The value to pass to
        ControllerPublishVolumeRequest. Defaults to false
        (read/write).
        """
        self._properties['readOnly'] = value

    @property
    def volume_attributes(self) -> dict:
        """
        Attributes of the volume to publish.
        """
        return self._properties.get('volumeAttributes')

    @volume_attributes.setter
    def volume_attributes(self, value: dict):
        """
        Attributes of the volume to publish.
        """
        self._properties['volumeAttributes'] = value

    @property
    def volume_handle(self) -> str:
        """
        VolumeHandle is the unique volume name returned by the CSI
        volume plugins CreateVolume to refer to the volume on all
        subsequent calls. Required.
        """
        return self._properties.get('volumeHandle')

    @volume_handle.setter
    def volume_handle(self, value: str):
        """
        VolumeHandle is the unique volume name returned by the CSI
        volume plugins CreateVolume to refer to the volume on all
        subsequent calls. Required.
        """
        self._properties['volumeHandle'] = value

    def __enter__(self) -> 'CSIPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIVolumeSource(_kuber_definitions.Definition):
    """
    Represents a source location of a volume to mount, managed
    by an external CSI driver
    """

    def __init__(
            self,
            driver: str = None,
            fs_type: str = None,
            node_publish_secret_ref: 'LocalObjectReference' = None,
            read_only: bool = None,
            volume_attributes: dict = None,
    ):
        """Create CSIVolumeSource instance."""
        super(CSIVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CSIVolumeSource'
        )
        self._properties = {
            'driver': driver or '',
            'fsType': fs_type or '',
            'nodePublishSecretRef': node_publish_secret_ref or LocalObjectReference(),
            'readOnly': read_only or None,
            'volumeAttributes': volume_attributes or {},

        }
        self._types = {
            'driver': (str, None),
            'fsType': (str, None),
            'nodePublishSecretRef': (LocalObjectReference, None),
            'readOnly': (bool, None),
            'volumeAttributes': (dict, None),

        }

    @property
    def driver(self) -> str:
        """
        Driver is the name of the CSI driver that handles this
        volume. Consult with your admin for the correct name as
        registered in the cluster.
        """
        return self._properties.get('driver')

    @driver.setter
    def driver(self, value: str):
        """
        Driver is the name of the CSI driver that handles this
        volume. Consult with your admin for the correct name as
        registered in the cluster.
        """
        self._properties['driver'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not
        provided, the empty value is passed to the associated CSI
        driver which will determine the default filesystem to apply.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not
        provided, the empty value is passed to the associated CSI
        driver which will determine the default filesystem to apply.
        """
        self._properties['fsType'] = value

    @property
    def node_publish_secret_ref(self) -> 'LocalObjectReference':
        """
        NodePublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodePublishVolume and
        NodeUnpublishVolume calls. This field is optional, and  may
        be empty if no secret is required. If the secret object
        contains more than one secret, all secret references are
        passed.
        """
        return self._properties.get('nodePublishSecretRef')

    @node_publish_secret_ref.setter
    def node_publish_secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        NodePublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver
        to complete the CSI NodePublishVolume and
        NodeUnpublishVolume calls. This field is optional, and  may
        be empty if no secret is required. If the secret object
        contains more than one secret, all secret references are
        passed.
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['nodePublishSecretRef'] = value

    @property
    def read_only(self) -> bool:
        """
        Specifies a read-only configuration for the volume. Defaults
        to false (read/write).
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Specifies a read-only configuration for the volume. Defaults
        to false (read/write).
        """
        self._properties['readOnly'] = value

    @property
    def volume_attributes(self) -> dict:
        """
        VolumeAttributes stores driver-specific properties that are
        passed to the CSI driver. Consult your driver's
        documentation for supported values.
        """
        return self._properties.get('volumeAttributes')

    @volume_attributes.setter
    def volume_attributes(self, value: dict):
        """
        VolumeAttributes stores driver-specific properties that are
        passed to the CSI driver. Consult your driver's
        documentation for supported values.
        """
        self._properties['volumeAttributes'] = value

    def __enter__(self) -> 'CSIVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Capabilities(_kuber_definitions.Definition):
    """
    Adds and removes POSIX capabilities from running containers.
    """

    def __init__(
            self,
            add: typing.List[str] = None,
            drop: typing.List[str] = None,
    ):
        """Create Capabilities instance."""
        super(Capabilities, self).__init__(
            api_version='core/v1',
            kind='Capabilities'
        )
        self._properties = {
            'add': add or [],
            'drop': drop or [],

        }
        self._types = {
            'add': (list, str),
            'drop': (list, str),

        }

    @property
    def add(self) -> typing.List[str]:
        """
        Added capabilities
        """
        return self._properties.get('add')

    @add.setter
    def add(self, value: typing.List[str]):
        """
        Added capabilities
        """
        self._properties['add'] = value

    @property
    def drop(self) -> typing.List[str]:
        """
        Removed capabilities
        """
        return self._properties.get('drop')

    @drop.setter
    def drop(self, value: typing.List[str]):
        """
        Removed capabilities
        """
        self._properties['drop'] = value

    def __enter__(self) -> 'Capabilities':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CephFSPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime
    of a pod Cephfs volumes do not support ownership management
    or SELinux relabeling.
    """

    def __init__(
            self,
            monitors: typing.List[str] = None,
            path: str = None,
            read_only: bool = None,
            secret_file: str = None,
            secret_ref: 'SecretReference' = None,
            user: str = None,
    ):
        """Create CephFSPersistentVolumeSource instance."""
        super(CephFSPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CephFSPersistentVolumeSource'
        )
        self._properties = {
            'monitors': monitors or [],
            'path': path or '',
            'readOnly': read_only or None,
            'secretFile': secret_file or '',
            'secretRef': secret_ref or SecretReference(),
            'user': user or '',

        }
        self._types = {
            'monitors': (list, str),
            'path': (str, None),
            'readOnly': (bool, None),
            'secretFile': (str, None),
            'secretRef': (SecretReference, None),
            'user': (str, None),

        }

    @property
    def monitors(self) -> typing.List[str]:
        """
        Required: Monitors is a collection of Ceph monitors More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        return self._properties.get('monitors')

    @monitors.setter
    def monitors(self, value: typing.List[str]):
        """
        Required: Monitors is a collection of Ceph monitors More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        self._properties['monitors'] = value

    @property
    def path(self) -> str:
        """
        Optional: Used as the mounted root, rather than the full
        Ceph tree, default is /
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Optional: Used as the mounted root, rather than the full
        Ceph tree, default is /
        """
        self._properties['path'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info: https
        ://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#ho
        w-to-use-it
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info: https
        ://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#ho
        w-to-use-it
        """
        self._properties['readOnly'] = value

    @property
    def secret_file(self) -> str:
        """
        Optional: SecretFile is the path to key ring for User,
        default is /etc/ceph/user.secret More info: https://releases
        .k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it
        """
        return self._properties.get('secretFile')

    @secret_file.setter
    def secret_file(self, value: str):
        """
        Optional: SecretFile is the path to key ring for User,
        default is /etc/ceph/user.secret More info: https://releases
        .k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it
        """
        self._properties['secretFile'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        Optional: SecretRef is reference to the authentication
        secret for User, default is empty. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-
        it
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        Optional: SecretRef is reference to the authentication
        secret for User, default is empty. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-
        it
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def user(self) -> str:
        """
        Optional: User is the rados user name, default is admin More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        Optional: User is the rados user name, default is admin More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        self._properties['user'] = value

    def __enter__(self) -> 'CephFSPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CephFSVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime
    of a pod Cephfs volumes do not support ownership management
    or SELinux relabeling.
    """

    def __init__(
            self,
            monitors: typing.List[str] = None,
            path: str = None,
            read_only: bool = None,
            secret_file: str = None,
            secret_ref: 'LocalObjectReference' = None,
            user: str = None,
    ):
        """Create CephFSVolumeSource instance."""
        super(CephFSVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CephFSVolumeSource'
        )
        self._properties = {
            'monitors': monitors or [],
            'path': path or '',
            'readOnly': read_only or None,
            'secretFile': secret_file or '',
            'secretRef': secret_ref or LocalObjectReference(),
            'user': user or '',

        }
        self._types = {
            'monitors': (list, str),
            'path': (str, None),
            'readOnly': (bool, None),
            'secretFile': (str, None),
            'secretRef': (LocalObjectReference, None),
            'user': (str, None),

        }

    @property
    def monitors(self) -> typing.List[str]:
        """
        Required: Monitors is a collection of Ceph monitors More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        return self._properties.get('monitors')

    @monitors.setter
    def monitors(self, value: typing.List[str]):
        """
        Required: Monitors is a collection of Ceph monitors More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        self._properties['monitors'] = value

    @property
    def path(self) -> str:
        """
        Optional: Used as the mounted root, rather than the full
        Ceph tree, default is /
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Optional: Used as the mounted root, rather than the full
        Ceph tree, default is /
        """
        self._properties['path'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info: https
        ://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#ho
        w-to-use-it
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info: https
        ://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#ho
        w-to-use-it
        """
        self._properties['readOnly'] = value

    @property
    def secret_file(self) -> str:
        """
        Optional: SecretFile is the path to key ring for User,
        default is /etc/ceph/user.secret More info: https://releases
        .k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it
        """
        return self._properties.get('secretFile')

    @secret_file.setter
    def secret_file(self, value: str):
        """
        Optional: SecretFile is the path to key ring for User,
        default is /etc/ceph/user.secret More info: https://releases
        .k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it
        """
        self._properties['secretFile'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        Optional: SecretRef is reference to the authentication
        secret for User, default is empty. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-
        it
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        Optional: SecretRef is reference to the authentication
        secret for User, default is empty. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-
        it
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def user(self) -> str:
        """
        Optional: User is the rados user name, default is admin More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        Optional: User is the rados user name, default is admin More
        info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/R
        EADME.md#how-to-use-it
        """
        self._properties['user'] = value

    def __enter__(self) -> 'CephFSVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CinderPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents a cinder volume resource in Openstack. A Cinder
    volume must exist before mounting to a container. The volume
    must also be in the same region as the kubelet. Cinder
    volumes support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            read_only: bool = None,
            secret_ref: 'SecretReference' = None,
            volume_id: str = None,
    ):
        """Create CinderPersistentVolumeSource instance."""
        super(CinderPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CinderPersistentVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or SecretReference(),
            'volumeID': volume_id or '',

        }
        self._types = {
            'fsType': (str, None),
            'readOnly': (bool, None),
            'secretRef': (SecretReference, None),
            'volumeID': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Examples: "ext4",
        "xfs", "ntfs". Implicitly inferred to be "ext4" if
        unspecified. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Examples: "ext4",
        "xfs", "ntfs". Implicitly inferred to be "ext4" if
        unspecified. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['fsType'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        Optional: points to a secret object containing parameters
        used to connect to OpenStack.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        Optional: points to a secret object containing parameters
        used to connect to OpenStack.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def volume_id(self) -> str:
        """
        volume id used to identify the volume in cinder More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('volumeID')

    @volume_id.setter
    def volume_id(self, value: str):
        """
        volume id used to identify the volume in cinder More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['volumeID'] = value

    def __enter__(self) -> 'CinderPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CinderVolumeSource(_kuber_definitions.Definition):
    """
    Represents a cinder volume resource in Openstack. A Cinder
    volume must exist before mounting to a container. The volume
    must also be in the same region as the kubelet. Cinder
    volumes support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
            volume_id: str = None,
    ):
        """Create CinderVolumeSource instance."""
        super(CinderVolumeSource, self).__init__(
            api_version='core/v1',
            kind='CinderVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),
            'volumeID': volume_id or '',

        }
        self._types = {
            'fsType': (str, None),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),
            'volumeID': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Examples: "ext4",
        "xfs", "ntfs". Implicitly inferred to be "ext4" if
        unspecified. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Examples: "ext4",
        "xfs", "ntfs". Implicitly inferred to be "ext4" if
        unspecified. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['fsType'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts. More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        Optional: points to a secret object containing parameters
        used to connect to OpenStack.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        Optional: points to a secret object containing parameters
        used to connect to OpenStack.
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def volume_id(self) -> str:
        """
        volume id used to identify the volume in cinder More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('volumeID')

    @volume_id.setter
    def volume_id(self, value: str):
        """
        volume id used to identify the volume in cinder More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        self._properties['volumeID'] = value

    def __enter__(self) -> 'CinderVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClientIPConfig(_kuber_definitions.Definition):
    """
    ClientIPConfig represents the configurations of Client IP
    based session affinity.
    """

    def __init__(
            self,
            timeout_seconds: int = None,
    ):
        """Create ClientIPConfig instance."""
        super(ClientIPConfig, self).__init__(
            api_version='core/v1',
            kind='ClientIPConfig'
        )
        self._properties = {
            'timeoutSeconds': timeout_seconds or None,

        }
        self._types = {
            'timeoutSeconds': (int, None),

        }

    @property
    def timeout_seconds(self) -> int:
        """
        timeoutSeconds specifies the seconds of ClientIP type
        session sticky time. The value must be >0 && <=86400(for 1
        day) if ServiceAffinity == "ClientIP". Default value is
        10800(for 3 hours).
        """
        return self._properties.get('timeoutSeconds')

    @timeout_seconds.setter
    def timeout_seconds(self, value: int):
        """
        timeoutSeconds specifies the seconds of ClientIP type
        session sticky time. The value must be >0 && <=86400(for 1
        day) if ServiceAffinity == "ClientIP". Default value is
        10800(for 3 hours).
        """
        self._properties['timeoutSeconds'] = value

    def __enter__(self) -> 'ClientIPConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ComponentCondition(_kuber_definitions.Definition):
    """
    Information about the condition of a component.
    """

    def __init__(
            self,
            error: str = None,
            message: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create ComponentCondition instance."""
        super(ComponentCondition, self).__init__(
            api_version='core/v1',
            kind='ComponentCondition'
        )
        self._properties = {
            'error': error or '',
            'message': message or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'error': (str, None),
            'message': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def error(self) -> str:
        """
        Condition error code for a component. For example, a health
        check error code.
        """
        return self._properties.get('error')

    @error.setter
    def error(self, value: str):
        """
        Condition error code for a component. For example, a health
        check error code.
        """
        self._properties['error'] = value

    @property
    def message(self) -> str:
        """
        Message about the condition for a component. For example,
        information about a health check.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Message about the condition for a component. For example,
        information about a health check.
        """
        self._properties['message'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition for a component. Valid values for
        "Healthy": "True", "False", or "Unknown".
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition for a component. Valid values for
        "Healthy": "True", "False", or "Unknown".
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of condition for a component. Valid value: "Healthy"
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of condition for a component. Valid value: "Healthy"
        """
        self._properties['type'] = value

    def __enter__(self) -> 'ComponentCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ComponentStatus(_kuber_definitions.Resource):
    """
    ComponentStatus (and ComponentStatusList) holds the cluster
    validation info.
    """

    def __init__(
            self,
            conditions: typing.List['ComponentCondition'] = None,
            metadata: 'ObjectMeta' = None,
    ):
        """Create ComponentStatus instance."""
        super(ComponentStatus, self).__init__(
            api_version='core/v1',
            kind='ComponentStatus'
        )
        self._properties = {
            'conditions': conditions or [],
            'metadata': metadata or ObjectMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'conditions': (list, ComponentCondition),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),

        }

    @property
    def conditions(self) -> typing.List['ComponentCondition']:
        """
        List of component conditions observed
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['ComponentCondition'], typing.List[dict]]
    ):
        """
        List of component conditions observed
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ComponentCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the ComponentStatus in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_component_status',
            'create_component_status'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the ComponentStatus in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_component_status',
            'replace_component_status'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the ComponentStatus in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_component_status',
            'patch_component_status'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ComponentStatus from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_component_status',
            'read_component_status'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the ComponentStatus from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_component_status',
            'delete_component_status'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ComponentStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ComponentStatusList(_kuber_definitions.Collection):
    """
    Status of all the conditions for the component as a list of
    ComponentStatus objects.
    """

    def __init__(
            self,
            items: typing.List['ComponentStatus'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ComponentStatusList instance."""
        super(ComponentStatusList, self).__init__(
            api_version='core/v1',
            kind='ComponentStatusList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ComponentStatus),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ComponentStatus']:
        """
        List of ComponentStatus objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ComponentStatus'], typing.List[dict]]
    ):
        """
        List of ComponentStatus objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ComponentStatus().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ComponentStatusList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMap(_kuber_definitions.Resource):
    """
    ConfigMap holds configuration data for pods to consume.
    """

    def __init__(
            self,
            binary_data: dict = None,
            data: dict = None,
            metadata: 'ObjectMeta' = None,
    ):
        """Create ConfigMap instance."""
        super(ConfigMap, self).__init__(
            api_version='core/v1',
            kind='ConfigMap'
        )
        self._properties = {
            'binaryData': binary_data or {},
            'data': data or {},
            'metadata': metadata or ObjectMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'binaryData': (dict, None),
            'data': (dict, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),

        }

    @property
    def binary_data(self) -> dict:
        """
        BinaryData contains the binary data. Each key must consist
        of alphanumeric characters, '-', '_' or '.'. BinaryData can
        contain byte sequences that are not in the UTF-8 range. The
        keys stored in BinaryData must not overlap with the ones in
        the Data field, this is enforced during validation process.
        Using this field will require 1.10+ apiserver and kubelet.
        """
        return self._properties.get('binaryData')

    @binary_data.setter
    def binary_data(self, value: dict):
        """
        BinaryData contains the binary data. Each key must consist
        of alphanumeric characters, '-', '_' or '.'. BinaryData can
        contain byte sequences that are not in the UTF-8 range. The
        keys stored in BinaryData must not overlap with the ones in
        the Data field, this is enforced during validation process.
        Using this field will require 1.10+ apiserver and kubelet.
        """
        self._properties['binaryData'] = value

    @property
    def data(self) -> dict:
        """
        Data contains the configuration data. Each key must consist
        of alphanumeric characters, '-', '_' or '.'. Values with
        non-UTF-8 byte sequences must use the BinaryData field. The
        keys stored in Data must not overlap with the keys in the
        BinaryData field, this is enforced during validation
        process.
        """
        return self._properties.get('data')

    @data.setter
    def data(self, value: dict):
        """
        Data contains the configuration data. Each key must consist
        of alphanumeric characters, '-', '_' or '.'. Values with
        non-UTF-8 byte sequences must use the BinaryData field. The
        keys stored in Data must not overlap with the keys in the
        BinaryData field, this is enforced during validation
        process.
        """
        self._properties['data'] = value

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the ConfigMap in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_config_map',
            'create_config_map'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the ConfigMap in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_config_map',
            'replace_config_map'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the ConfigMap in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_config_map',
            'patch_config_map'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ConfigMap from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_config_map',
            'read_config_map'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the ConfigMap from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_config_map',
            'delete_config_map'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ConfigMap':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapEnvSource(_kuber_definitions.Definition):
    """
    ConfigMapEnvSource selects a ConfigMap to populate the
    environment variables with.

    The contents of the target
    ConfigMap's Data field will represent the key-value pairs as
    environment variables.
    """

    def __init__(
            self,
            name: str = None,
            optional: bool = None,
    ):
        """Create ConfigMapEnvSource instance."""
        super(ConfigMapEnvSource, self).__init__(
            api_version='core/v1',
            kind='ConfigMapEnvSource'
        )
        self._properties = {
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the ConfigMap must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the ConfigMap must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'ConfigMapEnvSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapKeySelector(_kuber_definitions.Definition):
    """
    Selects a key from a ConfigMap.
    """

    def __init__(
            self,
            key: str = None,
            name: str = None,
            optional: bool = None,
    ):
        """Create ConfigMapKeySelector instance."""
        super(ConfigMapKeySelector, self).__init__(
            api_version='core/v1',
            kind='ConfigMapKeySelector'
        )
        self._properties = {
            'key': key or '',
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'key': (str, None),
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def key(self) -> str:
        """
        The key to select.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        The key to select.
        """
        self._properties['key'] = value

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the ConfigMap or it's key must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the ConfigMap or it's key must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'ConfigMapKeySelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapList(_kuber_definitions.Collection):
    """
    ConfigMapList is a resource containing a list of ConfigMap
    objects.
    """

    def __init__(
            self,
            items: typing.List['ConfigMap'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ConfigMapList instance."""
        super(ConfigMapList, self).__init__(
            api_version='core/v1',
            kind='ConfigMapList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ConfigMap),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ConfigMap']:
        """
        Items is the list of ConfigMaps.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ConfigMap'], typing.List[dict]]
    ):
        """
        Items is the list of ConfigMaps.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ConfigMap().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ConfigMapList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapNodeConfigSource(_kuber_definitions.Definition):
    """
    ConfigMapNodeConfigSource contains the information to
    reference a ConfigMap as a config source for the Node.
    """

    def __init__(
            self,
            kubelet_config_key: str = None,
            name: str = None,
            namespace: str = None,
            resource_version: str = None,
            uid: str = None,
    ):
        """Create ConfigMapNodeConfigSource instance."""
        super(ConfigMapNodeConfigSource, self).__init__(
            api_version='core/v1',
            kind='ConfigMapNodeConfigSource'
        )
        self._properties = {
            'kubeletConfigKey': kubelet_config_key or '',
            'name': name or '',
            'namespace': namespace or '',
            'resourceVersion': resource_version or '',
            'uid': uid or '',

        }
        self._types = {
            'kubeletConfigKey': (str, None),
            'name': (str, None),
            'namespace': (str, None),
            'resourceVersion': (str, None),
            'uid': (str, None),

        }

    @property
    def kubelet_config_key(self) -> str:
        """
        KubeletConfigKey declares which key of the referenced
        ConfigMap corresponds to the KubeletConfiguration structure
        This field is required in all cases.
        """
        return self._properties.get('kubeletConfigKey')

    @kubelet_config_key.setter
    def kubelet_config_key(self, value: str):
        """
        KubeletConfigKey declares which key of the referenced
        ConfigMap corresponds to the KubeletConfiguration structure
        This field is required in all cases.
        """
        self._properties['kubeletConfigKey'] = value

    @property
    def name(self) -> str:
        """
        Name is the metadata.name of the referenced ConfigMap. This
        field is required in all cases.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the metadata.name of the referenced ConfigMap. This
        field is required in all cases.
        """
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        Namespace is the metadata.namespace of the referenced
        ConfigMap. This field is required in all cases.
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace is the metadata.namespace of the referenced
        ConfigMap. This field is required in all cases.
        """
        self._properties['namespace'] = value

    @property
    def resource_version(self) -> str:
        """
        ResourceVersion is the metadata.ResourceVersion of the
        referenced ConfigMap. This field is forbidden in Node.Spec,
        and required in Node.Status.
        """
        return self._properties.get('resourceVersion')

    @resource_version.setter
    def resource_version(self, value: str):
        """
        ResourceVersion is the metadata.ResourceVersion of the
        referenced ConfigMap. This field is forbidden in Node.Spec,
        and required in Node.Status.
        """
        self._properties['resourceVersion'] = value

    @property
    def uid(self) -> str:
        """
        UID is the metadata.UID of the referenced ConfigMap. This
        field is forbidden in Node.Spec, and required in
        Node.Status.
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        UID is the metadata.UID of the referenced ConfigMap. This
        field is forbidden in Node.Spec, and required in
        Node.Status.
        """
        self._properties['uid'] = value

    def __enter__(self) -> 'ConfigMapNodeConfigSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapProjection(_kuber_definitions.Definition):
    """
    Adapts a ConfigMap into a projected volume.

    The contents of
    the target ConfigMap's Data field will be presented in a
    projected volume as files using the keys in the Data field
    as the file names, unless the items element is populated
    with specific mappings of keys to paths. Note that this is
    identical to a configmap volume source without the default
    mode.
    """

    def __init__(
            self,
            items: typing.List['KeyToPath'] = None,
            name: str = None,
            optional: bool = None,
    ):
        """Create ConfigMapProjection instance."""
        super(ConfigMapProjection, self).__init__(
            api_version='core/v1',
            kind='ConfigMapProjection'
        )
        self._properties = {
            'items': items or [],
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'items': (list, KeyToPath),
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def items(self) -> typing.List['KeyToPath']:
        """
        If unspecified, each key-value pair in the Data field of the
        referenced ConfigMap will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the ConfigMap, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['KeyToPath'], typing.List[dict]]
    ):
        """
        If unspecified, each key-value pair in the Data field of the
        referenced ConfigMap will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the ConfigMap, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = KeyToPath().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the ConfigMap or it's keys must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the ConfigMap or it's keys must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'ConfigMapProjection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ConfigMapVolumeSource(_kuber_definitions.Definition):
    """
    Adapts a ConfigMap into a volume.

    The contents of the
    target ConfigMap's Data field will be presented in a volume
    as files using the keys in the Data field as the file names,
    unless the items element is populated with specific mappings
    of keys to paths. ConfigMap volumes support ownership
    management and SELinux relabeling.
    """

    def __init__(
            self,
            default_mode: int = None,
            items: typing.List['KeyToPath'] = None,
            name: str = None,
            optional: bool = None,
    ):
        """Create ConfigMapVolumeSource instance."""
        super(ConfigMapVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ConfigMapVolumeSource'
        )
        self._properties = {
            'defaultMode': default_mode or None,
            'items': items or [],
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'defaultMode': (int, None),
            'items': (list, KeyToPath),
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def default_mode(self) -> int:
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        return self._properties.get('defaultMode')

    @default_mode.setter
    def default_mode(self, value: int):
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        self._properties['defaultMode'] = value

    @property
    def items(self) -> typing.List['KeyToPath']:
        """
        If unspecified, each key-value pair in the Data field of the
        referenced ConfigMap will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the ConfigMap, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['KeyToPath'], typing.List[dict]]
    ):
        """
        If unspecified, each key-value pair in the Data field of the
        referenced ConfigMap will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the ConfigMap, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = KeyToPath().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the ConfigMap or it's keys must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the ConfigMap or it's keys must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'ConfigMapVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Container(_kuber_definitions.Definition):
    """
    A single application container that you want to run within a
    pod.
    """

    def __init__(
            self,
            args: typing.List[str] = None,
            command: typing.List[str] = None,
            env: typing.List['EnvVar'] = None,
            env_from: typing.List['EnvFromSource'] = None,
            image: str = None,
            image_pull_policy: str = None,
            lifecycle: 'Lifecycle' = None,
            liveness_probe: 'Probe' = None,
            name: str = None,
            ports: typing.List['ContainerPort'] = None,
            readiness_probe: 'Probe' = None,
            resources: 'ResourceRequirements' = None,
            security_context: 'SecurityContext' = None,
            stdin: bool = None,
            stdin_once: bool = None,
            termination_message_path: str = None,
            termination_message_policy: str = None,
            tty: bool = None,
            volume_devices: typing.List['VolumeDevice'] = None,
            volume_mounts: typing.List['VolumeMount'] = None,
            working_dir: str = None,
    ):
        """Create Container instance."""
        super(Container, self).__init__(
            api_version='core/v1',
            kind='Container'
        )
        self._properties = {
            'args': args or [],
            'command': command or [],
            'env': env or [],
            'envFrom': env_from or [],
            'image': image or '',
            'imagePullPolicy': image_pull_policy or '',
            'lifecycle': lifecycle or Lifecycle(),
            'livenessProbe': liveness_probe or Probe(),
            'name': name or '',
            'ports': ports or [],
            'readinessProbe': readiness_probe or Probe(),
            'resources': resources or ResourceRequirements(),
            'securityContext': security_context or SecurityContext(),
            'stdin': stdin or None,
            'stdinOnce': stdin_once or None,
            'terminationMessagePath': termination_message_path or '',
            'terminationMessagePolicy': termination_message_policy or '',
            'tty': tty or None,
            'volumeDevices': volume_devices or [],
            'volumeMounts': volume_mounts or [],
            'workingDir': working_dir or '',

        }
        self._types = {
            'args': (list, str),
            'command': (list, str),
            'env': (list, EnvVar),
            'envFrom': (list, EnvFromSource),
            'image': (str, None),
            'imagePullPolicy': (str, None),
            'lifecycle': (Lifecycle, None),
            'livenessProbe': (Probe, None),
            'name': (str, None),
            'ports': (list, ContainerPort),
            'readinessProbe': (Probe, None),
            'resources': (ResourceRequirements, None),
            'securityContext': (SecurityContext, None),
            'stdin': (bool, None),
            'stdinOnce': (bool, None),
            'terminationMessagePath': (str, None),
            'terminationMessagePolicy': (str, None),
            'tty': (bool, None),
            'volumeDevices': (list, VolumeDevice),
            'volumeMounts': (list, VolumeMount),
            'workingDir': (str, None),

        }

    @property
    def args(self) -> typing.List[str]:
        """
        Arguments to the entrypoint. The docker image's CMD is used
        if this is not provided. Variable references $(VAR_NAME) are
        expanded using the container's environment. If a variable
        cannot be resolved, the reference in the input string will
        be unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never
        be expanded, regardless of whether the variable exists or
        not. Cannot be updated. More info:
        https://kubernetes.io/docs/tasks/inject-data-
        application/define-command-argument-container/#running-a-
        command-in-a-shell
        """
        return self._properties.get('args')

    @args.setter
    def args(self, value: typing.List[str]):
        """
        Arguments to the entrypoint. The docker image's CMD is used
        if this is not provided. Variable references $(VAR_NAME) are
        expanded using the container's environment. If a variable
        cannot be resolved, the reference in the input string will
        be unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never
        be expanded, regardless of whether the variable exists or
        not. Cannot be updated. More info:
        https://kubernetes.io/docs/tasks/inject-data-
        application/define-command-argument-container/#running-a-
        command-in-a-shell
        """
        self._properties['args'] = value

    @property
    def command(self) -> typing.List[str]:
        """
        Entrypoint array. Not executed within a shell. The docker
        image's ENTRYPOINT is used if this is not provided. Variable
        references $(VAR_NAME) are expanded using the container's
        environment. If a variable cannot be resolved, the reference
        in the input string will be unchanged. The $(VAR_NAME)
        syntax can be escaped with a double $$, ie: $$(VAR_NAME).
        Escaped references will never be expanded, regardless of
        whether the variable exists or not. Cannot be updated. More
        info: https://kubernetes.io/docs/tasks/inject-data-
        application/define-command-argument-container/#running-a-
        command-in-a-shell
        """
        return self._properties.get('command')

    @command.setter
    def command(self, value: typing.List[str]):
        """
        Entrypoint array. Not executed within a shell. The docker
        image's ENTRYPOINT is used if this is not provided. Variable
        references $(VAR_NAME) are expanded using the container's
        environment. If a variable cannot be resolved, the reference
        in the input string will be unchanged. The $(VAR_NAME)
        syntax can be escaped with a double $$, ie: $$(VAR_NAME).
        Escaped references will never be expanded, regardless of
        whether the variable exists or not. Cannot be updated. More
        info: https://kubernetes.io/docs/tasks/inject-data-
        application/define-command-argument-container/#running-a-
        command-in-a-shell
        """
        self._properties['command'] = value

    @property
    def env(self) -> typing.List['EnvVar']:
        """
        List of environment variables to set in the container.
        Cannot be updated.
        """
        return self._properties.get('env')

    @env.setter
    def env(
            self,
            value: typing.Union[typing.List['EnvVar'], typing.List[dict]]
    ):
        """
        List of environment variables to set in the container.
        Cannot be updated.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EnvVar().from_dict(item)
            cleaned.append(item)
        self._properties['env'] = cleaned

    @property
    def env_from(self) -> typing.List['EnvFromSource']:
        """
        List of sources to populate environment variables in the
        container. The keys defined within a source must be a
        C_IDENTIFIER. All invalid keys will be reported as an event
        when the container is starting. When a key exists in
        multiple sources, the value associated with the last source
        will take precedence. Values defined by an Env with a
        duplicate key will take precedence. Cannot be updated.
        """
        return self._properties.get('envFrom')

    @env_from.setter
    def env_from(
            self,
            value: typing.Union[typing.List['EnvFromSource'], typing.List[dict]]
    ):
        """
        List of sources to populate environment variables in the
        container. The keys defined within a source must be a
        C_IDENTIFIER. All invalid keys will be reported as an event
        when the container is starting. When a key exists in
        multiple sources, the value associated with the last source
        will take precedence. Values defined by an Env with a
        duplicate key will take precedence. Cannot be updated.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EnvFromSource().from_dict(item)
            cleaned.append(item)
        self._properties['envFrom'] = cleaned

    @property
    def image(self) -> str:
        """
        Docker image name. More info:
        https://kubernetes.io/docs/concepts/containers/images This
        field is optional to allow higher level config management to
        default or override container images in workload controllers
        like Deployments and StatefulSets.
        """
        return self._properties.get('image')

    @image.setter
    def image(self, value: str):
        """
        Docker image name. More info:
        https://kubernetes.io/docs/concepts/containers/images This
        field is optional to allow higher level config management to
        default or override container images in workload controllers
        like Deployments and StatefulSets.
        """
        self._properties['image'] = value

    @property
    def image_pull_policy(self) -> str:
        """
        Image pull policy. One of Always, Never, IfNotPresent.
        Defaults to Always if :latest tag is specified, or
        IfNotPresent otherwise. Cannot be updated. More info: https:
        //kubernetes.io/docs/concepts/containers/images#updating-
        images
        """
        return self._properties.get('imagePullPolicy')

    @image_pull_policy.setter
    def image_pull_policy(self, value: str):
        """
        Image pull policy. One of Always, Never, IfNotPresent.
        Defaults to Always if :latest tag is specified, or
        IfNotPresent otherwise. Cannot be updated. More info: https:
        //kubernetes.io/docs/concepts/containers/images#updating-
        images
        """
        self._properties['imagePullPolicy'] = value

    @property
    def lifecycle(self) -> 'Lifecycle':
        """
        Actions that the management system should take in response
        to container lifecycle events. Cannot be updated.
        """
        return self._properties.get('lifecycle')

    @lifecycle.setter
    def lifecycle(self, value: typing.Union['Lifecycle', dict]):
        """
        Actions that the management system should take in response
        to container lifecycle events. Cannot be updated.
        """
        if isinstance(value, dict):
            value = Lifecycle().from_dict(value)
        self._properties['lifecycle'] = value

    @property
    def liveness_probe(self) -> 'Probe':
        """
        Periodic probe of container liveness. Container will be
        restarted if the probe fails. Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        return self._properties.get('livenessProbe')

    @liveness_probe.setter
    def liveness_probe(self, value: typing.Union['Probe', dict]):
        """
        Periodic probe of container liveness. Container will be
        restarted if the probe fails. Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        if isinstance(value, dict):
            value = Probe().from_dict(value)
        self._properties['livenessProbe'] = value

    @property
    def name(self) -> str:
        """
        Name of the container specified as a DNS_LABEL. Each
        container in a pod must have a unique name (DNS_LABEL).
        Cannot be updated.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the container specified as a DNS_LABEL. Each
        container in a pod must have a unique name (DNS_LABEL).
        Cannot be updated.
        """
        self._properties['name'] = value

    @property
    def ports(self) -> typing.List['ContainerPort']:
        """
        List of ports to expose from the container. Exposing a port
        here gives the system additional information about the
        network connections a container uses, but is primarily
        informational. Not specifying a port here DOES NOT prevent
        that port from being exposed. Any port which is listening on
        the default "0.0.0.0" address inside a container will be
        accessible from the network. Cannot be updated.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['ContainerPort'], typing.List[dict]]
    ):
        """
        List of ports to expose from the container. Exposing a port
        here gives the system additional information about the
        network connections a container uses, but is primarily
        informational. Not specifying a port here DOES NOT prevent
        that port from being exposed. Any port which is listening on
        the default "0.0.0.0" address inside a container will be
        accessible from the network. Cannot be updated.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ContainerPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    @property
    def readiness_probe(self) -> 'Probe':
        """
        Periodic probe of container service readiness. Container
        will be removed from service endpoints if the probe fails.
        Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        return self._properties.get('readinessProbe')

    @readiness_probe.setter
    def readiness_probe(self, value: typing.Union['Probe', dict]):
        """
        Periodic probe of container service readiness. Container
        will be removed from service endpoints if the probe fails.
        Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        if isinstance(value, dict):
            value = Probe().from_dict(value)
        self._properties['readinessProbe'] = value

    @property
    def resources(self) -> 'ResourceRequirements':
        """
        Compute Resources required by this container. Cannot be
        updated. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        return self._properties.get('resources')

    @resources.setter
    def resources(self, value: typing.Union['ResourceRequirements', dict]):
        """
        Compute Resources required by this container. Cannot be
        updated. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        if isinstance(value, dict):
            value = ResourceRequirements().from_dict(value)
        self._properties['resources'] = value

    @property
    def security_context(self) -> 'SecurityContext':
        """
        Security options the pod should run with. More info:
        https://kubernetes.io/docs/concepts/policy/security-context/
        More info: https://kubernetes.io/docs/tasks/configure-pod-
        container/security-context/
        """
        return self._properties.get('securityContext')

    @security_context.setter
    def security_context(self, value: typing.Union['SecurityContext', dict]):
        """
        Security options the pod should run with. More info:
        https://kubernetes.io/docs/concepts/policy/security-context/
        More info: https://kubernetes.io/docs/tasks/configure-pod-
        container/security-context/
        """
        if isinstance(value, dict):
            value = SecurityContext().from_dict(value)
        self._properties['securityContext'] = value

    @property
    def stdin(self) -> bool:
        """
        Whether this container should allocate a buffer for stdin in
        the container runtime. If this is not set, reads from stdin
        in the container will always result in EOF. Default is
        false.
        """
        return self._properties.get('stdin')

    @stdin.setter
    def stdin(self, value: bool):
        """
        Whether this container should allocate a buffer for stdin in
        the container runtime. If this is not set, reads from stdin
        in the container will always result in EOF. Default is
        false.
        """
        self._properties['stdin'] = value

    @property
    def stdin_once(self) -> bool:
        """
        Whether the container runtime should close the stdin channel
        after it has been opened by a single attach. When stdin is
        true the stdin stream will remain open across multiple
        attach sessions. If stdinOnce is set to true, stdin is
        opened on container start, is empty until the first client
        attaches to stdin, and then remains open and accepts data
        until the client disconnects, at which time stdin is closed
        and remains closed until the container is restarted. If this
        flag is false, a container processes that reads from stdin
        will never receive an EOF. Default is false
        """
        return self._properties.get('stdinOnce')

    @stdin_once.setter
    def stdin_once(self, value: bool):
        """
        Whether the container runtime should close the stdin channel
        after it has been opened by a single attach. When stdin is
        true the stdin stream will remain open across multiple
        attach sessions. If stdinOnce is set to true, stdin is
        opened on container start, is empty until the first client
        attaches to stdin, and then remains open and accepts data
        until the client disconnects, at which time stdin is closed
        and remains closed until the container is restarted. If this
        flag is false, a container processes that reads from stdin
        will never receive an EOF. Default is false
        """
        self._properties['stdinOnce'] = value

    @property
    def termination_message_path(self) -> str:
        """
        Optional: Path at which the file to which the container's
        termination message will be written is mounted into the
        container's filesystem. Message written is intended to be
        brief final status, such as an assertion failure message.
        Will be truncated by the node if greater than 4096 bytes.
        The total message length across all containers will be
        limited to 12kb. Defaults to /dev/termination-log. Cannot be
        updated.
        """
        return self._properties.get('terminationMessagePath')

    @termination_message_path.setter
    def termination_message_path(self, value: str):
        """
        Optional: Path at which the file to which the container's
        termination message will be written is mounted into the
        container's filesystem. Message written is intended to be
        brief final status, such as an assertion failure message.
        Will be truncated by the node if greater than 4096 bytes.
        The total message length across all containers will be
        limited to 12kb. Defaults to /dev/termination-log. Cannot be
        updated.
        """
        self._properties['terminationMessagePath'] = value

    @property
    def termination_message_policy(self) -> str:
        """
        Indicate how the termination message should be populated.
        File will use the contents of terminationMessagePath to
        populate the container status message on both success and
        failure. FallbackToLogsOnError will use the last chunk of
        container log output if the termination message file is
        empty and the container exited with an error. The log output
        is limited to 2048 bytes or 80 lines, whichever is smaller.
        Defaults to File. Cannot be updated.
        """
        return self._properties.get('terminationMessagePolicy')

    @termination_message_policy.setter
    def termination_message_policy(self, value: str):
        """
        Indicate how the termination message should be populated.
        File will use the contents of terminationMessagePath to
        populate the container status message on both success and
        failure. FallbackToLogsOnError will use the last chunk of
        container log output if the termination message file is
        empty and the container exited with an error. The log output
        is limited to 2048 bytes or 80 lines, whichever is smaller.
        Defaults to File. Cannot be updated.
        """
        self._properties['terminationMessagePolicy'] = value

    @property
    def tty(self) -> bool:
        """
        Whether this container should allocate a TTY for itself,
        also requires 'stdin' to be true. Default is false.
        """
        return self._properties.get('tty')

    @tty.setter
    def tty(self, value: bool):
        """
        Whether this container should allocate a TTY for itself,
        also requires 'stdin' to be true. Default is false.
        """
        self._properties['tty'] = value

    @property
    def volume_devices(self) -> typing.List['VolumeDevice']:
        """
        volumeDevices is the list of block devices to be used by the
        container. This is a beta feature.
        """
        return self._properties.get('volumeDevices')

    @volume_devices.setter
    def volume_devices(
            self,
            value: typing.Union[typing.List['VolumeDevice'], typing.List[dict]]
    ):
        """
        volumeDevices is the list of block devices to be used by the
        container. This is a beta feature.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = VolumeDevice().from_dict(item)
            cleaned.append(item)
        self._properties['volumeDevices'] = cleaned

    @property
    def volume_mounts(self) -> typing.List['VolumeMount']:
        """
        Pod volumes to mount into the container's filesystem. Cannot
        be updated.
        """
        return self._properties.get('volumeMounts')

    @volume_mounts.setter
    def volume_mounts(
            self,
            value: typing.Union[typing.List['VolumeMount'], typing.List[dict]]
    ):
        """
        Pod volumes to mount into the container's filesystem. Cannot
        be updated.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = VolumeMount().from_dict(item)
            cleaned.append(item)
        self._properties['volumeMounts'] = cleaned

    @property
    def working_dir(self) -> str:
        """
        Container's working directory. If not specified, the
        container runtime's default will be used, which might be
        configured in the container image. Cannot be updated.
        """
        return self._properties.get('workingDir')

    @working_dir.setter
    def working_dir(self, value: str):
        """
        Container's working directory. If not specified, the
        container runtime's default will be used, which might be
        configured in the container image. Cannot be updated.
        """
        self._properties['workingDir'] = value

    def __enter__(self) -> 'Container':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerImage(_kuber_definitions.Definition):
    """
    Describe a container image
    """

    def __init__(
            self,
            names: typing.List[str] = None,
            size_bytes: int = None,
    ):
        """Create ContainerImage instance."""
        super(ContainerImage, self).__init__(
            api_version='core/v1',
            kind='ContainerImage'
        )
        self._properties = {
            'names': names or [],
            'sizeBytes': size_bytes or None,

        }
        self._types = {
            'names': (list, str),
            'sizeBytes': (int, None),

        }

    @property
    def names(self) -> typing.List[str]:
        """
        Names by which this image is known. e.g.
        ["k8s.gcr.io/hyperkube:v1.0.7",
        "dockerhub.io/google_containers/hyperkube:v1.0.7"]
        """
        return self._properties.get('names')

    @names.setter
    def names(self, value: typing.List[str]):
        """
        Names by which this image is known. e.g.
        ["k8s.gcr.io/hyperkube:v1.0.7",
        "dockerhub.io/google_containers/hyperkube:v1.0.7"]
        """
        self._properties['names'] = value

    @property
    def size_bytes(self) -> int:
        """
        The size of the image in bytes.
        """
        return self._properties.get('sizeBytes')

    @size_bytes.setter
    def size_bytes(self, value: int):
        """
        The size of the image in bytes.
        """
        self._properties['sizeBytes'] = value

    def __enter__(self) -> 'ContainerImage':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerPort(_kuber_definitions.Definition):
    """
    ContainerPort represents a network port in a single
    container.
    """

    def __init__(
            self,
            container_port: int = None,
            host_ip: str = None,
            host_port: int = None,
            name: str = None,
            protocol: str = None,
    ):
        """Create ContainerPort instance."""
        super(ContainerPort, self).__init__(
            api_version='core/v1',
            kind='ContainerPort'
        )
        self._properties = {
            'containerPort': container_port or None,
            'hostIP': host_ip or '',
            'hostPort': host_port or None,
            'name': name or '',
            'protocol': protocol or '',

        }
        self._types = {
            'containerPort': (int, None),
            'hostIP': (str, None),
            'hostPort': (int, None),
            'name': (str, None),
            'protocol': (str, None),

        }

    @property
    def container_port(self) -> int:
        """
        Number of port to expose on the pod's IP address. This must
        be a valid port number, 0 < x < 65536.
        """
        return self._properties.get('containerPort')

    @container_port.setter
    def container_port(self, value: int):
        """
        Number of port to expose on the pod's IP address. This must
        be a valid port number, 0 < x < 65536.
        """
        self._properties['containerPort'] = value

    @property
    def host_ip(self) -> str:
        """
        What host IP to bind the external port to.
        """
        return self._properties.get('hostIP')

    @host_ip.setter
    def host_ip(self, value: str):
        """
        What host IP to bind the external port to.
        """
        self._properties['hostIP'] = value

    @property
    def host_port(self) -> int:
        """
        Number of port to expose on the host. If specified, this
        must be a valid port number, 0 < x < 65536. If HostNetwork
        is specified, this must match ContainerPort. Most containers
        do not need this.
        """
        return self._properties.get('hostPort')

    @host_port.setter
    def host_port(self, value: int):
        """
        Number of port to expose on the host. If specified, this
        must be a valid port number, 0 < x < 65536. If HostNetwork
        is specified, this must match ContainerPort. Most containers
        do not need this.
        """
        self._properties['hostPort'] = value

    @property
    def name(self) -> str:
        """
        If specified, this must be an IANA_SVC_NAME and unique
        within the pod. Each named port in a pod must have a unique
        name. Name for the port that can be referred to by services.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        If specified, this must be an IANA_SVC_NAME and unique
        within the pod. Each named port in a pod must have a unique
        name. Name for the port that can be referred to by services.
        """
        self._properties['name'] = value

    @property
    def protocol(self) -> str:
        """
        Protocol for port. Must be UDP, TCP, or SCTP. Defaults to
        "TCP".
        """
        return self._properties.get('protocol')

    @protocol.setter
    def protocol(self, value: str):
        """
        Protocol for port. Must be UDP, TCP, or SCTP. Defaults to
        "TCP".
        """
        self._properties['protocol'] = value

    def __enter__(self) -> 'ContainerPort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerState(_kuber_definitions.Definition):
    """
    ContainerState holds a possible state of container. Only one
    of its members may be specified. If none of them is
    specified, the default one is ContainerStateWaiting.
    """

    def __init__(
            self,
            running: 'ContainerStateRunning' = None,
            terminated: 'ContainerStateTerminated' = None,
            waiting: 'ContainerStateWaiting' = None,
    ):
        """Create ContainerState instance."""
        super(ContainerState, self).__init__(
            api_version='core/v1',
            kind='ContainerState'
        )
        self._properties = {
            'running': running or ContainerStateRunning(),
            'terminated': terminated or ContainerStateTerminated(),
            'waiting': waiting or ContainerStateWaiting(),

        }
        self._types = {
            'running': (ContainerStateRunning, None),
            'terminated': (ContainerStateTerminated, None),
            'waiting': (ContainerStateWaiting, None),

        }

    @property
    def running(self) -> 'ContainerStateRunning':
        """
        Details about a running container
        """
        return self._properties.get('running')

    @running.setter
    def running(self, value: typing.Union['ContainerStateRunning', dict]):
        """
        Details about a running container
        """
        if isinstance(value, dict):
            value = ContainerStateRunning().from_dict(value)
        self._properties['running'] = value

    @property
    def terminated(self) -> 'ContainerStateTerminated':
        """
        Details about a terminated container
        """
        return self._properties.get('terminated')

    @terminated.setter
    def terminated(self, value: typing.Union['ContainerStateTerminated', dict]):
        """
        Details about a terminated container
        """
        if isinstance(value, dict):
            value = ContainerStateTerminated().from_dict(value)
        self._properties['terminated'] = value

    @property
    def waiting(self) -> 'ContainerStateWaiting':
        """
        Details about a waiting container
        """
        return self._properties.get('waiting')

    @waiting.setter
    def waiting(self, value: typing.Union['ContainerStateWaiting', dict]):
        """
        Details about a waiting container
        """
        if isinstance(value, dict):
            value = ContainerStateWaiting().from_dict(value)
        self._properties['waiting'] = value

    def __enter__(self) -> 'ContainerState':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerStateRunning(_kuber_definitions.Definition):
    """
    ContainerStateRunning is a running state of a container.
    """

    def __init__(
            self,
            started_at: str = None,
    ):
        """Create ContainerStateRunning instance."""
        super(ContainerStateRunning, self).__init__(
            api_version='core/v1',
            kind='ContainerStateRunning'
        )
        self._properties = {
            'startedAt': started_at or None,

        }
        self._types = {
            'startedAt': (str, None),

        }

    @property
    def started_at(self) -> str:
        """
        Time at which the container was last (re-)started
        """
        return self._properties.get('startedAt')

    @started_at.setter
    def started_at(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Time at which the container was last (re-)started
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['startedAt'] = value

    def __enter__(self) -> 'ContainerStateRunning':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerStateTerminated(_kuber_definitions.Definition):
    """
    ContainerStateTerminated is a terminated state of a
    container.
    """

    def __init__(
            self,
            container_id: str = None,
            exit_code: int = None,
            finished_at: str = None,
            message: str = None,
            reason: str = None,
            signal: int = None,
            started_at: str = None,
    ):
        """Create ContainerStateTerminated instance."""
        super(ContainerStateTerminated, self).__init__(
            api_version='core/v1',
            kind='ContainerStateTerminated'
        )
        self._properties = {
            'containerID': container_id or '',
            'exitCode': exit_code or None,
            'finishedAt': finished_at or None,
            'message': message or '',
            'reason': reason or '',
            'signal': signal or None,
            'startedAt': started_at or None,

        }
        self._types = {
            'containerID': (str, None),
            'exitCode': (int, None),
            'finishedAt': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'signal': (int, None),
            'startedAt': (str, None),

        }

    @property
    def container_id(self) -> str:
        """
        Container's ID in the format 'docker://<container_id>'
        """
        return self._properties.get('containerID')

    @container_id.setter
    def container_id(self, value: str):
        """
        Container's ID in the format 'docker://<container_id>'
        """
        self._properties['containerID'] = value

    @property
    def exit_code(self) -> int:
        """
        Exit status from the last termination of the container
        """
        return self._properties.get('exitCode')

    @exit_code.setter
    def exit_code(self, value: int):
        """
        Exit status from the last termination of the container
        """
        self._properties['exitCode'] = value

    @property
    def finished_at(self) -> str:
        """
        Time at which the container last terminated
        """
        return self._properties.get('finishedAt')

    @finished_at.setter
    def finished_at(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Time at which the container last terminated
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['finishedAt'] = value

    @property
    def message(self) -> str:
        """
        Message regarding the last termination of the container
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Message regarding the last termination of the container
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        (brief) reason from the last termination of the container
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        (brief) reason from the last termination of the container
        """
        self._properties['reason'] = value

    @property
    def signal(self) -> int:
        """
        Signal from the last termination of the container
        """
        return self._properties.get('signal')

    @signal.setter
    def signal(self, value: int):
        """
        Signal from the last termination of the container
        """
        self._properties['signal'] = value

    @property
    def started_at(self) -> str:
        """
        Time at which previous execution of the container started
        """
        return self._properties.get('startedAt')

    @started_at.setter
    def started_at(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Time at which previous execution of the container started
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['startedAt'] = value

    def __enter__(self) -> 'ContainerStateTerminated':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerStateWaiting(_kuber_definitions.Definition):
    """
    ContainerStateWaiting is a waiting state of a container.
    """

    def __init__(
            self,
            message: str = None,
            reason: str = None,
    ):
        """Create ContainerStateWaiting instance."""
        super(ContainerStateWaiting, self).__init__(
            api_version='core/v1',
            kind='ContainerStateWaiting'
        )
        self._properties = {
            'message': message or '',
            'reason': reason or '',

        }
        self._types = {
            'message': (str, None),
            'reason': (str, None),

        }

    @property
    def message(self) -> str:
        """
        Message regarding why the container is not yet running.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Message regarding why the container is not yet running.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        (brief) reason the container is not yet running.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        (brief) reason the container is not yet running.
        """
        self._properties['reason'] = value

    def __enter__(self) -> 'ContainerStateWaiting':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerStatus(_kuber_definitions.Definition):
    """
    ContainerStatus contains details for the current status of
    this container.
    """

    def __init__(
            self,
            container_id: str = None,
            image: str = None,
            image_id: str = None,
            last_state: 'ContainerState' = None,
            name: str = None,
            ready: bool = None,
            restart_count: int = None,
            state: 'ContainerState' = None,
    ):
        """Create ContainerStatus instance."""
        super(ContainerStatus, self).__init__(
            api_version='core/v1',
            kind='ContainerStatus'
        )
        self._properties = {
            'containerID': container_id or '',
            'image': image or '',
            'imageID': image_id or '',
            'lastState': last_state or ContainerState(),
            'name': name or '',
            'ready': ready or None,
            'restartCount': restart_count or None,
            'state': state or ContainerState(),

        }
        self._types = {
            'containerID': (str, None),
            'image': (str, None),
            'imageID': (str, None),
            'lastState': (ContainerState, None),
            'name': (str, None),
            'ready': (bool, None),
            'restartCount': (int, None),
            'state': (ContainerState, None),

        }

    @property
    def container_id(self) -> str:
        """
        Container's ID in the format 'docker://<container_id>'.
        """
        return self._properties.get('containerID')

    @container_id.setter
    def container_id(self, value: str):
        """
        Container's ID in the format 'docker://<container_id>'.
        """
        self._properties['containerID'] = value

    @property
    def image(self) -> str:
        """
        The image the container is running. More info:
        https://kubernetes.io/docs/concepts/containers/images
        """
        return self._properties.get('image')

    @image.setter
    def image(self, value: str):
        """
        The image the container is running. More info:
        https://kubernetes.io/docs/concepts/containers/images
        """
        self._properties['image'] = value

    @property
    def image_id(self) -> str:
        """
        ImageID of the container's image.
        """
        return self._properties.get('imageID')

    @image_id.setter
    def image_id(self, value: str):
        """
        ImageID of the container's image.
        """
        self._properties['imageID'] = value

    @property
    def last_state(self) -> 'ContainerState':
        """
        Details about the container's last termination condition.
        """
        return self._properties.get('lastState')

    @last_state.setter
    def last_state(self, value: typing.Union['ContainerState', dict]):
        """
        Details about the container's last termination condition.
        """
        if isinstance(value, dict):
            value = ContainerState().from_dict(value)
        self._properties['lastState'] = value

    @property
    def name(self) -> str:
        """
        This must be a DNS_LABEL. Each container in a pod must have
        a unique name. Cannot be updated.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        This must be a DNS_LABEL. Each container in a pod must have
        a unique name. Cannot be updated.
        """
        self._properties['name'] = value

    @property
    def ready(self) -> bool:
        """
        Specifies whether the container has passed its readiness
        probe.
        """
        return self._properties.get('ready')

    @ready.setter
    def ready(self, value: bool):
        """
        Specifies whether the container has passed its readiness
        probe.
        """
        self._properties['ready'] = value

    @property
    def restart_count(self) -> int:
        """
        The number of times the container has been restarted,
        currently based on the number of dead containers that have
        not yet been removed. Note that this is calculated from dead
        containers. But those containers are subject to garbage
        collection. This value will get capped at 5 by GC.
        """
        return self._properties.get('restartCount')

    @restart_count.setter
    def restart_count(self, value: int):
        """
        The number of times the container has been restarted,
        currently based on the number of dead containers that have
        not yet been removed. Note that this is calculated from dead
        containers. But those containers are subject to garbage
        collection. This value will get capped at 5 by GC.
        """
        self._properties['restartCount'] = value

    @property
    def state(self) -> 'ContainerState':
        """
        Details about the container's current condition.
        """
        return self._properties.get('state')

    @state.setter
    def state(self, value: typing.Union['ContainerState', dict]):
        """
        Details about the container's current condition.
        """
        if isinstance(value, dict):
            value = ContainerState().from_dict(value)
        self._properties['state'] = value

    def __enter__(self) -> 'ContainerStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonEndpoint(_kuber_definitions.Definition):
    """
    DaemonEndpoint contains information about a single Daemon
    endpoint.
    """

    def __init__(
            self,
            port: int = None,
    ):
        """Create DaemonEndpoint instance."""
        super(DaemonEndpoint, self).__init__(
            api_version='core/v1',
            kind='DaemonEndpoint'
        )
        self._properties = {
            'Port': port or None,

        }
        self._types = {
            'Port': (int, None),

        }

    @property
    def port(self) -> int:
        """
        Port number of the given endpoint.
        """
        return self._properties.get('Port')

    @port.setter
    def port(self, value: int):
        """
        Port number of the given endpoint.
        """
        self._properties['Port'] = value

    def __enter__(self) -> 'DaemonEndpoint':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DownwardAPIProjection(_kuber_definitions.Definition):
    """
    Represents downward API info for projecting into a projected
    volume. Note that this is identical to a downwardAPI volume
    source without the default mode.
    """

    def __init__(
            self,
            items: typing.List['DownwardAPIVolumeFile'] = None,
    ):
        """Create DownwardAPIProjection instance."""
        super(DownwardAPIProjection, self).__init__(
            api_version='core/v1',
            kind='DownwardAPIProjection'
        )
        self._properties = {
            'items': items or [],

        }
        self._types = {
            'items': (list, DownwardAPIVolumeFile),

        }

    @property
    def items(self) -> typing.List['DownwardAPIVolumeFile']:
        """
        Items is a list of DownwardAPIVolume file
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['DownwardAPIVolumeFile'], typing.List[dict]]
    ):
        """
        Items is a list of DownwardAPIVolume file
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = DownwardAPIVolumeFile().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    def __enter__(self) -> 'DownwardAPIProjection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DownwardAPIVolumeFile(_kuber_definitions.Definition):
    """
    DownwardAPIVolumeFile represents information to create the
    file containing the pod field
    """

    def __init__(
            self,
            field_ref: 'ObjectFieldSelector' = None,
            mode: int = None,
            path: str = None,
            resource_field_ref: 'ResourceFieldSelector' = None,
    ):
        """Create DownwardAPIVolumeFile instance."""
        super(DownwardAPIVolumeFile, self).__init__(
            api_version='core/v1',
            kind='DownwardAPIVolumeFile'
        )
        self._properties = {
            'fieldRef': field_ref or ObjectFieldSelector(),
            'mode': mode or None,
            'path': path or '',
            'resourceFieldRef': resource_field_ref or ResourceFieldSelector(),

        }
        self._types = {
            'fieldRef': (ObjectFieldSelector, None),
            'mode': (int, None),
            'path': (str, None),
            'resourceFieldRef': (ResourceFieldSelector, None),

        }

    @property
    def field_ref(self) -> 'ObjectFieldSelector':
        """
        Required: Selects a field of the pod: only annotations,
        labels, name and namespace are supported.
        """
        return self._properties.get('fieldRef')

    @field_ref.setter
    def field_ref(self, value: typing.Union['ObjectFieldSelector', dict]):
        """
        Required: Selects a field of the pod: only annotations,
        labels, name and namespace are supported.
        """
        if isinstance(value, dict):
            value = ObjectFieldSelector().from_dict(value)
        self._properties['fieldRef'] = value

    @property
    def mode(self) -> int:
        """
        Optional: mode bits to use on this file, must be a value
        between 0 and 0777. If not specified, the volume defaultMode
        will be used. This might be in conflict with other options
        that affect the file mode, like fsGroup, and the result can
        be other mode bits set.
        """
        return self._properties.get('mode')

    @mode.setter
    def mode(self, value: int):
        """
        Optional: mode bits to use on this file, must be a value
        between 0 and 0777. If not specified, the volume defaultMode
        will be used. This might be in conflict with other options
        that affect the file mode, like fsGroup, and the result can
        be other mode bits set.
        """
        self._properties['mode'] = value

    @property
    def path(self) -> str:
        """
        Required: Path is  the relative path name of the file to be
        created. Must not be absolute or contain the '..' path. Must
        be utf-8 encoded. The first item of the relative path must
        not start with '..'
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Required: Path is  the relative path name of the file to be
        created. Must not be absolute or contain the '..' path. Must
        be utf-8 encoded. The first item of the relative path must
        not start with '..'
        """
        self._properties['path'] = value

    @property
    def resource_field_ref(self) -> 'ResourceFieldSelector':
        """
        Selects a resource of the container: only resources limits
        and requests (limits.cpu, limits.memory, requests.cpu and
        requests.memory) are currently supported.
        """
        return self._properties.get('resourceFieldRef')

    @resource_field_ref.setter
    def resource_field_ref(self, value: typing.Union['ResourceFieldSelector', dict]):
        """
        Selects a resource of the container: only resources limits
        and requests (limits.cpu, limits.memory, requests.cpu and
        requests.memory) are currently supported.
        """
        if isinstance(value, dict):
            value = ResourceFieldSelector().from_dict(value)
        self._properties['resourceFieldRef'] = value

    def __enter__(self) -> 'DownwardAPIVolumeFile':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DownwardAPIVolumeSource(_kuber_definitions.Definition):
    """
    DownwardAPIVolumeSource represents a volume containing
    downward API info. Downward API volumes support ownership
    management and SELinux relabeling.
    """

    def __init__(
            self,
            default_mode: int = None,
            items: typing.List['DownwardAPIVolumeFile'] = None,
    ):
        """Create DownwardAPIVolumeSource instance."""
        super(DownwardAPIVolumeSource, self).__init__(
            api_version='core/v1',
            kind='DownwardAPIVolumeSource'
        )
        self._properties = {
            'defaultMode': default_mode or None,
            'items': items or [],

        }
        self._types = {
            'defaultMode': (int, None),
            'items': (list, DownwardAPIVolumeFile),

        }

    @property
    def default_mode(self) -> int:
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        return self._properties.get('defaultMode')

    @default_mode.setter
    def default_mode(self, value: int):
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        self._properties['defaultMode'] = value

    @property
    def items(self) -> typing.List['DownwardAPIVolumeFile']:
        """
        Items is a list of downward API volume file
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['DownwardAPIVolumeFile'], typing.List[dict]]
    ):
        """
        Items is a list of downward API volume file
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = DownwardAPIVolumeFile().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    def __enter__(self) -> 'DownwardAPIVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EmptyDirVolumeSource(_kuber_definitions.Definition):
    """
    Represents an empty directory for a pod. Empty directory
    volumes support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            medium: str = None,
            size_limit: typing.Union[str, int, None] = None,
    ):
        """Create EmptyDirVolumeSource instance."""
        super(EmptyDirVolumeSource, self).__init__(
            api_version='core/v1',
            kind='EmptyDirVolumeSource'
        )
        self._properties = {
            'medium': medium or '',
            'sizeLimit': size_limit or None,

        }
        self._types = {
            'medium': (str, None),
            'sizeLimit': (str, None),

        }

    @property
    def medium(self) -> str:
        """
        What type of storage medium should back this directory. The
        default is "" which means to use the node's default medium.
        Must be an empty string (default) or Memory. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#emptydir
        """
        return self._properties.get('medium')

    @medium.setter
    def medium(self, value: str):
        """
        What type of storage medium should back this directory. The
        default is "" which means to use the node's default medium.
        Must be an empty string (default) or Memory. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#emptydir
        """
        self._properties['medium'] = value

    @property
    def size_limit(self) -> typing.Optional[str]:
        """
        Total amount of local storage required for this EmptyDir
        volume. The size limit is also applicable for memory medium.
        The maximum usage on memory medium EmptyDir would be the
        minimum value between the SizeLimit specified here and the
        sum of memory limits of all containers in a pod. The default
        is nil which means that the limit is undefined. More info:
        http://kubernetes.io/docs/user-guide/volumes#emptydir
        """
        value = self._properties.get('sizeLimit')
        return f'{value}' if value is not None else None

    @size_limit.setter
    def size_limit(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Total amount of local storage required for this EmptyDir
        volume. The size limit is also applicable for memory medium.
        The maximum usage on memory medium EmptyDir would be the
        minimum value between the SizeLimit specified here and the
        sum of memory limits of all containers in a pod. The default
        is nil which means that the limit is undefined. More info:
        http://kubernetes.io/docs/user-guide/volumes#emptydir
        """
        self._properties['sizeLimit'] = None if value is None else f'{value}'

    def __enter__(self) -> 'EmptyDirVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointAddress(_kuber_definitions.Definition):
    """
    EndpointAddress is a tuple that describes single IP address.
    """

    def __init__(
            self,
            hostname: str = None,
            ip: str = None,
            node_name: str = None,
            target_ref: 'ObjectReference' = None,
    ):
        """Create EndpointAddress instance."""
        super(EndpointAddress, self).__init__(
            api_version='core/v1',
            kind='EndpointAddress'
        )
        self._properties = {
            'hostname': hostname or '',
            'ip': ip or '',
            'nodeName': node_name or '',
            'targetRef': target_ref or ObjectReference(),

        }
        self._types = {
            'hostname': (str, None),
            'ip': (str, None),
            'nodeName': (str, None),
            'targetRef': (ObjectReference, None),

        }

    @property
    def hostname(self) -> str:
        """
        The Hostname of this endpoint
        """
        return self._properties.get('hostname')

    @hostname.setter
    def hostname(self, value: str):
        """
        The Hostname of this endpoint
        """
        self._properties['hostname'] = value

    @property
    def ip(self) -> str:
        """
        The IP of this endpoint. May not be loopback (127.0.0.0/8),
        link-local (169.254.0.0/16), or link-local multicast
        ((224.0.0.0/24). IPv6 is also accepted but not fully
        supported on all platforms. Also, certain kubernetes
        components, like kube-proxy, are not IPv6 ready.
        """
        return self._properties.get('ip')

    @ip.setter
    def ip(self, value: str):
        """
        The IP of this endpoint. May not be loopback (127.0.0.0/8),
        link-local (169.254.0.0/16), or link-local multicast
        ((224.0.0.0/24). IPv6 is also accepted but not fully
        supported on all platforms. Also, certain kubernetes
        components, like kube-proxy, are not IPv6 ready.
        """
        self._properties['ip'] = value

    @property
    def node_name(self) -> str:
        """
        Optional: Node hosting this endpoint. This can be used to
        determine endpoints local to a node.
        """
        return self._properties.get('nodeName')

    @node_name.setter
    def node_name(self, value: str):
        """
        Optional: Node hosting this endpoint. This can be used to
        determine endpoints local to a node.
        """
        self._properties['nodeName'] = value

    @property
    def target_ref(self) -> 'ObjectReference':
        """
        Reference to object providing the endpoint.
        """
        return self._properties.get('targetRef')

    @target_ref.setter
    def target_ref(self, value: typing.Union['ObjectReference', dict]):
        """
        Reference to object providing the endpoint.
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['targetRef'] = value

    def __enter__(self) -> 'EndpointAddress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointPort(_kuber_definitions.Definition):
    """
    EndpointPort is a tuple that describes a single port.
    """

    def __init__(
            self,
            name: str = None,
            port: int = None,
            protocol: str = None,
    ):
        """Create EndpointPort instance."""
        super(EndpointPort, self).__init__(
            api_version='core/v1',
            kind='EndpointPort'
        )
        self._properties = {
            'name': name or '',
            'port': port or None,
            'protocol': protocol or '',

        }
        self._types = {
            'name': (str, None),
            'port': (int, None),
            'protocol': (str, None),

        }

    @property
    def name(self) -> str:
        """
        The name of this port (corresponds to ServicePort.Name).
        Must be a DNS_LABEL. Optional only if one port is defined.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        The name of this port (corresponds to ServicePort.Name).
        Must be a DNS_LABEL. Optional only if one port is defined.
        """
        self._properties['name'] = value

    @property
    def port(self) -> int:
        """
        The port number of the endpoint.
        """
        return self._properties.get('port')

    @port.setter
    def port(self, value: int):
        """
        The port number of the endpoint.
        """
        self._properties['port'] = value

    @property
    def protocol(self) -> str:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP.
        Default is TCP.
        """
        return self._properties.get('protocol')

    @protocol.setter
    def protocol(self, value: str):
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP.
        Default is TCP.
        """
        self._properties['protocol'] = value

    def __enter__(self) -> 'EndpointPort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointSubset(_kuber_definitions.Definition):
    """
    EndpointSubset is a group of addresses with a common set of
    ports. The expanded set of endpoints is the Cartesian
    product of Addresses x Ports. For example, given:
      {
    Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    Ports:     [{"name": "a", "port": 8675}, {"name": "b",
    "port": 309}]
      }
    The resulting set of endpoints can be
    viewed as:
        a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
        b:
    [ 10.10.1.1:309, 10.10.2.2:309 ]
    """

    def __init__(
            self,
            addresses: typing.List['EndpointAddress'] = None,
            not_ready_addresses: typing.List['EndpointAddress'] = None,
            ports: typing.List['EndpointPort'] = None,
    ):
        """Create EndpointSubset instance."""
        super(EndpointSubset, self).__init__(
            api_version='core/v1',
            kind='EndpointSubset'
        )
        self._properties = {
            'addresses': addresses or [],
            'notReadyAddresses': not_ready_addresses or [],
            'ports': ports or [],

        }
        self._types = {
            'addresses': (list, EndpointAddress),
            'notReadyAddresses': (list, EndpointAddress),
            'ports': (list, EndpointPort),

        }

    @property
    def addresses(self) -> typing.List['EndpointAddress']:
        """
        IP addresses which offer the related ports that are marked
        as ready. These endpoints should be considered safe for load
        balancers and clients to utilize.
        """
        return self._properties.get('addresses')

    @addresses.setter
    def addresses(
            self,
            value: typing.Union[typing.List['EndpointAddress'], typing.List[dict]]
    ):
        """
        IP addresses which offer the related ports that are marked
        as ready. These endpoints should be considered safe for load
        balancers and clients to utilize.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EndpointAddress().from_dict(item)
            cleaned.append(item)
        self._properties['addresses'] = cleaned

    @property
    def not_ready_addresses(self) -> typing.List['EndpointAddress']:
        """
        IP addresses which offer the related ports but are not
        currently marked as ready because they have not yet finished
        starting, have recently failed a readiness check, or have
        recently failed a liveness check.
        """
        return self._properties.get('notReadyAddresses')

    @not_ready_addresses.setter
    def not_ready_addresses(
            self,
            value: typing.Union[typing.List['EndpointAddress'], typing.List[dict]]
    ):
        """
        IP addresses which offer the related ports but are not
        currently marked as ready because they have not yet finished
        starting, have recently failed a readiness check, or have
        recently failed a liveness check.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EndpointAddress().from_dict(item)
            cleaned.append(item)
        self._properties['notReadyAddresses'] = cleaned

    @property
    def ports(self) -> typing.List['EndpointPort']:
        """
        Port numbers available on the related IP addresses.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['EndpointPort'], typing.List[dict]]
    ):
        """
        Port numbers available on the related IP addresses.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EndpointPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    def __enter__(self) -> 'EndpointSubset':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Endpoints(_kuber_definitions.Resource):
    """
    Endpoints is a collection of endpoints that implement the
    actual service. Example:
      Name: "mysvc",
      Subsets: [
        {
    Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    Ports: [{"name": "a", "port": 8675}, {"name": "b", "port":
    309}]
        },
        {
          Addresses: [{"ip": "10.10.3.3"}],
    Ports: [{"name": "a", "port": 93}, {"name": "b", "port":
    76}]
        },
     ]
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            subsets: typing.List['EndpointSubset'] = None,
    ):
        """Create Endpoints instance."""
        super(Endpoints, self).__init__(
            api_version='core/v1',
            kind='Endpoints'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'subsets': subsets or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'subsets': (list, EndpointSubset),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def subsets(self) -> typing.List['EndpointSubset']:
        """
        The set of all endpoints is the union of all subsets.
        Addresses are placed into subsets according to the IPs they
        share. A single address with multiple ports, some of which
        are ready and some of which are not (because they come from
        different containers) will result in the address being
        displayed in different subsets for the different ports. No
        address will appear in both Addresses and NotReadyAddresses
        in the same subset. Sets of addresses and ports that
        comprise a service.
        """
        return self._properties.get('subsets')

    @subsets.setter
    def subsets(
            self,
            value: typing.Union[typing.List['EndpointSubset'], typing.List[dict]]
    ):
        """
        The set of all endpoints is the union of all subsets.
        Addresses are placed into subsets according to the IPs they
        share. A single address with multiple ports, some of which
        are ready and some of which are not (because they come from
        different containers) will result in the address being
        displayed in different subsets for the different ports. No
        address will appear in both Addresses and NotReadyAddresses
        in the same subset. Sets of addresses and ports that
        comprise a service.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EndpointSubset().from_dict(item)
            cleaned.append(item)
        self._properties['subsets'] = cleaned

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Endpoints in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_endpoints',
            'create_endpoints'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the Endpoints in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_endpoints',
            'replace_endpoints'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the Endpoints in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_endpoints',
            'patch_endpoints'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Endpoints from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_endpoints',
            'read_endpoints'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Endpoints from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_endpoints',
            'delete_endpoints'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Endpoints':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointsList(_kuber_definitions.Collection):
    """
    EndpointsList is a list of endpoints.
    """

    def __init__(
            self,
            items: typing.List['Endpoints'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create EndpointsList instance."""
        super(EndpointsList, self).__init__(
            api_version='core/v1',
            kind='EndpointsList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Endpoints),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Endpoints']:
        """
        List of endpoints.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Endpoints'], typing.List[dict]]
    ):
        """
        List of endpoints.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Endpoints().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'EndpointsList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EnvFromSource(_kuber_definitions.Definition):
    """
    EnvFromSource represents the source of a set of ConfigMaps
    """

    def __init__(
            self,
            config_map_ref: 'ConfigMapEnvSource' = None,
            prefix: str = None,
            secret_ref: 'SecretEnvSource' = None,
    ):
        """Create EnvFromSource instance."""
        super(EnvFromSource, self).__init__(
            api_version='core/v1',
            kind='EnvFromSource'
        )
        self._properties = {
            'configMapRef': config_map_ref or ConfigMapEnvSource(),
            'prefix': prefix or '',
            'secretRef': secret_ref or SecretEnvSource(),

        }
        self._types = {
            'configMapRef': (ConfigMapEnvSource, None),
            'prefix': (str, None),
            'secretRef': (SecretEnvSource, None),

        }

    @property
    def config_map_ref(self) -> 'ConfigMapEnvSource':
        """
        The ConfigMap to select from
        """
        return self._properties.get('configMapRef')

    @config_map_ref.setter
    def config_map_ref(self, value: typing.Union['ConfigMapEnvSource', dict]):
        """
        The ConfigMap to select from
        """
        if isinstance(value, dict):
            value = ConfigMapEnvSource().from_dict(value)
        self._properties['configMapRef'] = value

    @property
    def prefix(self) -> str:
        """
        An optional identifier to prepend to each key in the
        ConfigMap. Must be a C_IDENTIFIER.
        """
        return self._properties.get('prefix')

    @prefix.setter
    def prefix(self, value: str):
        """
        An optional identifier to prepend to each key in the
        ConfigMap. Must be a C_IDENTIFIER.
        """
        self._properties['prefix'] = value

    @property
    def secret_ref(self) -> 'SecretEnvSource':
        """
        The Secret to select from
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretEnvSource', dict]):
        """
        The Secret to select from
        """
        if isinstance(value, dict):
            value = SecretEnvSource().from_dict(value)
        self._properties['secretRef'] = value

    def __enter__(self) -> 'EnvFromSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EnvVar(_kuber_definitions.Definition):
    """
    EnvVar represents an environment variable present in a
    Container.
    """

    def __init__(
            self,
            name: str = None,
            value: str = None,
            value_from: 'EnvVarSource' = None,
    ):
        """Create EnvVar instance."""
        super(EnvVar, self).__init__(
            api_version='core/v1',
            kind='EnvVar'
        )
        self._properties = {
            'name': name or '',
            'value': value or '',
            'valueFrom': value_from or EnvVarSource(),

        }
        self._types = {
            'name': (str, None),
            'value': (str, None),
            'valueFrom': (EnvVarSource, None),

        }

    @property
    def name(self) -> str:
        """
        Name of the environment variable. Must be a C_IDENTIFIER.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the environment variable. Must be a C_IDENTIFIER.
        """
        self._properties['name'] = value

    @property
    def value(self) -> str:
        """
        Variable references $(VAR_NAME) are expanded using the
        previous defined environment variables in the container and
        any service environment variables. If a variable cannot be
        resolved, the reference in the input string will be
        unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never
        be expanded, regardless of whether the variable exists or
        not. Defaults to "".
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """
        Variable references $(VAR_NAME) are expanded using the
        previous defined environment variables in the container and
        any service environment variables. If a variable cannot be
        resolved, the reference in the input string will be
        unchanged. The $(VAR_NAME) syntax can be escaped with a
        double $$, ie: $$(VAR_NAME). Escaped references will never
        be expanded, regardless of whether the variable exists or
        not. Defaults to "".
        """
        self._properties['value'] = value

    @property
    def value_from(self) -> 'EnvVarSource':
        """
        Source for the environment variable's value. Cannot be used
        if value is not empty.
        """
        return self._properties.get('valueFrom')

    @value_from.setter
    def value_from(self, value: typing.Union['EnvVarSource', dict]):
        """
        Source for the environment variable's value. Cannot be used
        if value is not empty.
        """
        if isinstance(value, dict):
            value = EnvVarSource().from_dict(value)
        self._properties['valueFrom'] = value

    def __enter__(self) -> 'EnvVar':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EnvVarSource(_kuber_definitions.Definition):
    """
    EnvVarSource represents a source for the value of an EnvVar.
    """

    def __init__(
            self,
            config_map_key_ref: 'ConfigMapKeySelector' = None,
            field_ref: 'ObjectFieldSelector' = None,
            resource_field_ref: 'ResourceFieldSelector' = None,
            secret_key_ref: 'SecretKeySelector' = None,
    ):
        """Create EnvVarSource instance."""
        super(EnvVarSource, self).__init__(
            api_version='core/v1',
            kind='EnvVarSource'
        )
        self._properties = {
            'configMapKeyRef': config_map_key_ref or ConfigMapKeySelector(),
            'fieldRef': field_ref or ObjectFieldSelector(),
            'resourceFieldRef': resource_field_ref or ResourceFieldSelector(),
            'secretKeyRef': secret_key_ref or SecretKeySelector(),

        }
        self._types = {
            'configMapKeyRef': (ConfigMapKeySelector, None),
            'fieldRef': (ObjectFieldSelector, None),
            'resourceFieldRef': (ResourceFieldSelector, None),
            'secretKeyRef': (SecretKeySelector, None),

        }

    @property
    def config_map_key_ref(self) -> 'ConfigMapKeySelector':
        """
        Selects a key of a ConfigMap.
        """
        return self._properties.get('configMapKeyRef')

    @config_map_key_ref.setter
    def config_map_key_ref(self, value: typing.Union['ConfigMapKeySelector', dict]):
        """
        Selects a key of a ConfigMap.
        """
        if isinstance(value, dict):
            value = ConfigMapKeySelector().from_dict(value)
        self._properties['configMapKeyRef'] = value

    @property
    def field_ref(self) -> 'ObjectFieldSelector':
        """
        Selects a field of the pod: supports metadata.name,
        metadata.namespace, metadata.labels, metadata.annotations,
        spec.nodeName, spec.serviceAccountName, status.hostIP,
        status.podIP.
        """
        return self._properties.get('fieldRef')

    @field_ref.setter
    def field_ref(self, value: typing.Union['ObjectFieldSelector', dict]):
        """
        Selects a field of the pod: supports metadata.name,
        metadata.namespace, metadata.labels, metadata.annotations,
        spec.nodeName, spec.serviceAccountName, status.hostIP,
        status.podIP.
        """
        if isinstance(value, dict):
            value = ObjectFieldSelector().from_dict(value)
        self._properties['fieldRef'] = value

    @property
    def resource_field_ref(self) -> 'ResourceFieldSelector':
        """
        Selects a resource of the container: only resources limits
        and requests (limits.cpu, limits.memory, limits.ephemeral-
        storage, requests.cpu, requests.memory and
        requests.ephemeral-storage) are currently supported.
        """
        return self._properties.get('resourceFieldRef')

    @resource_field_ref.setter
    def resource_field_ref(self, value: typing.Union['ResourceFieldSelector', dict]):
        """
        Selects a resource of the container: only resources limits
        and requests (limits.cpu, limits.memory, limits.ephemeral-
        storage, requests.cpu, requests.memory and
        requests.ephemeral-storage) are currently supported.
        """
        if isinstance(value, dict):
            value = ResourceFieldSelector().from_dict(value)
        self._properties['resourceFieldRef'] = value

    @property
    def secret_key_ref(self) -> 'SecretKeySelector':
        """
        Selects a key of a secret in the pod's namespace
        """
        return self._properties.get('secretKeyRef')

    @secret_key_ref.setter
    def secret_key_ref(self, value: typing.Union['SecretKeySelector', dict]):
        """
        Selects a key of a secret in the pod's namespace
        """
        if isinstance(value, dict):
            value = SecretKeySelector().from_dict(value)
        self._properties['secretKeyRef'] = value

    def __enter__(self) -> 'EnvVarSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Event(_kuber_definitions.Resource):
    """
    Event is a report of an event somewhere in the cluster.
    """

    def __init__(
            self,
            action: str = None,
            count: int = None,
            event_time: 'MicroTime' = None,
            first_timestamp: str = None,
            involved_object: 'ObjectReference' = None,
            last_timestamp: str = None,
            message: str = None,
            metadata: 'ObjectMeta' = None,
            reason: str = None,
            related: 'ObjectReference' = None,
            reporting_component: str = None,
            reporting_instance: str = None,
            series: 'EventSeries' = None,
            source: 'EventSource' = None,
            type_: str = None,
    ):
        """Create Event instance."""
        super(Event, self).__init__(
            api_version='core/v1',
            kind='Event'
        )
        self._properties = {
            'action': action or '',
            'count': count or None,
            'eventTime': event_time or MicroTime(),
            'firstTimestamp': first_timestamp or None,
            'involvedObject': involved_object or ObjectReference(),
            'lastTimestamp': last_timestamp or None,
            'message': message or '',
            'metadata': metadata or ObjectMeta(),
            'reason': reason or '',
            'related': related or ObjectReference(),
            'reportingComponent': reporting_component or '',
            'reportingInstance': reporting_instance or '',
            'series': series or EventSeries(),
            'source': source or EventSource(),
            'type': type_ or '',

        }
        self._types = {
            'action': (str, None),
            'apiVersion': (str, None),
            'count': (int, None),
            'eventTime': (MicroTime, None),
            'firstTimestamp': (str, None),
            'involvedObject': (ObjectReference, None),
            'kind': (str, None),
            'lastTimestamp': (str, None),
            'message': (str, None),
            'metadata': (ObjectMeta, None),
            'reason': (str, None),
            'related': (ObjectReference, None),
            'reportingComponent': (str, None),
            'reportingInstance': (str, None),
            'series': (EventSeries, None),
            'source': (EventSource, None),
            'type': (str, None),

        }

    @property
    def action(self) -> str:
        """
        What action was taken/failed regarding to the Regarding
        object.
        """
        return self._properties.get('action')

    @action.setter
    def action(self, value: str):
        """
        What action was taken/failed regarding to the Regarding
        object.
        """
        self._properties['action'] = value

    @property
    def count(self) -> int:
        """
        The number of times this event has occurred.
        """
        return self._properties.get('count')

    @count.setter
    def count(self, value: int):
        """
        The number of times this event has occurred.
        """
        self._properties['count'] = value

    @property
    def event_time(self) -> 'MicroTime':
        """
        Time when this Event was first observed.
        """
        return self._properties.get('eventTime')

    @event_time.setter
    def event_time(self, value: typing.Union['MicroTime', dict]):
        """
        Time when this Event was first observed.
        """
        if isinstance(value, dict):
            value = MicroTime().from_dict(value)
        self._properties['eventTime'] = value

    @property
    def first_timestamp(self) -> str:
        """
        The time at which the event was first recorded. (Time of
        server receipt is in TypeMeta.)
        """
        return self._properties.get('firstTimestamp')

    @first_timestamp.setter
    def first_timestamp(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The time at which the event was first recorded. (Time of
        server receipt is in TypeMeta.)
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['firstTimestamp'] = value

    @property
    def involved_object(self) -> 'ObjectReference':
        """
        The object that this event is about.
        """
        return self._properties.get('involvedObject')

    @involved_object.setter
    def involved_object(self, value: typing.Union['ObjectReference', dict]):
        """
        The object that this event is about.
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['involvedObject'] = value

    @property
    def last_timestamp(self) -> str:
        """
        The time at which the most recent occurrence of this event
        was recorded.
        """
        return self._properties.get('lastTimestamp')

    @last_timestamp.setter
    def last_timestamp(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The time at which the most recent occurrence of this event
        was recorded.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTimestamp'] = value

    @property
    def message(self) -> str:
        """
        A human-readable description of the status of this
        operation.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human-readable description of the status of this
        operation.
        """
        self._properties['message'] = value

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def reason(self) -> str:
        """
        This should be a short, machine understandable string that
        gives the reason for the transition into the object's
        current status.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        This should be a short, machine understandable string that
        gives the reason for the transition into the object's
        current status.
        """
        self._properties['reason'] = value

    @property
    def related(self) -> 'ObjectReference':
        """
        Optional secondary object for more complex actions.
        """
        return self._properties.get('related')

    @related.setter
    def related(self, value: typing.Union['ObjectReference', dict]):
        """
        Optional secondary object for more complex actions.
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['related'] = value

    @property
    def reporting_component(self) -> str:
        """
        Name of the controller that emitted this Event, e.g.
        `kubernetes.io/kubelet`.
        """
        return self._properties.get('reportingComponent')

    @reporting_component.setter
    def reporting_component(self, value: str):
        """
        Name of the controller that emitted this Event, e.g.
        `kubernetes.io/kubelet`.
        """
        self._properties['reportingComponent'] = value

    @property
    def reporting_instance(self) -> str:
        """
        ID of the controller instance, e.g. `kubelet-xyzf`.
        """
        return self._properties.get('reportingInstance')

    @reporting_instance.setter
    def reporting_instance(self, value: str):
        """
        ID of the controller instance, e.g. `kubelet-xyzf`.
        """
        self._properties['reportingInstance'] = value

    @property
    def series(self) -> 'EventSeries':
        """
        Data about the Event series this event represents or nil if
        it's a singleton Event.
        """
        return self._properties.get('series')

    @series.setter
    def series(self, value: typing.Union['EventSeries', dict]):
        """
        Data about the Event series this event represents or nil if
        it's a singleton Event.
        """
        if isinstance(value, dict):
            value = EventSeries().from_dict(value)
        self._properties['series'] = value

    @property
    def source(self) -> 'EventSource':
        """
        The component reporting this event. Should be a short
        machine understandable string.
        """
        return self._properties.get('source')

    @source.setter
    def source(self, value: typing.Union['EventSource', dict]):
        """
        The component reporting this event. Should be a short
        machine understandable string.
        """
        if isinstance(value, dict):
            value = EventSource().from_dict(value)
        self._properties['source'] = value

    @property
    def type_(self) -> str:
        """
        Type of this event (Normal, Warning), new types could be
        added in the future
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of this event (Normal, Warning), new types could be
        added in the future
        """
        self._properties['type'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Event in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_event',
            'create_event'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the Event in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_event',
            'replace_event'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the Event in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_event',
            'patch_event'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Event from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_event',
            'read_event'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Event from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_event',
            'delete_event'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Event':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EventList(_kuber_definitions.Collection):
    """
    EventList is a list of events.
    """

    def __init__(
            self,
            items: typing.List['Event'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create EventList instance."""
        super(EventList, self).__init__(
            api_version='core/v1',
            kind='EventList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Event),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Event']:
        """
        List of events
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Event'], typing.List[dict]]
    ):
        """
        List of events
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Event().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'EventList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EventSeries(_kuber_definitions.Definition):
    """
    EventSeries contain information on series of events, i.e.
    thing that was/is happening continuously for some time.
    """

    def __init__(
            self,
            count: int = None,
            last_observed_time: 'MicroTime' = None,
            state: str = None,
    ):
        """Create EventSeries instance."""
        super(EventSeries, self).__init__(
            api_version='core/v1',
            kind='EventSeries'
        )
        self._properties = {
            'count': count or None,
            'lastObservedTime': last_observed_time or MicroTime(),
            'state': state or '',

        }
        self._types = {
            'count': (int, None),
            'lastObservedTime': (MicroTime, None),
            'state': (str, None),

        }

    @property
    def count(self) -> int:
        """
        Number of occurrences in this series up to the last
        heartbeat time
        """
        return self._properties.get('count')

    @count.setter
    def count(self, value: int):
        """
        Number of occurrences in this series up to the last
        heartbeat time
        """
        self._properties['count'] = value

    @property
    def last_observed_time(self) -> 'MicroTime':
        """
        Time of the last occurrence observed
        """
        return self._properties.get('lastObservedTime')

    @last_observed_time.setter
    def last_observed_time(self, value: typing.Union['MicroTime', dict]):
        """
        Time of the last occurrence observed
        """
        if isinstance(value, dict):
            value = MicroTime().from_dict(value)
        self._properties['lastObservedTime'] = value

    @property
    def state(self) -> str:
        """
        State of this Series: Ongoing or Finished
        """
        return self._properties.get('state')

    @state.setter
    def state(self, value: str):
        """
        State of this Series: Ongoing or Finished
        """
        self._properties['state'] = value

    def __enter__(self) -> 'EventSeries':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EventSource(_kuber_definitions.Definition):
    """
    EventSource contains information for an event.
    """

    def __init__(
            self,
            component: str = None,
            host: str = None,
    ):
        """Create EventSource instance."""
        super(EventSource, self).__init__(
            api_version='core/v1',
            kind='EventSource'
        )
        self._properties = {
            'component': component or '',
            'host': host or '',

        }
        self._types = {
            'component': (str, None),
            'host': (str, None),

        }

    @property
    def component(self) -> str:
        """
        Component from which the event is generated.
        """
        return self._properties.get('component')

    @component.setter
    def component(self, value: str):
        """
        Component from which the event is generated.
        """
        self._properties['component'] = value

    @property
    def host(self) -> str:
        """
        Node name on which the event is generated.
        """
        return self._properties.get('host')

    @host.setter
    def host(self, value: str):
        """
        Node name on which the event is generated.
        """
        self._properties['host'] = value

    def __enter__(self) -> 'EventSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ExecAction(_kuber_definitions.Definition):
    """
    ExecAction describes a "run in container" action.
    """

    def __init__(
            self,
            command: typing.List[str] = None,
    ):
        """Create ExecAction instance."""
        super(ExecAction, self).__init__(
            api_version='core/v1',
            kind='ExecAction'
        )
        self._properties = {
            'command': command or [],

        }
        self._types = {
            'command': (list, str),

        }

    @property
    def command(self) -> typing.List[str]:
        """
        Command is the command line to execute inside the container,
        the working directory for the command  is root ('/') in the
        container's filesystem. The command is simply exec'd, it is
        not run inside a shell, so traditional shell instructions
        ('|', etc) won't work. To use a shell, you need to
        explicitly call out to that shell. Exit status of 0 is
        treated as live/healthy and non-zero is unhealthy.
        """
        return self._properties.get('command')

    @command.setter
    def command(self, value: typing.List[str]):
        """
        Command is the command line to execute inside the container,
        the working directory for the command  is root ('/') in the
        container's filesystem. The command is simply exec'd, it is
        not run inside a shell, so traditional shell instructions
        ('|', etc) won't work. To use a shell, you need to
        explicitly call out to that shell. Exit status of 0 is
        treated as live/healthy and non-zero is unhealthy.
        """
        self._properties['command'] = value

    def __enter__(self) -> 'ExecAction':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FCVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Fibre Channel volume. Fibre Channel volumes can
    only be mounted as read/write once. Fibre Channel volumes
    support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            lun: int = None,
            read_only: bool = None,
            target_wwns: typing.List[str] = None,
            wwids: typing.List[str] = None,
    ):
        """Create FCVolumeSource instance."""
        super(FCVolumeSource, self).__init__(
            api_version='core/v1',
            kind='FCVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'lun': lun or None,
            'readOnly': read_only or None,
            'targetWWNs': target_wwns or [],
            'wwids': wwids or [],

        }
        self._types = {
            'fsType': (str, None),
            'lun': (int, None),
            'readOnly': (bool, None),
            'targetWWNs': (list, str),
            'wwids': (list, str),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def lun(self) -> int:
        """
        Optional: FC target lun number
        """
        return self._properties.get('lun')

    @lun.setter
    def lun(self, value: int):
        """
        Optional: FC target lun number
        """
        self._properties['lun'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def target_wwns(self) -> typing.List[str]:
        """
        Optional: FC target worldwide names (WWNs)
        """
        return self._properties.get('targetWWNs')

    @target_wwns.setter
    def target_wwns(self, value: typing.List[str]):
        """
        Optional: FC target worldwide names (WWNs)
        """
        self._properties['targetWWNs'] = value

    @property
    def wwids(self) -> typing.List[str]:
        """
        Optional: FC volume world wide identifiers (wwids) Either
        wwids or combination of targetWWNs and lun must be set, but
        not both simultaneously.
        """
        return self._properties.get('wwids')

    @wwids.setter
    def wwids(self, value: typing.List[str]):
        """
        Optional: FC volume world wide identifiers (wwids) Either
        wwids or combination of targetWWNs and lun must be set, but
        not both simultaneously.
        """
        self._properties['wwids'] = value

    def __enter__(self) -> 'FCVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlexPersistentVolumeSource(_kuber_definitions.Definition):
    """
    FlexPersistentVolumeSource represents a generic persistent
    volume resource that is provisioned/attached using an exec
    based plugin.
    """

    def __init__(
            self,
            driver: str = None,
            fs_type: str = None,
            options: dict = None,
            read_only: bool = None,
            secret_ref: 'SecretReference' = None,
    ):
        """Create FlexPersistentVolumeSource instance."""
        super(FlexPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='FlexPersistentVolumeSource'
        )
        self._properties = {
            'driver': driver or '',
            'fsType': fs_type or '',
            'options': options or {},
            'readOnly': read_only or None,
            'secretRef': secret_ref or SecretReference(),

        }
        self._types = {
            'driver': (str, None),
            'fsType': (str, None),
            'options': (dict, None),
            'readOnly': (bool, None),
            'secretRef': (SecretReference, None),

        }

    @property
    def driver(self) -> str:
        """
        Driver is the name of the driver to use for this volume.
        """
        return self._properties.get('driver')

    @driver.setter
    def driver(self, value: str):
        """
        Driver is the name of the driver to use for this volume.
        """
        self._properties['driver'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". The default filesystem depends on FlexVolume script.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". The default filesystem depends on FlexVolume script.
        """
        self._properties['fsType'] = value

    @property
    def options(self) -> dict:
        """
        Optional: Extra command options if any.
        """
        return self._properties.get('options')

    @options.setter
    def options(self, value: dict):
        """
        Optional: Extra command options if any.
        """
        self._properties['options'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        Optional: SecretRef is reference to the secret object
        containing sensitive information to pass to the plugin
        scripts. This may be empty if no secret object is specified.
        If the secret object contains more than one secret, all
        secrets are passed to the plugin scripts.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        Optional: SecretRef is reference to the secret object
        containing sensitive information to pass to the plugin
        scripts. This may be empty if no secret object is specified.
        If the secret object contains more than one secret, all
        secrets are passed to the plugin scripts.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    def __enter__(self) -> 'FlexPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlexVolumeSource(_kuber_definitions.Definition):
    """
    FlexVolume represents a generic volume resource that is
    provisioned/attached using an exec based plugin.
    """

    def __init__(
            self,
            driver: str = None,
            fs_type: str = None,
            options: dict = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
    ):
        """Create FlexVolumeSource instance."""
        super(FlexVolumeSource, self).__init__(
            api_version='core/v1',
            kind='FlexVolumeSource'
        )
        self._properties = {
            'driver': driver or '',
            'fsType': fs_type or '',
            'options': options or {},
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),

        }
        self._types = {
            'driver': (str, None),
            'fsType': (str, None),
            'options': (dict, None),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),

        }

    @property
    def driver(self) -> str:
        """
        Driver is the name of the driver to use for this volume.
        """
        return self._properties.get('driver')

    @driver.setter
    def driver(self, value: str):
        """
        Driver is the name of the driver to use for this volume.
        """
        self._properties['driver'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". The default filesystem depends on FlexVolume script.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". The default filesystem depends on FlexVolume script.
        """
        self._properties['fsType'] = value

    @property
    def options(self) -> dict:
        """
        Optional: Extra command options if any.
        """
        return self._properties.get('options')

    @options.setter
    def options(self, value: dict):
        """
        Optional: Extra command options if any.
        """
        self._properties['options'] = value

    @property
    def read_only(self) -> bool:
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Optional: Defaults to false (read/write). ReadOnly here will
        force the ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        Optional: SecretRef is reference to the secret object
        containing sensitive information to pass to the plugin
        scripts. This may be empty if no secret object is specified.
        If the secret object contains more than one secret, all
        secrets are passed to the plugin scripts.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        Optional: SecretRef is reference to the secret object
        containing sensitive information to pass to the plugin
        scripts. This may be empty if no secret object is specified.
        If the secret object contains more than one secret, all
        secrets are passed to the plugin scripts.
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    def __enter__(self) -> 'FlexVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlockerVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Flocker volume mounted by the Flocker agent.
    One and only one of datasetName and datasetUUID should be
    set. Flocker volumes do not support ownership management or
    SELinux relabeling.
    """

    def __init__(
            self,
            dataset_name: str = None,
            dataset_uuid: str = None,
    ):
        """Create FlockerVolumeSource instance."""
        super(FlockerVolumeSource, self).__init__(
            api_version='core/v1',
            kind='FlockerVolumeSource'
        )
        self._properties = {
            'datasetName': dataset_name or '',
            'datasetUUID': dataset_uuid or '',

        }
        self._types = {
            'datasetName': (str, None),
            'datasetUUID': (str, None),

        }

    @property
    def dataset_name(self) -> str:
        """
        Name of the dataset stored as metadata -> name on the
        dataset for Flocker should be considered as deprecated
        """
        return self._properties.get('datasetName')

    @dataset_name.setter
    def dataset_name(self, value: str):
        """
        Name of the dataset stored as metadata -> name on the
        dataset for Flocker should be considered as deprecated
        """
        self._properties['datasetName'] = value

    @property
    def dataset_uuid(self) -> str:
        """
        UUID of the dataset. This is unique identifier of a Flocker
        dataset
        """
        return self._properties.get('datasetUUID')

    @dataset_uuid.setter
    def dataset_uuid(self, value: str):
        """
        UUID of the dataset. This is unique identifier of a Flocker
        dataset
        """
        self._properties['datasetUUID'] = value

    def __enter__(self) -> 'FlockerVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GCEPersistentDiskVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Persistent Disk resource in Google Compute
    Engine.

    A GCE PD must exist before mounting to a container.
    The disk must also be in the same GCE project and zone as
    the kubelet. A GCE PD can only be mounted as read/write once
    or read-only many times. GCE PDs support ownership
    management and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            partition: int = None,
            pd_name: str = None,
            read_only: bool = None,
    ):
        """Create GCEPersistentDiskVolumeSource instance."""
        super(GCEPersistentDiskVolumeSource, self).__init__(
            api_version='core/v1',
            kind='GCEPersistentDiskVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'partition': partition or None,
            'pdName': pd_name or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'fsType': (str, None),
            'partition': (int, None),
            'pdName': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#gcepersi
        stentdisk
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#gcepersi
        stentdisk
        """
        self._properties['fsType'] = value

    @property
    def partition(self) -> int:
        """
        The partition in the volume that you want to mount. If
        omitted, the default is to mount by volume name. Examples:
        For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you
        can leave the property empty). More info: https://kubernetes
        .io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        return self._properties.get('partition')

    @partition.setter
    def partition(self, value: int):
        """
        The partition in the volume that you want to mount. If
        omitted, the default is to mount by volume name. Examples:
        For volume /dev/sda1, you specify the partition as "1".
        Similarly, the volume partition for /dev/sda is "0" (or you
        can leave the property empty). More info: https://kubernetes
        .io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        self._properties['partition'] = value

    @property
    def pd_name(self) -> str:
        """
        Unique name of the PD resource in GCE. Used to identify the
        disk in GCE. More info: https://kubernetes.io/docs/concepts/
        storage/volumes#gcepersistentdisk
        """
        return self._properties.get('pdName')

    @pd_name.setter
    def pd_name(self, value: str):
        """
        Unique name of the PD resource in GCE. Used to identify the
        disk in GCE. More info: https://kubernetes.io/docs/concepts/
        storage/volumes#gcepersistentdisk
        """
        self._properties['pdName'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://kubernet
        es.io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://kubernet
        es.io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'GCEPersistentDiskVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GitRepoVolumeSource(_kuber_definitions.Definition):
    """
    Represents a volume that is populated with the contents of a
    git repository. Git repo volumes do not support ownership
    management. Git repo volumes support SELinux relabeling.
    DEPRECATED: GitRepo is deprecated. To provision a container
    with a git repo, mount an EmptyDir into an InitContainer
    that clones the repo using git, then mount the EmptyDir into
    the Pod's container.
    """

    def __init__(
            self,
            directory: str = None,
            repository: str = None,
            revision: str = None,
    ):
        """Create GitRepoVolumeSource instance."""
        super(GitRepoVolumeSource, self).__init__(
            api_version='core/v1',
            kind='GitRepoVolumeSource'
        )
        self._properties = {
            'directory': directory or '',
            'repository': repository or '',
            'revision': revision or '',

        }
        self._types = {
            'directory': (str, None),
            'repository': (str, None),
            'revision': (str, None),

        }

    @property
    def directory(self) -> str:
        """
        Target directory name. Must not contain or start with '..'.
        If '.' is supplied, the volume directory will be the git
        repository.  Otherwise, if specified, the volume will
        contain the git repository in the subdirectory with the
        given name.
        """
        return self._properties.get('directory')

    @directory.setter
    def directory(self, value: str):
        """
        Target directory name. Must not contain or start with '..'.
        If '.' is supplied, the volume directory will be the git
        repository.  Otherwise, if specified, the volume will
        contain the git repository in the subdirectory with the
        given name.
        """
        self._properties['directory'] = value

    @property
    def repository(self) -> str:
        """
        Repository URL
        """
        return self._properties.get('repository')

    @repository.setter
    def repository(self, value: str):
        """
        Repository URL
        """
        self._properties['repository'] = value

    @property
    def revision(self) -> str:
        """
        Commit hash for the specified revision.
        """
        return self._properties.get('revision')

    @revision.setter
    def revision(self, value: str):
        """
        Commit hash for the specified revision.
        """
        self._properties['revision'] = value

    def __enter__(self) -> 'GitRepoVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GlusterfsPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Glusterfs mount that lasts the lifetime of a
    pod. Glusterfs volumes do not support ownership management
    or SELinux relabeling.
    """

    def __init__(
            self,
            endpoints: str = None,
            endpoints_namespace: str = None,
            path: str = None,
            read_only: bool = None,
    ):
        """Create GlusterfsPersistentVolumeSource instance."""
        super(GlusterfsPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='GlusterfsPersistentVolumeSource'
        )
        self._properties = {
            'endpoints': endpoints or '',
            'endpointsNamespace': endpoints_namespace or '',
            'path': path or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'endpoints': (str, None),
            'endpointsNamespace': (str, None),
            'path': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def endpoints(self) -> str:
        """
        EndpointsName is the endpoint name that details Glusterfs
        topology. More info: https://releases.k8s.io/HEAD/examples/v
        olumes/glusterfs/README.md#create-a-pod
        """
        return self._properties.get('endpoints')

    @endpoints.setter
    def endpoints(self, value: str):
        """
        EndpointsName is the endpoint name that details Glusterfs
        topology. More info: https://releases.k8s.io/HEAD/examples/v
        olumes/glusterfs/README.md#create-a-pod
        """
        self._properties['endpoints'] = value

    @property
    def endpoints_namespace(self) -> str:
        """
        EndpointsNamespace is the namespace that contains Glusterfs
        endpoint. If this field is empty, the EndpointNamespace
        defaults to the same namespace as the bound PVC. More info:
        https://releases.k8s.io/HEAD/examples/volumes/glusterfs/READ
        ME.md#create-a-pod
        """
        return self._properties.get('endpointsNamespace')

    @endpoints_namespace.setter
    def endpoints_namespace(self, value: str):
        """
        EndpointsNamespace is the namespace that contains Glusterfs
        endpoint. If this field is empty, the EndpointNamespace
        defaults to the same namespace as the bound PVC. More info:
        https://releases.k8s.io/HEAD/examples/volumes/glusterfs/READ
        ME.md#create-a-pod
        """
        self._properties['endpointsNamespace'] = value

    @property
    def path(self) -> str:
        """
        Path is the Glusterfs volume path. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-
        a-pod
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is the Glusterfs volume path. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-
        a-pod
        """
        self._properties['path'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the Glusterfs volume to be mounted
        with read-only permissions. Defaults to false. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/glusterfs/README
        .md#create-a-pod
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the Glusterfs volume to be mounted
        with read-only permissions. Defaults to false. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/glusterfs/README
        .md#create-a-pod
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'GlusterfsPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GlusterfsVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Glusterfs mount that lasts the lifetime of a
    pod. Glusterfs volumes do not support ownership management
    or SELinux relabeling.
    """

    def __init__(
            self,
            endpoints: str = None,
            path: str = None,
            read_only: bool = None,
    ):
        """Create GlusterfsVolumeSource instance."""
        super(GlusterfsVolumeSource, self).__init__(
            api_version='core/v1',
            kind='GlusterfsVolumeSource'
        )
        self._properties = {
            'endpoints': endpoints or '',
            'path': path or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'endpoints': (str, None),
            'path': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def endpoints(self) -> str:
        """
        EndpointsName is the endpoint name that details Glusterfs
        topology. More info: https://releases.k8s.io/HEAD/examples/v
        olumes/glusterfs/README.md#create-a-pod
        """
        return self._properties.get('endpoints')

    @endpoints.setter
    def endpoints(self, value: str):
        """
        EndpointsName is the endpoint name that details Glusterfs
        topology. More info: https://releases.k8s.io/HEAD/examples/v
        olumes/glusterfs/README.md#create-a-pod
        """
        self._properties['endpoints'] = value

    @property
    def path(self) -> str:
        """
        Path is the Glusterfs volume path. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-
        a-pod
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is the Glusterfs volume path. More info: https://releas
        es.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-
        a-pod
        """
        self._properties['path'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the Glusterfs volume to be mounted
        with read-only permissions. Defaults to false. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/glusterfs/README
        .md#create-a-pod
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the Glusterfs volume to be mounted
        with read-only permissions. Defaults to false. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/glusterfs/README
        .md#create-a-pod
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'GlusterfsVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPGetAction(_kuber_definitions.Definition):
    """
    HTTPGetAction describes an action based on HTTP Get
    requests.
    """

    def __init__(
            self,
            host: str = None,
            http_headers: typing.List['HTTPHeader'] = None,
            path: str = None,
            port: typing.Union[str, int, None] = None,
            scheme: str = None,
    ):
        """Create HTTPGetAction instance."""
        super(HTTPGetAction, self).__init__(
            api_version='core/v1',
            kind='HTTPGetAction'
        )
        self._properties = {
            'host': host or '',
            'httpHeaders': http_headers or [],
            'path': path or '',
            'port': port or None,
            'scheme': scheme or '',

        }
        self._types = {
            'host': (str, None),
            'httpHeaders': (list, HTTPHeader),
            'path': (str, None),
            'port': (int, None),
            'scheme': (str, None),

        }

    @property
    def host(self) -> str:
        """
        Host name to connect to, defaults to the pod IP. You
        probably want to set "Host" in httpHeaders instead.
        """
        return self._properties.get('host')

    @host.setter
    def host(self, value: str):
        """
        Host name to connect to, defaults to the pod IP. You
        probably want to set "Host" in httpHeaders instead.
        """
        self._properties['host'] = value

    @property
    def http_headers(self) -> typing.List['HTTPHeader']:
        """
        Custom headers to set in the request. HTTP allows repeated
        headers.
        """
        return self._properties.get('httpHeaders')

    @http_headers.setter
    def http_headers(
            self,
            value: typing.Union[typing.List['HTTPHeader'], typing.List[dict]]
    ):
        """
        Custom headers to set in the request. HTTP allows repeated
        headers.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HTTPHeader().from_dict(item)
            cleaned.append(item)
        self._properties['httpHeaders'] = cleaned

    @property
    def path(self) -> str:
        """
        Path to access on the HTTP server.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path to access on the HTTP server.
        """
        self._properties['path'] = value

    @property
    def port(self) -> typing.Optional[int]:
        """
        Name or number of the port to access on the container.
        Number must be in the range 1 to 65535. Name must be an
        IANA_SVC_NAME.
        """
        value = self._properties.get('port')
        return int(value) if value is not None else None

    @port.setter
    def port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Name or number of the port to access on the container.
        Number must be in the range 1 to 65535. Name must be an
        IANA_SVC_NAME.
        """
        self._properties['port'] = None if value is None else f'{value}'

    @property
    def scheme(self) -> str:
        """
        Scheme to use for connecting to the host. Defaults to HTTP.
        """
        return self._properties.get('scheme')

    @scheme.setter
    def scheme(self, value: str):
        """
        Scheme to use for connecting to the host. Defaults to HTTP.
        """
        self._properties['scheme'] = value

    def __enter__(self) -> 'HTTPGetAction':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPHeader(_kuber_definitions.Definition):
    """
    HTTPHeader describes a custom header to be used in HTTP
    probes
    """

    def __init__(
            self,
            name: str = None,
            value: str = None,
    ):
        """Create HTTPHeader instance."""
        super(HTTPHeader, self).__init__(
            api_version='core/v1',
            kind='HTTPHeader'
        )
        self._properties = {
            'name': name or '',
            'value': value or '',

        }
        self._types = {
            'name': (str, None),
            'value': (str, None),

        }

    @property
    def name(self) -> str:
        """
        The header field name
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        The header field name
        """
        self._properties['name'] = value

    @property
    def value(self) -> str:
        """
        The header field value
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """
        The header field value
        """
        self._properties['value'] = value

    def __enter__(self) -> 'HTTPHeader':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Handler(_kuber_definitions.Definition):
    """
    Handler defines a specific action that should be taken
    """

    def __init__(
            self,
            exec_: 'ExecAction' = None,
            http_get: 'HTTPGetAction' = None,
            tcp_socket: 'TCPSocketAction' = None,
    ):
        """Create Handler instance."""
        super(Handler, self).__init__(
            api_version='core/v1',
            kind='Handler'
        )
        self._properties = {
            'exec': exec_ or ExecAction(),
            'httpGet': http_get or HTTPGetAction(),
            'tcpSocket': tcp_socket or TCPSocketAction(),

        }
        self._types = {
            'exec': (ExecAction, None),
            'httpGet': (HTTPGetAction, None),
            'tcpSocket': (TCPSocketAction, None),

        }

    @property
    def exec_(self) -> 'ExecAction':
        """
        One and only one of the following should be specified. Exec
        specifies the action to take.
        """
        return self._properties.get('exec')

    @exec_.setter
    def exec_(self, value: typing.Union['ExecAction', dict]):
        """
        One and only one of the following should be specified. Exec
        specifies the action to take.
        """
        if isinstance(value, dict):
            value = ExecAction().from_dict(value)
        self._properties['exec'] = value

    @property
    def http_get(self) -> 'HTTPGetAction':
        """
        HTTPGet specifies the http request to perform.
        """
        return self._properties.get('httpGet')

    @http_get.setter
    def http_get(self, value: typing.Union['HTTPGetAction', dict]):
        """
        HTTPGet specifies the http request to perform.
        """
        if isinstance(value, dict):
            value = HTTPGetAction().from_dict(value)
        self._properties['httpGet'] = value

    @property
    def tcp_socket(self) -> 'TCPSocketAction':
        """
        TCPSocket specifies an action involving a TCP port. TCP
        hooks not yet supported
        """
        return self._properties.get('tcpSocket')

    @tcp_socket.setter
    def tcp_socket(self, value: typing.Union['TCPSocketAction', dict]):
        """
        TCPSocket specifies an action involving a TCP port. TCP
        hooks not yet supported
        """
        if isinstance(value, dict):
            value = TCPSocketAction().from_dict(value)
        self._properties['tcpSocket'] = value

    def __enter__(self) -> 'Handler':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HostAlias(_kuber_definitions.Definition):
    """
    HostAlias holds the mapping between IP and hostnames that
    will be injected as an entry in the pod's hosts file.
    """

    def __init__(
            self,
            hostnames: typing.List[str] = None,
            ip: str = None,
    ):
        """Create HostAlias instance."""
        super(HostAlias, self).__init__(
            api_version='core/v1',
            kind='HostAlias'
        )
        self._properties = {
            'hostnames': hostnames or [],
            'ip': ip or '',

        }
        self._types = {
            'hostnames': (list, str),
            'ip': (str, None),

        }

    @property
    def hostnames(self) -> typing.List[str]:
        """
        Hostnames for the above IP address.
        """
        return self._properties.get('hostnames')

    @hostnames.setter
    def hostnames(self, value: typing.List[str]):
        """
        Hostnames for the above IP address.
        """
        self._properties['hostnames'] = value

    @property
    def ip(self) -> str:
        """
        IP address of the host file entry.
        """
        return self._properties.get('ip')

    @ip.setter
    def ip(self, value: str):
        """
        IP address of the host file entry.
        """
        self._properties['ip'] = value

    def __enter__(self) -> 'HostAlias':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HostPathVolumeSource(_kuber_definitions.Definition):
    """
    Represents a host path mapped into a pod. Host path volumes
    do not support ownership management or SELinux relabeling.
    """

    def __init__(
            self,
            path: str = None,
            type_: str = None,
    ):
        """Create HostPathVolumeSource instance."""
        super(HostPathVolumeSource, self).__init__(
            api_version='core/v1',
            kind='HostPathVolumeSource'
        )
        self._properties = {
            'path': path or '',
            'type': type_ or '',

        }
        self._types = {
            'path': (str, None),
            'type': (str, None),

        }

    @property
    def path(self) -> str:
        """
        Path of the directory on the host. If the path is a symlink,
        it will follow the link to the real path. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path of the directory on the host. If the path is a symlink,
        it will follow the link to the real path. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        self._properties['path'] = value

    @property
    def type_(self) -> str:
        """
        Type for HostPath Volume Defaults to "" More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type for HostPath Volume Defaults to "" More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        self._properties['type'] = value

    def __enter__(self) -> 'HostPathVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ISCSIPersistentVolumeSource(_kuber_definitions.Definition):
    """
    ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI
    volumes can only be mounted as read/write once. ISCSI
    volumes support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            chap_auth_discovery: bool = None,
            chap_auth_session: bool = None,
            fs_type: str = None,
            initiator_name: str = None,
            iqn: str = None,
            iscsi_interface: str = None,
            lun: int = None,
            portals: typing.List[str] = None,
            read_only: bool = None,
            secret_ref: 'SecretReference' = None,
            target_portal: str = None,
    ):
        """Create ISCSIPersistentVolumeSource instance."""
        super(ISCSIPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ISCSIPersistentVolumeSource'
        )
        self._properties = {
            'chapAuthDiscovery': chap_auth_discovery or None,
            'chapAuthSession': chap_auth_session or None,
            'fsType': fs_type or '',
            'initiatorName': initiator_name or '',
            'iqn': iqn or '',
            'iscsiInterface': iscsi_interface or '',
            'lun': lun or None,
            'portals': portals or [],
            'readOnly': read_only or None,
            'secretRef': secret_ref or SecretReference(),
            'targetPortal': target_portal or '',

        }
        self._types = {
            'chapAuthDiscovery': (bool, None),
            'chapAuthSession': (bool, None),
            'fsType': (str, None),
            'initiatorName': (str, None),
            'iqn': (str, None),
            'iscsiInterface': (str, None),
            'lun': (int, None),
            'portals': (list, str),
            'readOnly': (bool, None),
            'secretRef': (SecretReference, None),
            'targetPortal': (str, None),

        }

    @property
    def chap_auth_discovery(self) -> bool:
        """
        whether support iSCSI Discovery CHAP authentication
        """
        return self._properties.get('chapAuthDiscovery')

    @chap_auth_discovery.setter
    def chap_auth_discovery(self, value: bool):
        """
        whether support iSCSI Discovery CHAP authentication
        """
        self._properties['chapAuthDiscovery'] = value

    @property
    def chap_auth_session(self) -> bool:
        """
        whether support iSCSI Session CHAP authentication
        """
        return self._properties.get('chapAuthSession')

    @chap_auth_session.setter
    def chap_auth_session(self, value: bool):
        """
        whether support iSCSI Session CHAP authentication
        """
        self._properties['chapAuthSession'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#iscsi
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#iscsi
        """
        self._properties['fsType'] = value

    @property
    def initiator_name(self) -> str:
        """
        Custom iSCSI Initiator Name. If initiatorName is specified
        with iscsiInterface simultaneously, new iSCSI interface
        <target portal>:<volume name> will be created for the
        connection.
        """
        return self._properties.get('initiatorName')

    @initiator_name.setter
    def initiator_name(self, value: str):
        """
        Custom iSCSI Initiator Name. If initiatorName is specified
        with iscsiInterface simultaneously, new iSCSI interface
        <target portal>:<volume name> will be created for the
        connection.
        """
        self._properties['initiatorName'] = value

    @property
    def iqn(self) -> str:
        """
        Target iSCSI Qualified Name.
        """
        return self._properties.get('iqn')

    @iqn.setter
    def iqn(self, value: str):
        """
        Target iSCSI Qualified Name.
        """
        self._properties['iqn'] = value

    @property
    def iscsi_interface(self) -> str:
        """
        iSCSI Interface Name that uses an iSCSI transport. Defaults
        to 'default' (tcp).
        """
        return self._properties.get('iscsiInterface')

    @iscsi_interface.setter
    def iscsi_interface(self, value: str):
        """
        iSCSI Interface Name that uses an iSCSI transport. Defaults
        to 'default' (tcp).
        """
        self._properties['iscsiInterface'] = value

    @property
    def lun(self) -> int:
        """
        iSCSI Target Lun number.
        """
        return self._properties.get('lun')

    @lun.setter
    def lun(self, value: int):
        """
        iSCSI Target Lun number.
        """
        self._properties['lun'] = value

    @property
    def portals(self) -> typing.List[str]:
        """
        iSCSI Target Portal List. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        return self._properties.get('portals')

    @portals.setter
    def portals(self, value: typing.List[str]):
        """
        iSCSI Target Portal List. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        self._properties['portals'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        CHAP Secret for iSCSI target and initiator authentication
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        CHAP Secret for iSCSI target and initiator authentication
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def target_portal(self) -> str:
        """
        iSCSI Target Portal. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        return self._properties.get('targetPortal')

    @target_portal.setter
    def target_portal(self, value: str):
        """
        iSCSI Target Portal. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        self._properties['targetPortal'] = value

    def __enter__(self) -> 'ISCSIPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ISCSIVolumeSource(_kuber_definitions.Definition):
    """
    Represents an ISCSI disk. ISCSI volumes can only be mounted
    as read/write once. ISCSI volumes support ownership
    management and SELinux relabeling.
    """

    def __init__(
            self,
            chap_auth_discovery: bool = None,
            chap_auth_session: bool = None,
            fs_type: str = None,
            initiator_name: str = None,
            iqn: str = None,
            iscsi_interface: str = None,
            lun: int = None,
            portals: typing.List[str] = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
            target_portal: str = None,
    ):
        """Create ISCSIVolumeSource instance."""
        super(ISCSIVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ISCSIVolumeSource'
        )
        self._properties = {
            'chapAuthDiscovery': chap_auth_discovery or None,
            'chapAuthSession': chap_auth_session or None,
            'fsType': fs_type or '',
            'initiatorName': initiator_name or '',
            'iqn': iqn or '',
            'iscsiInterface': iscsi_interface or '',
            'lun': lun or None,
            'portals': portals or [],
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),
            'targetPortal': target_portal or '',

        }
        self._types = {
            'chapAuthDiscovery': (bool, None),
            'chapAuthSession': (bool, None),
            'fsType': (str, None),
            'initiatorName': (str, None),
            'iqn': (str, None),
            'iscsiInterface': (str, None),
            'lun': (int, None),
            'portals': (list, str),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),
            'targetPortal': (str, None),

        }

    @property
    def chap_auth_discovery(self) -> bool:
        """
        whether support iSCSI Discovery CHAP authentication
        """
        return self._properties.get('chapAuthDiscovery')

    @chap_auth_discovery.setter
    def chap_auth_discovery(self, value: bool):
        """
        whether support iSCSI Discovery CHAP authentication
        """
        self._properties['chapAuthDiscovery'] = value

    @property
    def chap_auth_session(self) -> bool:
        """
        whether support iSCSI Session CHAP authentication
        """
        return self._properties.get('chapAuthSession')

    @chap_auth_session.setter
    def chap_auth_session(self, value: bool):
        """
        whether support iSCSI Session CHAP authentication
        """
        self._properties['chapAuthSession'] = value

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#iscsi
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#iscsi
        """
        self._properties['fsType'] = value

    @property
    def initiator_name(self) -> str:
        """
        Custom iSCSI Initiator Name. If initiatorName is specified
        with iscsiInterface simultaneously, new iSCSI interface
        <target portal>:<volume name> will be created for the
        connection.
        """
        return self._properties.get('initiatorName')

    @initiator_name.setter
    def initiator_name(self, value: str):
        """
        Custom iSCSI Initiator Name. If initiatorName is specified
        with iscsiInterface simultaneously, new iSCSI interface
        <target portal>:<volume name> will be created for the
        connection.
        """
        self._properties['initiatorName'] = value

    @property
    def iqn(self) -> str:
        """
        Target iSCSI Qualified Name.
        """
        return self._properties.get('iqn')

    @iqn.setter
    def iqn(self, value: str):
        """
        Target iSCSI Qualified Name.
        """
        self._properties['iqn'] = value

    @property
    def iscsi_interface(self) -> str:
        """
        iSCSI Interface Name that uses an iSCSI transport. Defaults
        to 'default' (tcp).
        """
        return self._properties.get('iscsiInterface')

    @iscsi_interface.setter
    def iscsi_interface(self, value: str):
        """
        iSCSI Interface Name that uses an iSCSI transport. Defaults
        to 'default' (tcp).
        """
        self._properties['iscsiInterface'] = value

    @property
    def lun(self) -> int:
        """
        iSCSI Target Lun number.
        """
        return self._properties.get('lun')

    @lun.setter
    def lun(self, value: int):
        """
        iSCSI Target Lun number.
        """
        self._properties['lun'] = value

    @property
    def portals(self) -> typing.List[str]:
        """
        iSCSI Target Portal List. The portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        return self._properties.get('portals')

    @portals.setter
    def portals(self, value: typing.List[str]):
        """
        iSCSI Target Portal List. The portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        self._properties['portals'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        CHAP Secret for iSCSI target and initiator authentication
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        CHAP Secret for iSCSI target and initiator authentication
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def target_portal(self) -> str:
        """
        iSCSI Target Portal. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        return self._properties.get('targetPortal')

    @target_portal.setter
    def target_portal(self, value: str):
        """
        iSCSI Target Portal. The Portal is either an IP or
        ip_addr:port if the port is other than default (typically
        TCP ports 860 and 3260).
        """
        self._properties['targetPortal'] = value

    def __enter__(self) -> 'ISCSIVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class KeyToPath(_kuber_definitions.Definition):
    """
    Maps a string key to a path within a volume.
    """

    def __init__(
            self,
            key: str = None,
            mode: int = None,
            path: str = None,
    ):
        """Create KeyToPath instance."""
        super(KeyToPath, self).__init__(
            api_version='core/v1',
            kind='KeyToPath'
        )
        self._properties = {
            'key': key or '',
            'mode': mode or None,
            'path': path or '',

        }
        self._types = {
            'key': (str, None),
            'mode': (int, None),
            'path': (str, None),

        }

    @property
    def key(self) -> str:
        """
        The key to project.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        The key to project.
        """
        self._properties['key'] = value

    @property
    def mode(self) -> int:
        """
        Optional: mode bits to use on this file, must be a value
        between 0 and 0777. If not specified, the volume defaultMode
        will be used. This might be in conflict with other options
        that affect the file mode, like fsGroup, and the result can
        be other mode bits set.
        """
        return self._properties.get('mode')

    @mode.setter
    def mode(self, value: int):
        """
        Optional: mode bits to use on this file, must be a value
        between 0 and 0777. If not specified, the volume defaultMode
        will be used. This might be in conflict with other options
        that affect the file mode, like fsGroup, and the result can
        be other mode bits set.
        """
        self._properties['mode'] = value

    @property
    def path(self) -> str:
        """
        The relative path of the file to map the key to. May not be
        an absolute path. May not contain the path element '..'. May
        not start with the string '..'.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        The relative path of the file to map the key to. May not be
        an absolute path. May not contain the path element '..'. May
        not start with the string '..'.
        """
        self._properties['path'] = value

    def __enter__(self) -> 'KeyToPath':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Lifecycle(_kuber_definitions.Definition):
    """
    Lifecycle describes actions that the management system
    should take in response to container lifecycle events. For
    the PostStart and PreStop lifecycle handlers, management of
    the container blocks until the action is complete, unless
    the container process fails, in which case the handler is
    aborted.
    """

    def __init__(
            self,
            post_start: 'Handler' = None,
            pre_stop: 'Handler' = None,
    ):
        """Create Lifecycle instance."""
        super(Lifecycle, self).__init__(
            api_version='core/v1',
            kind='Lifecycle'
        )
        self._properties = {
            'postStart': post_start or Handler(),
            'preStop': pre_stop or Handler(),

        }
        self._types = {
            'postStart': (Handler, None),
            'preStop': (Handler, None),

        }

    @property
    def post_start(self) -> 'Handler':
        """
        PostStart is called immediately after a container is
        created. If the handler fails, the container is terminated
        and restarted according to its restart policy. Other
        management of the container blocks until the hook completes.
        More info:
        https://kubernetes.io/docs/concepts/containers/container-
        lifecycle-hooks/#container-hooks
        """
        return self._properties.get('postStart')

    @post_start.setter
    def post_start(self, value: typing.Union['Handler', dict]):
        """
        PostStart is called immediately after a container is
        created. If the handler fails, the container is terminated
        and restarted according to its restart policy. Other
        management of the container blocks until the hook completes.
        More info:
        https://kubernetes.io/docs/concepts/containers/container-
        lifecycle-hooks/#container-hooks
        """
        if isinstance(value, dict):
            value = Handler().from_dict(value)
        self._properties['postStart'] = value

    @property
    def pre_stop(self) -> 'Handler':
        """
        PreStop is called immediately before a container is
        terminated due to an API request or management event such as
        liveness probe failure, preemption, resource contention,
        etc. The handler is not called if the container crashes or
        exits. The reason for termination is passed to the handler.
        The Pod's termination grace period countdown begins before
        the PreStop hooked is executed. Regardless of the outcome of
        the handler, the container will eventually terminate within
        the Pod's termination grace period. Other management of the
        container blocks until the hook completes or until the
        termination grace period is reached. More info:
        https://kubernetes.io/docs/concepts/containers/container-
        lifecycle-hooks/#container-hooks
        """
        return self._properties.get('preStop')

    @pre_stop.setter
    def pre_stop(self, value: typing.Union['Handler', dict]):
        """
        PreStop is called immediately before a container is
        terminated due to an API request or management event such as
        liveness probe failure, preemption, resource contention,
        etc. The handler is not called if the container crashes or
        exits. The reason for termination is passed to the handler.
        The Pod's termination grace period countdown begins before
        the PreStop hooked is executed. Regardless of the outcome of
        the handler, the container will eventually terminate within
        the Pod's termination grace period. Other management of the
        container blocks until the hook completes or until the
        termination grace period is reached. More info:
        https://kubernetes.io/docs/concepts/containers/container-
        lifecycle-hooks/#container-hooks
        """
        if isinstance(value, dict):
            value = Handler().from_dict(value)
        self._properties['preStop'] = value

    def __enter__(self) -> 'Lifecycle':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitRange(_kuber_definitions.Resource):
    """
    LimitRange sets resource usage limits for each kind of
    resource in a Namespace.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'LimitRangeSpec' = None,
    ):
        """Create LimitRange instance."""
        super(LimitRange, self).__init__(
            api_version='core/v1',
            kind='LimitRange'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or LimitRangeSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (LimitRangeSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'LimitRangeSpec':
        """
        Spec defines the limits enforced. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['LimitRangeSpec', dict]):
        """
        Spec defines the limits enforced. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = LimitRangeSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the LimitRange in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_limit_range',
            'create_limit_range'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the LimitRange in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_limit_range',
            'replace_limit_range'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the LimitRange in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_limit_range',
            'patch_limit_range'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the LimitRange from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_limit_range',
            'read_limit_range'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the LimitRange from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_limit_range',
            'delete_limit_range'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'LimitRange':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitRangeItem(_kuber_definitions.Definition):
    """
    LimitRangeItem defines a min/max usage limit for any
    resource that matches on kind.
    """

    def __init__(
            self,
            default: dict = None,
            default_request: dict = None,
            max_: dict = None,
            max_limit_request_ratio: dict = None,
            min_: dict = None,
            type_: str = None,
    ):
        """Create LimitRangeItem instance."""
        super(LimitRangeItem, self).__init__(
            api_version='core/v1',
            kind='LimitRangeItem'
        )
        self._properties = {
            'default': default or {},
            'defaultRequest': default_request or {},
            'max': max_ or {},
            'maxLimitRequestRatio': max_limit_request_ratio or {},
            'min': min_ or {},
            'type': type_ or '',

        }
        self._types = {
            'default': (dict, None),
            'defaultRequest': (dict, None),
            'max': (dict, None),
            'maxLimitRequestRatio': (dict, None),
            'min': (dict, None),
            'type': (str, None),

        }

    @property
    def default(self) -> dict:
        """
        Default resource requirement limit value by resource name if
        resource limit is omitted.
        """
        return self._properties.get('default')

    @default.setter
    def default(self, value: dict):
        """
        Default resource requirement limit value by resource name if
        resource limit is omitted.
        """
        self._properties['default'] = value

    @property
    def default_request(self) -> dict:
        """
        DefaultRequest is the default resource requirement request
        value by resource name if resource request is omitted.
        """
        return self._properties.get('defaultRequest')

    @default_request.setter
    def default_request(self, value: dict):
        """
        DefaultRequest is the default resource requirement request
        value by resource name if resource request is omitted.
        """
        self._properties['defaultRequest'] = value

    @property
    def max_(self) -> dict:
        """
        Max usage constraints on this kind by resource name.
        """
        return self._properties.get('max')

    @max_.setter
    def max_(self, value: dict):
        """
        Max usage constraints on this kind by resource name.
        """
        self._properties['max'] = value

    @property
    def max_limit_request_ratio(self) -> dict:
        """
        MaxLimitRequestRatio if specified, the named resource must
        have a request and limit that are both non-zero where limit
        divided by request is less than or equal to the enumerated
        value; this represents the max burst for the named resource.
        """
        return self._properties.get('maxLimitRequestRatio')

    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, value: dict):
        """
        MaxLimitRequestRatio if specified, the named resource must
        have a request and limit that are both non-zero where limit
        divided by request is less than or equal to the enumerated
        value; this represents the max burst for the named resource.
        """
        self._properties['maxLimitRequestRatio'] = value

    @property
    def min_(self) -> dict:
        """
        Min usage constraints on this kind by resource name.
        """
        return self._properties.get('min')

    @min_.setter
    def min_(self, value: dict):
        """
        Min usage constraints on this kind by resource name.
        """
        self._properties['min'] = value

    @property
    def type_(self) -> str:
        """
        Type of resource that this limit applies to.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of resource that this limit applies to.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'LimitRangeItem':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitRangeList(_kuber_definitions.Collection):
    """
    LimitRangeList is a list of LimitRange items.
    """

    def __init__(
            self,
            items: typing.List['LimitRange'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create LimitRangeList instance."""
        super(LimitRangeList, self).__init__(
            api_version='core/v1',
            kind='LimitRangeList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, LimitRange),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['LimitRange']:
        """
        Items is a list of LimitRange objects. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['LimitRange'], typing.List[dict]]
    ):
        """
        Items is a list of LimitRange objects. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LimitRange().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'LimitRangeList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitRangeSpec(_kuber_definitions.Definition):
    """
    LimitRangeSpec defines a min/max usage limit for resources
    that match on kind.
    """

    def __init__(
            self,
            limits: typing.List['LimitRangeItem'] = None,
    ):
        """Create LimitRangeSpec instance."""
        super(LimitRangeSpec, self).__init__(
            api_version='core/v1',
            kind='LimitRangeSpec'
        )
        self._properties = {
            'limits': limits or [],

        }
        self._types = {
            'limits': (list, LimitRangeItem),

        }

    @property
    def limits(self) -> typing.List['LimitRangeItem']:
        """
        Limits is the list of LimitRangeItem objects that are
        enforced.
        """
        return self._properties.get('limits')

    @limits.setter
    def limits(
            self,
            value: typing.Union[typing.List['LimitRangeItem'], typing.List[dict]]
    ):
        """
        Limits is the list of LimitRangeItem objects that are
        enforced.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LimitRangeItem().from_dict(item)
            cleaned.append(item)
        self._properties['limits'] = cleaned

    def __enter__(self) -> 'LimitRangeSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LoadBalancerIngress(_kuber_definitions.Definition):
    """
    LoadBalancerIngress represents the status of a load-balancer
    ingress point: traffic intended for the service should be
    sent to an ingress point.
    """

    def __init__(
            self,
            hostname: str = None,
            ip: str = None,
    ):
        """Create LoadBalancerIngress instance."""
        super(LoadBalancerIngress, self).__init__(
            api_version='core/v1',
            kind='LoadBalancerIngress'
        )
        self._properties = {
            'hostname': hostname or '',
            'ip': ip or '',

        }
        self._types = {
            'hostname': (str, None),
            'ip': (str, None),

        }

    @property
    def hostname(self) -> str:
        """
        Hostname is set for load-balancer ingress points that are
        DNS based (typically AWS load-balancers)
        """
        return self._properties.get('hostname')

    @hostname.setter
    def hostname(self, value: str):
        """
        Hostname is set for load-balancer ingress points that are
        DNS based (typically AWS load-balancers)
        """
        self._properties['hostname'] = value

    @property
    def ip(self) -> str:
        """
        IP is set for load-balancer ingress points that are IP based
        (typically GCE or OpenStack load-balancers)
        """
        return self._properties.get('ip')

    @ip.setter
    def ip(self, value: str):
        """
        IP is set for load-balancer ingress points that are IP based
        (typically GCE or OpenStack load-balancers)
        """
        self._properties['ip'] = value

    def __enter__(self) -> 'LoadBalancerIngress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LoadBalancerStatus(_kuber_definitions.Definition):
    """
    LoadBalancerStatus represents the status of a load-balancer.
    """

    def __init__(
            self,
            ingress: typing.List['LoadBalancerIngress'] = None,
    ):
        """Create LoadBalancerStatus instance."""
        super(LoadBalancerStatus, self).__init__(
            api_version='core/v1',
            kind='LoadBalancerStatus'
        )
        self._properties = {
            'ingress': ingress or [],

        }
        self._types = {
            'ingress': (list, LoadBalancerIngress),

        }

    @property
    def ingress(self) -> typing.List['LoadBalancerIngress']:
        """
        Ingress is a list containing ingress points for the load-
        balancer. Traffic intended for the service should be sent to
        these ingress points.
        """
        return self._properties.get('ingress')

    @ingress.setter
    def ingress(
            self,
            value: typing.Union[typing.List['LoadBalancerIngress'], typing.List[dict]]
    ):
        """
        Ingress is a list containing ingress points for the load-
        balancer. Traffic intended for the service should be sent to
        these ingress points.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LoadBalancerIngress().from_dict(item)
            cleaned.append(item)
        self._properties['ingress'] = cleaned

    def __enter__(self) -> 'LoadBalancerStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LocalObjectReference(_kuber_definitions.Definition):
    """
    LocalObjectReference contains enough information to let you
    locate the referenced object inside the same namespace.
    """

    def __init__(
            self,
            name: str = None,
    ):
        """Create LocalObjectReference instance."""
        super(LocalObjectReference, self).__init__(
            api_version='core/v1',
            kind='LocalObjectReference'
        )
        self._properties = {
            'name': name or '',

        }
        self._types = {
            'name': (str, None),

        }

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    def __enter__(self) -> 'LocalObjectReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LocalVolumeSource(_kuber_definitions.Definition):
    """
    Local represents directly-attached storage with node
    affinity (Beta feature)
    """

    def __init__(
            self,
            fs_type: str = None,
            path: str = None,
    ):
        """Create LocalVolumeSource instance."""
        super(LocalVolumeSource, self).__init__(
            api_version='core/v1',
            kind='LocalVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'path': path or '',

        }
        self._types = {
            'fsType': (str, None),
            'path': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. It applies only when the Path is a
        block device. Must be a filesystem type supported by the
        host operating system. Ex. "ext4", "xfs", "ntfs". The
        default value is to auto-select a fileystem if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. It applies only when the Path is a
        block device. Must be a filesystem type supported by the
        host operating system. Ex. "ext4", "xfs", "ntfs". The
        default value is to auto-select a fileystem if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def path(self) -> str:
        """
        The full path to the volume on the node. It can be either a
        directory or block device (disk, partition, ...).
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        The full path to the volume on the node. It can be either a
        directory or block device (disk, partition, ...).
        """
        self._properties['path'] = value

    def __enter__(self) -> 'LocalVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NFSVolumeSource(_kuber_definitions.Definition):
    """
    Represents an NFS mount that lasts the lifetime of a pod.
    NFS volumes do not support ownership management or SELinux
    relabeling.
    """

    def __init__(
            self,
            path: str = None,
            read_only: bool = None,
            server: str = None,
    ):
        """Create NFSVolumeSource instance."""
        super(NFSVolumeSource, self).__init__(
            api_version='core/v1',
            kind='NFSVolumeSource'
        )
        self._properties = {
            'path': path or '',
            'readOnly': read_only or None,
            'server': server or '',

        }
        self._types = {
            'path': (str, None),
            'readOnly': (bool, None),
            'server': (str, None),

        }

    @property
    def path(self) -> str:
        """
        Path that is exported by the NFS server. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path that is exported by the NFS server. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        self._properties['path'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the NFS export to be mounted with
        read-only permissions. Defaults to false. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the NFS export to be mounted with
        read-only permissions. Defaults to false. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        self._properties['readOnly'] = value

    @property
    def server(self) -> str:
        """
        Server is the hostname or IP address of the NFS server. More
        info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        return self._properties.get('server')

    @server.setter
    def server(self, value: str):
        """
        Server is the hostname or IP address of the NFS server. More
        info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        self._properties['server'] = value

    def __enter__(self) -> 'NFSVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Namespace(_kuber_definitions.Resource):
    """
    Namespace provides a scope for Names. Use of multiple
    namespaces is optional.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'NamespaceSpec' = None,
            status: 'NamespaceStatus' = None,
    ):
        """Create Namespace instance."""
        super(Namespace, self).__init__(
            api_version='core/v1',
            kind='Namespace'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or NamespaceSpec(),
            'status': status or NamespaceStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (NamespaceSpec, None),
            'status': (NamespaceStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'NamespaceSpec':
        """
        Spec defines the behavior of the Namespace. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['NamespaceSpec', dict]):
        """
        Spec defines the behavior of the Namespace. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = NamespaceSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'NamespaceStatus':
        """
        Status describes the current status of a Namespace. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['NamespaceStatus', dict]):
        """
        Status describes the current status of a Namespace. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = NamespaceStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'NamespaceStatus':
        """
        Creates the Namespace in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_namespace',
            'create_namespace'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            NamespaceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'NamespaceStatus':
        """
        Replaces the Namespace in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_namespace',
            'replace_namespace'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            NamespaceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'NamespaceStatus':
        """
        Patches the Namespace in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_namespace',
            'patch_namespace'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            NamespaceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'NamespaceStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_namespace',
            'read_namespace'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            NamespaceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Namespace from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_namespace',
            'read_namespace'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Namespace from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_namespace',
            'delete_namespace'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Namespace':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamespaceList(_kuber_definitions.Collection):
    """
    NamespaceList is a list of Namespaces.
    """

    def __init__(
            self,
            items: typing.List['Namespace'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create NamespaceList instance."""
        super(NamespaceList, self).__init__(
            api_version='core/v1',
            kind='NamespaceList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Namespace),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Namespace']:
        """
        Items is the list of Namespace objects in the list. More
        info: https://kubernetes.io/docs/concepts/overview/working-
        with-objects/namespaces/
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Namespace'], typing.List[dict]]
    ):
        """
        Items is the list of Namespace objects in the list. More
        info: https://kubernetes.io/docs/concepts/overview/working-
        with-objects/namespaces/
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Namespace().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'NamespaceList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamespaceSpec(_kuber_definitions.Definition):
    """
    NamespaceSpec describes the attributes on a Namespace.
    """

    def __init__(
            self,
            finalizers: typing.List[str] = None,
    ):
        """Create NamespaceSpec instance."""
        super(NamespaceSpec, self).__init__(
            api_version='core/v1',
            kind='NamespaceSpec'
        )
        self._properties = {
            'finalizers': finalizers or [],

        }
        self._types = {
            'finalizers': (list, str),

        }

    @property
    def finalizers(self) -> typing.List[str]:
        """
        Finalizers is an opaque list of values that must be empty to
        permanently remove object from storage. More info:
        https://kubernetes.io/docs/tasks/administer-
        cluster/namespaces/
        """
        return self._properties.get('finalizers')

    @finalizers.setter
    def finalizers(self, value: typing.List[str]):
        """
        Finalizers is an opaque list of values that must be empty to
        permanently remove object from storage. More info:
        https://kubernetes.io/docs/tasks/administer-
        cluster/namespaces/
        """
        self._properties['finalizers'] = value

    def __enter__(self) -> 'NamespaceSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamespaceStatus(_kuber_definitions.Definition):
    """
    NamespaceStatus is information about the current status of a
    Namespace.
    """

    def __init__(
            self,
            phase: str = None,
    ):
        """Create NamespaceStatus instance."""
        super(NamespaceStatus, self).__init__(
            api_version='core/v1',
            kind='NamespaceStatus'
        )
        self._properties = {
            'phase': phase or '',

        }
        self._types = {
            'phase': (str, None),

        }

    @property
    def phase(self) -> str:
        """
        Phase is the current lifecycle phase of the namespace. More
        info: https://kubernetes.io/docs/tasks/administer-
        cluster/namespaces/
        """
        return self._properties.get('phase')

    @phase.setter
    def phase(self, value: str):
        """
        Phase is the current lifecycle phase of the namespace. More
        info: https://kubernetes.io/docs/tasks/administer-
        cluster/namespaces/
        """
        self._properties['phase'] = value

    def __enter__(self) -> 'NamespaceStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Node(_kuber_definitions.Resource):
    """
    Node is a worker node in Kubernetes. Each node will have a
    unique identifier in the cache (i.e. in etcd).
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'NodeSpec' = None,
            status: 'NodeStatus' = None,
    ):
        """Create Node instance."""
        super(Node, self).__init__(
            api_version='core/v1',
            kind='Node'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or NodeSpec(),
            'status': status or NodeStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (NodeSpec, None),
            'status': (NodeStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'NodeSpec':
        """
        Spec defines the behavior of a node.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['NodeSpec', dict]):
        """
        Spec defines the behavior of a node.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = NodeSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'NodeStatus':
        """
        Most recently observed status of the node. Populated by the
        system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['NodeStatus', dict]):
        """
        Most recently observed status of the node. Populated by the
        system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = NodeStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'NodeStatus':
        """
        Creates the Node in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_node',
            'create_node'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            NodeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'NodeStatus':
        """
        Replaces the Node in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_node',
            'replace_node'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            NodeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'NodeStatus':
        """
        Patches the Node in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_node',
            'patch_node'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            NodeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'NodeStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_node',
            'read_node'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            NodeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Node from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_node',
            'read_node'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Node from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_node',
            'delete_node'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Node':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeAddress(_kuber_definitions.Definition):
    """
    NodeAddress contains information for the node's address.
    """

    def __init__(
            self,
            address: str = None,
            type_: str = None,
    ):
        """Create NodeAddress instance."""
        super(NodeAddress, self).__init__(
            api_version='core/v1',
            kind='NodeAddress'
        )
        self._properties = {
            'address': address or '',
            'type': type_ or '',

        }
        self._types = {
            'address': (str, None),
            'type': (str, None),

        }

    @property
    def address(self) -> str:
        """
        The node address.
        """
        return self._properties.get('address')

    @address.setter
    def address(self, value: str):
        """
        The node address.
        """
        self._properties['address'] = value

    @property
    def type_(self) -> str:
        """
        Node address type, one of Hostname, ExternalIP or
        InternalIP.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Node address type, one of Hostname, ExternalIP or
        InternalIP.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'NodeAddress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeAffinity(_kuber_definitions.Definition):
    """
    Node affinity is a group of node affinity scheduling rules.
    """

    def __init__(
            self,
            preferred_during_scheduling_ignored_during_execution: typing.List['PreferredSchedulingTerm'] = None,
            required_during_scheduling_ignored_during_execution: 'NodeSelector' = None,
    ):
        """Create NodeAffinity instance."""
        super(NodeAffinity, self).__init__(
            api_version='core/v1',
            kind='NodeAffinity'
        )
        self._properties = {
            'preferredDuringSchedulingIgnoredDuringExecution': preferred_during_scheduling_ignored_during_execution or [],
            'requiredDuringSchedulingIgnoredDuringExecution': required_during_scheduling_ignored_during_execution or NodeSelector(),

        }
        self._types = {
            'preferredDuringSchedulingIgnoredDuringExecution': (list, PreferredSchedulingTerm),
            'requiredDuringSchedulingIgnoredDuringExecution': (NodeSelector, None),

        }

    @property
    def preferred_during_scheduling_ignored_during_execution(self) -> typing.List['PreferredSchedulingTerm']:
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the affinity expressions specified by this field,
        but it may choose a node that violates one or more of the
        expressions. The node that is most preferred is the one with
        the greatest sum of weights, i.e. for each node that meets
        all of the scheduling requirements (resource request,
        requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node matches the
        corresponding matchExpressions; the node(s) with the highest
        sum are the most preferred.
        """
        return self._properties.get('preferredDuringSchedulingIgnoredDuringExecution')

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(
            self,
            value: typing.Union[typing.List['PreferredSchedulingTerm'], typing.List[dict]]
    ):
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the affinity expressions specified by this field,
        but it may choose a node that violates one or more of the
        expressions. The node that is most preferred is the one with
        the greatest sum of weights, i.e. for each node that meets
        all of the scheduling requirements (resource request,
        requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node matches the
        corresponding matchExpressions; the node(s) with the highest
        sum are the most preferred.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PreferredSchedulingTerm().from_dict(item)
            cleaned.append(item)
        self._properties['preferredDuringSchedulingIgnoredDuringExecution'] = cleaned

    @property
    def required_during_scheduling_ignored_during_execution(self) -> 'NodeSelector':
        """
        If the affinity requirements specified by this field are not
        met at scheduling time, the pod will not be scheduled onto
        the node. If the affinity requirements specified by this
        field cease to be met at some point during pod execution
        (e.g. due to an update), the system may or may not try to
        eventually evict the pod from its node.
        """
        return self._properties.get('requiredDuringSchedulingIgnoredDuringExecution')

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, value: typing.Union['NodeSelector', dict]):
        """
        If the affinity requirements specified by this field are not
        met at scheduling time, the pod will not be scheduled onto
        the node. If the affinity requirements specified by this
        field cease to be met at some point during pod execution
        (e.g. due to an update), the system may or may not try to
        eventually evict the pod from its node.
        """
        if isinstance(value, dict):
            value = NodeSelector().from_dict(value)
        self._properties['requiredDuringSchedulingIgnoredDuringExecution'] = value

    def __enter__(self) -> 'NodeAffinity':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeCondition(_kuber_definitions.Definition):
    """
    NodeCondition contains condition information for a node.
    """

    def __init__(
            self,
            last_heartbeat_time: str = None,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create NodeCondition instance."""
        super(NodeCondition, self).__init__(
            api_version='core/v1',
            kind='NodeCondition'
        )
        self._properties = {
            'lastHeartbeatTime': last_heartbeat_time or None,
            'lastTransitionTime': last_transition_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastHeartbeatTime': (str, None),
            'lastTransitionTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_heartbeat_time(self) -> str:
        """
        Last time we got an update on a given condition.
        """
        return self._properties.get('lastHeartbeatTime')

    @last_heartbeat_time.setter
    def last_heartbeat_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time we got an update on a given condition.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastHeartbeatTime'] = value

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transit from one status to another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition transit from one status to another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        Human readable message indicating details about last
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Human readable message indicating details about last
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        (brief) reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        (brief) reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of node condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of node condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'NodeCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeConfigSource(_kuber_definitions.Definition):
    """
    NodeConfigSource specifies a source of node configuration.
    Exactly one subfield (excluding metadata) must be non-nil.
    """

    def __init__(
            self,
            config_map: 'ConfigMapNodeConfigSource' = None,
    ):
        """Create NodeConfigSource instance."""
        super(NodeConfigSource, self).__init__(
            api_version='core/v1',
            kind='NodeConfigSource'
        )
        self._properties = {
            'configMap': config_map or ConfigMapNodeConfigSource(),

        }
        self._types = {
            'configMap': (ConfigMapNodeConfigSource, None),

        }

    @property
    def config_map(self) -> 'ConfigMapNodeConfigSource':
        """
        ConfigMap is a reference to a Node's ConfigMap
        """
        return self._properties.get('configMap')

    @config_map.setter
    def config_map(self, value: typing.Union['ConfigMapNodeConfigSource', dict]):
        """
        ConfigMap is a reference to a Node's ConfigMap
        """
        if isinstance(value, dict):
            value = ConfigMapNodeConfigSource().from_dict(value)
        self._properties['configMap'] = value

    def __enter__(self) -> 'NodeConfigSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeConfigStatus(_kuber_definitions.Definition):
    """
    NodeConfigStatus describes the status of the config assigned
    by Node.Spec.ConfigSource.
    """

    def __init__(
            self,
            active: 'NodeConfigSource' = None,
            assigned: 'NodeConfigSource' = None,
            error: str = None,
            last_known_good: 'NodeConfigSource' = None,
    ):
        """Create NodeConfigStatus instance."""
        super(NodeConfigStatus, self).__init__(
            api_version='core/v1',
            kind='NodeConfigStatus'
        )
        self._properties = {
            'active': active or NodeConfigSource(),
            'assigned': assigned or NodeConfigSource(),
            'error': error or '',
            'lastKnownGood': last_known_good or NodeConfigSource(),

        }
        self._types = {
            'active': (NodeConfigSource, None),
            'assigned': (NodeConfigSource, None),
            'error': (str, None),
            'lastKnownGood': (NodeConfigSource, None),

        }

    @property
    def active(self) -> 'NodeConfigSource':
        """
        Active reports the checkpointed config the node is actively
        using. Active will represent either the current version of
        the Assigned config, or the current LastKnownGood config,
        depending on whether attempting to use the Assigned config
        results in an error.
        """
        return self._properties.get('active')

    @active.setter
    def active(self, value: typing.Union['NodeConfigSource', dict]):
        """
        Active reports the checkpointed config the node is actively
        using. Active will represent either the current version of
        the Assigned config, or the current LastKnownGood config,
        depending on whether attempting to use the Assigned config
        results in an error.
        """
        if isinstance(value, dict):
            value = NodeConfigSource().from_dict(value)
        self._properties['active'] = value

    @property
    def assigned(self) -> 'NodeConfigSource':
        """
        Assigned reports the checkpointed config the node will try
        to use. When Node.Spec.ConfigSource is updated, the node
        checkpoints the associated config payload to local disk,
        along with a record indicating intended config. The node
        refers to this record to choose its config checkpoint, and
        reports this record in Assigned. Assigned only updates in
        the status after the record has been checkpointed to disk.
        When the Kubelet is restarted, it tries to make the Assigned
        config the Active config by loading and validating the
        checkpointed payload identified by Assigned.
        """
        return self._properties.get('assigned')

    @assigned.setter
    def assigned(self, value: typing.Union['NodeConfigSource', dict]):
        """
        Assigned reports the checkpointed config the node will try
        to use. When Node.Spec.ConfigSource is updated, the node
        checkpoints the associated config payload to local disk,
        along with a record indicating intended config. The node
        refers to this record to choose its config checkpoint, and
        reports this record in Assigned. Assigned only updates in
        the status after the record has been checkpointed to disk.
        When the Kubelet is restarted, it tries to make the Assigned
        config the Active config by loading and validating the
        checkpointed payload identified by Assigned.
        """
        if isinstance(value, dict):
            value = NodeConfigSource().from_dict(value)
        self._properties['assigned'] = value

    @property
    def error(self) -> str:
        """
        Error describes any problems reconciling the
        Spec.ConfigSource to the Active config. Errors may occur,
        for example, attempting to checkpoint Spec.ConfigSource to
        the local Assigned record, attempting to checkpoint the
        payload associated with Spec.ConfigSource, attempting to
        load or validate the Assigned config, etc. Errors may occur
        at different points while syncing config. Earlier errors
        (e.g. download or checkpointing errors) will not result in a
        rollback to LastKnownGood, and may resolve across Kubelet
        retries. Later errors (e.g. loading or validating a
        checkpointed config) will result in a rollback to
        LastKnownGood. In the latter case, it is usually possible to
        resolve the error by fixing the config assigned in
        Spec.ConfigSource. You can find additional information for
        debugging by searching the error message in the Kubelet log.
        Error is a human-readable description of the error state;
        machines can check whether or not Error is empty, but should
        not rely on the stability of the Error text across Kubelet
        versions.
        """
        return self._properties.get('error')

    @error.setter
    def error(self, value: str):
        """
        Error describes any problems reconciling the
        Spec.ConfigSource to the Active config. Errors may occur,
        for example, attempting to checkpoint Spec.ConfigSource to
        the local Assigned record, attempting to checkpoint the
        payload associated with Spec.ConfigSource, attempting to
        load or validate the Assigned config, etc. Errors may occur
        at different points while syncing config. Earlier errors
        (e.g. download or checkpointing errors) will not result in a
        rollback to LastKnownGood, and may resolve across Kubelet
        retries. Later errors (e.g. loading or validating a
        checkpointed config) will result in a rollback to
        LastKnownGood. In the latter case, it is usually possible to
        resolve the error by fixing the config assigned in
        Spec.ConfigSource. You can find additional information for
        debugging by searching the error message in the Kubelet log.
        Error is a human-readable description of the error state;
        machines can check whether or not Error is empty, but should
        not rely on the stability of the Error text across Kubelet
        versions.
        """
        self._properties['error'] = value

    @property
    def last_known_good(self) -> 'NodeConfigSource':
        """
        LastKnownGood reports the checkpointed config the node will
        fall back to when it encounters an error attempting to use
        the Assigned config. The Assigned config becomes the
        LastKnownGood config when the node determines that the
        Assigned config is stable and correct. This is currently
        implemented as a 10-minute soak period starting when the
        local record of Assigned config is updated. If the Assigned
        config is Active at the end of this period, it becomes the
        LastKnownGood. Note that if Spec.ConfigSource is reset to
        nil (use local defaults), the LastKnownGood is also
        immediately reset to nil, because the local default config
        is always assumed good. You should not make assumptions
        about the node's method of determining config stability and
        correctness, as this may change or become configurable in
        the future.
        """
        return self._properties.get('lastKnownGood')

    @last_known_good.setter
    def last_known_good(self, value: typing.Union['NodeConfigSource', dict]):
        """
        LastKnownGood reports the checkpointed config the node will
        fall back to when it encounters an error attempting to use
        the Assigned config. The Assigned config becomes the
        LastKnownGood config when the node determines that the
        Assigned config is stable and correct. This is currently
        implemented as a 10-minute soak period starting when the
        local record of Assigned config is updated. If the Assigned
        config is Active at the end of this period, it becomes the
        LastKnownGood. Note that if Spec.ConfigSource is reset to
        nil (use local defaults), the LastKnownGood is also
        immediately reset to nil, because the local default config
        is always assumed good. You should not make assumptions
        about the node's method of determining config stability and
        correctness, as this may change or become configurable in
        the future.
        """
        if isinstance(value, dict):
            value = NodeConfigSource().from_dict(value)
        self._properties['lastKnownGood'] = value

    def __enter__(self) -> 'NodeConfigStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeDaemonEndpoints(_kuber_definitions.Definition):
    """
    NodeDaemonEndpoints lists ports opened by daemons running on
    the Node.
    """

    def __init__(
            self,
            kubelet_endpoint: 'DaemonEndpoint' = None,
    ):
        """Create NodeDaemonEndpoints instance."""
        super(NodeDaemonEndpoints, self).__init__(
            api_version='core/v1',
            kind='NodeDaemonEndpoints'
        )
        self._properties = {
            'kubeletEndpoint': kubelet_endpoint or DaemonEndpoint(),

        }
        self._types = {
            'kubeletEndpoint': (DaemonEndpoint, None),

        }

    @property
    def kubelet_endpoint(self) -> 'DaemonEndpoint':
        """
        Endpoint on which Kubelet is listening.
        """
        return self._properties.get('kubeletEndpoint')

    @kubelet_endpoint.setter
    def kubelet_endpoint(self, value: typing.Union['DaemonEndpoint', dict]):
        """
        Endpoint on which Kubelet is listening.
        """
        if isinstance(value, dict):
            value = DaemonEndpoint().from_dict(value)
        self._properties['kubeletEndpoint'] = value

    def __enter__(self) -> 'NodeDaemonEndpoints':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeList(_kuber_definitions.Collection):
    """
    NodeList is the whole list of all Nodes which have been
    registered with master.
    """

    def __init__(
            self,
            items: typing.List['Node'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create NodeList instance."""
        super(NodeList, self).__init__(
            api_version='core/v1',
            kind='NodeList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Node),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Node']:
        """
        List of nodes
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Node'], typing.List[dict]]
    ):
        """
        List of nodes
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Node().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'NodeList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeSelector(_kuber_definitions.Definition):
    """
    A node selector represents the union of the results of one
    or more label queries over a set of nodes; that is, it
    represents the OR of the selectors represented by the node
    selector terms.
    """

    def __init__(
            self,
            node_selector_terms: typing.List['NodeSelectorTerm'] = None,
    ):
        """Create NodeSelector instance."""
        super(NodeSelector, self).__init__(
            api_version='core/v1',
            kind='NodeSelector'
        )
        self._properties = {
            'nodeSelectorTerms': node_selector_terms or [],

        }
        self._types = {
            'nodeSelectorTerms': (list, NodeSelectorTerm),

        }

    @property
    def node_selector_terms(self) -> typing.List['NodeSelectorTerm']:
        """
        Required. A list of node selector terms. The terms are ORed.
        """
        return self._properties.get('nodeSelectorTerms')

    @node_selector_terms.setter
    def node_selector_terms(
            self,
            value: typing.Union[typing.List['NodeSelectorTerm'], typing.List[dict]]
    ):
        """
        Required. A list of node selector terms. The terms are ORed.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NodeSelectorTerm().from_dict(item)
            cleaned.append(item)
        self._properties['nodeSelectorTerms'] = cleaned

    def __enter__(self) -> 'NodeSelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeSelectorRequirement(_kuber_definitions.Definition):
    """
    A node selector requirement is a selector that contains
    values, a key, and an operator that relates the key and
    values.
    """

    def __init__(
            self,
            key: str = None,
            operator: str = None,
            values: typing.List[str] = None,
    ):
        """Create NodeSelectorRequirement instance."""
        super(NodeSelectorRequirement, self).__init__(
            api_version='core/v1',
            kind='NodeSelectorRequirement'
        )
        self._properties = {
            'key': key or '',
            'operator': operator or '',
            'values': values or [],

        }
        self._types = {
            'key': (str, None),
            'operator': (str, None),
            'values': (list, str),

        }

    @property
    def key(self) -> str:
        """
        The label key that the selector applies to.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        The label key that the selector applies to.
        """
        self._properties['key'] = value

    @property
    def operator(self) -> str:
        """
        Represents a key's relationship to a set of values. Valid
        operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        """
        return self._properties.get('operator')

    @operator.setter
    def operator(self, value: str):
        """
        Represents a key's relationship to a set of values. Valid
        operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        """
        self._properties['operator'] = value

    @property
    def values(self) -> typing.List[str]:
        """
        An array of string values. If the operator is In or NotIn,
        the values array must be non-empty. If the operator is
        Exists or DoesNotExist, the values array must be empty. If
        the operator is Gt or Lt, the values array must have a
        single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.
        """
        return self._properties.get('values')

    @values.setter
    def values(self, value: typing.List[str]):
        """
        An array of string values. If the operator is In or NotIn,
        the values array must be non-empty. If the operator is
        Exists or DoesNotExist, the values array must be empty. If
        the operator is Gt or Lt, the values array must have a
        single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.
        """
        self._properties['values'] = value

    def __enter__(self) -> 'NodeSelectorRequirement':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeSelectorTerm(_kuber_definitions.Definition):
    """
    A null or empty node selector term matches no objects. The
    requirements of them are ANDed. The TopologySelectorTerm
    type implements a subset of the NodeSelectorTerm.
    """

    def __init__(
            self,
            match_expressions: typing.List['NodeSelectorRequirement'] = None,
            match_fields: typing.List['NodeSelectorRequirement'] = None,
    ):
        """Create NodeSelectorTerm instance."""
        super(NodeSelectorTerm, self).__init__(
            api_version='core/v1',
            kind='NodeSelectorTerm'
        )
        self._properties = {
            'matchExpressions': match_expressions or [],
            'matchFields': match_fields or [],

        }
        self._types = {
            'matchExpressions': (list, NodeSelectorRequirement),
            'matchFields': (list, NodeSelectorRequirement),

        }

    @property
    def match_expressions(self) -> typing.List['NodeSelectorRequirement']:
        """
        A list of node selector requirements by node's labels.
        """
        return self._properties.get('matchExpressions')

    @match_expressions.setter
    def match_expressions(
            self,
            value: typing.Union[typing.List['NodeSelectorRequirement'], typing.List[dict]]
    ):
        """
        A list of node selector requirements by node's labels.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NodeSelectorRequirement().from_dict(item)
            cleaned.append(item)
        self._properties['matchExpressions'] = cleaned

    @property
    def match_fields(self) -> typing.List['NodeSelectorRequirement']:
        """
        A list of node selector requirements by node's fields.
        """
        return self._properties.get('matchFields')

    @match_fields.setter
    def match_fields(
            self,
            value: typing.Union[typing.List['NodeSelectorRequirement'], typing.List[dict]]
    ):
        """
        A list of node selector requirements by node's fields.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NodeSelectorRequirement().from_dict(item)
            cleaned.append(item)
        self._properties['matchFields'] = cleaned

    def __enter__(self) -> 'NodeSelectorTerm':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeSpec(_kuber_definitions.Definition):
    """
    NodeSpec describes the attributes that a node is created
    with.
    """

    def __init__(
            self,
            config_source: 'NodeConfigSource' = None,
            external_id: str = None,
            pod_cidr: str = None,
            provider_id: str = None,
            taints: typing.List['Taint'] = None,
            unschedulable: bool = None,
    ):
        """Create NodeSpec instance."""
        super(NodeSpec, self).__init__(
            api_version='core/v1',
            kind='NodeSpec'
        )
        self._properties = {
            'configSource': config_source or NodeConfigSource(),
            'externalID': external_id or '',
            'podCIDR': pod_cidr or '',
            'providerID': provider_id or '',
            'taints': taints or [],
            'unschedulable': unschedulable or None,

        }
        self._types = {
            'configSource': (NodeConfigSource, None),
            'externalID': (str, None),
            'podCIDR': (str, None),
            'providerID': (str, None),
            'taints': (list, Taint),
            'unschedulable': (bool, None),

        }

    @property
    def config_source(self) -> 'NodeConfigSource':
        """
        If specified, the source to get node configuration from The
        DynamicKubeletConfig feature gate must be enabled for the
        Kubelet to use this field
        """
        return self._properties.get('configSource')

    @config_source.setter
    def config_source(self, value: typing.Union['NodeConfigSource', dict]):
        """
        If specified, the source to get node configuration from The
        DynamicKubeletConfig feature gate must be enabled for the
        Kubelet to use this field
        """
        if isinstance(value, dict):
            value = NodeConfigSource().from_dict(value)
        self._properties['configSource'] = value

    @property
    def external_id(self) -> str:
        """
        Deprecated. Not all kubelets will set this field. Remove
        field after 1.13. see: https://issues.k8s.io/61966
        """
        return self._properties.get('externalID')

    @external_id.setter
    def external_id(self, value: str):
        """
        Deprecated. Not all kubelets will set this field. Remove
        field after 1.13. see: https://issues.k8s.io/61966
        """
        self._properties['externalID'] = value

    @property
    def pod_cidr(self) -> str:
        """
        PodCIDR represents the pod IP range assigned to the node.
        """
        return self._properties.get('podCIDR')

    @pod_cidr.setter
    def pod_cidr(self, value: str):
        """
        PodCIDR represents the pod IP range assigned to the node.
        """
        self._properties['podCIDR'] = value

    @property
    def provider_id(self) -> str:
        """
        ID of the node assigned by the cloud provider in the format:
        <ProviderName>://<ProviderSpecificNodeID>
        """
        return self._properties.get('providerID')

    @provider_id.setter
    def provider_id(self, value: str):
        """
        ID of the node assigned by the cloud provider in the format:
        <ProviderName>://<ProviderSpecificNodeID>
        """
        self._properties['providerID'] = value

    @property
    def taints(self) -> typing.List['Taint']:
        """
        If specified, the node's taints.
        """
        return self._properties.get('taints')

    @taints.setter
    def taints(
            self,
            value: typing.Union[typing.List['Taint'], typing.List[dict]]
    ):
        """
        If specified, the node's taints.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Taint().from_dict(item)
            cleaned.append(item)
        self._properties['taints'] = cleaned

    @property
    def unschedulable(self) -> bool:
        """
        Unschedulable controls node schedulability of new pods. By
        default, node is schedulable. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#manual-node-
        administration
        """
        return self._properties.get('unschedulable')

    @unschedulable.setter
    def unschedulable(self, value: bool):
        """
        Unschedulable controls node schedulability of new pods. By
        default, node is schedulable. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#manual-node-
        administration
        """
        self._properties['unschedulable'] = value

    def __enter__(self) -> 'NodeSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeStatus(_kuber_definitions.Definition):
    """
    NodeStatus is information about the current status of a
    node.
    """

    def __init__(
            self,
            addresses: typing.List['NodeAddress'] = None,
            allocatable: dict = None,
            capacity: dict = None,
            conditions: typing.List['NodeCondition'] = None,
            config: 'NodeConfigStatus' = None,
            daemon_endpoints: 'NodeDaemonEndpoints' = None,
            images: typing.List['ContainerImage'] = None,
            node_info: 'NodeSystemInfo' = None,
            phase: str = None,
            volumes_attached: typing.List['AttachedVolume'] = None,
            volumes_in_use: typing.List[str] = None,
    ):
        """Create NodeStatus instance."""
        super(NodeStatus, self).__init__(
            api_version='core/v1',
            kind='NodeStatus'
        )
        self._properties = {
            'addresses': addresses or [],
            'allocatable': allocatable or {},
            'capacity': capacity or {},
            'conditions': conditions or [],
            'config': config or NodeConfigStatus(),
            'daemonEndpoints': daemon_endpoints or NodeDaemonEndpoints(),
            'images': images or [],
            'nodeInfo': node_info or NodeSystemInfo(),
            'phase': phase or '',
            'volumesAttached': volumes_attached or [],
            'volumesInUse': volumes_in_use or [],

        }
        self._types = {
            'addresses': (list, NodeAddress),
            'allocatable': (dict, None),
            'capacity': (dict, None),
            'conditions': (list, NodeCondition),
            'config': (NodeConfigStatus, None),
            'daemonEndpoints': (NodeDaemonEndpoints, None),
            'images': (list, ContainerImage),
            'nodeInfo': (NodeSystemInfo, None),
            'phase': (str, None),
            'volumesAttached': (list, AttachedVolume),
            'volumesInUse': (list, str),

        }

    @property
    def addresses(self) -> typing.List['NodeAddress']:
        """
        List of addresses reachable to the node. Queried from cloud
        provider, if available. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#addresses
        """
        return self._properties.get('addresses')

    @addresses.setter
    def addresses(
            self,
            value: typing.Union[typing.List['NodeAddress'], typing.List[dict]]
    ):
        """
        List of addresses reachable to the node. Queried from cloud
        provider, if available. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#addresses
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NodeAddress().from_dict(item)
            cleaned.append(item)
        self._properties['addresses'] = cleaned

    @property
    def allocatable(self) -> dict:
        """
        Allocatable represents the resources of a node that are
        available for scheduling. Defaults to Capacity.
        """
        return self._properties.get('allocatable')

    @allocatable.setter
    def allocatable(self, value: dict):
        """
        Allocatable represents the resources of a node that are
        available for scheduling. Defaults to Capacity.
        """
        self._properties['allocatable'] = value

    @property
    def capacity(self) -> dict:
        """
        Capacity represents the total resources of a node. More
        info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#capacity
        """
        return self._properties.get('capacity')

    @capacity.setter
    def capacity(self, value: dict):
        """
        Capacity represents the total resources of a node. More
        info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#capacity
        """
        self._properties['capacity'] = value

    @property
    def conditions(self) -> typing.List['NodeCondition']:
        """
        Conditions is an array of current observed node conditions.
        More info:
        https://kubernetes.io/docs/concepts/nodes/node/#condition
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['NodeCondition'], typing.List[dict]]
    ):
        """
        Conditions is an array of current observed node conditions.
        More info:
        https://kubernetes.io/docs/concepts/nodes/node/#condition
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NodeCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def config(self) -> 'NodeConfigStatus':
        """
        Status of the config assigned to the node via the dynamic
        Kubelet config feature.
        """
        return self._properties.get('config')

    @config.setter
    def config(self, value: typing.Union['NodeConfigStatus', dict]):
        """
        Status of the config assigned to the node via the dynamic
        Kubelet config feature.
        """
        if isinstance(value, dict):
            value = NodeConfigStatus().from_dict(value)
        self._properties['config'] = value

    @property
    def daemon_endpoints(self) -> 'NodeDaemonEndpoints':
        """
        Endpoints of daemons running on the Node.
        """
        return self._properties.get('daemonEndpoints')

    @daemon_endpoints.setter
    def daemon_endpoints(self, value: typing.Union['NodeDaemonEndpoints', dict]):
        """
        Endpoints of daemons running on the Node.
        """
        if isinstance(value, dict):
            value = NodeDaemonEndpoints().from_dict(value)
        self._properties['daemonEndpoints'] = value

    @property
    def images(self) -> typing.List['ContainerImage']:
        """
        List of container images on this node
        """
        return self._properties.get('images')

    @images.setter
    def images(
            self,
            value: typing.Union[typing.List['ContainerImage'], typing.List[dict]]
    ):
        """
        List of container images on this node
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ContainerImage().from_dict(item)
            cleaned.append(item)
        self._properties['images'] = cleaned

    @property
    def node_info(self) -> 'NodeSystemInfo':
        """
        Set of ids/uuids to uniquely identify the node. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#info
        """
        return self._properties.get('nodeInfo')

    @node_info.setter
    def node_info(self, value: typing.Union['NodeSystemInfo', dict]):
        """
        Set of ids/uuids to uniquely identify the node. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#info
        """
        if isinstance(value, dict):
            value = NodeSystemInfo().from_dict(value)
        self._properties['nodeInfo'] = value

    @property
    def phase(self) -> str:
        """
        NodePhase is the recently observed lifecycle phase of the
        node. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#phase The
        field is never populated, and now is deprecated.
        """
        return self._properties.get('phase')

    @phase.setter
    def phase(self, value: str):
        """
        NodePhase is the recently observed lifecycle phase of the
        node. More info:
        https://kubernetes.io/docs/concepts/nodes/node/#phase The
        field is never populated, and now is deprecated.
        """
        self._properties['phase'] = value

    @property
    def volumes_attached(self) -> typing.List['AttachedVolume']:
        """
        List of volumes that are attached to the node.
        """
        return self._properties.get('volumesAttached')

    @volumes_attached.setter
    def volumes_attached(
            self,
            value: typing.Union[typing.List['AttachedVolume'], typing.List[dict]]
    ):
        """
        List of volumes that are attached to the node.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = AttachedVolume().from_dict(item)
            cleaned.append(item)
        self._properties['volumesAttached'] = cleaned

    @property
    def volumes_in_use(self) -> typing.List[str]:
        """
        List of attachable volumes in use (mounted) by the node.
        """
        return self._properties.get('volumesInUse')

    @volumes_in_use.setter
    def volumes_in_use(self, value: typing.List[str]):
        """
        List of attachable volumes in use (mounted) by the node.
        """
        self._properties['volumesInUse'] = value

    def __enter__(self) -> 'NodeStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NodeSystemInfo(_kuber_definitions.Definition):
    """
    NodeSystemInfo is a set of ids/uuids to uniquely identify
    the node.
    """

    def __init__(
            self,
            architecture: str = None,
            boot_id: str = None,
            container_runtime_version: str = None,
            kernel_version: str = None,
            kube_proxy_version: str = None,
            kubelet_version: str = None,
            machine_id: str = None,
            operating_system: str = None,
            os_image: str = None,
            system_uuid: str = None,
    ):
        """Create NodeSystemInfo instance."""
        super(NodeSystemInfo, self).__init__(
            api_version='core/v1',
            kind='NodeSystemInfo'
        )
        self._properties = {
            'architecture': architecture or '',
            'bootID': boot_id or '',
            'containerRuntimeVersion': container_runtime_version or '',
            'kernelVersion': kernel_version or '',
            'kubeProxyVersion': kube_proxy_version or '',
            'kubeletVersion': kubelet_version or '',
            'machineID': machine_id or '',
            'operatingSystem': operating_system or '',
            'osImage': os_image or '',
            'systemUUID': system_uuid or '',

        }
        self._types = {
            'architecture': (str, None),
            'bootID': (str, None),
            'containerRuntimeVersion': (str, None),
            'kernelVersion': (str, None),
            'kubeProxyVersion': (str, None),
            'kubeletVersion': (str, None),
            'machineID': (str, None),
            'operatingSystem': (str, None),
            'osImage': (str, None),
            'systemUUID': (str, None),

        }

    @property
    def architecture(self) -> str:
        """
        The Architecture reported by the node
        """
        return self._properties.get('architecture')

    @architecture.setter
    def architecture(self, value: str):
        """
        The Architecture reported by the node
        """
        self._properties['architecture'] = value

    @property
    def boot_id(self) -> str:
        """
        Boot ID reported by the node.
        """
        return self._properties.get('bootID')

    @boot_id.setter
    def boot_id(self, value: str):
        """
        Boot ID reported by the node.
        """
        self._properties['bootID'] = value

    @property
    def container_runtime_version(self) -> str:
        """
        ContainerRuntime Version reported by the node through
        runtime remote API (e.g. docker://1.5.0).
        """
        return self._properties.get('containerRuntimeVersion')

    @container_runtime_version.setter
    def container_runtime_version(self, value: str):
        """
        ContainerRuntime Version reported by the node through
        runtime remote API (e.g. docker://1.5.0).
        """
        self._properties['containerRuntimeVersion'] = value

    @property
    def kernel_version(self) -> str:
        """
        Kernel Version reported by the node from 'uname -r' (e.g.
        3.16.0-0.bpo.4-amd64).
        """
        return self._properties.get('kernelVersion')

    @kernel_version.setter
    def kernel_version(self, value: str):
        """
        Kernel Version reported by the node from 'uname -r' (e.g.
        3.16.0-0.bpo.4-amd64).
        """
        self._properties['kernelVersion'] = value

    @property
    def kube_proxy_version(self) -> str:
        """
        KubeProxy Version reported by the node.
        """
        return self._properties.get('kubeProxyVersion')

    @kube_proxy_version.setter
    def kube_proxy_version(self, value: str):
        """
        KubeProxy Version reported by the node.
        """
        self._properties['kubeProxyVersion'] = value

    @property
    def kubelet_version(self) -> str:
        """
        Kubelet Version reported by the node.
        """
        return self._properties.get('kubeletVersion')

    @kubelet_version.setter
    def kubelet_version(self, value: str):
        """
        Kubelet Version reported by the node.
        """
        self._properties['kubeletVersion'] = value

    @property
    def machine_id(self) -> str:
        """
        MachineID reported by the node. For unique machine
        identification in the cluster this field is preferred. Learn
        more from man(5) machine-id: http://man7.org/linux/man-
        pages/man5/machine-id.5.html
        """
        return self._properties.get('machineID')

    @machine_id.setter
    def machine_id(self, value: str):
        """
        MachineID reported by the node. For unique machine
        identification in the cluster this field is preferred. Learn
        more from man(5) machine-id: http://man7.org/linux/man-
        pages/man5/machine-id.5.html
        """
        self._properties['machineID'] = value

    @property
    def operating_system(self) -> str:
        """
        The Operating System reported by the node
        """
        return self._properties.get('operatingSystem')

    @operating_system.setter
    def operating_system(self, value: str):
        """
        The Operating System reported by the node
        """
        self._properties['operatingSystem'] = value

    @property
    def os_image(self) -> str:
        """
        OS Image reported by the node from /etc/os-release (e.g.
        Debian GNU/Linux 7 (wheezy)).
        """
        return self._properties.get('osImage')

    @os_image.setter
    def os_image(self, value: str):
        """
        OS Image reported by the node from /etc/os-release (e.g.
        Debian GNU/Linux 7 (wheezy)).
        """
        self._properties['osImage'] = value

    @property
    def system_uuid(self) -> str:
        """
        SystemUUID reported by the node. For unique machine
        identification MachineID is preferred. This field is
        specific to Red Hat hosts
        https://access.redhat.com/documentation/en-
        US/Red_Hat_Subscription_Management/1/html/RHSM/getting-
        system-uuid.html
        """
        return self._properties.get('systemUUID')

    @system_uuid.setter
    def system_uuid(self, value: str):
        """
        SystemUUID reported by the node. For unique machine
        identification MachineID is preferred. This field is
        specific to Red Hat hosts
        https://access.redhat.com/documentation/en-
        US/Red_Hat_Subscription_Management/1/html/RHSM/getting-
        system-uuid.html
        """
        self._properties['systemUUID'] = value

    def __enter__(self) -> 'NodeSystemInfo':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ObjectFieldSelector(_kuber_definitions.Definition):
    """
    ObjectFieldSelector selects an APIVersioned field of an
    object.
    """

    def __init__(
            self,
            api_version: str = None,
            field_path: str = None,
    ):
        """Create ObjectFieldSelector instance."""
        super(ObjectFieldSelector, self).__init__(
            api_version='core/v1',
            kind='ObjectFieldSelector'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'fieldPath': field_path or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'fieldPath': (str, None),

        }

    @property
    def api_version(self) -> str:
        """
        Version of the schema the FieldPath is written in terms of,
        defaults to "v1".
        """
        return self._properties.get('apiVersion')

    @api_version.setter
    def api_version(self, value: str):
        """
        Version of the schema the FieldPath is written in terms of,
        defaults to "v1".
        """
        self._properties['apiVersion'] = value

    @property
    def field_path(self) -> str:
        """
        Path of the field to select in the specified API version.
        """
        return self._properties.get('fieldPath')

    @field_path.setter
    def field_path(self, value: str):
        """
        Path of the field to select in the specified API version.
        """
        self._properties['fieldPath'] = value

    def __enter__(self) -> 'ObjectFieldSelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ObjectReference(_kuber_definitions.Definition):
    """
    ObjectReference contains enough information to let you
    inspect or modify the referred object.
    """

    def __init__(
            self,
            api_version: str = None,
            field_path: str = None,
            kind: str = None,
            name: str = None,
            namespace: str = None,
            resource_version: str = None,
            uid: str = None,
    ):
        """Create ObjectReference instance."""
        super(ObjectReference, self).__init__(
            api_version='core/v1',
            kind='ObjectReference'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'fieldPath': field_path or '',
            'kind': kind or '',
            'name': name or '',
            'namespace': namespace or '',
            'resourceVersion': resource_version or '',
            'uid': uid or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'fieldPath': (str, None),
            'kind': (str, None),
            'name': (str, None),
            'namespace': (str, None),
            'resourceVersion': (str, None),
            'uid': (str, None),

        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent.
        """
        return self._properties.get('apiVersion')

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent.
        """
        self._properties['apiVersion'] = value

    @property
    def field_path(self) -> str:
        """
        If referring to a piece of an object instead of an entire
        object, this string should contain a valid JSON/Go field
        access statement, such as
        desiredState.manifest.containers[2]. For example, if the
        object reference is to a container within a pod, this would
        take on a value like: "spec.containers{name}" (where "name"
        refers to the name of the container that triggered the
        event) or if no container name is specified
        "spec.containers[2]" (container with index 2 in this pod).
        This syntax is chosen only to have some well-defined way of
        referencing a part of an object.
        """
        return self._properties.get('fieldPath')

    @field_path.setter
    def field_path(self, value: str):
        """
        If referring to a piece of an object instead of an entire
        object, this string should contain a valid JSON/Go field
        access statement, such as
        desiredState.manifest.containers[2]. For example, if the
        object reference is to a container within a pod, this would
        take on a value like: "spec.containers{name}" (where "name"
        refers to the name of the container that triggered the
        event) or if no container name is specified
        "spec.containers[2]" (container with index 2 in this pod).
        This syntax is chosen only to have some well-defined way of
        referencing a part of an object.
        """
        self._properties['fieldPath'] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        Namespace of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/namespaces/
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/namespaces/
        """
        self._properties['namespace'] = value

    @property
    def resource_version(self) -> str:
        """
        Specific resourceVersion to which this reference is made, if
        any. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        return self._properties.get('resourceVersion')

    @resource_version.setter
    def resource_version(self, value: str):
        """
        Specific resourceVersion to which this reference is made, if
        any. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        self._properties['resourceVersion'] = value

    @property
    def uid(self) -> str:
        """
        UID of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#uids
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        UID of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#uids
        """
        self._properties['uid'] = value

    def __enter__(self) -> 'ObjectReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolume(_kuber_definitions.Resource):
    """
    PersistentVolume (PV) is a storage resource provisioned by
    an administrator. It is analogous to a node. More info:
    https://kubernetes.io/docs/concepts/storage/persistent-
    volumes
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PersistentVolumeSpec' = None,
            status: 'PersistentVolumeStatus' = None,
    ):
        """Create PersistentVolume instance."""
        super(PersistentVolume, self).__init__(
            api_version='core/v1',
            kind='PersistentVolume'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PersistentVolumeSpec(),
            'status': status or PersistentVolumeStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PersistentVolumeSpec, None),
            'status': (PersistentVolumeStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PersistentVolumeSpec':
        """
        Spec defines a specification of a persistent volume owned by
        the cluster. Provisioned by an administrator. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistent-volumes
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PersistentVolumeSpec', dict]):
        """
        Spec defines a specification of a persistent volume owned by
        the cluster. Provisioned by an administrator. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistent-volumes
        """
        if isinstance(value, dict):
            value = PersistentVolumeSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'PersistentVolumeStatus':
        """
        Status represents the current information/status for the
        persistent volume. Populated by the system. Read-only. More
        info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistent-volumes
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['PersistentVolumeStatus', dict]):
        """
        Status represents the current information/status for the
        persistent volume. Populated by the system. Read-only. More
        info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistent-volumes
        """
        if isinstance(value, dict):
            value = PersistentVolumeStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeStatus':
        """
        Creates the PersistentVolume in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_persistent_volume',
            'create_persistent_volume'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            PersistentVolumeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeStatus':
        """
        Replaces the PersistentVolume in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_persistent_volume',
            'replace_persistent_volume'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PersistentVolumeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeStatus':
        """
        Patches the PersistentVolume in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_persistent_volume',
            'patch_persistent_volume'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PersistentVolumeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_persistent_volume',
            'read_persistent_volume'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            PersistentVolumeStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the PersistentVolume from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_persistent_volume',
            'read_persistent_volume'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the PersistentVolume from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_persistent_volume',
            'delete_persistent_volume'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PersistentVolume':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaim(_kuber_definitions.Resource):
    """
    PersistentVolumeClaim is a user's request for and claim to a
    persistent volume
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PersistentVolumeClaimSpec' = None,
            status: 'PersistentVolumeClaimStatus' = None,
    ):
        """Create PersistentVolumeClaim instance."""
        super(PersistentVolumeClaim, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaim'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PersistentVolumeClaimSpec(),
            'status': status or PersistentVolumeClaimStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PersistentVolumeClaimSpec, None),
            'status': (PersistentVolumeClaimStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PersistentVolumeClaimSpec':
        """
        Spec defines the desired characteristics of a volume
        requested by a pod author. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PersistentVolumeClaimSpec', dict]):
        """
        Spec defines the desired characteristics of a volume
        requested by a pod author. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        if isinstance(value, dict):
            value = PersistentVolumeClaimSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'PersistentVolumeClaimStatus':
        """
        Status represents the current information/status of a
        persistent volume claim. Read-only. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['PersistentVolumeClaimStatus', dict]):
        """
        Status represents the current information/status of a
        persistent volume claim. Read-only. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        if isinstance(value, dict):
            value = PersistentVolumeClaimStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeClaimStatus':
        """
        Creates the PersistentVolumeClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_persistent_volume_claim',
            'create_persistent_volume_claim'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            PersistentVolumeClaimStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeClaimStatus':
        """
        Replaces the PersistentVolumeClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_persistent_volume_claim',
            'replace_persistent_volume_claim'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PersistentVolumeClaimStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeClaimStatus':
        """
        Patches the PersistentVolumeClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_persistent_volume_claim',
            'patch_persistent_volume_claim'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PersistentVolumeClaimStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'PersistentVolumeClaimStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_persistent_volume_claim',
            'read_persistent_volume_claim'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            PersistentVolumeClaimStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the PersistentVolumeClaim from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_persistent_volume_claim',
            'read_persistent_volume_claim'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the PersistentVolumeClaim from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_persistent_volume_claim',
            'delete_persistent_volume_claim'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PersistentVolumeClaim':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaimCondition(_kuber_definitions.Definition):
    """
    PersistentVolumeClaimCondition contails details about state
    of pvc
    """

    def __init__(
            self,
            last_probe_time: str = None,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create PersistentVolumeClaimCondition instance."""
        super(PersistentVolumeClaimCondition, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaimCondition'
        )
        self._properties = {
            'lastProbeTime': last_probe_time or None,
            'lastTransitionTime': last_transition_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastProbeTime': (str, None),
            'lastTransitionTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_probe_time(self) -> str:
        """
        Last time we probed the condition.
        """
        return self._properties.get('lastProbeTime')

    @last_probe_time.setter
    def last_probe_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time we probed the condition.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastProbeTime'] = value

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        Human-readable message indicating details about last
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Human-readable message indicating details about last
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        Unique, this should be a short, machine understandable
        string that gives the reason for condition's last
        transition. If it reports "ResizeStarted" that means the
        underlying persistent volume is being resized.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        Unique, this should be a short, machine understandable
        string that gives the reason for condition's last
        transition. If it reports "ResizeStarted" that means the
        underlying persistent volume is being resized.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """

        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """

        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """

        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """

        """
        self._properties['type'] = value

    def __enter__(self) -> 'PersistentVolumeClaimCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaimList(_kuber_definitions.Collection):
    """
    PersistentVolumeClaimList is a list of PersistentVolumeClaim
    items.
    """

    def __init__(
            self,
            items: typing.List['PersistentVolumeClaim'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PersistentVolumeClaimList instance."""
        super(PersistentVolumeClaimList, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaimList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PersistentVolumeClaim),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PersistentVolumeClaim']:
        """
        A list of persistent volume claims. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PersistentVolumeClaim'], typing.List[dict]]
    ):
        """
        A list of persistent volume claims. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PersistentVolumeClaim().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PersistentVolumeClaimList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaimSpec(_kuber_definitions.Definition):
    """
    PersistentVolumeClaimSpec describes the common attributes of
    storage devices and allows a Source for provider-specific
    attributes
    """

    def __init__(
            self,
            access_modes: typing.List[str] = None,
            data_source: 'TypedLocalObjectReference' = None,
            resources: 'ResourceRequirements' = None,
            selector: 'LabelSelector' = None,
            storage_class_name: str = None,
            volume_mode: str = None,
            volume_name: str = None,
    ):
        """Create PersistentVolumeClaimSpec instance."""
        super(PersistentVolumeClaimSpec, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaimSpec'
        )
        self._properties = {
            'accessModes': access_modes or [],
            'dataSource': data_source or TypedLocalObjectReference(),
            'resources': resources or ResourceRequirements(),
            'selector': selector or LabelSelector(),
            'storageClassName': storage_class_name or '',
            'volumeMode': volume_mode or '',
            'volumeName': volume_name or '',

        }
        self._types = {
            'accessModes': (list, str),
            'dataSource': (TypedLocalObjectReference, None),
            'resources': (ResourceRequirements, None),
            'selector': (LabelSelector, None),
            'storageClassName': (str, None),
            'volumeMode': (str, None),
            'volumeName': (str, None),

        }

    @property
    def access_modes(self) -> typing.List[str]:
        """
        AccessModes contains the desired access modes the volume
        should have. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes-1
        """
        return self._properties.get('accessModes')

    @access_modes.setter
    def access_modes(self, value: typing.List[str]):
        """
        AccessModes contains the desired access modes the volume
        should have. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes-1
        """
        self._properties['accessModes'] = value

    @property
    def data_source(self) -> 'TypedLocalObjectReference':
        """
        This field requires the VolumeSnapshotDataSource alpha
        feature gate to be enabled and currently VolumeSnapshot is
        the only supported data source. If the provisioner can
        support VolumeSnapshot data source, it will create a new
        volume and data will be restored to the volume at the same
        time. If the provisioner does not support VolumeSnapshot
        data source, volume will not be created and the failure will
        be reported as an event. In the future, we plan to support
        more data source types and the behavior of the provisioner
        may change.
        """
        return self._properties.get('dataSource')

    @data_source.setter
    def data_source(self, value: typing.Union['TypedLocalObjectReference', dict]):
        """
        This field requires the VolumeSnapshotDataSource alpha
        feature gate to be enabled and currently VolumeSnapshot is
        the only supported data source. If the provisioner can
        support VolumeSnapshot data source, it will create a new
        volume and data will be restored to the volume at the same
        time. If the provisioner does not support VolumeSnapshot
        data source, volume will not be created and the failure will
        be reported as an event. In the future, we plan to support
        more data source types and the behavior of the provisioner
        may change.
        """
        if isinstance(value, dict):
            value = TypedLocalObjectReference().from_dict(value)
        self._properties['dataSource'] = value

    @property
    def resources(self) -> 'ResourceRequirements':
        """
        Resources represents the minimum resources the volume should
        have. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#resources
        """
        return self._properties.get('resources')

    @resources.setter
    def resources(self, value: typing.Union['ResourceRequirements', dict]):
        """
        Resources represents the minimum resources the volume should
        have. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#resources
        """
        if isinstance(value, dict):
            value = ResourceRequirements().from_dict(value)
        self._properties['resources'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        A label query over volumes to consider for binding.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        A label query over volumes to consider for binding.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def storage_class_name(self) -> str:
        """
        Name of the StorageClass required by the claim. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#class-1
        """
        return self._properties.get('storageClassName')

    @storage_class_name.setter
    def storage_class_name(self, value: str):
        """
        Name of the StorageClass required by the claim. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#class-1
        """
        self._properties['storageClassName'] = value

    @property
    def volume_mode(self) -> str:
        """
        volumeMode defines what type of volume is required by the
        claim. Value of Filesystem is implied when not included in
        claim spec. This is a beta feature.
        """
        return self._properties.get('volumeMode')

    @volume_mode.setter
    def volume_mode(self, value: str):
        """
        volumeMode defines what type of volume is required by the
        claim. Value of Filesystem is implied when not included in
        claim spec. This is a beta feature.
        """
        self._properties['volumeMode'] = value

    @property
    def volume_name(self) -> str:
        """
        VolumeName is the binding reference to the PersistentVolume
        backing this claim.
        """
        return self._properties.get('volumeName')

    @volume_name.setter
    def volume_name(self, value: str):
        """
        VolumeName is the binding reference to the PersistentVolume
        backing this claim.
        """
        self._properties['volumeName'] = value

    def __enter__(self) -> 'PersistentVolumeClaimSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaimStatus(_kuber_definitions.Definition):
    """
    PersistentVolumeClaimStatus is the current status of a
    persistent volume claim.
    """

    def __init__(
            self,
            access_modes: typing.List[str] = None,
            capacity: dict = None,
            conditions: typing.List['PersistentVolumeClaimCondition'] = None,
            phase: str = None,
    ):
        """Create PersistentVolumeClaimStatus instance."""
        super(PersistentVolumeClaimStatus, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaimStatus'
        )
        self._properties = {
            'accessModes': access_modes or [],
            'capacity': capacity or {},
            'conditions': conditions or [],
            'phase': phase or '',

        }
        self._types = {
            'accessModes': (list, str),
            'capacity': (dict, None),
            'conditions': (list, PersistentVolumeClaimCondition),
            'phase': (str, None),

        }

    @property
    def access_modes(self) -> typing.List[str]:
        """
        AccessModes contains the actual access modes the volume
        backing the PVC has. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes-1
        """
        return self._properties.get('accessModes')

    @access_modes.setter
    def access_modes(self, value: typing.List[str]):
        """
        AccessModes contains the actual access modes the volume
        backing the PVC has. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes-1
        """
        self._properties['accessModes'] = value

    @property
    def capacity(self) -> dict:
        """
        Represents the actual resources of the underlying volume.
        """
        return self._properties.get('capacity')

    @capacity.setter
    def capacity(self, value: dict):
        """
        Represents the actual resources of the underlying volume.
        """
        self._properties['capacity'] = value

    @property
    def conditions(self) -> typing.List['PersistentVolumeClaimCondition']:
        """
        Current Condition of persistent volume claim. If underlying
        persistent volume is being resized then the Condition will
        be set to 'ResizeStarted'.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['PersistentVolumeClaimCondition'], typing.List[dict]]
    ):
        """
        Current Condition of persistent volume claim. If underlying
        persistent volume is being resized then the Condition will
        be set to 'ResizeStarted'.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PersistentVolumeClaimCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def phase(self) -> str:
        """
        Phase represents the current phase of PersistentVolumeClaim.
        """
        return self._properties.get('phase')

    @phase.setter
    def phase(self, value: str):
        """
        Phase represents the current phase of PersistentVolumeClaim.
        """
        self._properties['phase'] = value

    def __enter__(self) -> 'PersistentVolumeClaimStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeClaimVolumeSource(_kuber_definitions.Definition):
    """
    PersistentVolumeClaimVolumeSource references the user's PVC
    in the same namespace. This volume finds the bound PV and
    mounts that volume for the pod. A
    PersistentVolumeClaimVolumeSource is, essentially, a wrapper
    around another type of volume that is owned by someone else
    (the system).
    """

    def __init__(
            self,
            claim_name: str = None,
            read_only: bool = None,
    ):
        """Create PersistentVolumeClaimVolumeSource instance."""
        super(PersistentVolumeClaimVolumeSource, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeClaimVolumeSource'
        )
        self._properties = {
            'claimName': claim_name or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'claimName': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def claim_name(self) -> str:
        """
        ClaimName is the name of a PersistentVolumeClaim in the same
        namespace as the pod using this volume. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        return self._properties.get('claimName')

    @claim_name.setter
    def claim_name(self, value: str):
        """
        ClaimName is the name of a PersistentVolumeClaim in the same
        namespace as the pod using this volume. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        self._properties['claimName'] = value

    @property
    def read_only(self) -> bool:
        """
        Will force the ReadOnly setting in VolumeMounts. Default
        false.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Will force the ReadOnly setting in VolumeMounts. Default
        false.
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'PersistentVolumeClaimVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeList(_kuber_definitions.Collection):
    """
    PersistentVolumeList is a list of PersistentVolume items.
    """

    def __init__(
            self,
            items: typing.List['PersistentVolume'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PersistentVolumeList instance."""
        super(PersistentVolumeList, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PersistentVolume),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PersistentVolume']:
        """
        List of persistent volumes. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PersistentVolume'], typing.List[dict]]
    ):
        """
        List of persistent volumes. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PersistentVolume().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PersistentVolumeList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeSpec(_kuber_definitions.Definition):
    """
    PersistentVolumeSpec is the specification of a persistent
    volume.
    """

    def __init__(
            self,
            access_modes: typing.List[str] = None,
            aws_elastic_block_store: 'AWSElasticBlockStoreVolumeSource' = None,
            azure_disk: 'AzureDiskVolumeSource' = None,
            azure_file: 'AzureFilePersistentVolumeSource' = None,
            capacity: dict = None,
            cephfs: 'CephFSPersistentVolumeSource' = None,
            cinder: 'CinderPersistentVolumeSource' = None,
            claim_ref: 'ObjectReference' = None,
            csi: 'CSIPersistentVolumeSource' = None,
            fc: 'FCVolumeSource' = None,
            flex_volume: 'FlexPersistentVolumeSource' = None,
            flocker: 'FlockerVolumeSource' = None,
            gce_persistent_disk: 'GCEPersistentDiskVolumeSource' = None,
            glusterfs: 'GlusterfsPersistentVolumeSource' = None,
            host_path: 'HostPathVolumeSource' = None,
            iscsi: 'ISCSIPersistentVolumeSource' = None,
            local: 'LocalVolumeSource' = None,
            mount_options: typing.List[str] = None,
            nfs: 'NFSVolumeSource' = None,
            node_affinity: 'VolumeNodeAffinity' = None,
            persistent_volume_reclaim_policy: str = None,
            photon_persistent_disk: 'PhotonPersistentDiskVolumeSource' = None,
            portworx_volume: 'PortworxVolumeSource' = None,
            quobyte: 'QuobyteVolumeSource' = None,
            rbd: 'RBDPersistentVolumeSource' = None,
            scale_io: 'ScaleIOPersistentVolumeSource' = None,
            storage_class_name: str = None,
            storageos: 'StorageOSPersistentVolumeSource' = None,
            volume_mode: str = None,
            vsphere_volume: 'VsphereVirtualDiskVolumeSource' = None,
    ):
        """Create PersistentVolumeSpec instance."""
        super(PersistentVolumeSpec, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeSpec'
        )
        self._properties = {
            'accessModes': access_modes or [],
            'awsElasticBlockStore': aws_elastic_block_store or AWSElasticBlockStoreVolumeSource(),
            'azureDisk': azure_disk or AzureDiskVolumeSource(),
            'azureFile': azure_file or AzureFilePersistentVolumeSource(),
            'capacity': capacity or {},
            'cephfs': cephfs or CephFSPersistentVolumeSource(),
            'cinder': cinder or CinderPersistentVolumeSource(),
            'claimRef': claim_ref or ObjectReference(),
            'csi': csi or CSIPersistentVolumeSource(),
            'fc': fc or FCVolumeSource(),
            'flexVolume': flex_volume or FlexPersistentVolumeSource(),
            'flocker': flocker or FlockerVolumeSource(),
            'gcePersistentDisk': gce_persistent_disk or GCEPersistentDiskVolumeSource(),
            'glusterfs': glusterfs or GlusterfsPersistentVolumeSource(),
            'hostPath': host_path or HostPathVolumeSource(),
            'iscsi': iscsi or ISCSIPersistentVolumeSource(),
            'local': local or LocalVolumeSource(),
            'mountOptions': mount_options or [],
            'nfs': nfs or NFSVolumeSource(),
            'nodeAffinity': node_affinity or VolumeNodeAffinity(),
            'persistentVolumeReclaimPolicy': persistent_volume_reclaim_policy or '',
            'photonPersistentDisk': photon_persistent_disk or PhotonPersistentDiskVolumeSource(),
            'portworxVolume': portworx_volume or PortworxVolumeSource(),
            'quobyte': quobyte or QuobyteVolumeSource(),
            'rbd': rbd or RBDPersistentVolumeSource(),
            'scaleIO': scale_io or ScaleIOPersistentVolumeSource(),
            'storageClassName': storage_class_name or '',
            'storageos': storageos or StorageOSPersistentVolumeSource(),
            'volumeMode': volume_mode or '',
            'vsphereVolume': vsphere_volume or VsphereVirtualDiskVolumeSource(),

        }
        self._types = {
            'accessModes': (list, str),
            'awsElasticBlockStore': (AWSElasticBlockStoreVolumeSource, None),
            'azureDisk': (AzureDiskVolumeSource, None),
            'azureFile': (AzureFilePersistentVolumeSource, None),
            'capacity': (dict, None),
            'cephfs': (CephFSPersistentVolumeSource, None),
            'cinder': (CinderPersistentVolumeSource, None),
            'claimRef': (ObjectReference, None),
            'csi': (CSIPersistentVolumeSource, None),
            'fc': (FCVolumeSource, None),
            'flexVolume': (FlexPersistentVolumeSource, None),
            'flocker': (FlockerVolumeSource, None),
            'gcePersistentDisk': (GCEPersistentDiskVolumeSource, None),
            'glusterfs': (GlusterfsPersistentVolumeSource, None),
            'hostPath': (HostPathVolumeSource, None),
            'iscsi': (ISCSIPersistentVolumeSource, None),
            'local': (LocalVolumeSource, None),
            'mountOptions': (list, str),
            'nfs': (NFSVolumeSource, None),
            'nodeAffinity': (VolumeNodeAffinity, None),
            'persistentVolumeReclaimPolicy': (str, None),
            'photonPersistentDisk': (PhotonPersistentDiskVolumeSource, None),
            'portworxVolume': (PortworxVolumeSource, None),
            'quobyte': (QuobyteVolumeSource, None),
            'rbd': (RBDPersistentVolumeSource, None),
            'scaleIO': (ScaleIOPersistentVolumeSource, None),
            'storageClassName': (str, None),
            'storageos': (StorageOSPersistentVolumeSource, None),
            'volumeMode': (str, None),
            'vsphereVolume': (VsphereVirtualDiskVolumeSource, None),

        }

    @property
    def access_modes(self) -> typing.List[str]:
        """
        AccessModes contains all ways the volume can be mounted.
        More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes
        """
        return self._properties.get('accessModes')

    @access_modes.setter
    def access_modes(self, value: typing.List[str]):
        """
        AccessModes contains all ways the volume can be mounted.
        More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#access-modes
        """
        self._properties['accessModes'] = value

    @property
    def aws_elastic_block_store(self) -> 'AWSElasticBlockStoreVolumeSource':
        """
        AWSElasticBlockStore represents an AWS Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#awselasticblockstore
        """
        return self._properties.get('awsElasticBlockStore')

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, value: typing.Union['AWSElasticBlockStoreVolumeSource', dict]):
        """
        AWSElasticBlockStore represents an AWS Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#awselasticblockstore
        """
        if isinstance(value, dict):
            value = AWSElasticBlockStoreVolumeSource().from_dict(value)
        self._properties['awsElasticBlockStore'] = value

    @property
    def azure_disk(self) -> 'AzureDiskVolumeSource':
        """
        AzureDisk represents an Azure Data Disk mount on the host
        and bind mount to the pod.
        """
        return self._properties.get('azureDisk')

    @azure_disk.setter
    def azure_disk(self, value: typing.Union['AzureDiskVolumeSource', dict]):
        """
        AzureDisk represents an Azure Data Disk mount on the host
        and bind mount to the pod.
        """
        if isinstance(value, dict):
            value = AzureDiskVolumeSource().from_dict(value)
        self._properties['azureDisk'] = value

    @property
    def azure_file(self) -> 'AzureFilePersistentVolumeSource':
        """
        AzureFile represents an Azure File Service mount on the host
        and bind mount to the pod.
        """
        return self._properties.get('azureFile')

    @azure_file.setter
    def azure_file(self, value: typing.Union['AzureFilePersistentVolumeSource', dict]):
        """
        AzureFile represents an Azure File Service mount on the host
        and bind mount to the pod.
        """
        if isinstance(value, dict):
            value = AzureFilePersistentVolumeSource().from_dict(value)
        self._properties['azureFile'] = value

    @property
    def capacity(self) -> dict:
        """
        A description of the persistent volume's resources and
        capacity. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#capacity
        """
        return self._properties.get('capacity')

    @capacity.setter
    def capacity(self, value: dict):
        """
        A description of the persistent volume's resources and
        capacity. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#capacity
        """
        self._properties['capacity'] = value

    @property
    def cephfs(self) -> 'CephFSPersistentVolumeSource':
        """
        CephFS represents a Ceph FS mount on the host that shares a
        pod's lifetime
        """
        return self._properties.get('cephfs')

    @cephfs.setter
    def cephfs(self, value: typing.Union['CephFSPersistentVolumeSource', dict]):
        """
        CephFS represents a Ceph FS mount on the host that shares a
        pod's lifetime
        """
        if isinstance(value, dict):
            value = CephFSPersistentVolumeSource().from_dict(value)
        self._properties['cephfs'] = value

    @property
    def cinder(self) -> 'CinderPersistentVolumeSource':
        """
        Cinder represents a cinder volume attached and mounted on
        kubelets host machine More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('cinder')

    @cinder.setter
    def cinder(self, value: typing.Union['CinderPersistentVolumeSource', dict]):
        """
        Cinder represents a cinder volume attached and mounted on
        kubelets host machine More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        if isinstance(value, dict):
            value = CinderPersistentVolumeSource().from_dict(value)
        self._properties['cinder'] = value

    @property
    def claim_ref(self) -> 'ObjectReference':
        """
        ClaimRef is part of a bi-directional binding between
        PersistentVolume and PersistentVolumeClaim. Expected to be
        non-nil when bound. claim.VolumeName is the authoritative
        bind between PV and PVC. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#binding
        """
        return self._properties.get('claimRef')

    @claim_ref.setter
    def claim_ref(self, value: typing.Union['ObjectReference', dict]):
        """
        ClaimRef is part of a bi-directional binding between
        PersistentVolume and PersistentVolumeClaim. Expected to be
        non-nil when bound. claim.VolumeName is the authoritative
        bind between PV and PVC. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#binding
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['claimRef'] = value

    @property
    def csi(self) -> 'CSIPersistentVolumeSource':
        """
        CSI represents storage that is handled by an external CSI
        driver (Beta feature).
        """
        return self._properties.get('csi')

    @csi.setter
    def csi(self, value: typing.Union['CSIPersistentVolumeSource', dict]):
        """
        CSI represents storage that is handled by an external CSI
        driver (Beta feature).
        """
        if isinstance(value, dict):
            value = CSIPersistentVolumeSource().from_dict(value)
        self._properties['csi'] = value

    @property
    def fc(self) -> 'FCVolumeSource':
        """
        FC represents a Fibre Channel resource that is attached to a
        kubelet's host machine and then exposed to the pod.
        """
        return self._properties.get('fc')

    @fc.setter
    def fc(self, value: typing.Union['FCVolumeSource', dict]):
        """
        FC represents a Fibre Channel resource that is attached to a
        kubelet's host machine and then exposed to the pod.
        """
        if isinstance(value, dict):
            value = FCVolumeSource().from_dict(value)
        self._properties['fc'] = value

    @property
    def flex_volume(self) -> 'FlexPersistentVolumeSource':
        """
        FlexVolume represents a generic volume resource that is
        provisioned/attached using an exec based plugin.
        """
        return self._properties.get('flexVolume')

    @flex_volume.setter
    def flex_volume(self, value: typing.Union['FlexPersistentVolumeSource', dict]):
        """
        FlexVolume represents a generic volume resource that is
        provisioned/attached using an exec based plugin.
        """
        if isinstance(value, dict):
            value = FlexPersistentVolumeSource().from_dict(value)
        self._properties['flexVolume'] = value

    @property
    def flocker(self) -> 'FlockerVolumeSource':
        """
        Flocker represents a Flocker volume attached to a kubelet's
        host machine and exposed to the pod for its usage. This
        depends on the Flocker control service being running
        """
        return self._properties.get('flocker')

    @flocker.setter
    def flocker(self, value: typing.Union['FlockerVolumeSource', dict]):
        """
        Flocker represents a Flocker volume attached to a kubelet's
        host machine and exposed to the pod for its usage. This
        depends on the Flocker control service being running
        """
        if isinstance(value, dict):
            value = FlockerVolumeSource().from_dict(value)
        self._properties['flocker'] = value

    @property
    def gce_persistent_disk(self) -> 'GCEPersistentDiskVolumeSource':
        """
        GCEPersistentDisk represents a GCE Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. Provisioned by an admin. More info: https://kubernetes.
        io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        return self._properties.get('gcePersistentDisk')

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, value: typing.Union['GCEPersistentDiskVolumeSource', dict]):
        """
        GCEPersistentDisk represents a GCE Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. Provisioned by an admin. More info: https://kubernetes.
        io/docs/concepts/storage/volumes#gcepersistentdisk
        """
        if isinstance(value, dict):
            value = GCEPersistentDiskVolumeSource().from_dict(value)
        self._properties['gcePersistentDisk'] = value

    @property
    def glusterfs(self) -> 'GlusterfsPersistentVolumeSource':
        """
        Glusterfs represents a Glusterfs volume that is attached to
        a host and exposed to the pod. Provisioned by an admin. More
        info: https://releases.k8s.io/HEAD/examples/volumes/glusterf
        s/README.md
        """
        return self._properties.get('glusterfs')

    @glusterfs.setter
    def glusterfs(self, value: typing.Union['GlusterfsPersistentVolumeSource', dict]):
        """
        Glusterfs represents a Glusterfs volume that is attached to
        a host and exposed to the pod. Provisioned by an admin. More
        info: https://releases.k8s.io/HEAD/examples/volumes/glusterf
        s/README.md
        """
        if isinstance(value, dict):
            value = GlusterfsPersistentVolumeSource().from_dict(value)
        self._properties['glusterfs'] = value

    @property
    def host_path(self) -> 'HostPathVolumeSource':
        """
        HostPath represents a directory on the host. Provisioned by
        a developer or tester. This is useful for single-node
        development and testing only! On-host storage is not
        supported in any way and WILL NOT WORK in a multi-node
        cluster. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        return self._properties.get('hostPath')

    @host_path.setter
    def host_path(self, value: typing.Union['HostPathVolumeSource', dict]):
        """
        HostPath represents a directory on the host. Provisioned by
        a developer or tester. This is useful for single-node
        development and testing only! On-host storage is not
        supported in any way and WILL NOT WORK in a multi-node
        cluster. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        if isinstance(value, dict):
            value = HostPathVolumeSource().from_dict(value)
        self._properties['hostPath'] = value

    @property
    def iscsi(self) -> 'ISCSIPersistentVolumeSource':
        """
        ISCSI represents an ISCSI Disk resource that is attached to
        a kubelet's host machine and then exposed to the pod.
        Provisioned by an admin.
        """
        return self._properties.get('iscsi')

    @iscsi.setter
    def iscsi(self, value: typing.Union['ISCSIPersistentVolumeSource', dict]):
        """
        ISCSI represents an ISCSI Disk resource that is attached to
        a kubelet's host machine and then exposed to the pod.
        Provisioned by an admin.
        """
        if isinstance(value, dict):
            value = ISCSIPersistentVolumeSource().from_dict(value)
        self._properties['iscsi'] = value

    @property
    def local(self) -> 'LocalVolumeSource':
        """
        Local represents directly-attached storage with node
        affinity
        """
        return self._properties.get('local')

    @local.setter
    def local(self, value: typing.Union['LocalVolumeSource', dict]):
        """
        Local represents directly-attached storage with node
        affinity
        """
        if isinstance(value, dict):
            value = LocalVolumeSource().from_dict(value)
        self._properties['local'] = value

    @property
    def mount_options(self) -> typing.List[str]:
        """
        A list of mount options, e.g. ["ro", "soft"]. Not validated
        - mount will simply fail if one is invalid. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes/#mount-options
        """
        return self._properties.get('mountOptions')

    @mount_options.setter
    def mount_options(self, value: typing.List[str]):
        """
        A list of mount options, e.g. ["ro", "soft"]. Not validated
        - mount will simply fail if one is invalid. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes/#mount-options
        """
        self._properties['mountOptions'] = value

    @property
    def nfs(self) -> 'NFSVolumeSource':
        """
        NFS represents an NFS mount on the host. Provisioned by an
        admin. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        return self._properties.get('nfs')

    @nfs.setter
    def nfs(self, value: typing.Union['NFSVolumeSource', dict]):
        """
        NFS represents an NFS mount on the host. Provisioned by an
        admin. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        if isinstance(value, dict):
            value = NFSVolumeSource().from_dict(value)
        self._properties['nfs'] = value

    @property
    def node_affinity(self) -> 'VolumeNodeAffinity':
        """
        NodeAffinity defines constraints that limit what nodes this
        volume can be accessed from. This field influences the
        scheduling of pods that use this volume.
        """
        return self._properties.get('nodeAffinity')

    @node_affinity.setter
    def node_affinity(self, value: typing.Union['VolumeNodeAffinity', dict]):
        """
        NodeAffinity defines constraints that limit what nodes this
        volume can be accessed from. This field influences the
        scheduling of pods that use this volume.
        """
        if isinstance(value, dict):
            value = VolumeNodeAffinity().from_dict(value)
        self._properties['nodeAffinity'] = value

    @property
    def persistent_volume_reclaim_policy(self) -> str:
        """
        What happens to a persistent volume when released from its
        claim. Valid options are Retain (default for manually
        created PersistentVolumes), Delete (default for dynamically
        provisioned PersistentVolumes), and Recycle (deprecated).
        Recycle must be supported by the volume plugin underlying
        this PersistentVolume. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#reclaiming
        """
        return self._properties.get('persistentVolumeReclaimPolicy')

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, value: str):
        """
        What happens to a persistent volume when released from its
        claim. Valid options are Retain (default for manually
        created PersistentVolumes), Delete (default for dynamically
        provisioned PersistentVolumes), and Recycle (deprecated).
        Recycle must be supported by the volume plugin underlying
        this PersistentVolume. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#reclaiming
        """
        self._properties['persistentVolumeReclaimPolicy'] = value

    @property
    def photon_persistent_disk(self) -> 'PhotonPersistentDiskVolumeSource':
        """
        PhotonPersistentDisk represents a PhotonController
        persistent disk attached and mounted on kubelets host
        machine
        """
        return self._properties.get('photonPersistentDisk')

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, value: typing.Union['PhotonPersistentDiskVolumeSource', dict]):
        """
        PhotonPersistentDisk represents a PhotonController
        persistent disk attached and mounted on kubelets host
        machine
        """
        if isinstance(value, dict):
            value = PhotonPersistentDiskVolumeSource().from_dict(value)
        self._properties['photonPersistentDisk'] = value

    @property
    def portworx_volume(self) -> 'PortworxVolumeSource':
        """
        PortworxVolume represents a portworx volume attached and
        mounted on kubelets host machine
        """
        return self._properties.get('portworxVolume')

    @portworx_volume.setter
    def portworx_volume(self, value: typing.Union['PortworxVolumeSource', dict]):
        """
        PortworxVolume represents a portworx volume attached and
        mounted on kubelets host machine
        """
        if isinstance(value, dict):
            value = PortworxVolumeSource().from_dict(value)
        self._properties['portworxVolume'] = value

    @property
    def quobyte(self) -> 'QuobyteVolumeSource':
        """
        Quobyte represents a Quobyte mount on the host that shares a
        pod's lifetime
        """
        return self._properties.get('quobyte')

    @quobyte.setter
    def quobyte(self, value: typing.Union['QuobyteVolumeSource', dict]):
        """
        Quobyte represents a Quobyte mount on the host that shares a
        pod's lifetime
        """
        if isinstance(value, dict):
            value = QuobyteVolumeSource().from_dict(value)
        self._properties['quobyte'] = value

    @property
    def rbd(self) -> 'RBDPersistentVolumeSource':
        """
        RBD represents a Rados Block Device mount on the host that
        shares a pod's lifetime. More info:
        https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md
        """
        return self._properties.get('rbd')

    @rbd.setter
    def rbd(self, value: typing.Union['RBDPersistentVolumeSource', dict]):
        """
        RBD represents a Rados Block Device mount on the host that
        shares a pod's lifetime. More info:
        https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md
        """
        if isinstance(value, dict):
            value = RBDPersistentVolumeSource().from_dict(value)
        self._properties['rbd'] = value

    @property
    def scale_io(self) -> 'ScaleIOPersistentVolumeSource':
        """
        ScaleIO represents a ScaleIO persistent volume attached and
        mounted on Kubernetes nodes.
        """
        return self._properties.get('scaleIO')

    @scale_io.setter
    def scale_io(self, value: typing.Union['ScaleIOPersistentVolumeSource', dict]):
        """
        ScaleIO represents a ScaleIO persistent volume attached and
        mounted on Kubernetes nodes.
        """
        if isinstance(value, dict):
            value = ScaleIOPersistentVolumeSource().from_dict(value)
        self._properties['scaleIO'] = value

    @property
    def storage_class_name(self) -> str:
        """
        Name of StorageClass to which this persistent volume
        belongs. Empty value means that this volume does not belong
        to any StorageClass.
        """
        return self._properties.get('storageClassName')

    @storage_class_name.setter
    def storage_class_name(self, value: str):
        """
        Name of StorageClass to which this persistent volume
        belongs. Empty value means that this volume does not belong
        to any StorageClass.
        """
        self._properties['storageClassName'] = value

    @property
    def storageos(self) -> 'StorageOSPersistentVolumeSource':
        """
        StorageOS represents a StorageOS volume that is attached to
        the kubelet's host machine and mounted into the pod More
        info: https://releases.k8s.io/HEAD/examples/volumes/storageo
        s/README.md
        """
        return self._properties.get('storageos')

    @storageos.setter
    def storageos(self, value: typing.Union['StorageOSPersistentVolumeSource', dict]):
        """
        StorageOS represents a StorageOS volume that is attached to
        the kubelet's host machine and mounted into the pod More
        info: https://releases.k8s.io/HEAD/examples/volumes/storageo
        s/README.md
        """
        if isinstance(value, dict):
            value = StorageOSPersistentVolumeSource().from_dict(value)
        self._properties['storageos'] = value

    @property
    def volume_mode(self) -> str:
        """
        volumeMode defines if a volume is intended to be used with a
        formatted filesystem or to remain in raw block state. Value
        of Filesystem is implied when not included in spec. This is
        a beta feature.
        """
        return self._properties.get('volumeMode')

    @volume_mode.setter
    def volume_mode(self, value: str):
        """
        volumeMode defines if a volume is intended to be used with a
        formatted filesystem or to remain in raw block state. Value
        of Filesystem is implied when not included in spec. This is
        a beta feature.
        """
        self._properties['volumeMode'] = value

    @property
    def vsphere_volume(self) -> 'VsphereVirtualDiskVolumeSource':
        """
        VsphereVolume represents a vSphere volume attached and
        mounted on kubelets host machine
        """
        return self._properties.get('vsphereVolume')

    @vsphere_volume.setter
    def vsphere_volume(self, value: typing.Union['VsphereVirtualDiskVolumeSource', dict]):
        """
        VsphereVolume represents a vSphere volume attached and
        mounted on kubelets host machine
        """
        if isinstance(value, dict):
            value = VsphereVirtualDiskVolumeSource().from_dict(value)
        self._properties['vsphereVolume'] = value

    def __enter__(self) -> 'PersistentVolumeSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PersistentVolumeStatus(_kuber_definitions.Definition):
    """
    PersistentVolumeStatus is the current status of a persistent
    volume.
    """

    def __init__(
            self,
            message: str = None,
            phase: str = None,
            reason: str = None,
    ):
        """Create PersistentVolumeStatus instance."""
        super(PersistentVolumeStatus, self).__init__(
            api_version='core/v1',
            kind='PersistentVolumeStatus'
        )
        self._properties = {
            'message': message or '',
            'phase': phase or '',
            'reason': reason or '',

        }
        self._types = {
            'message': (str, None),
            'phase': (str, None),
            'reason': (str, None),

        }

    @property
    def message(self) -> str:
        """
        A human-readable message indicating details about why the
        volume is in this state.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human-readable message indicating details about why the
        volume is in this state.
        """
        self._properties['message'] = value

    @property
    def phase(self) -> str:
        """
        Phase indicates if a volume is available, bound to a claim,
        or released by a claim. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#phase
        """
        return self._properties.get('phase')

    @phase.setter
    def phase(self, value: str):
        """
        Phase indicates if a volume is available, bound to a claim,
        or released by a claim. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#phase
        """
        self._properties['phase'] = value

    @property
    def reason(self) -> str:
        """
        Reason is a brief CamelCase string that describes any
        failure and is meant for machine parsing and tidy display in
        the CLI.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        Reason is a brief CamelCase string that describes any
        failure and is meant for machine parsing and tidy display in
        the CLI.
        """
        self._properties['reason'] = value

    def __enter__(self) -> 'PersistentVolumeStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PhotonPersistentDiskVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Photon Controller persistent disk resource.
    """

    def __init__(
            self,
            fs_type: str = None,
            pd_id: str = None,
    ):
        """Create PhotonPersistentDiskVolumeSource instance."""
        super(PhotonPersistentDiskVolumeSource, self).__init__(
            api_version='core/v1',
            kind='PhotonPersistentDiskVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'pdID': pd_id or '',

        }
        self._types = {
            'fsType': (str, None),
            'pdID': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def pd_id(self) -> str:
        """
        ID that identifies Photon Controller persistent disk
        """
        return self._properties.get('pdID')

    @pd_id.setter
    def pd_id(self, value: str):
        """
        ID that identifies Photon Controller persistent disk
        """
        self._properties['pdID'] = value

    def __enter__(self) -> 'PhotonPersistentDiskVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Pod(_kuber_definitions.Resource):
    """
    Pod is a collection of containers that can run on a host.
    This resource is created by clients and scheduled onto
    hosts.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PodSpec' = None,
            status: 'PodStatus' = None,
    ):
        """Create Pod instance."""
        super(Pod, self).__init__(
            api_version='core/v1',
            kind='Pod'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PodSpec(),
            'status': status or PodStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PodSpec, None),
            'status': (PodStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PodSpec':
        """
        Specification of the desired behavior of the pod. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PodSpec', dict]):
        """
        Specification of the desired behavior of the pod. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = PodSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'PodStatus':
        """
        Most recently observed status of the pod. This data may not
        be up to date. Populated by the system. Read-only. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['PodStatus', dict]):
        """
        Most recently observed status of the pod. This data may not
        be up to date. Populated by the system. Read-only. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = PodStatus().from_dict(value)
        self._properties['status'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'Pod':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.containers if c.name == name), None)

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodStatus':
        """
        Creates the Pod in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_pod',
            'create_pod'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            PodStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodStatus':
        """
        Replaces the Pod in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_pod',
            'replace_pod'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PodStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodStatus':
        """
        Patches the Pod in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_pod',
            'patch_pod'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            PodStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'PodStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_pod',
            'read_pod'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            PodStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Pod from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_pod',
            'read_pod'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Pod from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_pod',
            'delete_pod'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Pod':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodAffinity(_kuber_definitions.Definition):
    """
    Pod affinity is a group of inter pod affinity scheduling
    rules.
    """

    def __init__(
            self,
            preferred_during_scheduling_ignored_during_execution: typing.List['WeightedPodAffinityTerm'] = None,
            required_during_scheduling_ignored_during_execution: typing.List['PodAffinityTerm'] = None,
    ):
        """Create PodAffinity instance."""
        super(PodAffinity, self).__init__(
            api_version='core/v1',
            kind='PodAffinity'
        )
        self._properties = {
            'preferredDuringSchedulingIgnoredDuringExecution': preferred_during_scheduling_ignored_during_execution or [],
            'requiredDuringSchedulingIgnoredDuringExecution': required_during_scheduling_ignored_during_execution or [],

        }
        self._types = {
            'preferredDuringSchedulingIgnoredDuringExecution': (list, WeightedPodAffinityTerm),
            'requiredDuringSchedulingIgnoredDuringExecution': (list, PodAffinityTerm),

        }

    @property
    def preferred_during_scheduling_ignored_during_execution(self) -> typing.List['WeightedPodAffinityTerm']:
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the affinity expressions specified by this field,
        but it may choose a node that violates one or more of the
        expressions. The node that is most preferred is the one with
        the greatest sum of weights, i.e. for each node that meets
        all of the scheduling requirements (resource request,
        requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node has pods
        which matches the corresponding podAffinityTerm; the node(s)
        with the highest sum are the most preferred.
        """
        return self._properties.get('preferredDuringSchedulingIgnoredDuringExecution')

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(
            self,
            value: typing.Union[typing.List['WeightedPodAffinityTerm'], typing.List[dict]]
    ):
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the affinity expressions specified by this field,
        but it may choose a node that violates one or more of the
        expressions. The node that is most preferred is the one with
        the greatest sum of weights, i.e. for each node that meets
        all of the scheduling requirements (resource request,
        requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node has pods
        which matches the corresponding podAffinityTerm; the node(s)
        with the highest sum are the most preferred.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = WeightedPodAffinityTerm().from_dict(item)
            cleaned.append(item)
        self._properties['preferredDuringSchedulingIgnoredDuringExecution'] = cleaned

    @property
    def required_during_scheduling_ignored_during_execution(self) -> typing.List['PodAffinityTerm']:
        """
        If the affinity requirements specified by this field are not
        met at scheduling time, the pod will not be scheduled onto
        the node. If the affinity requirements specified by this
        field cease to be met at some point during pod execution
        (e.g. due to a pod label update), the system may or may not
        try to eventually evict the pod from its node. When there
        are multiple elements, the lists of nodes corresponding to
        each podAffinityTerm are intersected, i.e. all terms must be
        satisfied.
        """
        return self._properties.get('requiredDuringSchedulingIgnoredDuringExecution')

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(
            self,
            value: typing.Union[typing.List['PodAffinityTerm'], typing.List[dict]]
    ):
        """
        If the affinity requirements specified by this field are not
        met at scheduling time, the pod will not be scheduled onto
        the node. If the affinity requirements specified by this
        field cease to be met at some point during pod execution
        (e.g. due to a pod label update), the system may or may not
        try to eventually evict the pod from its node. When there
        are multiple elements, the lists of nodes corresponding to
        each podAffinityTerm are intersected, i.e. all terms must be
        satisfied.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodAffinityTerm().from_dict(item)
            cleaned.append(item)
        self._properties['requiredDuringSchedulingIgnoredDuringExecution'] = cleaned

    def __enter__(self) -> 'PodAffinity':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodAffinityTerm(_kuber_definitions.Definition):
    """
    Defines a set of pods (namely those matching the
    labelSelector relative to the given namespace(s)) that this
    pod should be co-located (affinity) or not co-located (anti-
    affinity) with, where co-located is defined as running on a
    node whose value of the label with key <topologyKey> matches
    that of any node on which a pod of the set of pods is
    running
    """

    def __init__(
            self,
            label_selector: 'LabelSelector' = None,
            namespaces: typing.List[str] = None,
            topology_key: str = None,
    ):
        """Create PodAffinityTerm instance."""
        super(PodAffinityTerm, self).__init__(
            api_version='core/v1',
            kind='PodAffinityTerm'
        )
        self._properties = {
            'labelSelector': label_selector or LabelSelector(),
            'namespaces': namespaces or [],
            'topologyKey': topology_key or '',

        }
        self._types = {
            'labelSelector': (LabelSelector, None),
            'namespaces': (list, str),
            'topologyKey': (str, None),

        }

    @property
    def label_selector(self) -> 'LabelSelector':
        """
        A label query over a set of resources, in this case pods.
        """
        return self._properties.get('labelSelector')

    @label_selector.setter
    def label_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        A label query over a set of resources, in this case pods.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['labelSelector'] = value

    @property
    def namespaces(self) -> typing.List[str]:
        """
        namespaces specifies which namespaces the labelSelector
        applies to (matches against); null or empty list means "this
        pod's namespace"
        """
        return self._properties.get('namespaces')

    @namespaces.setter
    def namespaces(self, value: typing.List[str]):
        """
        namespaces specifies which namespaces the labelSelector
        applies to (matches against); null or empty list means "this
        pod's namespace"
        """
        self._properties['namespaces'] = value

    @property
    def topology_key(self) -> str:
        """
        This pod should be co-located (affinity) or not co-located
        (anti-affinity) with the pods matching the labelSelector in
        the specified namespaces, where co-located is defined as
        running on a node whose value of the label with key
        topologyKey matches that of any node on which any of the
        selected pods is running. Empty topologyKey is not allowed.
        """
        return self._properties.get('topologyKey')

    @topology_key.setter
    def topology_key(self, value: str):
        """
        This pod should be co-located (affinity) or not co-located
        (anti-affinity) with the pods matching the labelSelector in
        the specified namespaces, where co-located is defined as
        running on a node whose value of the label with key
        topologyKey matches that of any node on which any of the
        selected pods is running. Empty topologyKey is not allowed.
        """
        self._properties['topologyKey'] = value

    def __enter__(self) -> 'PodAffinityTerm':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodAntiAffinity(_kuber_definitions.Definition):
    """
    Pod anti affinity is a group of inter pod anti affinity
    scheduling rules.
    """

    def __init__(
            self,
            preferred_during_scheduling_ignored_during_execution: typing.List['WeightedPodAffinityTerm'] = None,
            required_during_scheduling_ignored_during_execution: typing.List['PodAffinityTerm'] = None,
    ):
        """Create PodAntiAffinity instance."""
        super(PodAntiAffinity, self).__init__(
            api_version='core/v1',
            kind='PodAntiAffinity'
        )
        self._properties = {
            'preferredDuringSchedulingIgnoredDuringExecution': preferred_during_scheduling_ignored_during_execution or [],
            'requiredDuringSchedulingIgnoredDuringExecution': required_during_scheduling_ignored_during_execution or [],

        }
        self._types = {
            'preferredDuringSchedulingIgnoredDuringExecution': (list, WeightedPodAffinityTerm),
            'requiredDuringSchedulingIgnoredDuringExecution': (list, PodAffinityTerm),

        }

    @property
    def preferred_during_scheduling_ignored_during_execution(self) -> typing.List['WeightedPodAffinityTerm']:
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the anti-affinity expressions specified by this
        field, but it may choose a node that violates one or more of
        the expressions. The node that is most preferred is the one
        with the greatest sum of weights, i.e. for each node that
        meets all of the scheduling requirements (resource request,
        requiredDuringScheduling anti-affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node has pods
        which matches the corresponding podAffinityTerm; the node(s)
        with the highest sum are the most preferred.
        """
        return self._properties.get('preferredDuringSchedulingIgnoredDuringExecution')

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(
            self,
            value: typing.Union[typing.List['WeightedPodAffinityTerm'], typing.List[dict]]
    ):
        """
        The scheduler will prefer to schedule pods to nodes that
        satisfy the anti-affinity expressions specified by this
        field, but it may choose a node that violates one or more of
        the expressions. The node that is most preferred is the one
        with the greatest sum of weights, i.e. for each node that
        meets all of the scheduling requirements (resource request,
        requiredDuringScheduling anti-affinity expressions, etc.),
        compute a sum by iterating through the elements of this
        field and adding "weight" to the sum if the node has pods
        which matches the corresponding podAffinityTerm; the node(s)
        with the highest sum are the most preferred.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = WeightedPodAffinityTerm().from_dict(item)
            cleaned.append(item)
        self._properties['preferredDuringSchedulingIgnoredDuringExecution'] = cleaned

    @property
    def required_during_scheduling_ignored_during_execution(self) -> typing.List['PodAffinityTerm']:
        """
        If the anti-affinity requirements specified by this field
        are not met at scheduling time, the pod will not be
        scheduled onto the node. If the anti-affinity requirements
        specified by this field cease to be met at some point during
        pod execution (e.g. due to a pod label update), the system
        may or may not try to eventually evict the pod from its
        node. When there are multiple elements, the lists of nodes
        corresponding to each podAffinityTerm are intersected, i.e.
        all terms must be satisfied.
        """
        return self._properties.get('requiredDuringSchedulingIgnoredDuringExecution')

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(
            self,
            value: typing.Union[typing.List['PodAffinityTerm'], typing.List[dict]]
    ):
        """
        If the anti-affinity requirements specified by this field
        are not met at scheduling time, the pod will not be
        scheduled onto the node. If the anti-affinity requirements
        specified by this field cease to be met at some point during
        pod execution (e.g. due to a pod label update), the system
        may or may not try to eventually evict the pod from its
        node. When there are multiple elements, the lists of nodes
        corresponding to each podAffinityTerm are intersected, i.e.
        all terms must be satisfied.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodAffinityTerm().from_dict(item)
            cleaned.append(item)
        self._properties['requiredDuringSchedulingIgnoredDuringExecution'] = cleaned

    def __enter__(self) -> 'PodAntiAffinity':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodCondition(_kuber_definitions.Definition):
    """
    PodCondition contains details for the current condition of
    this pod.
    """

    def __init__(
            self,
            last_probe_time: str = None,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create PodCondition instance."""
        super(PodCondition, self).__init__(
            api_version='core/v1',
            kind='PodCondition'
        )
        self._properties = {
            'lastProbeTime': last_probe_time or None,
            'lastTransitionTime': last_transition_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastProbeTime': (str, None),
            'lastTransitionTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_probe_time(self) -> str:
        """
        Last time we probed the condition.
        """
        return self._properties.get('lastProbeTime')

    @last_probe_time.setter
    def last_probe_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time we probed the condition.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastProbeTime'] = value

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        Human-readable message indicating details about last
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        Human-readable message indicating details about last
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        Unique, one-word, CamelCase reason for the condition's last
        transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        Unique, one-word, CamelCase reason for the condition's last
        transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status is the status of the condition. Can be True, False,
        Unknown. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status is the status of the condition. Can be True, False,
        Unknown. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type is the type of the condition. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type is the type of the condition. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        self._properties['type'] = value

    def __enter__(self) -> 'PodCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDNSConfig(_kuber_definitions.Definition):
    """
    PodDNSConfig defines the DNS parameters of a pod in addition
    to those generated from DNSPolicy.
    """

    def __init__(
            self,
            nameservers: typing.List[str] = None,
            options: typing.List['PodDNSConfigOption'] = None,
            searches: typing.List[str] = None,
    ):
        """Create PodDNSConfig instance."""
        super(PodDNSConfig, self).__init__(
            api_version='core/v1',
            kind='PodDNSConfig'
        )
        self._properties = {
            'nameservers': nameservers or [],
            'options': options or [],
            'searches': searches or [],

        }
        self._types = {
            'nameservers': (list, str),
            'options': (list, PodDNSConfigOption),
            'searches': (list, str),

        }

    @property
    def nameservers(self) -> typing.List[str]:
        """
        A list of DNS name server IP addresses. This will be
        appended to the base nameservers generated from DNSPolicy.
        Duplicated nameservers will be removed.
        """
        return self._properties.get('nameservers')

    @nameservers.setter
    def nameservers(self, value: typing.List[str]):
        """
        A list of DNS name server IP addresses. This will be
        appended to the base nameservers generated from DNSPolicy.
        Duplicated nameservers will be removed.
        """
        self._properties['nameservers'] = value

    @property
    def options(self) -> typing.List['PodDNSConfigOption']:
        """
        A list of DNS resolver options. This will be merged with the
        base options generated from DNSPolicy. Duplicated entries
        will be removed. Resolution options given in Options will
        override those that appear in the base DNSPolicy.
        """
        return self._properties.get('options')

    @options.setter
    def options(
            self,
            value: typing.Union[typing.List['PodDNSConfigOption'], typing.List[dict]]
    ):
        """
        A list of DNS resolver options. This will be merged with the
        base options generated from DNSPolicy. Duplicated entries
        will be removed. Resolution options given in Options will
        override those that appear in the base DNSPolicy.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodDNSConfigOption().from_dict(item)
            cleaned.append(item)
        self._properties['options'] = cleaned

    @property
    def searches(self) -> typing.List[str]:
        """
        A list of DNS search domains for host-name lookup. This will
        be appended to the base search paths generated from
        DNSPolicy. Duplicated search paths will be removed.
        """
        return self._properties.get('searches')

    @searches.setter
    def searches(self, value: typing.List[str]):
        """
        A list of DNS search domains for host-name lookup. This will
        be appended to the base search paths generated from
        DNSPolicy. Duplicated search paths will be removed.
        """
        self._properties['searches'] = value

    def __enter__(self) -> 'PodDNSConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDNSConfigOption(_kuber_definitions.Definition):
    """
    PodDNSConfigOption defines DNS resolver options of a pod.
    """

    def __init__(
            self,
            name: str = None,
            value: str = None,
    ):
        """Create PodDNSConfigOption instance."""
        super(PodDNSConfigOption, self).__init__(
            api_version='core/v1',
            kind='PodDNSConfigOption'
        )
        self._properties = {
            'name': name or '',
            'value': value or '',

        }
        self._types = {
            'name': (str, None),
            'value': (str, None),

        }

    @property
    def name(self) -> str:
        """
        Required.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Required.
        """
        self._properties['name'] = value

    @property
    def value(self) -> str:
        """

        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """

        """
        self._properties['value'] = value

    def __enter__(self) -> 'PodDNSConfigOption':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodList(_kuber_definitions.Collection):
    """
    PodList is a list of Pods.
    """

    def __init__(
            self,
            items: typing.List['Pod'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodList instance."""
        super(PodList, self).__init__(
            api_version='core/v1',
            kind='PodList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Pod),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Pod']:
        """
        List of pods. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Pod'], typing.List[dict]]
    ):
        """
        List of pods. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Pod().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PodList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodReadinessGate(_kuber_definitions.Definition):
    """
    PodReadinessGate contains the reference to a pod condition
    """

    def __init__(
            self,
            condition_type: str = None,
    ):
        """Create PodReadinessGate instance."""
        super(PodReadinessGate, self).__init__(
            api_version='core/v1',
            kind='PodReadinessGate'
        )
        self._properties = {
            'conditionType': condition_type or '',

        }
        self._types = {
            'conditionType': (str, None),

        }

    @property
    def condition_type(self) -> str:
        """
        ConditionType refers to a condition in the pod's condition
        list with matching type.
        """
        return self._properties.get('conditionType')

    @condition_type.setter
    def condition_type(self, value: str):
        """
        ConditionType refers to a condition in the pod's condition
        list with matching type.
        """
        self._properties['conditionType'] = value

    def __enter__(self) -> 'PodReadinessGate':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityContext(_kuber_definitions.Definition):
    """
    PodSecurityContext holds pod-level security attributes and
    common container settings. Some fields are also present in
    container.securityContext.  Field values of
    container.securityContext take precedence over field values
    of PodSecurityContext.
    """

    def __init__(
            self,
            fs_group: int = None,
            run_as_group: int = None,
            run_as_non_root: bool = None,
            run_as_user: int = None,
            se_linux_options: 'SELinuxOptions' = None,
            supplemental_groups: typing.List[int] = None,
            sysctls: typing.List['Sysctl'] = None,
    ):
        """Create PodSecurityContext instance."""
        super(PodSecurityContext, self).__init__(
            api_version='core/v1',
            kind='PodSecurityContext'
        )
        self._properties = {
            'fsGroup': fs_group or None,
            'runAsGroup': run_as_group or None,
            'runAsNonRoot': run_as_non_root or None,
            'runAsUser': run_as_user or None,
            'seLinuxOptions': se_linux_options or SELinuxOptions(),
            'supplementalGroups': supplemental_groups or [],
            'sysctls': sysctls or [],

        }
        self._types = {
            'fsGroup': (int, None),
            'runAsGroup': (int, None),
            'runAsNonRoot': (bool, None),
            'runAsUser': (int, None),
            'seLinuxOptions': (SELinuxOptions, None),
            'supplementalGroups': (list, int),
            'sysctls': (list, Sysctl),

        }

    @property
    def fs_group(self) -> int:
        """
        A special supplemental group that applies to all containers
        in a pod. Some volume types allow the Kubelet to change the
        ownership of that volume to be owned by the pod:

        1. The
        owning GID will be the FSGroup 2. The setgid bit is set (new
        files created in the volume will be owned by FSGroup) 3. The
        permission bits are OR'd with rw-rw----

        If unset, the
        Kubelet will not modify the ownership and permissions of any
        volume.
        """
        return self._properties.get('fsGroup')

    @fs_group.setter
    def fs_group(self, value: int):
        """
        A special supplemental group that applies to all containers
        in a pod. Some volume types allow the Kubelet to change the
        ownership of that volume to be owned by the pod:

        1. The
        owning GID will be the FSGroup 2. The setgid bit is set (new
        files created in the volume will be owned by FSGroup) 3. The
        permission bits are OR'd with rw-rw----

        If unset, the
        Kubelet will not modify the ownership and permissions of any
        volume.
        """
        self._properties['fsGroup'] = value

    @property
    def run_as_group(self) -> int:
        """
        The GID to run the entrypoint of the container process. Uses
        runtime default if unset. May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        """
        return self._properties.get('runAsGroup')

    @run_as_group.setter
    def run_as_group(self, value: int):
        """
        The GID to run the entrypoint of the container process. Uses
        runtime default if unset. May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        """
        self._properties['runAsGroup'] = value

    @property
    def run_as_non_root(self) -> bool:
        """
        Indicates that the container must run as a non-root user. If
        true, the Kubelet will validate the image at runtime to
        ensure that it does not run as UID 0 (root) and fail to
        start the container if it does. If unset or false, no such
        validation will be performed. May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        return self._properties.get('runAsNonRoot')

    @run_as_non_root.setter
    def run_as_non_root(self, value: bool):
        """
        Indicates that the container must run as a non-root user. If
        true, the Kubelet will validate the image at runtime to
        ensure that it does not run as UID 0 (root) and fail to
        start the container if it does. If unset or false, no such
        validation will be performed. May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        self._properties['runAsNonRoot'] = value

    @property
    def run_as_user(self) -> int:
        """
        The UID to run the entrypoint of the container process.
        Defaults to user specified in image metadata if unspecified.
        May also be set in SecurityContext.  If set in both
        SecurityContext and PodSecurityContext, the value specified
        in SecurityContext takes precedence for that container.
        """
        return self._properties.get('runAsUser')

    @run_as_user.setter
    def run_as_user(self, value: int):
        """
        The UID to run the entrypoint of the container process.
        Defaults to user specified in image metadata if unspecified.
        May also be set in SecurityContext.  If set in both
        SecurityContext and PodSecurityContext, the value specified
        in SecurityContext takes precedence for that container.
        """
        self._properties['runAsUser'] = value

    @property
    def se_linux_options(self) -> 'SELinuxOptions':
        """
        The SELinux context to be applied to all containers. If
        unspecified, the container runtime will allocate a random
        SELinux context for each container.  May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        """
        return self._properties.get('seLinuxOptions')

    @se_linux_options.setter
    def se_linux_options(self, value: typing.Union['SELinuxOptions', dict]):
        """
        The SELinux context to be applied to all containers. If
        unspecified, the container runtime will allocate a random
        SELinux context for each container.  May also be set in
        SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        """
        if isinstance(value, dict):
            value = SELinuxOptions().from_dict(value)
        self._properties['seLinuxOptions'] = value

    @property
    def supplemental_groups(self) -> typing.List[int]:
        """
        A list of groups applied to the first process run in each
        container, in addition to the container's primary GID.  If
        unspecified, no groups will be added to any container.
        """
        return self._properties.get('supplementalGroups')

    @supplemental_groups.setter
    def supplemental_groups(self, value: typing.List[int]):
        """
        A list of groups applied to the first process run in each
        container, in addition to the container's primary GID.  If
        unspecified, no groups will be added to any container.
        """
        self._properties['supplementalGroups'] = value

    @property
    def sysctls(self) -> typing.List['Sysctl']:
        """
        Sysctls hold a list of namespaced sysctls used for the pod.
        Pods with unsupported sysctls (by the container runtime)
        might fail to launch.
        """
        return self._properties.get('sysctls')

    @sysctls.setter
    def sysctls(
            self,
            value: typing.Union[typing.List['Sysctl'], typing.List[dict]]
    ):
        """
        Sysctls hold a list of namespaced sysctls used for the pod.
        Pods with unsupported sysctls (by the container runtime)
        might fail to launch.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Sysctl().from_dict(item)
            cleaned.append(item)
        self._properties['sysctls'] = cleaned

    def __enter__(self) -> 'PodSecurityContext':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSpec(_kuber_definitions.Definition):
    """
    PodSpec is a description of a pod.
    """

    def __init__(
            self,
            active_deadline_seconds: int = None,
            affinity: 'Affinity' = None,
            automount_service_account_token: bool = None,
            containers: typing.List['Container'] = None,
            dns_config: 'PodDNSConfig' = None,
            dns_policy: str = None,
            enable_service_links: bool = None,
            host_aliases: typing.List['HostAlias'] = None,
            host_ipc: bool = None,
            host_network: bool = None,
            host_pid: bool = None,
            hostname: str = None,
            image_pull_secrets: typing.List['LocalObjectReference'] = None,
            init_containers: typing.List['Container'] = None,
            node_name: str = None,
            node_selector: dict = None,
            priority: int = None,
            priority_class_name: str = None,
            readiness_gates: typing.List['PodReadinessGate'] = None,
            restart_policy: str = None,
            runtime_class_name: str = None,
            scheduler_name: str = None,
            security_context: 'PodSecurityContext' = None,
            service_account: str = None,
            service_account_name: str = None,
            share_process_namespace: bool = None,
            subdomain: str = None,
            termination_grace_period_seconds: int = None,
            tolerations: typing.List['Toleration'] = None,
            volumes: typing.List['Volume'] = None,
    ):
        """Create PodSpec instance."""
        super(PodSpec, self).__init__(
            api_version='core/v1',
            kind='PodSpec'
        )
        self._properties = {
            'activeDeadlineSeconds': active_deadline_seconds or None,
            'affinity': affinity or Affinity(),
            'automountServiceAccountToken': automount_service_account_token or None,
            'containers': containers or [],
            'dnsConfig': dns_config or PodDNSConfig(),
            'dnsPolicy': dns_policy or '',
            'enableServiceLinks': enable_service_links or None,
            'hostAliases': host_aliases or [],
            'hostIPC': host_ipc or None,
            'hostNetwork': host_network or None,
            'hostPID': host_pid or None,
            'hostname': hostname or '',
            'imagePullSecrets': image_pull_secrets or [],
            'initContainers': init_containers or [],
            'nodeName': node_name or '',
            'nodeSelector': node_selector or {},
            'priority': priority or None,
            'priorityClassName': priority_class_name or '',
            'readinessGates': readiness_gates or [],
            'restartPolicy': restart_policy or '',
            'runtimeClassName': runtime_class_name or '',
            'schedulerName': scheduler_name or '',
            'securityContext': security_context or PodSecurityContext(),
            'serviceAccount': service_account or '',
            'serviceAccountName': service_account_name or '',
            'shareProcessNamespace': share_process_namespace or None,
            'subdomain': subdomain or '',
            'terminationGracePeriodSeconds': termination_grace_period_seconds or None,
            'tolerations': tolerations or [],
            'volumes': volumes or [],

        }
        self._types = {
            'activeDeadlineSeconds': (int, None),
            'affinity': (Affinity, None),
            'automountServiceAccountToken': (bool, None),
            'containers': (list, Container),
            'dnsConfig': (PodDNSConfig, None),
            'dnsPolicy': (str, None),
            'enableServiceLinks': (bool, None),
            'hostAliases': (list, HostAlias),
            'hostIPC': (bool, None),
            'hostNetwork': (bool, None),
            'hostPID': (bool, None),
            'hostname': (str, None),
            'imagePullSecrets': (list, LocalObjectReference),
            'initContainers': (list, Container),
            'nodeName': (str, None),
            'nodeSelector': (dict, None),
            'priority': (int, None),
            'priorityClassName': (str, None),
            'readinessGates': (list, PodReadinessGate),
            'restartPolicy': (str, None),
            'runtimeClassName': (str, None),
            'schedulerName': (str, None),
            'securityContext': (PodSecurityContext, None),
            'serviceAccount': (str, None),
            'serviceAccountName': (str, None),
            'shareProcessNamespace': (bool, None),
            'subdomain': (str, None),
            'terminationGracePeriodSeconds': (int, None),
            'tolerations': (list, Toleration),
            'volumes': (list, Volume),

        }

    @property
    def active_deadline_seconds(self) -> int:
        """
        Optional duration in seconds the pod may be active on the
        node relative to StartTime before the system will actively
        try to mark it failed and kill associated containers. Value
        must be a positive integer.
        """
        return self._properties.get('activeDeadlineSeconds')

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, value: int):
        """
        Optional duration in seconds the pod may be active on the
        node relative to StartTime before the system will actively
        try to mark it failed and kill associated containers. Value
        must be a positive integer.
        """
        self._properties['activeDeadlineSeconds'] = value

    @property
    def affinity(self) -> 'Affinity':
        """
        If specified, the pod's scheduling constraints
        """
        return self._properties.get('affinity')

    @affinity.setter
    def affinity(self, value: typing.Union['Affinity', dict]):
        """
        If specified, the pod's scheduling constraints
        """
        if isinstance(value, dict):
            value = Affinity().from_dict(value)
        self._properties['affinity'] = value

    @property
    def automount_service_account_token(self) -> bool:
        """
        AutomountServiceAccountToken indicates whether a service
        account token should be automatically mounted.
        """
        return self._properties.get('automountServiceAccountToken')

    @automount_service_account_token.setter
    def automount_service_account_token(self, value: bool):
        """
        AutomountServiceAccountToken indicates whether a service
        account token should be automatically mounted.
        """
        self._properties['automountServiceAccountToken'] = value

    @property
    def containers(self) -> typing.List['Container']:
        """
        List of containers belonging to the pod. Containers cannot
        currently be added or removed. There must be at least one
        container in a Pod. Cannot be updated.
        """
        return self._properties.get('containers')

    @containers.setter
    def containers(
            self,
            value: typing.Union[typing.List['Container'], typing.List[dict]]
    ):
        """
        List of containers belonging to the pod. Containers cannot
        currently be added or removed. There must be at least one
        container in a Pod. Cannot be updated.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Container().from_dict(item)
            cleaned.append(item)
        self._properties['containers'] = cleaned

    @property
    def dns_config(self) -> 'PodDNSConfig':
        """
        Specifies the DNS parameters of a pod. Parameters specified
        here will be merged to the generated DNS configuration based
        on DNSPolicy.
        """
        return self._properties.get('dnsConfig')

    @dns_config.setter
    def dns_config(self, value: typing.Union['PodDNSConfig', dict]):
        """
        Specifies the DNS parameters of a pod. Parameters specified
        here will be merged to the generated DNS configuration based
        on DNSPolicy.
        """
        if isinstance(value, dict):
            value = PodDNSConfig().from_dict(value)
        self._properties['dnsConfig'] = value

    @property
    def dns_policy(self) -> str:
        """
        Set DNS policy for the pod. Defaults to "ClusterFirst".
        Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst',
        'Default' or 'None'. DNS parameters given in DNSConfig will
        be merged with the policy selected with DNSPolicy. To have
        DNS options set along with hostNetwork, you have to specify
        DNS policy explicitly to 'ClusterFirstWithHostNet'.
        """
        return self._properties.get('dnsPolicy')

    @dns_policy.setter
    def dns_policy(self, value: str):
        """
        Set DNS policy for the pod. Defaults to "ClusterFirst".
        Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst',
        'Default' or 'None'. DNS parameters given in DNSConfig will
        be merged with the policy selected with DNSPolicy. To have
        DNS options set along with hostNetwork, you have to specify
        DNS policy explicitly to 'ClusterFirstWithHostNet'.
        """
        self._properties['dnsPolicy'] = value

    @property
    def enable_service_links(self) -> bool:
        """
        EnableServiceLinks indicates whether information about
        services should be injected into pod's environment
        variables, matching the syntax of Docker links. Optional:
        Defaults to true.
        """
        return self._properties.get('enableServiceLinks')

    @enable_service_links.setter
    def enable_service_links(self, value: bool):
        """
        EnableServiceLinks indicates whether information about
        services should be injected into pod's environment
        variables, matching the syntax of Docker links. Optional:
        Defaults to true.
        """
        self._properties['enableServiceLinks'] = value

    @property
    def host_aliases(self) -> typing.List['HostAlias']:
        """
        HostAliases is an optional list of hosts and IPs that will
        be injected into the pod's hosts file if specified. This is
        only valid for non-hostNetwork pods.
        """
        return self._properties.get('hostAliases')

    @host_aliases.setter
    def host_aliases(
            self,
            value: typing.Union[typing.List['HostAlias'], typing.List[dict]]
    ):
        """
        HostAliases is an optional list of hosts and IPs that will
        be injected into the pod's hosts file if specified. This is
        only valid for non-hostNetwork pods.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HostAlias().from_dict(item)
            cleaned.append(item)
        self._properties['hostAliases'] = cleaned

    @property
    def host_ipc(self) -> bool:
        """
        Use the host's ipc namespace. Optional: Default to false.
        """
        return self._properties.get('hostIPC')

    @host_ipc.setter
    def host_ipc(self, value: bool):
        """
        Use the host's ipc namespace. Optional: Default to false.
        """
        self._properties['hostIPC'] = value

    @property
    def host_network(self) -> bool:
        """
        Host networking requested for this pod. Use the host's
        network namespace. If this option is set, the ports that
        will be used must be specified. Default to false.
        """
        return self._properties.get('hostNetwork')

    @host_network.setter
    def host_network(self, value: bool):
        """
        Host networking requested for this pod. Use the host's
        network namespace. If this option is set, the ports that
        will be used must be specified. Default to false.
        """
        self._properties['hostNetwork'] = value

    @property
    def host_pid(self) -> bool:
        """
        Use the host's pid namespace. Optional: Default to false.
        """
        return self._properties.get('hostPID')

    @host_pid.setter
    def host_pid(self, value: bool):
        """
        Use the host's pid namespace. Optional: Default to false.
        """
        self._properties['hostPID'] = value

    @property
    def hostname(self) -> str:
        """
        Specifies the hostname of the Pod If not specified, the
        pod's hostname will be set to a system-defined value.
        """
        return self._properties.get('hostname')

    @hostname.setter
    def hostname(self, value: str):
        """
        Specifies the hostname of the Pod If not specified, the
        pod's hostname will be set to a system-defined value.
        """
        self._properties['hostname'] = value

    @property
    def image_pull_secrets(self) -> typing.List['LocalObjectReference']:
        """
        ImagePullSecrets is an optional list of references to
        secrets in the same namespace to use for pulling any of the
        images used by this PodSpec. If specified, these secrets
        will be passed to individual puller implementations for them
        to use. For example, in the case of docker, only
        DockerConfig type secrets are honored. More info: https://ku
        bernetes.io/docs/concepts/containers/images#specifying-
        imagepullsecrets-on-a-pod
        """
        return self._properties.get('imagePullSecrets')

    @image_pull_secrets.setter
    def image_pull_secrets(
            self,
            value: typing.Union[typing.List['LocalObjectReference'], typing.List[dict]]
    ):
        """
        ImagePullSecrets is an optional list of references to
        secrets in the same namespace to use for pulling any of the
        images used by this PodSpec. If specified, these secrets
        will be passed to individual puller implementations for them
        to use. For example, in the case of docker, only
        DockerConfig type secrets are honored. More info: https://ku
        bernetes.io/docs/concepts/containers/images#specifying-
        imagepullsecrets-on-a-pod
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LocalObjectReference().from_dict(item)
            cleaned.append(item)
        self._properties['imagePullSecrets'] = cleaned

    @property
    def init_containers(self) -> typing.List['Container']:
        """
        List of initialization containers belonging to the pod. Init
        containers are executed in order prior to containers being
        started. If any init container fails, the pod is considered
        to have failed and is handled according to its
        restartPolicy. The name for an init container or normal
        container must be unique among all containers. Init
        containers may not have Lifecycle actions, Readiness probes,
        or Liveness probes. The resourceRequirements of an init
        container are taken into account during scheduling by
        finding the highest request/limit for each resource type,
        and then using the max of of that value or the sum of the
        normal containers. Limits are applied to init containers in
        a similar fashion. Init containers cannot currently be added
        or removed. Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/init-
        containers/
        """
        return self._properties.get('initContainers')

    @init_containers.setter
    def init_containers(
            self,
            value: typing.Union[typing.List['Container'], typing.List[dict]]
    ):
        """
        List of initialization containers belonging to the pod. Init
        containers are executed in order prior to containers being
        started. If any init container fails, the pod is considered
        to have failed and is handled according to its
        restartPolicy. The name for an init container or normal
        container must be unique among all containers. Init
        containers may not have Lifecycle actions, Readiness probes,
        or Liveness probes. The resourceRequirements of an init
        container are taken into account during scheduling by
        finding the highest request/limit for each resource type,
        and then using the max of of that value or the sum of the
        normal containers. Limits are applied to init containers in
        a similar fashion. Init containers cannot currently be added
        or removed. Cannot be updated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/init-
        containers/
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Container().from_dict(item)
            cleaned.append(item)
        self._properties['initContainers'] = cleaned

    @property
    def node_name(self) -> str:
        """
        NodeName is a request to schedule this pod onto a specific
        node. If it is non-empty, the scheduler simply schedules
        this pod onto that node, assuming that it fits resource
        requirements.
        """
        return self._properties.get('nodeName')

    @node_name.setter
    def node_name(self, value: str):
        """
        NodeName is a request to schedule this pod onto a specific
        node. If it is non-empty, the scheduler simply schedules
        this pod onto that node, assuming that it fits resource
        requirements.
        """
        self._properties['nodeName'] = value

    @property
    def node_selector(self) -> dict:
        """
        NodeSelector is a selector which must be true for the pod to
        fit on a node. Selector which must match a node's labels for
        the pod to be scheduled on that node. More info:
        https://kubernetes.io/docs/concepts/configuration/assign-
        pod-node/
        """
        return self._properties.get('nodeSelector')

    @node_selector.setter
    def node_selector(self, value: dict):
        """
        NodeSelector is a selector which must be true for the pod to
        fit on a node. Selector which must match a node's labels for
        the pod to be scheduled on that node. More info:
        https://kubernetes.io/docs/concepts/configuration/assign-
        pod-node/
        """
        self._properties['nodeSelector'] = value

    @property
    def priority(self) -> int:
        """
        The priority value. Various system components use this field
        to find the priority of the pod. When Priority Admission
        Controller is enabled, it prevents users from setting this
        field. The admission controller populates this field from
        PriorityClassName. The higher the value, the higher the
        priority.
        """
        return self._properties.get('priority')

    @priority.setter
    def priority(self, value: int):
        """
        The priority value. Various system components use this field
        to find the priority of the pod. When Priority Admission
        Controller is enabled, it prevents users from setting this
        field. The admission controller populates this field from
        PriorityClassName. The higher the value, the higher the
        priority.
        """
        self._properties['priority'] = value

    @property
    def priority_class_name(self) -> str:
        """
        If specified, indicates the pod's priority. "system-node-
        critical" and "system-cluster-critical" are two special
        keywords which indicate the highest priorities with the
        former being the highest priority. Any other name must be
        defined by creating a PriorityClass object with that name.
        If not specified, the pod priority will be default or zero
        if there is no default.
        """
        return self._properties.get('priorityClassName')

    @priority_class_name.setter
    def priority_class_name(self, value: str):
        """
        If specified, indicates the pod's priority. "system-node-
        critical" and "system-cluster-critical" are two special
        keywords which indicate the highest priorities with the
        former being the highest priority. Any other name must be
        defined by creating a PriorityClass object with that name.
        If not specified, the pod priority will be default or zero
        if there is no default.
        """
        self._properties['priorityClassName'] = value

    @property
    def readiness_gates(self) -> typing.List['PodReadinessGate']:
        """
        If specified, all readiness gates will be evaluated for pod
        readiness. A pod is ready when all its containers are ready
        AND all conditions specified in the readiness gates have
        status equal to "True" More info:
        https://git.k8s.io/enhancements/keps/sig-network/0007-pod-
        ready%2B%2B.md
        """
        return self._properties.get('readinessGates')

    @readiness_gates.setter
    def readiness_gates(
            self,
            value: typing.Union[typing.List['PodReadinessGate'], typing.List[dict]]
    ):
        """
        If specified, all readiness gates will be evaluated for pod
        readiness. A pod is ready when all its containers are ready
        AND all conditions specified in the readiness gates have
        status equal to "True" More info:
        https://git.k8s.io/enhancements/keps/sig-network/0007-pod-
        ready%2B%2B.md
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodReadinessGate().from_dict(item)
            cleaned.append(item)
        self._properties['readinessGates'] = cleaned

    @property
    def restart_policy(self) -> str:
        """
        Restart policy for all containers within the pod. One of
        Always, OnFailure, Never. Default to Always. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle/#restart-policy
        """
        return self._properties.get('restartPolicy')

    @restart_policy.setter
    def restart_policy(self, value: str):
        """
        Restart policy for all containers within the pod. One of
        Always, OnFailure, Never. Default to Always. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle/#restart-policy
        """
        self._properties['restartPolicy'] = value

    @property
    def runtime_class_name(self) -> str:
        """
        RuntimeClassName refers to a RuntimeClass object in the
        node.k8s.io group, which should be used to run this pod.  If
        no RuntimeClass resource matches the named class, the pod
        will not be run. If unset or empty, the "legacy"
        RuntimeClass will be used, which is an implicit class with
        an empty definition that uses the default runtime handler.
        More info: https://git.k8s.io/enhancements/keps/sig-
        node/runtime-class.md This is an alpha feature and may
        change in the future.
        """
        return self._properties.get('runtimeClassName')

    @runtime_class_name.setter
    def runtime_class_name(self, value: str):
        """
        RuntimeClassName refers to a RuntimeClass object in the
        node.k8s.io group, which should be used to run this pod.  If
        no RuntimeClass resource matches the named class, the pod
        will not be run. If unset or empty, the "legacy"
        RuntimeClass will be used, which is an implicit class with
        an empty definition that uses the default runtime handler.
        More info: https://git.k8s.io/enhancements/keps/sig-
        node/runtime-class.md This is an alpha feature and may
        change in the future.
        """
        self._properties['runtimeClassName'] = value

    @property
    def scheduler_name(self) -> str:
        """
        If specified, the pod will be dispatched by specified
        scheduler. If not specified, the pod will be dispatched by
        default scheduler.
        """
        return self._properties.get('schedulerName')

    @scheduler_name.setter
    def scheduler_name(self, value: str):
        """
        If specified, the pod will be dispatched by specified
        scheduler. If not specified, the pod will be dispatched by
        default scheduler.
        """
        self._properties['schedulerName'] = value

    @property
    def security_context(self) -> 'PodSecurityContext':
        """
        SecurityContext holds pod-level security attributes and
        common container settings. Optional: Defaults to empty.  See
        type description for default values of each field.
        """
        return self._properties.get('securityContext')

    @security_context.setter
    def security_context(self, value: typing.Union['PodSecurityContext', dict]):
        """
        SecurityContext holds pod-level security attributes and
        common container settings. Optional: Defaults to empty.  See
        type description for default values of each field.
        """
        if isinstance(value, dict):
            value = PodSecurityContext().from_dict(value)
        self._properties['securityContext'] = value

    @property
    def service_account(self) -> str:
        """
        DeprecatedServiceAccount is a depreciated alias for
        ServiceAccountName. Deprecated: Use serviceAccountName
        instead.
        """
        return self._properties.get('serviceAccount')

    @service_account.setter
    def service_account(self, value: str):
        """
        DeprecatedServiceAccount is a depreciated alias for
        ServiceAccountName. Deprecated: Use serviceAccountName
        instead.
        """
        self._properties['serviceAccount'] = value

    @property
    def service_account_name(self) -> str:
        """
        ServiceAccountName is the name of the ServiceAccount to use
        to run this pod. More info:
        https://kubernetes.io/docs/tasks/configure-pod-
        container/configure-service-account/
        """
        return self._properties.get('serviceAccountName')

    @service_account_name.setter
    def service_account_name(self, value: str):
        """
        ServiceAccountName is the name of the ServiceAccount to use
        to run this pod. More info:
        https://kubernetes.io/docs/tasks/configure-pod-
        container/configure-service-account/
        """
        self._properties['serviceAccountName'] = value

    @property
    def share_process_namespace(self) -> bool:
        """
        Share a single process namespace between all of the
        containers in a pod. When this is set containers will be
        able to view and signal processes from other containers in
        the same pod, and the first process in each container will
        not be assigned PID 1. HostPID and ShareProcessNamespace
        cannot both be set. Optional: Default to false. This field
        is beta-level and may be disabled with the
        PodShareProcessNamespace feature.
        """
        return self._properties.get('shareProcessNamespace')

    @share_process_namespace.setter
    def share_process_namespace(self, value: bool):
        """
        Share a single process namespace between all of the
        containers in a pod. When this is set containers will be
        able to view and signal processes from other containers in
        the same pod, and the first process in each container will
        not be assigned PID 1. HostPID and ShareProcessNamespace
        cannot both be set. Optional: Default to false. This field
        is beta-level and may be disabled with the
        PodShareProcessNamespace feature.
        """
        self._properties['shareProcessNamespace'] = value

    @property
    def subdomain(self) -> str:
        """
        If specified, the fully qualified Pod hostname will be
        "<hostname>.<subdomain>.<pod namespace>.svc.<cluster
        domain>". If not specified, the pod will not have a
        domainname at all.
        """
        return self._properties.get('subdomain')

    @subdomain.setter
    def subdomain(self, value: str):
        """
        If specified, the fully qualified Pod hostname will be
        "<hostname>.<subdomain>.<pod namespace>.svc.<cluster
        domain>". If not specified, the pod will not have a
        domainname at all.
        """
        self._properties['subdomain'] = value

    @property
    def termination_grace_period_seconds(self) -> int:
        """
        Optional duration in seconds the pod needs to terminate
        gracefully. May be decreased in delete request. Value must
        be non-negative integer. The value zero indicates delete
        immediately. If this value is nil, the default grace period
        will be used instead. The grace period is the duration in
        seconds after the processes running in the pod are sent a
        termination signal and the time when the processes are
        forcibly halted with a kill signal. Set this value longer
        than the expected cleanup time for your process. Defaults to
        30 seconds.
        """
        return self._properties.get('terminationGracePeriodSeconds')

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, value: int):
        """
        Optional duration in seconds the pod needs to terminate
        gracefully. May be decreased in delete request. Value must
        be non-negative integer. The value zero indicates delete
        immediately. If this value is nil, the default grace period
        will be used instead. The grace period is the duration in
        seconds after the processes running in the pod are sent a
        termination signal and the time when the processes are
        forcibly halted with a kill signal. Set this value longer
        than the expected cleanup time for your process. Defaults to
        30 seconds.
        """
        self._properties['terminationGracePeriodSeconds'] = value

    @property
    def tolerations(self) -> typing.List['Toleration']:
        """
        If specified, the pod's tolerations.
        """
        return self._properties.get('tolerations')

    @tolerations.setter
    def tolerations(
            self,
            value: typing.Union[typing.List['Toleration'], typing.List[dict]]
    ):
        """
        If specified, the pod's tolerations.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Toleration().from_dict(item)
            cleaned.append(item)
        self._properties['tolerations'] = cleaned

    @property
    def volumes(self) -> typing.List['Volume']:
        """
        List of volumes that can be mounted by containers belonging
        to the pod. More info:
        https://kubernetes.io/docs/concepts/storage/volumes
        """
        return self._properties.get('volumes')

    @volumes.setter
    def volumes(
            self,
            value: typing.Union[typing.List['Volume'], typing.List[dict]]
    ):
        """
        List of volumes that can be mounted by containers belonging
        to the pod. More info:
        https://kubernetes.io/docs/concepts/storage/volumes
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Volume().from_dict(item)
            cleaned.append(item)
        self._properties['volumes'] = cleaned

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'PodSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.containers if c.name == name), None)

    def __enter__(self) -> 'PodSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodStatus(_kuber_definitions.Definition):
    """
    PodStatus represents information about the status of a pod.
    Status may trail the actual state of a system, especially if
    the node that hosts the pod cannot contact the control
    plane.
    """

    def __init__(
            self,
            conditions: typing.List['PodCondition'] = None,
            container_statuses: typing.List['ContainerStatus'] = None,
            host_ip: str = None,
            init_container_statuses: typing.List['ContainerStatus'] = None,
            message: str = None,
            nominated_node_name: str = None,
            phase: str = None,
            pod_ip: str = None,
            qos_class: str = None,
            reason: str = None,
            start_time: str = None,
    ):
        """Create PodStatus instance."""
        super(PodStatus, self).__init__(
            api_version='core/v1',
            kind='PodStatus'
        )
        self._properties = {
            'conditions': conditions or [],
            'containerStatuses': container_statuses or [],
            'hostIP': host_ip or '',
            'initContainerStatuses': init_container_statuses or [],
            'message': message or '',
            'nominatedNodeName': nominated_node_name or '',
            'phase': phase or '',
            'podIP': pod_ip or '',
            'qosClass': qos_class or '',
            'reason': reason or '',
            'startTime': start_time or None,

        }
        self._types = {
            'conditions': (list, PodCondition),
            'containerStatuses': (list, ContainerStatus),
            'hostIP': (str, None),
            'initContainerStatuses': (list, ContainerStatus),
            'message': (str, None),
            'nominatedNodeName': (str, None),
            'phase': (str, None),
            'podIP': (str, None),
            'qosClass': (str, None),
            'reason': (str, None),
            'startTime': (str, None),

        }

    @property
    def conditions(self) -> typing.List['PodCondition']:
        """
        Current service state of pod. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['PodCondition'], typing.List[dict]]
    ):
        """
        Current service state of pod. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-conditions
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def container_statuses(self) -> typing.List['ContainerStatus']:
        """
        The list has one entry per container in the manifest. Each
        entry is currently the output of `docker inspect`. More
        info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-and-container-status
        """
        return self._properties.get('containerStatuses')

    @container_statuses.setter
    def container_statuses(
            self,
            value: typing.Union[typing.List['ContainerStatus'], typing.List[dict]]
    ):
        """
        The list has one entry per container in the manifest. Each
        entry is currently the output of `docker inspect`. More
        info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-and-container-status
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ContainerStatus().from_dict(item)
            cleaned.append(item)
        self._properties['containerStatuses'] = cleaned

    @property
    def host_ip(self) -> str:
        """
        IP address of the host to which the pod is assigned. Empty
        if not yet scheduled.
        """
        return self._properties.get('hostIP')

    @host_ip.setter
    def host_ip(self, value: str):
        """
        IP address of the host to which the pod is assigned. Empty
        if not yet scheduled.
        """
        self._properties['hostIP'] = value

    @property
    def init_container_statuses(self) -> typing.List['ContainerStatus']:
        """
        The list has one entry per init container in the manifest.
        The most recent successful init container will have ready =
        true, the most recently started container will have
        startTime set. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-and-container-status
        """
        return self._properties.get('initContainerStatuses')

    @init_container_statuses.setter
    def init_container_statuses(
            self,
            value: typing.Union[typing.List['ContainerStatus'], typing.List[dict]]
    ):
        """
        The list has one entry per init container in the manifest.
        The most recent successful init container will have ready =
        true, the most recently started container will have
        startTime set. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-and-container-status
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ContainerStatus().from_dict(item)
            cleaned.append(item)
        self._properties['initContainerStatuses'] = cleaned

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about why the
        pod is in this condition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about why the
        pod is in this condition.
        """
        self._properties['message'] = value

    @property
    def nominated_node_name(self) -> str:
        """
        nominatedNodeName is set only when this pod preempts other
        pods on the node, but it cannot be scheduled right away as
        preemption victims receive their graceful termination
        periods. This field does not guarantee that the pod will be
        scheduled on this node. Scheduler may decide to place the
        pod elsewhere if other nodes become available sooner.
        Scheduler may also decide to give the resources on this node
        to a higher priority pod that is created after preemption.
        As a result, this field may be different than
        PodSpec.nodeName when the pod is scheduled.
        """
        return self._properties.get('nominatedNodeName')

    @nominated_node_name.setter
    def nominated_node_name(self, value: str):
        """
        nominatedNodeName is set only when this pod preempts other
        pods on the node, but it cannot be scheduled right away as
        preemption victims receive their graceful termination
        periods. This field does not guarantee that the pod will be
        scheduled on this node. Scheduler may decide to place the
        pod elsewhere if other nodes become available sooner.
        Scheduler may also decide to give the resources on this node
        to a higher priority pod that is created after preemption.
        As a result, this field may be different than
        PodSpec.nodeName when the pod is scheduled.
        """
        self._properties['nominatedNodeName'] = value

    @property
    def phase(self) -> str:
        """
        The phase of a Pod is a simple, high-level summary of where
        the Pod is in its lifecycle. The conditions array, the
        reason and message fields, and the individual container
        status arrays contain more detail about the pod's status.
        There are five possible phase values:

        Pending: The pod has
        been accepted by the Kubernetes system, but one or more of
        the container images has not been created. This includes
        time before being scheduled as well as time spent
        downloading images over the network, which could take a
        while. Running: The pod has been bound to a node, and all of
        the containers have been created. At least one container is
        still running, or is in the process of starting or
        restarting. Succeeded: All containers in the pod have
        terminated in success, and will not be restarted. Failed:
        All containers in the pod have terminated, and at least one
        container has terminated in failure. The container either
        exited with non-zero status or was terminated by the system.
        Unknown: For some reason the state of the pod could not be
        obtained, typically due to an error in communicating with
        the host of the pod.

        More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-phase
        """
        return self._properties.get('phase')

    @phase.setter
    def phase(self, value: str):
        """
        The phase of a Pod is a simple, high-level summary of where
        the Pod is in its lifecycle. The conditions array, the
        reason and message fields, and the individual container
        status arrays contain more detail about the pod's status.
        There are five possible phase values:

        Pending: The pod has
        been accepted by the Kubernetes system, but one or more of
        the container images has not been created. This includes
        time before being scheduled as well as time spent
        downloading images over the network, which could take a
        while. Running: The pod has been bound to a node, and all of
        the containers have been created. At least one container is
        still running, or is in the process of starting or
        restarting. Succeeded: All containers in the pod have
        terminated in success, and will not be restarted. Failed:
        All containers in the pod have terminated, and at least one
        container has terminated in failure. The container either
        exited with non-zero status or was terminated by the system.
        Unknown: For some reason the state of the pod could not be
        obtained, typically due to an error in communicating with
        the host of the pod.

        More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#pod-phase
        """
        self._properties['phase'] = value

    @property
    def pod_ip(self) -> str:
        """
        IP address allocated to the pod. Routable at least within
        the cluster. Empty if not yet allocated.
        """
        return self._properties.get('podIP')

    @pod_ip.setter
    def pod_ip(self, value: str):
        """
        IP address allocated to the pod. Routable at least within
        the cluster. Empty if not yet allocated.
        """
        self._properties['podIP'] = value

    @property
    def qos_class(self) -> str:
        """
        The Quality of Service (QOS) classification assigned to the
        pod based on resource requirements See PodQOSClass type for
        available QOS classes More info:
        https://git.k8s.io/community/contributors/design-
        proposals/node/resource-qos.md
        """
        return self._properties.get('qosClass')

    @qos_class.setter
    def qos_class(self, value: str):
        """
        The Quality of Service (QOS) classification assigned to the
        pod based on resource requirements See PodQOSClass type for
        available QOS classes More info:
        https://git.k8s.io/community/contributors/design-
        proposals/node/resource-qos.md
        """
        self._properties['qosClass'] = value

    @property
    def reason(self) -> str:
        """
        A brief CamelCase message indicating details about why the
        pod is in this state. e.g. 'Evicted'
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        A brief CamelCase message indicating details about why the
        pod is in this state. e.g. 'Evicted'
        """
        self._properties['reason'] = value

    @property
    def start_time(self) -> str:
        """
        RFC 3339 date and time at which the object was acknowledged
        by the Kubelet. This is before the Kubelet pulled the
        container image(s) for the pod.
        """
        return self._properties.get('startTime')

    @start_time.setter
    def start_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        RFC 3339 date and time at which the object was acknowledged
        by the Kubelet. This is before the Kubelet pulled the
        container image(s) for the pod.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['startTime'] = value

    def __enter__(self) -> 'PodStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodTemplate(_kuber_definitions.Resource):
    """
    PodTemplate describes a template for creating copies of a
    predefined pod.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            template: 'PodTemplateSpec' = None,
    ):
        """Create PodTemplate instance."""
        super(PodTemplate, self).__init__(
            api_version='core/v1',
            kind='PodTemplate'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'template': template or PodTemplateSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'template': (PodTemplateSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        Template defines the pods that will be created from this pod
        template.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        Template defines the pods that will be created from this pod
        template.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'PodTemplate':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the PodTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_pod_template',
            'create_pod_template'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the PodTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_pod_template',
            'replace_pod_template'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the PodTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_pod_template',
            'patch_pod_template'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the PodTemplate from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_pod_template',
            'read_pod_template'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the PodTemplate from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_pod_template',
            'delete_pod_template'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PodTemplate':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodTemplateList(_kuber_definitions.Collection):
    """
    PodTemplateList is a list of PodTemplates.
    """

    def __init__(
            self,
            items: typing.List['PodTemplate'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodTemplateList instance."""
        super(PodTemplateList, self).__init__(
            api_version='core/v1',
            kind='PodTemplateList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PodTemplate),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PodTemplate']:
        """
        List of pod templates
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PodTemplate'], typing.List[dict]]
    ):
        """
        List of pod templates
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodTemplate().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'PodTemplateList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodTemplateSpec(_kuber_definitions.Definition):
    """
    PodTemplateSpec describes the data a pod should have when
    created from a template
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PodSpec' = None,
    ):
        """Create PodTemplateSpec instance."""
        super(PodTemplateSpec, self).__init__(
            api_version='core/v1',
            kind='PodTemplateSpec'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PodSpec(),

        }
        self._types = {
            'metadata': (ObjectMeta, None),
            'spec': (PodSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PodSpec':
        """
        Specification of the desired behavior of the pod. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PodSpec', dict]):
        """
        Specification of the desired behavior of the pod. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = PodSpec().from_dict(value)
        self._properties['spec'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'PodTemplateSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.containers if c.name == name), None)

    def __enter__(self) -> 'PodTemplateSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PortworxVolumeSource(_kuber_definitions.Definition):
    """
    PortworxVolumeSource represents a Portworx volume resource.
    """

    def __init__(
            self,
            fs_type: str = None,
            read_only: bool = None,
            volume_id: str = None,
    ):
        """Create PortworxVolumeSource instance."""
        super(PortworxVolumeSource, self).__init__(
            api_version='core/v1',
            kind='PortworxVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'readOnly': read_only or None,
            'volumeID': volume_id or '',

        }
        self._types = {
            'fsType': (str, None),
            'readOnly': (bool, None),
            'volumeID': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        FSType represents the filesystem type to mount Must be a
        filesystem type supported by the host operating system. Ex.
        "ext4", "xfs". Implicitly inferred to be "ext4" if
        unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        FSType represents the filesystem type to mount Must be a
        filesystem type supported by the host operating system. Ex.
        "ext4", "xfs". Implicitly inferred to be "ext4" if
        unspecified.
        """
        self._properties['fsType'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def volume_id(self) -> str:
        """
        VolumeID uniquely identifies a Portworx volume
        """
        return self._properties.get('volumeID')

    @volume_id.setter
    def volume_id(self, value: str):
        """
        VolumeID uniquely identifies a Portworx volume
        """
        self._properties['volumeID'] = value

    def __enter__(self) -> 'PortworxVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PreferredSchedulingTerm(_kuber_definitions.Definition):
    """
    An empty preferred scheduling term matches all objects with
    implicit weight 0 (i.e. it's a no-op). A null preferred
    scheduling term matches no objects (i.e. is also a no-op).
    """

    def __init__(
            self,
            preference: 'NodeSelectorTerm' = None,
            weight: int = None,
    ):
        """Create PreferredSchedulingTerm instance."""
        super(PreferredSchedulingTerm, self).__init__(
            api_version='core/v1',
            kind='PreferredSchedulingTerm'
        )
        self._properties = {
            'preference': preference or NodeSelectorTerm(),
            'weight': weight or None,

        }
        self._types = {
            'preference': (NodeSelectorTerm, None),
            'weight': (int, None),

        }

    @property
    def preference(self) -> 'NodeSelectorTerm':
        """
        A node selector term, associated with the corresponding
        weight.
        """
        return self._properties.get('preference')

    @preference.setter
    def preference(self, value: typing.Union['NodeSelectorTerm', dict]):
        """
        A node selector term, associated with the corresponding
        weight.
        """
        if isinstance(value, dict):
            value = NodeSelectorTerm().from_dict(value)
        self._properties['preference'] = value

    @property
    def weight(self) -> int:
        """
        Weight associated with matching the corresponding
        nodeSelectorTerm, in the range 1-100.
        """
        return self._properties.get('weight')

    @weight.setter
    def weight(self, value: int):
        """
        Weight associated with matching the corresponding
        nodeSelectorTerm, in the range 1-100.
        """
        self._properties['weight'] = value

    def __enter__(self) -> 'PreferredSchedulingTerm':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Probe(_kuber_definitions.Definition):
    """
    Probe describes a health check to be performed against a
    container to determine whether it is alive or ready to
    receive traffic.
    """

    def __init__(
            self,
            exec_: 'ExecAction' = None,
            failure_threshold: int = None,
            http_get: 'HTTPGetAction' = None,
            initial_delay_seconds: int = None,
            period_seconds: int = None,
            success_threshold: int = None,
            tcp_socket: 'TCPSocketAction' = None,
            timeout_seconds: int = None,
    ):
        """Create Probe instance."""
        super(Probe, self).__init__(
            api_version='core/v1',
            kind='Probe'
        )
        self._properties = {
            'exec': exec_ or ExecAction(),
            'failureThreshold': failure_threshold or None,
            'httpGet': http_get or HTTPGetAction(),
            'initialDelaySeconds': initial_delay_seconds or None,
            'periodSeconds': period_seconds or None,
            'successThreshold': success_threshold or None,
            'tcpSocket': tcp_socket or TCPSocketAction(),
            'timeoutSeconds': timeout_seconds or None,

        }
        self._types = {
            'exec': (ExecAction, None),
            'failureThreshold': (int, None),
            'httpGet': (HTTPGetAction, None),
            'initialDelaySeconds': (int, None),
            'periodSeconds': (int, None),
            'successThreshold': (int, None),
            'tcpSocket': (TCPSocketAction, None),
            'timeoutSeconds': (int, None),

        }

    @property
    def exec_(self) -> 'ExecAction':
        """
        One and only one of the following should be specified. Exec
        specifies the action to take.
        """
        return self._properties.get('exec')

    @exec_.setter
    def exec_(self, value: typing.Union['ExecAction', dict]):
        """
        One and only one of the following should be specified. Exec
        specifies the action to take.
        """
        if isinstance(value, dict):
            value = ExecAction().from_dict(value)
        self._properties['exec'] = value

    @property
    def failure_threshold(self) -> int:
        """
        Minimum consecutive failures for the probe to be considered
        failed after having succeeded. Defaults to 3. Minimum value
        is 1.
        """
        return self._properties.get('failureThreshold')

    @failure_threshold.setter
    def failure_threshold(self, value: int):
        """
        Minimum consecutive failures for the probe to be considered
        failed after having succeeded. Defaults to 3. Minimum value
        is 1.
        """
        self._properties['failureThreshold'] = value

    @property
    def http_get(self) -> 'HTTPGetAction':
        """
        HTTPGet specifies the http request to perform.
        """
        return self._properties.get('httpGet')

    @http_get.setter
    def http_get(self, value: typing.Union['HTTPGetAction', dict]):
        """
        HTTPGet specifies the http request to perform.
        """
        if isinstance(value, dict):
            value = HTTPGetAction().from_dict(value)
        self._properties['httpGet'] = value

    @property
    def initial_delay_seconds(self) -> int:
        """
        Number of seconds after the container has started before
        liveness probes are initiated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        return self._properties.get('initialDelaySeconds')

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: int):
        """
        Number of seconds after the container has started before
        liveness probes are initiated. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        self._properties['initialDelaySeconds'] = value

    @property
    def period_seconds(self) -> int:
        """
        How often (in seconds) to perform the probe. Default to 10
        seconds. Minimum value is 1.
        """
        return self._properties.get('periodSeconds')

    @period_seconds.setter
    def period_seconds(self, value: int):
        """
        How often (in seconds) to perform the probe. Default to 10
        seconds. Minimum value is 1.
        """
        self._properties['periodSeconds'] = value

    @property
    def success_threshold(self) -> int:
        """
        Minimum consecutive successes for the probe to be considered
        successful after having failed. Defaults to 1. Must be 1 for
        liveness. Minimum value is 1.
        """
        return self._properties.get('successThreshold')

    @success_threshold.setter
    def success_threshold(self, value: int):
        """
        Minimum consecutive successes for the probe to be considered
        successful after having failed. Defaults to 1. Must be 1 for
        liveness. Minimum value is 1.
        """
        self._properties['successThreshold'] = value

    @property
    def tcp_socket(self) -> 'TCPSocketAction':
        """
        TCPSocket specifies an action involving a TCP port. TCP
        hooks not yet supported
        """
        return self._properties.get('tcpSocket')

    @tcp_socket.setter
    def tcp_socket(self, value: typing.Union['TCPSocketAction', dict]):
        """
        TCPSocket specifies an action involving a TCP port. TCP
        hooks not yet supported
        """
        if isinstance(value, dict):
            value = TCPSocketAction().from_dict(value)
        self._properties['tcpSocket'] = value

    @property
    def timeout_seconds(self) -> int:
        """
        Number of seconds after which the probe times out. Defaults
        to 1 second. Minimum value is 1. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        return self._properties.get('timeoutSeconds')

    @timeout_seconds.setter
    def timeout_seconds(self, value: int):
        """
        Number of seconds after which the probe times out. Defaults
        to 1 second. Minimum value is 1. More info:
        https://kubernetes.io/docs/concepts/workloads/pods/pod-
        lifecycle#container-probes
        """
        self._properties['timeoutSeconds'] = value

    def __enter__(self) -> 'Probe':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ProjectedVolumeSource(_kuber_definitions.Definition):
    """
    Represents a projected volume source
    """

    def __init__(
            self,
            default_mode: int = None,
            sources: typing.List['VolumeProjection'] = None,
    ):
        """Create ProjectedVolumeSource instance."""
        super(ProjectedVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ProjectedVolumeSource'
        )
        self._properties = {
            'defaultMode': default_mode or None,
            'sources': sources or [],

        }
        self._types = {
            'defaultMode': (int, None),
            'sources': (list, VolumeProjection),

        }

    @property
    def default_mode(self) -> int:
        """
        Mode bits to use on created files by default. Must be a
        value between 0 and 0777. Directories within the path are
        not affected by this setting. This might be in conflict with
        other options that affect the file mode, like fsGroup, and
        the result can be other mode bits set.
        """
        return self._properties.get('defaultMode')

    @default_mode.setter
    def default_mode(self, value: int):
        """
        Mode bits to use on created files by default. Must be a
        value between 0 and 0777. Directories within the path are
        not affected by this setting. This might be in conflict with
        other options that affect the file mode, like fsGroup, and
        the result can be other mode bits set.
        """
        self._properties['defaultMode'] = value

    @property
    def sources(self) -> typing.List['VolumeProjection']:
        """
        list of volume projections
        """
        return self._properties.get('sources')

    @sources.setter
    def sources(
            self,
            value: typing.Union[typing.List['VolumeProjection'], typing.List[dict]]
    ):
        """
        list of volume projections
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = VolumeProjection().from_dict(item)
            cleaned.append(item)
        self._properties['sources'] = cleaned

    def __enter__(self) -> 'ProjectedVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class QuobyteVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Quobyte mount that lasts the lifetime of a pod.
    Quobyte volumes do not support ownership management or
    SELinux relabeling.
    """

    def __init__(
            self,
            group: str = None,
            read_only: bool = None,
            registry: str = None,
            tenant: str = None,
            user: str = None,
            volume: str = None,
    ):
        """Create QuobyteVolumeSource instance."""
        super(QuobyteVolumeSource, self).__init__(
            api_version='core/v1',
            kind='QuobyteVolumeSource'
        )
        self._properties = {
            'group': group or '',
            'readOnly': read_only or None,
            'registry': registry or '',
            'tenant': tenant or '',
            'user': user or '',
            'volume': volume or '',

        }
        self._types = {
            'group': (str, None),
            'readOnly': (bool, None),
            'registry': (str, None),
            'tenant': (str, None),
            'user': (str, None),
            'volume': (str, None),

        }

    @property
    def group(self) -> str:
        """
        Group to map volume access to Default is no group
        """
        return self._properties.get('group')

    @group.setter
    def group(self, value: str):
        """
        Group to map volume access to Default is no group
        """
        self._properties['group'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the Quobyte volume to be mounted
        with read-only permissions. Defaults to false.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the Quobyte volume to be mounted
        with read-only permissions. Defaults to false.
        """
        self._properties['readOnly'] = value

    @property
    def registry(self) -> str:
        """
        Registry represents a single or multiple Quobyte Registry
        services specified as a string as host:port pair (multiple
        entries are separated with commas) which acts as the central
        registry for volumes
        """
        return self._properties.get('registry')

    @registry.setter
    def registry(self, value: str):
        """
        Registry represents a single or multiple Quobyte Registry
        services specified as a string as host:port pair (multiple
        entries are separated with commas) which acts as the central
        registry for volumes
        """
        self._properties['registry'] = value

    @property
    def tenant(self) -> str:
        """
        Tenant owning the given Quobyte volume in the Backend Used
        with dynamically provisioned Quobyte volumes, value is set
        by the plugin
        """
        return self._properties.get('tenant')

    @tenant.setter
    def tenant(self, value: str):
        """
        Tenant owning the given Quobyte volume in the Backend Used
        with dynamically provisioned Quobyte volumes, value is set
        by the plugin
        """
        self._properties['tenant'] = value

    @property
    def user(self) -> str:
        """
        User to map volume access to Defaults to serivceaccount user
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        User to map volume access to Defaults to serivceaccount user
        """
        self._properties['user'] = value

    @property
    def volume(self) -> str:
        """
        Volume is a string that references an already created
        Quobyte volume by name.
        """
        return self._properties.get('volume')

    @volume.setter
    def volume(self, value: str):
        """
        Volume is a string that references an already created
        Quobyte volume by name.
        """
        self._properties['volume'] = value

    def __enter__(self) -> 'QuobyteVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RBDPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Rados Block Device mount that lasts the
    lifetime of a pod. RBD volumes support ownership management
    and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            image: str = None,
            keyring: str = None,
            monitors: typing.List[str] = None,
            pool: str = None,
            read_only: bool = None,
            secret_ref: 'SecretReference' = None,
            user: str = None,
    ):
        """Create RBDPersistentVolumeSource instance."""
        super(RBDPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='RBDPersistentVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'image': image or '',
            'keyring': keyring or '',
            'monitors': monitors or [],
            'pool': pool or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or SecretReference(),
            'user': user or '',

        }
        self._types = {
            'fsType': (str, None),
            'image': (str, None),
            'keyring': (str, None),
            'monitors': (list, str),
            'pool': (str, None),
            'readOnly': (bool, None),
            'secretRef': (SecretReference, None),
            'user': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#rbd
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#rbd
        """
        self._properties['fsType'] = value

    @property
    def image(self) -> str:
        """
        The rados image name. More info: https://releases.k8s.io/HEA
        D/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('image')

    @image.setter
    def image(self, value: str):
        """
        The rados image name. More info: https://releases.k8s.io/HEA
        D/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['image'] = value

    @property
    def keyring(self) -> str:
        """
        Keyring is the path to key ring for RBDUser. Default is
        /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/e
        xamples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('keyring')

    @keyring.setter
    def keyring(self, value: str):
        """
        Keyring is the path to key ring for RBDUser. Default is
        /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/e
        xamples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['keyring'] = value

    @property
    def monitors(self) -> typing.List[str]:
        """
        A collection of Ceph monitors. More info: https://releases.k
        8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('monitors')

    @monitors.setter
    def monitors(self, value: typing.List[str]):
        """
        A collection of Ceph monitors. More info: https://releases.k
        8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['monitors'] = value

    @property
    def pool(self) -> str:
        """
        The rados pool name. Default is rbd. More info: https://rele
        ases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-
        it
        """
        return self._properties.get('pool')

    @pool.setter
    def pool(self, value: str):
        """
        The rados pool name. Default is rbd. More info: https://rele
        ases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-
        it
        """
        self._properties['pool'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://releases
        .k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://releases
        .k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        SecretRef is name of the authentication secret for RBDUser.
        If provided overrides keyring. Default is nil. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#ho
        w-to-use-it
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        SecretRef is name of the authentication secret for RBDUser.
        If provided overrides keyring. Default is nil. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#ho
        w-to-use-it
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def user(self) -> str:
        """
        The rados user name. Default is admin. More info: https://re
        leases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-
        use-it
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        The rados user name. Default is admin. More info: https://re
        leases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-
        use-it
        """
        self._properties['user'] = value

    def __enter__(self) -> 'RBDPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RBDVolumeSource(_kuber_definitions.Definition):
    """
    Represents a Rados Block Device mount that lasts the
    lifetime of a pod. RBD volumes support ownership management
    and SELinux relabeling.
    """

    def __init__(
            self,
            fs_type: str = None,
            image: str = None,
            keyring: str = None,
            monitors: typing.List[str] = None,
            pool: str = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
            user: str = None,
    ):
        """Create RBDVolumeSource instance."""
        super(RBDVolumeSource, self).__init__(
            api_version='core/v1',
            kind='RBDVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'image': image or '',
            'keyring': keyring or '',
            'monitors': monitors or [],
            'pool': pool or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),
            'user': user or '',

        }
        self._types = {
            'fsType': (str, None),
            'image': (str, None),
            'keyring': (str, None),
            'monitors': (list, str),
            'pool': (str, None),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),
            'user': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#rbd
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type of the volume that you want to mount. Tip:
        Ensure that the filesystem type is supported by the host
        operating system. Examples: "ext4", "xfs", "ntfs".
        Implicitly inferred to be "ext4" if unspecified. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#rbd
        """
        self._properties['fsType'] = value

    @property
    def image(self) -> str:
        """
        The rados image name. More info: https://releases.k8s.io/HEA
        D/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('image')

    @image.setter
    def image(self, value: str):
        """
        The rados image name. More info: https://releases.k8s.io/HEA
        D/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['image'] = value

    @property
    def keyring(self) -> str:
        """
        Keyring is the path to key ring for RBDUser. Default is
        /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/e
        xamples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('keyring')

    @keyring.setter
    def keyring(self, value: str):
        """
        Keyring is the path to key ring for RBDUser. Default is
        /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/e
        xamples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['keyring'] = value

    @property
    def monitors(self) -> typing.List[str]:
        """
        A collection of Ceph monitors. More info: https://releases.k
        8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('monitors')

    @monitors.setter
    def monitors(self, value: typing.List[str]):
        """
        A collection of Ceph monitors. More info: https://releases.k
        8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['monitors'] = value

    @property
    def pool(self) -> str:
        """
        The rados pool name. Default is rbd. More info: https://rele
        ases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-
        it
        """
        return self._properties.get('pool')

    @pool.setter
    def pool(self, value: str):
        """
        The rados pool name. Default is rbd. More info: https://rele
        ases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-
        it
        """
        self._properties['pool'] = value

    @property
    def read_only(self) -> bool:
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://releases
        .k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        ReadOnly here will force the ReadOnly setting in
        VolumeMounts. Defaults to false. More info: https://releases
        .k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        SecretRef is name of the authentication secret for RBDUser.
        If provided overrides keyring. Default is nil. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#ho
        w-to-use-it
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        SecretRef is name of the authentication secret for RBDUser.
        If provided overrides keyring. Default is nil. More info: ht
        tps://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#ho
        w-to-use-it
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def user(self) -> str:
        """
        The rados user name. Default is admin. More info: https://re
        leases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-
        use-it
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        The rados user name. Default is admin. More info: https://re
        leases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-
        use-it
        """
        self._properties['user'] = value

    def __enter__(self) -> 'RBDVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicationController(_kuber_definitions.Resource):
    """
    ReplicationController represents the configuration of a
    replication controller.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ReplicationControllerSpec' = None,
            status: 'ReplicationControllerStatus' = None,
    ):
        """Create ReplicationController instance."""
        super(ReplicationController, self).__init__(
            api_version='core/v1',
            kind='ReplicationController'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ReplicationControllerSpec(),
            'status': status or ReplicationControllerStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (ReplicationControllerSpec, None),
            'status': (ReplicationControllerStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        If the Labels of a ReplicationController are empty, they are
        defaulted to be the same as the Pod(s) that the replication
        controller manages. Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        If the Labels of a ReplicationController are empty, they are
        defaulted to be the same as the Pod(s) that the replication
        controller manages. Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ReplicationControllerSpec':
        """
        Spec defines the specification of the desired behavior of
        the replication controller. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ReplicationControllerSpec', dict]):
        """
        Spec defines the specification of the desired behavior of
        the replication controller. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ReplicationControllerSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'ReplicationControllerStatus':
        """
        Status is the most recently observed status of the
        replication controller. This data may be out of date by some
        window of time. Populated by the system. Read-only. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['ReplicationControllerStatus', dict]):
        """
        Status is the most recently observed status of the
        replication controller. This data may be out of date by some
        window of time. Populated by the system. Read-only. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ReplicationControllerStatus().from_dict(value)
        self._properties['status'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'ReplicationController':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.template.spec.containers if c.name == name), None)

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicationControllerStatus':
        """
        Creates the ReplicationController in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_replication_controller',
            'create_replication_controller'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            ReplicationControllerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicationControllerStatus':
        """
        Replaces the ReplicationController in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_replication_controller',
            'replace_replication_controller'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ReplicationControllerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicationControllerStatus':
        """
        Patches the ReplicationController in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_replication_controller',
            'patch_replication_controller'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ReplicationControllerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'ReplicationControllerStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_replication_controller',
            'read_replication_controller'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            ReplicationControllerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ReplicationController from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_replication_controller',
            'read_replication_controller'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the ReplicationController from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_replication_controller',
            'delete_replication_controller'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ReplicationController':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicationControllerCondition(_kuber_definitions.Definition):
    """
    ReplicationControllerCondition describes the state of a
    replication controller at a certain point.
    """

    def __init__(
            self,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create ReplicationControllerCondition instance."""
        super(ReplicationControllerCondition, self).__init__(
            api_version='core/v1',
            kind='ReplicationControllerCondition'
        )
        self._properties = {
            'lastTransitionTime': last_transition_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastTransitionTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_transition_time(self) -> str:
        """
        The last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of replication controller condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of replication controller condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'ReplicationControllerCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicationControllerList(_kuber_definitions.Collection):
    """
    ReplicationControllerList is a collection of replication
    controllers.
    """

    def __init__(
            self,
            items: typing.List['ReplicationController'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ReplicationControllerList instance."""
        super(ReplicationControllerList, self).__init__(
            api_version='core/v1',
            kind='ReplicationControllerList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ReplicationController),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ReplicationController']:
        """
        List of replication controllers. More info: https://kubernet
        es.io/docs/concepts/workloads/controllers/replicationcontrol
        ler
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ReplicationController'], typing.List[dict]]
    ):
        """
        List of replication controllers. More info: https://kubernet
        es.io/docs/concepts/workloads/controllers/replicationcontrol
        ler
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ReplicationController().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ReplicationControllerList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicationControllerSpec(_kuber_definitions.Definition):
    """
    ReplicationControllerSpec is the specification of a
    replication controller.
    """

    def __init__(
            self,
            min_ready_seconds: int = None,
            replicas: int = None,
            selector: dict = None,
            template: 'PodTemplateSpec' = None,
    ):
        """Create ReplicationControllerSpec instance."""
        super(ReplicationControllerSpec, self).__init__(
            api_version='core/v1',
            kind='ReplicationControllerSpec'
        )
        self._properties = {
            'minReadySeconds': min_ready_seconds or None,
            'replicas': replicas or None,
            'selector': selector or {},
            'template': template or PodTemplateSpec(),

        }
        self._types = {
            'minReadySeconds': (int, None),
            'replicas': (int, None),
            'selector': (dict, None),
            'template': (PodTemplateSpec, None),

        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        return self._properties.get('minReadySeconds')

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        self._properties['minReadySeconds'] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller#w
        hat-is-a-replicationcontroller
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller#w
        hat-is-a-replicationcontroller
        """
        self._properties['replicas'] = value

    @property
    def selector(self) -> dict:
        """
        Selector is a label query over pods that should match the
        Replicas count. If Selector is empty, it is defaulted to the
        labels present on the Pod template. Label keys and values
        that must match in order to be controlled by this
        replication controller, if empty defaulted to labels on Pod
        template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: dict):
        """
        Selector is a label query over pods that should match the
        Replicas count. If Selector is empty, it is defaulted to the
        labels present on the Pod template. Label keys and values
        that must match in order to be controlled by this
        replication controller, if empty defaulted to labels on Pod
        template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        self._properties['selector'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. This takes
        precedence over a TemplateRef. More info: https://kubernetes
        .io/docs/concepts/workloads/controllers/replicationcontrolle
        r#pod-template
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. This takes
        precedence over a TemplateRef. More info: https://kubernetes
        .io/docs/concepts/workloads/controllers/replicationcontrolle
        r#pod-template
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'ReplicationControllerSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def __enter__(self) -> 'ReplicationControllerSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicationControllerStatus(_kuber_definitions.Definition):
    """
    ReplicationControllerStatus represents the current status of
    a replication controller.
    """

    def __init__(
            self,
            available_replicas: int = None,
            conditions: typing.List['ReplicationControllerCondition'] = None,
            fully_labeled_replicas: int = None,
            observed_generation: int = None,
            ready_replicas: int = None,
            replicas: int = None,
    ):
        """Create ReplicationControllerStatus instance."""
        super(ReplicationControllerStatus, self).__init__(
            api_version='core/v1',
            kind='ReplicationControllerStatus'
        )
        self._properties = {
            'availableReplicas': available_replicas or None,
            'conditions': conditions or [],
            'fullyLabeledReplicas': fully_labeled_replicas or None,
            'observedGeneration': observed_generation or None,
            'readyReplicas': ready_replicas or None,
            'replicas': replicas or None,

        }
        self._types = {
            'availableReplicas': (int, None),
            'conditions': (list, ReplicationControllerCondition),
            'fullyLabeledReplicas': (int, None),
            'observedGeneration': (int, None),
            'readyReplicas': (int, None),
            'replicas': (int, None),

        }

    @property
    def available_replicas(self) -> int:
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replication controller.
        """
        return self._properties.get('availableReplicas')

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replication controller.
        """
        self._properties['availableReplicas'] = value

    @property
    def conditions(self) -> typing.List['ReplicationControllerCondition']:
        """
        Represents the latest available observations of a
        replication controller's current state.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['ReplicationControllerCondition'], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        replication controller's current state.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ReplicationControllerCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def fully_labeled_replicas(self) -> int:
        """
        The number of pods that have labels matching the labels of
        the pod template of the replication controller.
        """
        return self._properties.get('fullyLabeledReplicas')

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, value: int):
        """
        The number of pods that have labels matching the labels of
        the pod template of the replication controller.
        """
        self._properties['fullyLabeledReplicas'] = value

    @property
    def observed_generation(self) -> int:
        """
        ObservedGeneration reflects the generation of the most
        recently observed replication controller.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        ObservedGeneration reflects the generation of the most
        recently observed replication controller.
        """
        self._properties['observedGeneration'] = value

    @property
    def ready_replicas(self) -> int:
        """
        The number of ready replicas for this replication
        controller.
        """
        return self._properties.get('readyReplicas')

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        The number of ready replicas for this replication
        controller.
        """
        self._properties['readyReplicas'] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller#what-is-a-
        replicationcontroller
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller#what-is-a-
        replicationcontroller
        """
        self._properties['replicas'] = value

    def __enter__(self) -> 'ReplicationControllerStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceFieldSelector(_kuber_definitions.Definition):
    """
    ResourceFieldSelector represents container resources (cpu,
    memory) and their output format
    """

    def __init__(
            self,
            container_name: str = None,
            divisor: typing.Union[str, int, None] = None,
            resource: str = None,
    ):
        """Create ResourceFieldSelector instance."""
        super(ResourceFieldSelector, self).__init__(
            api_version='core/v1',
            kind='ResourceFieldSelector'
        )
        self._properties = {
            'containerName': container_name or '',
            'divisor': divisor or None,
            'resource': resource or '',

        }
        self._types = {
            'containerName': (str, None),
            'divisor': (str, None),
            'resource': (str, None),

        }

    @property
    def container_name(self) -> str:
        """
        Container name: required for volumes, optional for env vars
        """
        return self._properties.get('containerName')

    @container_name.setter
    def container_name(self, value: str):
        """
        Container name: required for volumes, optional for env vars
        """
        self._properties['containerName'] = value

    @property
    def divisor(self) -> typing.Optional[str]:
        """
        Specifies the output format of the exposed resources,
        defaults to "1"
        """
        value = self._properties.get('divisor')
        return f'{value}' if value is not None else None

    @divisor.setter
    def divisor(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Specifies the output format of the exposed resources,
        defaults to "1"
        """
        self._properties['divisor'] = None if value is None else f'{value}'

    @property
    def resource(self) -> str:
        """
        Required: resource to select
        """
        return self._properties.get('resource')

    @resource.setter
    def resource(self, value: str):
        """
        Required: resource to select
        """
        self._properties['resource'] = value

    def __enter__(self) -> 'ResourceFieldSelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceQuota(_kuber_definitions.Resource):
    """
    ResourceQuota sets aggregate quota restrictions enforced per
    namespace
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ResourceQuotaSpec' = None,
            status: 'ResourceQuotaStatus' = None,
    ):
        """Create ResourceQuota instance."""
        super(ResourceQuota, self).__init__(
            api_version='core/v1',
            kind='ResourceQuota'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ResourceQuotaSpec(),
            'status': status or ResourceQuotaStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (ResourceQuotaSpec, None),
            'status': (ResourceQuotaStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ResourceQuotaSpec':
        """
        Spec defines the desired quota.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ResourceQuotaSpec', dict]):
        """
        Spec defines the desired quota.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ResourceQuotaSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'ResourceQuotaStatus':
        """
        Status defines the actual enforced quota and its current
        usage. https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['ResourceQuotaStatus', dict]):
        """
        Status defines the actual enforced quota and its current
        usage. https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ResourceQuotaStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'ResourceQuotaStatus':
        """
        Creates the ResourceQuota in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_resource_quota',
            'create_resource_quota'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            ResourceQuotaStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'ResourceQuotaStatus':
        """
        Replaces the ResourceQuota in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_resource_quota',
            'replace_resource_quota'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ResourceQuotaStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'ResourceQuotaStatus':
        """
        Patches the ResourceQuota in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_resource_quota',
            'patch_resource_quota'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ResourceQuotaStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'ResourceQuotaStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_resource_quota',
            'read_resource_quota'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            ResourceQuotaStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ResourceQuota from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_resource_quota',
            'read_resource_quota'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the ResourceQuota from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_resource_quota',
            'delete_resource_quota'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ResourceQuota':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceQuotaList(_kuber_definitions.Collection):
    """
    ResourceQuotaList is a list of ResourceQuota items.
    """

    def __init__(
            self,
            items: typing.List['ResourceQuota'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ResourceQuotaList instance."""
        super(ResourceQuotaList, self).__init__(
            api_version='core/v1',
            kind='ResourceQuotaList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ResourceQuota),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ResourceQuota']:
        """
        Items is a list of ResourceQuota objects. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ResourceQuota'], typing.List[dict]]
    ):
        """
        Items is a list of ResourceQuota objects. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ResourceQuota().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ResourceQuotaList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceQuotaSpec(_kuber_definitions.Definition):
    """
    ResourceQuotaSpec defines the desired hard limits to enforce
    for Quota.
    """

    def __init__(
            self,
            hard: dict = None,
            scope_selector: 'ScopeSelector' = None,
            scopes: typing.List[str] = None,
    ):
        """Create ResourceQuotaSpec instance."""
        super(ResourceQuotaSpec, self).__init__(
            api_version='core/v1',
            kind='ResourceQuotaSpec'
        )
        self._properties = {
            'hard': hard or {},
            'scopeSelector': scope_selector or ScopeSelector(),
            'scopes': scopes or [],

        }
        self._types = {
            'hard': (dict, None),
            'scopeSelector': (ScopeSelector, None),
            'scopes': (list, str),

        }

    @property
    def hard(self) -> dict:
        """
        hard is the set of desired hard limits for each named
        resource. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        return self._properties.get('hard')

    @hard.setter
    def hard(self, value: dict):
        """
        hard is the set of desired hard limits for each named
        resource. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        self._properties['hard'] = value

    @property
    def scope_selector(self) -> 'ScopeSelector':
        """
        scopeSelector is also a collection of filters like scopes
        that must match each object tracked by a quota but expressed
        using ScopeSelectorOperator in combination with possible
        values. For a resource to match, both scopes AND
        scopeSelector (if specified in spec), must be matched.
        """
        return self._properties.get('scopeSelector')

    @scope_selector.setter
    def scope_selector(self, value: typing.Union['ScopeSelector', dict]):
        """
        scopeSelector is also a collection of filters like scopes
        that must match each object tracked by a quota but expressed
        using ScopeSelectorOperator in combination with possible
        values. For a resource to match, both scopes AND
        scopeSelector (if specified in spec), must be matched.
        """
        if isinstance(value, dict):
            value = ScopeSelector().from_dict(value)
        self._properties['scopeSelector'] = value

    @property
    def scopes(self) -> typing.List[str]:
        """
        A collection of filters that must match each object tracked
        by a quota. If not specified, the quota matches all objects.
        """
        return self._properties.get('scopes')

    @scopes.setter
    def scopes(self, value: typing.List[str]):
        """
        A collection of filters that must match each object tracked
        by a quota. If not specified, the quota matches all objects.
        """
        self._properties['scopes'] = value

    def __enter__(self) -> 'ResourceQuotaSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceQuotaStatus(_kuber_definitions.Definition):
    """
    ResourceQuotaStatus defines the enforced hard limits and
    observed use.
    """

    def __init__(
            self,
            hard: dict = None,
            used: dict = None,
    ):
        """Create ResourceQuotaStatus instance."""
        super(ResourceQuotaStatus, self).__init__(
            api_version='core/v1',
            kind='ResourceQuotaStatus'
        )
        self._properties = {
            'hard': hard or {},
            'used': used or {},

        }
        self._types = {
            'hard': (dict, None),
            'used': (dict, None),

        }

    @property
    def hard(self) -> dict:
        """
        Hard is the set of enforced hard limits for each named
        resource. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        return self._properties.get('hard')

    @hard.setter
    def hard(self, value: dict):
        """
        Hard is the set of enforced hard limits for each named
        resource. More info:
        https://kubernetes.io/docs/concepts/policy/resource-quotas/
        """
        self._properties['hard'] = value

    @property
    def used(self) -> dict:
        """
        Used is the current observed total usage of the resource in
        the namespace.
        """
        return self._properties.get('used')

    @used.setter
    def used(self, value: dict):
        """
        Used is the current observed total usage of the resource in
        the namespace.
        """
        self._properties['used'] = value

    def __enter__(self) -> 'ResourceQuotaStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceRequirements(_kuber_definitions.Definition):
    """
    ResourceRequirements describes the compute resource
    requirements.
    """

    def __init__(
            self,
            limits: dict = None,
            requests: dict = None,
    ):
        """Create ResourceRequirements instance."""
        super(ResourceRequirements, self).__init__(
            api_version='core/v1',
            kind='ResourceRequirements'
        )
        self._properties = {
            'limits': limits or {},
            'requests': requests or {},

        }
        self._types = {
            'limits': (dict, None),
            'requests': (dict, None),

        }

    @property
    def limits(self) -> dict:
        """
        Limits describes the maximum amount of compute resources
        allowed. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        return self._properties.get('limits')

    @limits.setter
    def limits(self, value: dict):
        """
        Limits describes the maximum amount of compute resources
        allowed. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        self._properties['limits'] = value

    @property
    def requests(self) -> dict:
        """
        Requests describes the minimum amount of compute resources
        required. If Requests is omitted for a container, it
        defaults to Limits if that is explicitly specified,
        otherwise to an implementation-defined value. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        return self._properties.get('requests')

    @requests.setter
    def requests(self, value: dict):
        """
        Requests describes the minimum amount of compute resources
        required. If Requests is omitted for a container, it
        defaults to Limits if that is explicitly specified,
        otherwise to an implementation-defined value. More info:
        https://kubernetes.io/docs/concepts/configuration/manage-
        compute-resources-container/
        """
        self._properties['requests'] = value

    def __enter__(self) -> 'ResourceRequirements':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SELinuxOptions(_kuber_definitions.Definition):
    """
    SELinuxOptions are the labels to be applied to the container
    """

    def __init__(
            self,
            level: str = None,
            role: str = None,
            type_: str = None,
            user: str = None,
    ):
        """Create SELinuxOptions instance."""
        super(SELinuxOptions, self).__init__(
            api_version='core/v1',
            kind='SELinuxOptions'
        )
        self._properties = {
            'level': level or '',
            'role': role or '',
            'type': type_ or '',
            'user': user or '',

        }
        self._types = {
            'level': (str, None),
            'role': (str, None),
            'type': (str, None),
            'user': (str, None),

        }

    @property
    def level(self) -> str:
        """
        Level is SELinux level label that applies to the container.
        """
        return self._properties.get('level')

    @level.setter
    def level(self, value: str):
        """
        Level is SELinux level label that applies to the container.
        """
        self._properties['level'] = value

    @property
    def role(self) -> str:
        """
        Role is a SELinux role label that applies to the container.
        """
        return self._properties.get('role')

    @role.setter
    def role(self, value: str):
        """
        Role is a SELinux role label that applies to the container.
        """
        self._properties['role'] = value

    @property
    def type_(self) -> str:
        """
        Type is a SELinux type label that applies to the container.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type is a SELinux type label that applies to the container.
        """
        self._properties['type'] = value

    @property
    def user(self) -> str:
        """
        User is a SELinux user label that applies to the container.
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        User is a SELinux user label that applies to the container.
        """
        self._properties['user'] = value

    def __enter__(self) -> 'SELinuxOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleIOPersistentVolumeSource(_kuber_definitions.Definition):
    """
    ScaleIOPersistentVolumeSource represents a persistent
    ScaleIO volume
    """

    def __init__(
            self,
            fs_type: str = None,
            gateway: str = None,
            protection_domain: str = None,
            read_only: bool = None,
            secret_ref: 'SecretReference' = None,
            ssl_enabled: bool = None,
            storage_mode: str = None,
            storage_pool: str = None,
            system: str = None,
            volume_name: str = None,
    ):
        """Create ScaleIOPersistentVolumeSource instance."""
        super(ScaleIOPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ScaleIOPersistentVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'gateway': gateway or '',
            'protectionDomain': protection_domain or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or SecretReference(),
            'sslEnabled': ssl_enabled or None,
            'storageMode': storage_mode or '',
            'storagePool': storage_pool or '',
            'system': system or '',
            'volumeName': volume_name or '',

        }
        self._types = {
            'fsType': (str, None),
            'gateway': (str, None),
            'protectionDomain': (str, None),
            'readOnly': (bool, None),
            'secretRef': (SecretReference, None),
            'sslEnabled': (bool, None),
            'storageMode': (str, None),
            'storagePool': (str, None),
            'system': (str, None),
            'volumeName': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Default is "xfs"
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Default is "xfs"
        """
        self._properties['fsType'] = value

    @property
    def gateway(self) -> str:
        """
        The host address of the ScaleIO API Gateway.
        """
        return self._properties.get('gateway')

    @gateway.setter
    def gateway(self, value: str):
        """
        The host address of the ScaleIO API Gateway.
        """
        self._properties['gateway'] = value

    @property
    def protection_domain(self) -> str:
        """
        The name of the ScaleIO Protection Domain for the configured
        storage.
        """
        return self._properties.get('protectionDomain')

    @protection_domain.setter
    def protection_domain(self, value: str):
        """
        The name of the ScaleIO Protection Domain for the configured
        storage.
        """
        self._properties['protectionDomain'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'SecretReference':
        """
        SecretRef references to the secret for ScaleIO user and
        other sensitive information. If this is not provided, Login
        operation will fail.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['SecretReference', dict]):
        """
        SecretRef references to the secret for ScaleIO user and
        other sensitive information. If this is not provided, Login
        operation will fail.
        """
        if isinstance(value, dict):
            value = SecretReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def ssl_enabled(self) -> bool:
        """
        Flag to enable/disable SSL communication with Gateway,
        default false
        """
        return self._properties.get('sslEnabled')

    @ssl_enabled.setter
    def ssl_enabled(self, value: bool):
        """
        Flag to enable/disable SSL communication with Gateway,
        default false
        """
        self._properties['sslEnabled'] = value

    @property
    def storage_mode(self) -> str:
        """
        Indicates whether the storage for a volume should be
        ThickProvisioned or ThinProvisioned. Default is
        ThinProvisioned.
        """
        return self._properties.get('storageMode')

    @storage_mode.setter
    def storage_mode(self, value: str):
        """
        Indicates whether the storage for a volume should be
        ThickProvisioned or ThinProvisioned. Default is
        ThinProvisioned.
        """
        self._properties['storageMode'] = value

    @property
    def storage_pool(self) -> str:
        """
        The ScaleIO Storage Pool associated with the protection
        domain.
        """
        return self._properties.get('storagePool')

    @storage_pool.setter
    def storage_pool(self, value: str):
        """
        The ScaleIO Storage Pool associated with the protection
        domain.
        """
        self._properties['storagePool'] = value

    @property
    def system(self) -> str:
        """
        The name of the storage system as configured in ScaleIO.
        """
        return self._properties.get('system')

    @system.setter
    def system(self, value: str):
        """
        The name of the storage system as configured in ScaleIO.
        """
        self._properties['system'] = value

    @property
    def volume_name(self) -> str:
        """
        The name of a volume already created in the ScaleIO system
        that is associated with this volume source.
        """
        return self._properties.get('volumeName')

    @volume_name.setter
    def volume_name(self, value: str):
        """
        The name of a volume already created in the ScaleIO system
        that is associated with this volume source.
        """
        self._properties['volumeName'] = value

    def __enter__(self) -> 'ScaleIOPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleIOVolumeSource(_kuber_definitions.Definition):
    """
    ScaleIOVolumeSource represents a persistent ScaleIO volume
    """

    def __init__(
            self,
            fs_type: str = None,
            gateway: str = None,
            protection_domain: str = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
            ssl_enabled: bool = None,
            storage_mode: str = None,
            storage_pool: str = None,
            system: str = None,
            volume_name: str = None,
    ):
        """Create ScaleIOVolumeSource instance."""
        super(ScaleIOVolumeSource, self).__init__(
            api_version='core/v1',
            kind='ScaleIOVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'gateway': gateway or '',
            'protectionDomain': protection_domain or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),
            'sslEnabled': ssl_enabled or None,
            'storageMode': storage_mode or '',
            'storagePool': storage_pool or '',
            'system': system or '',
            'volumeName': volume_name or '',

        }
        self._types = {
            'fsType': (str, None),
            'gateway': (str, None),
            'protectionDomain': (str, None),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),
            'sslEnabled': (bool, None),
            'storageMode': (str, None),
            'storagePool': (str, None),
            'system': (str, None),
            'volumeName': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Default is "xfs".
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Default is "xfs".
        """
        self._properties['fsType'] = value

    @property
    def gateway(self) -> str:
        """
        The host address of the ScaleIO API Gateway.
        """
        return self._properties.get('gateway')

    @gateway.setter
    def gateway(self, value: str):
        """
        The host address of the ScaleIO API Gateway.
        """
        self._properties['gateway'] = value

    @property
    def protection_domain(self) -> str:
        """
        The name of the ScaleIO Protection Domain for the configured
        storage.
        """
        return self._properties.get('protectionDomain')

    @protection_domain.setter
    def protection_domain(self, value: str):
        """
        The name of the ScaleIO Protection Domain for the configured
        storage.
        """
        self._properties['protectionDomain'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        SecretRef references to the secret for ScaleIO user and
        other sensitive information. If this is not provided, Login
        operation will fail.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        SecretRef references to the secret for ScaleIO user and
        other sensitive information. If this is not provided, Login
        operation will fail.
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def ssl_enabled(self) -> bool:
        """
        Flag to enable/disable SSL communication with Gateway,
        default false
        """
        return self._properties.get('sslEnabled')

    @ssl_enabled.setter
    def ssl_enabled(self, value: bool):
        """
        Flag to enable/disable SSL communication with Gateway,
        default false
        """
        self._properties['sslEnabled'] = value

    @property
    def storage_mode(self) -> str:
        """
        Indicates whether the storage for a volume should be
        ThickProvisioned or ThinProvisioned. Default is
        ThinProvisioned.
        """
        return self._properties.get('storageMode')

    @storage_mode.setter
    def storage_mode(self, value: str):
        """
        Indicates whether the storage for a volume should be
        ThickProvisioned or ThinProvisioned. Default is
        ThinProvisioned.
        """
        self._properties['storageMode'] = value

    @property
    def storage_pool(self) -> str:
        """
        The ScaleIO Storage Pool associated with the protection
        domain.
        """
        return self._properties.get('storagePool')

    @storage_pool.setter
    def storage_pool(self, value: str):
        """
        The ScaleIO Storage Pool associated with the protection
        domain.
        """
        self._properties['storagePool'] = value

    @property
    def system(self) -> str:
        """
        The name of the storage system as configured in ScaleIO.
        """
        return self._properties.get('system')

    @system.setter
    def system(self, value: str):
        """
        The name of the storage system as configured in ScaleIO.
        """
        self._properties['system'] = value

    @property
    def volume_name(self) -> str:
        """
        The name of a volume already created in the ScaleIO system
        that is associated with this volume source.
        """
        return self._properties.get('volumeName')

    @volume_name.setter
    def volume_name(self, value: str):
        """
        The name of a volume already created in the ScaleIO system
        that is associated with this volume source.
        """
        self._properties['volumeName'] = value

    def __enter__(self) -> 'ScaleIOVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScopeSelector(_kuber_definitions.Definition):
    """
    A scope selector represents the AND of the selectors
    represented by the scoped-resource selector requirements.
    """

    def __init__(
            self,
            match_expressions: typing.List['ScopedResourceSelectorRequirement'] = None,
    ):
        """Create ScopeSelector instance."""
        super(ScopeSelector, self).__init__(
            api_version='core/v1',
            kind='ScopeSelector'
        )
        self._properties = {
            'matchExpressions': match_expressions or [],

        }
        self._types = {
            'matchExpressions': (list, ScopedResourceSelectorRequirement),

        }

    @property
    def match_expressions(self) -> typing.List['ScopedResourceSelectorRequirement']:
        """
        A list of scope selector requirements by scope of the
        resources.
        """
        return self._properties.get('matchExpressions')

    @match_expressions.setter
    def match_expressions(
            self,
            value: typing.Union[typing.List['ScopedResourceSelectorRequirement'], typing.List[dict]]
    ):
        """
        A list of scope selector requirements by scope of the
        resources.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ScopedResourceSelectorRequirement().from_dict(item)
            cleaned.append(item)
        self._properties['matchExpressions'] = cleaned

    def __enter__(self) -> 'ScopeSelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScopedResourceSelectorRequirement(_kuber_definitions.Definition):
    """
    A scoped-resource selector requirement is a selector that
    contains values, a scope name, and an operator that relates
    the scope name and values.
    """

    def __init__(
            self,
            operator: str = None,
            scope_name: str = None,
            values: typing.List[str] = None,
    ):
        """Create ScopedResourceSelectorRequirement instance."""
        super(ScopedResourceSelectorRequirement, self).__init__(
            api_version='core/v1',
            kind='ScopedResourceSelectorRequirement'
        )
        self._properties = {
            'operator': operator or '',
            'scopeName': scope_name or '',
            'values': values or [],

        }
        self._types = {
            'operator': (str, None),
            'scopeName': (str, None),
            'values': (list, str),

        }

    @property
    def operator(self) -> str:
        """
        Represents a scope's relationship to a set of values. Valid
        operators are In, NotIn, Exists, DoesNotExist.
        """
        return self._properties.get('operator')

    @operator.setter
    def operator(self, value: str):
        """
        Represents a scope's relationship to a set of values. Valid
        operators are In, NotIn, Exists, DoesNotExist.
        """
        self._properties['operator'] = value

    @property
    def scope_name(self) -> str:
        """
        The name of the scope that the selector applies to.
        """
        return self._properties.get('scopeName')

    @scope_name.setter
    def scope_name(self, value: str):
        """
        The name of the scope that the selector applies to.
        """
        self._properties['scopeName'] = value

    @property
    def values(self) -> typing.List[str]:
        """
        An array of string values. If the operator is In or NotIn,
        the values array must be non-empty. If the operator is
        Exists or DoesNotExist, the values array must be empty. This
        array is replaced during a strategic merge patch.
        """
        return self._properties.get('values')

    @values.setter
    def values(self, value: typing.List[str]):
        """
        An array of string values. If the operator is In or NotIn,
        the values array must be non-empty. If the operator is
        Exists or DoesNotExist, the values array must be empty. This
        array is replaced during a strategic merge patch.
        """
        self._properties['values'] = value

    def __enter__(self) -> 'ScopedResourceSelectorRequirement':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Secret(_kuber_definitions.Resource):
    """
    Secret holds secret data of a certain type. The total bytes
    of the values in the Data field must be less than
    MaxSecretSize bytes.
    """

    def __init__(
            self,
            data: dict = None,
            metadata: 'ObjectMeta' = None,
            string_data: dict = None,
            type_: str = None,
    ):
        """Create Secret instance."""
        super(Secret, self).__init__(
            api_version='core/v1',
            kind='Secret'
        )
        self._properties = {
            'data': data or {},
            'metadata': metadata or ObjectMeta(),
            'stringData': string_data or {},
            'type': type_ or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'data': (dict, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'stringData': (dict, None),
            'type': (str, None),

        }

    @property
    def data(self) -> dict:
        """
        Data contains the secret data. Each key must consist of
        alphanumeric characters, '-', '_' or '.'. The serialized
        form of the secret data is a base64 encoded string,
        representing the arbitrary (possibly non-string) data value
        here. Described in
        https://tools.ietf.org/html/rfc4648#section-4
        """
        return self._properties.get('data')

    @data.setter
    def data(self, value: dict):
        """
        Data contains the secret data. Each key must consist of
        alphanumeric characters, '-', '_' or '.'. The serialized
        form of the secret data is a base64 encoded string,
        representing the arbitrary (possibly non-string) data value
        here. Described in
        https://tools.ietf.org/html/rfc4648#section-4
        """
        self._properties['data'] = value

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def string_data(self) -> dict:
        """
        stringData allows specifying non-binary secret data in
        string form. It is provided as a write-only convenience
        method. All keys and values are merged into the data field
        on write, overwriting any existing values. It is never
        output when reading from the API.
        """
        return self._properties.get('stringData')

    @string_data.setter
    def string_data(self, value: dict):
        """
        stringData allows specifying non-binary secret data in
        string form. It is provided as a write-only convenience
        method. All keys and values are merged into the data field
        on write, overwriting any existing values. It is never
        output when reading from the API.
        """
        self._properties['stringData'] = value

    @property
    def type_(self) -> str:
        """
        Used to facilitate programmatic handling of secret data.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Used to facilitate programmatic handling of secret data.
        """
        self._properties['type'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Secret in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_secret',
            'create_secret'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the Secret in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_secret',
            'replace_secret'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the Secret in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_secret',
            'patch_secret'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Secret from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_secret',
            'read_secret'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Secret from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_secret',
            'delete_secret'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Secret':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretEnvSource(_kuber_definitions.Definition):
    """
    SecretEnvSource selects a Secret to populate the environment
    variables with.

    The contents of the target Secret's Data
    field will represent the key-value pairs as environment
    variables.
    """

    def __init__(
            self,
            name: str = None,
            optional: bool = None,
    ):
        """Create SecretEnvSource instance."""
        super(SecretEnvSource, self).__init__(
            api_version='core/v1',
            kind='SecretEnvSource'
        )
        self._properties = {
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the Secret must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the Secret must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'SecretEnvSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretKeySelector(_kuber_definitions.Definition):
    """
    SecretKeySelector selects a key of a Secret.
    """

    def __init__(
            self,
            key: str = None,
            name: str = None,
            optional: bool = None,
    ):
        """Create SecretKeySelector instance."""
        super(SecretKeySelector, self).__init__(
            api_version='core/v1',
            kind='SecretKeySelector'
        )
        self._properties = {
            'key': key or '',
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'key': (str, None),
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def key(self) -> str:
        """
        The key of the secret to select from.  Must be a valid
        secret key.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        The key of the secret to select from.  Must be a valid
        secret key.
        """
        self._properties['key'] = value

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the Secret or it's key must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the Secret or it's key must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'SecretKeySelector':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretList(_kuber_definitions.Collection):
    """
    SecretList is a list of Secret.
    """

    def __init__(
            self,
            items: typing.List['Secret'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create SecretList instance."""
        super(SecretList, self).__init__(
            api_version='core/v1',
            kind='SecretList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Secret),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Secret']:
        """
        Items is a list of secret objects. More info:
        https://kubernetes.io/docs/concepts/configuration/secret
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Secret'], typing.List[dict]]
    ):
        """
        Items is a list of secret objects. More info:
        https://kubernetes.io/docs/concepts/configuration/secret
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Secret().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'SecretList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretProjection(_kuber_definitions.Definition):
    """
    Adapts a secret into a projected volume.

    The contents of
    the target Secret's Data field will be presented in a
    projected volume as files using the keys in the Data field
    as the file names. Note that this is identical to a secret
    volume source without the default mode.
    """

    def __init__(
            self,
            items: typing.List['KeyToPath'] = None,
            name: str = None,
            optional: bool = None,
    ):
        """Create SecretProjection instance."""
        super(SecretProjection, self).__init__(
            api_version='core/v1',
            kind='SecretProjection'
        )
        self._properties = {
            'items': items or [],
            'name': name or '',
            'optional': optional or None,

        }
        self._types = {
            'items': (list, KeyToPath),
            'name': (str, None),
            'optional': (bool, None),

        }

    @property
    def items(self) -> typing.List['KeyToPath']:
        """
        If unspecified, each key-value pair in the Data field of the
        referenced Secret will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the Secret, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['KeyToPath'], typing.List[dict]]
    ):
        """
        If unspecified, each key-value pair in the Data field of the
        referenced Secret will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the Secret, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = KeyToPath().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def optional(self) -> bool:
        """
        Specify whether the Secret or its key must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the Secret or its key must be defined
        """
        self._properties['optional'] = value

    def __enter__(self) -> 'SecretProjection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretReference(_kuber_definitions.Definition):
    """
    SecretReference represents a Secret Reference. It has enough
    information to retrieve secret in any namespace
    """

    def __init__(
            self,
            name: str = None,
            namespace: str = None,
    ):
        """Create SecretReference instance."""
        super(SecretReference, self).__init__(
            api_version='core/v1',
            kind='SecretReference'
        )
        self._properties = {
            'name': name or '',
            'namespace': namespace or '',

        }
        self._types = {
            'name': (str, None),
            'namespace': (str, None),

        }

    @property
    def name(self) -> str:
        """
        Name is unique within a namespace to reference a secret
        resource.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is unique within a namespace to reference a secret
        resource.
        """
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        Namespace defines the space within which the secret name
        must be unique.
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace defines the space within which the secret name
        must be unique.
        """
        self._properties['namespace'] = value

    def __enter__(self) -> 'SecretReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecretVolumeSource(_kuber_definitions.Definition):
    """
    Adapts a Secret into a volume.

    The contents of the target
    Secret's Data field will be presented in a volume as files
    using the keys in the Data field as the file names. Secret
    volumes support ownership management and SELinux relabeling.
    """

    def __init__(
            self,
            default_mode: int = None,
            items: typing.List['KeyToPath'] = None,
            optional: bool = None,
            secret_name: str = None,
    ):
        """Create SecretVolumeSource instance."""
        super(SecretVolumeSource, self).__init__(
            api_version='core/v1',
            kind='SecretVolumeSource'
        )
        self._properties = {
            'defaultMode': default_mode or None,
            'items': items or [],
            'optional': optional or None,
            'secretName': secret_name or '',

        }
        self._types = {
            'defaultMode': (int, None),
            'items': (list, KeyToPath),
            'optional': (bool, None),
            'secretName': (str, None),

        }

    @property
    def default_mode(self) -> int:
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        return self._properties.get('defaultMode')

    @default_mode.setter
    def default_mode(self, value: int):
        """
        Optional: mode bits to use on created files by default. Must
        be a value between 0 and 0777. Defaults to 0644. Directories
        within the path are not affected by this setting. This might
        be in conflict with other options that affect the file mode,
        like fsGroup, and the result can be other mode bits set.
        """
        self._properties['defaultMode'] = value

    @property
    def items(self) -> typing.List['KeyToPath']:
        """
        If unspecified, each key-value pair in the Data field of the
        referenced Secret will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the Secret, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['KeyToPath'], typing.List[dict]]
    ):
        """
        If unspecified, each key-value pair in the Data field of the
        referenced Secret will be projected into the volume as a
        file whose name is the key and content is the value. If
        specified, the listed keys will be projected into the
        specified paths, and unlisted keys will not be present. If a
        key is specified which is not present in the Secret, the
        volume setup will error unless it is marked optional. Paths
        must be relative and may not contain the '..' path or start
        with '..'.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = KeyToPath().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def optional(self) -> bool:
        """
        Specify whether the Secret or it's keys must be defined
        """
        return self._properties.get('optional')

    @optional.setter
    def optional(self, value: bool):
        """
        Specify whether the Secret or it's keys must be defined
        """
        self._properties['optional'] = value

    @property
    def secret_name(self) -> str:
        """
        Name of the secret in the pod's namespace to use. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#secret
        """
        return self._properties.get('secretName')

    @secret_name.setter
    def secret_name(self, value: str):
        """
        Name of the secret in the pod's namespace to use. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#secret
        """
        self._properties['secretName'] = value

    def __enter__(self) -> 'SecretVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SecurityContext(_kuber_definitions.Definition):
    """
    SecurityContext holds security configuration that will be
    applied to a container. Some fields are present in both
    SecurityContext and PodSecurityContext.  When both are set,
    the values in SecurityContext take precedence.
    """

    def __init__(
            self,
            allow_privilege_escalation: bool = None,
            capabilities: 'Capabilities' = None,
            privileged: bool = None,
            proc_mount: str = None,
            read_only_root_filesystem: bool = None,
            run_as_group: int = None,
            run_as_non_root: bool = None,
            run_as_user: int = None,
            se_linux_options: 'SELinuxOptions' = None,
    ):
        """Create SecurityContext instance."""
        super(SecurityContext, self).__init__(
            api_version='core/v1',
            kind='SecurityContext'
        )
        self._properties = {
            'allowPrivilegeEscalation': allow_privilege_escalation or None,
            'capabilities': capabilities or Capabilities(),
            'privileged': privileged or None,
            'procMount': proc_mount or '',
            'readOnlyRootFilesystem': read_only_root_filesystem or None,
            'runAsGroup': run_as_group or None,
            'runAsNonRoot': run_as_non_root or None,
            'runAsUser': run_as_user or None,
            'seLinuxOptions': se_linux_options or SELinuxOptions(),

        }
        self._types = {
            'allowPrivilegeEscalation': (bool, None),
            'capabilities': (Capabilities, None),
            'privileged': (bool, None),
            'procMount': (str, None),
            'readOnlyRootFilesystem': (bool, None),
            'runAsGroup': (int, None),
            'runAsNonRoot': (bool, None),
            'runAsUser': (int, None),
            'seLinuxOptions': (SELinuxOptions, None),

        }

    @property
    def allow_privilege_escalation(self) -> bool:
        """
        AllowPrivilegeEscalation controls whether a process can gain
        more privileges than its parent process. This bool directly
        controls if the no_new_privs flag will be set on the
        container process. AllowPrivilegeEscalation is true always
        when the container is: 1) run as Privileged 2) has
        CAP_SYS_ADMIN
        """
        return self._properties.get('allowPrivilegeEscalation')

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, value: bool):
        """
        AllowPrivilegeEscalation controls whether a process can gain
        more privileges than its parent process. This bool directly
        controls if the no_new_privs flag will be set on the
        container process. AllowPrivilegeEscalation is true always
        when the container is: 1) run as Privileged 2) has
        CAP_SYS_ADMIN
        """
        self._properties['allowPrivilegeEscalation'] = value

    @property
    def capabilities(self) -> 'Capabilities':
        """
        The capabilities to add/drop when running containers.
        Defaults to the default set of capabilities granted by the
        container runtime.
        """
        return self._properties.get('capabilities')

    @capabilities.setter
    def capabilities(self, value: typing.Union['Capabilities', dict]):
        """
        The capabilities to add/drop when running containers.
        Defaults to the default set of capabilities granted by the
        container runtime.
        """
        if isinstance(value, dict):
            value = Capabilities().from_dict(value)
        self._properties['capabilities'] = value

    @property
    def privileged(self) -> bool:
        """
        Run container in privileged mode. Processes in privileged
        containers are essentially equivalent to root on the host.
        Defaults to false.
        """
        return self._properties.get('privileged')

    @privileged.setter
    def privileged(self, value: bool):
        """
        Run container in privileged mode. Processes in privileged
        containers are essentially equivalent to root on the host.
        Defaults to false.
        """
        self._properties['privileged'] = value

    @property
    def proc_mount(self) -> str:
        """
        procMount denotes the type of proc mount to use for the
        containers. The default is DefaultProcMount which uses the
        container runtime defaults for readonly paths and masked
        paths. This requires the ProcMountType feature flag to be
        enabled.
        """
        return self._properties.get('procMount')

    @proc_mount.setter
    def proc_mount(self, value: str):
        """
        procMount denotes the type of proc mount to use for the
        containers. The default is DefaultProcMount which uses the
        container runtime defaults for readonly paths and masked
        paths. This requires the ProcMountType feature flag to be
        enabled.
        """
        self._properties['procMount'] = value

    @property
    def read_only_root_filesystem(self) -> bool:
        """
        Whether this container has a read-only root filesystem.
        Default is false.
        """
        return self._properties.get('readOnlyRootFilesystem')

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, value: bool):
        """
        Whether this container has a read-only root filesystem.
        Default is false.
        """
        self._properties['readOnlyRootFilesystem'] = value

    @property
    def run_as_group(self) -> int:
        """
        The GID to run the entrypoint of the container process. Uses
        runtime default if unset. May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        return self._properties.get('runAsGroup')

    @run_as_group.setter
    def run_as_group(self, value: int):
        """
        The GID to run the entrypoint of the container process. Uses
        runtime default if unset. May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        self._properties['runAsGroup'] = value

    @property
    def run_as_non_root(self) -> bool:
        """
        Indicates that the container must run as a non-root user. If
        true, the Kubelet will validate the image at runtime to
        ensure that it does not run as UID 0 (root) and fail to
        start the container if it does. If unset or false, no such
        validation will be performed. May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        return self._properties.get('runAsNonRoot')

    @run_as_non_root.setter
    def run_as_non_root(self, value: bool):
        """
        Indicates that the container must run as a non-root user. If
        true, the Kubelet will validate the image at runtime to
        ensure that it does not run as UID 0 (root) and fail to
        start the container if it does. If unset or false, no such
        validation will be performed. May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        self._properties['runAsNonRoot'] = value

    @property
    def run_as_user(self) -> int:
        """
        The UID to run the entrypoint of the container process.
        Defaults to user specified in image metadata if unspecified.
        May also be set in PodSecurityContext.  If set in both
        SecurityContext and PodSecurityContext, the value specified
        in SecurityContext takes precedence.
        """
        return self._properties.get('runAsUser')

    @run_as_user.setter
    def run_as_user(self, value: int):
        """
        The UID to run the entrypoint of the container process.
        Defaults to user specified in image metadata if unspecified.
        May also be set in PodSecurityContext.  If set in both
        SecurityContext and PodSecurityContext, the value specified
        in SecurityContext takes precedence.
        """
        self._properties['runAsUser'] = value

    @property
    def se_linux_options(self) -> 'SELinuxOptions':
        """
        The SELinux context to be applied to the container. If
        unspecified, the container runtime will allocate a random
        SELinux context for each container.  May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        return self._properties.get('seLinuxOptions')

    @se_linux_options.setter
    def se_linux_options(self, value: typing.Union['SELinuxOptions', dict]):
        """
        The SELinux context to be applied to the container. If
        unspecified, the container runtime will allocate a random
        SELinux context for each container.  May also be set in
        PodSecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext
        takes precedence.
        """
        if isinstance(value, dict):
            value = SELinuxOptions().from_dict(value)
        self._properties['seLinuxOptions'] = value

    def __enter__(self) -> 'SecurityContext':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Service(_kuber_definitions.Resource):
    """
    Service is a named abstraction of software service (for
    example, mysql) consisting of local port (for example 3306)
    that the proxy listens on, and the selector that determines
    which pods will answer requests sent through the proxy.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ServiceSpec' = None,
            status: 'ServiceStatus' = None,
    ):
        """Create Service instance."""
        super(Service, self).__init__(
            api_version='core/v1',
            kind='Service'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ServiceSpec(),
            'status': status or ServiceStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (ServiceSpec, None),
            'status': (ServiceStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ServiceSpec':
        """
        Spec defines the behavior of a service.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ServiceSpec', dict]):
        """
        Spec defines the behavior of a service.
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ServiceSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'ServiceStatus':
        """
        Most recently observed status of the service. Populated by
        the system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['ServiceStatus', dict]):
        """
        Most recently observed status of the service. Populated by
        the system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ServiceStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'ServiceStatus':
        """
        Creates the Service in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_service',
            'create_service'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            ServiceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'ServiceStatus':
        """
        Replaces the Service in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_service',
            'replace_service'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ServiceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'ServiceStatus':
        """
        Patches the Service in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_service',
            'patch_service'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            ServiceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'ServiceStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_service',
            'read_service'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            ServiceStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Service from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_service',
            'read_service'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the Service from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_service',
            'delete_service'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'Service':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceAccount(_kuber_definitions.Resource):
    """
    ServiceAccount binds together: * a name, understood by
    users, and perhaps by peripheral systems, for an identity *
    a principal that can be authenticated and authorized * a set
    of secrets
    """

    def __init__(
            self,
            automount_service_account_token: bool = None,
            image_pull_secrets: typing.List['LocalObjectReference'] = None,
            metadata: 'ObjectMeta' = None,
            secrets: typing.List['ObjectReference'] = None,
    ):
        """Create ServiceAccount instance."""
        super(ServiceAccount, self).__init__(
            api_version='core/v1',
            kind='ServiceAccount'
        )
        self._properties = {
            'automountServiceAccountToken': automount_service_account_token or None,
            'imagePullSecrets': image_pull_secrets or [],
            'metadata': metadata or ObjectMeta(),
            'secrets': secrets or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'automountServiceAccountToken': (bool, None),
            'imagePullSecrets': (list, LocalObjectReference),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'secrets': (list, ObjectReference),

        }

    @property
    def automount_service_account_token(self) -> bool:
        """
        AutomountServiceAccountToken indicates whether pods running
        as this service account should have an API token
        automatically mounted. Can be overridden at the pod level.
        """
        return self._properties.get('automountServiceAccountToken')

    @automount_service_account_token.setter
    def automount_service_account_token(self, value: bool):
        """
        AutomountServiceAccountToken indicates whether pods running
        as this service account should have an API token
        automatically mounted. Can be overridden at the pod level.
        """
        self._properties['automountServiceAccountToken'] = value

    @property
    def image_pull_secrets(self) -> typing.List['LocalObjectReference']:
        """
        ImagePullSecrets is a list of references to secrets in the
        same namespace to use for pulling any images in pods that
        reference this ServiceAccount. ImagePullSecrets are distinct
        from Secrets because Secrets can be mounted in the pod, but
        ImagePullSecrets are only accessed by the kubelet. More
        info: https://kubernetes.io/docs/concepts/containers/images/
        #specifying-imagepullsecrets-on-a-pod
        """
        return self._properties.get('imagePullSecrets')

    @image_pull_secrets.setter
    def image_pull_secrets(
            self,
            value: typing.Union[typing.List['LocalObjectReference'], typing.List[dict]]
    ):
        """
        ImagePullSecrets is a list of references to secrets in the
        same namespace to use for pulling any images in pods that
        reference this ServiceAccount. ImagePullSecrets are distinct
        from Secrets because Secrets can be mounted in the pod, but
        ImagePullSecrets are only accessed by the kubelet. More
        info: https://kubernetes.io/docs/concepts/containers/images/
        #specifying-imagepullsecrets-on-a-pod
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LocalObjectReference().from_dict(item)
            cleaned.append(item)
        self._properties['imagePullSecrets'] = cleaned

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def secrets(self) -> typing.List['ObjectReference']:
        """
        Secrets is the list of secrets allowed to be used by pods
        running using this ServiceAccount. More info:
        https://kubernetes.io/docs/concepts/configuration/secret
        """
        return self._properties.get('secrets')

    @secrets.setter
    def secrets(
            self,
            value: typing.Union[typing.List['ObjectReference'], typing.List[dict]]
    ):
        """
        Secrets is the list of secrets allowed to be used by pods
        running using this ServiceAccount. More info:
        https://kubernetes.io/docs/concepts/configuration/secret
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ObjectReference().from_dict(item)
            cleaned.append(item)
        self._properties['secrets'] = cleaned

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the ServiceAccount in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_service_account',
            'create_service_account'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the ServiceAccount in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_service_account',
            'replace_service_account'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the ServiceAccount in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_service_account',
            'patch_service_account'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ServiceAccount from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_service_account',
            'read_service_account'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the ServiceAccount from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_service_account',
            'delete_service_account'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ServiceAccount':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceAccountList(_kuber_definitions.Collection):
    """
    ServiceAccountList is a list of ServiceAccount objects
    """

    def __init__(
            self,
            items: typing.List['ServiceAccount'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ServiceAccountList instance."""
        super(ServiceAccountList, self).__init__(
            api_version='core/v1',
            kind='ServiceAccountList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ServiceAccount),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ServiceAccount']:
        """
        List of ServiceAccounts. More info:
        https://kubernetes.io/docs/tasks/configure-pod-
        container/configure-service-account/
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ServiceAccount'], typing.List[dict]]
    ):
        """
        List of ServiceAccounts. More info:
        https://kubernetes.io/docs/tasks/configure-pod-
        container/configure-service-account/
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ServiceAccount().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ServiceAccountList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceAccountTokenProjection(_kuber_definitions.Definition):
    """
    ServiceAccountTokenProjection represents a projected service
    account token volume. This projection can be used to insert
    a service account token into the pods runtime filesystem for
    use against APIs (Kubernetes API Server or otherwise).
    """

    def __init__(
            self,
            audience: str = None,
            expiration_seconds: int = None,
            path: str = None,
    ):
        """Create ServiceAccountTokenProjection instance."""
        super(ServiceAccountTokenProjection, self).__init__(
            api_version='core/v1',
            kind='ServiceAccountTokenProjection'
        )
        self._properties = {
            'audience': audience or '',
            'expirationSeconds': expiration_seconds or None,
            'path': path or '',

        }
        self._types = {
            'audience': (str, None),
            'expirationSeconds': (int, None),
            'path': (str, None),

        }

    @property
    def audience(self) -> str:
        """
        Audience is the intended audience of the token. A recipient
        of a token must identify itself with an identifier specified
        in the audience of the token, and otherwise should reject
        the token. The audience defaults to the identifier of the
        apiserver.
        """
        return self._properties.get('audience')

    @audience.setter
    def audience(self, value: str):
        """
        Audience is the intended audience of the token. A recipient
        of a token must identify itself with an identifier specified
        in the audience of the token, and otherwise should reject
        the token. The audience defaults to the identifier of the
        apiserver.
        """
        self._properties['audience'] = value

    @property
    def expiration_seconds(self) -> int:
        """
        ExpirationSeconds is the requested duration of validity of
        the service account token. As the token approaches
        expiration, the kubelet volume plugin will proactively
        rotate the service account token. The kubelet will start
        trying to rotate the token if the token is older than 80
        percent of its time to live or if the token is older than 24
        hours.Defaults to 1 hour and must be at least 10 minutes.
        """
        return self._properties.get('expirationSeconds')

    @expiration_seconds.setter
    def expiration_seconds(self, value: int):
        """
        ExpirationSeconds is the requested duration of validity of
        the service account token. As the token approaches
        expiration, the kubelet volume plugin will proactively
        rotate the service account token. The kubelet will start
        trying to rotate the token if the token is older than 80
        percent of its time to live or if the token is older than 24
        hours.Defaults to 1 hour and must be at least 10 minutes.
        """
        self._properties['expirationSeconds'] = value

    @property
    def path(self) -> str:
        """
        Path is the path relative to the mount point of the file to
        project the token into.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is the path relative to the mount point of the file to
        project the token into.
        """
        self._properties['path'] = value

    def __enter__(self) -> 'ServiceAccountTokenProjection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceList(_kuber_definitions.Collection):
    """
    ServiceList holds a list of services.
    """

    def __init__(
            self,
            items: typing.List['Service'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ServiceList instance."""
        super(ServiceList, self).__init__(
            api_version='core/v1',
            kind='ServiceList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Service),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Service']:
        """
        List of services
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Service'], typing.List[dict]]
    ):
        """
        List of services
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Service().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.CoreV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoreV1Api(**kwargs)

    def __enter__(self) -> 'ServiceList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServicePort(_kuber_definitions.Definition):
    """
    ServicePort contains information on service's port.
    """

    def __init__(
            self,
            name: str = None,
            node_port: int = None,
            port: int = None,
            protocol: str = None,
            target_port: typing.Union[str, int, None] = None,
    ):
        """Create ServicePort instance."""
        super(ServicePort, self).__init__(
            api_version='core/v1',
            kind='ServicePort'
        )
        self._properties = {
            'name': name or '',
            'nodePort': node_port or None,
            'port': port or None,
            'protocol': protocol or '',
            'targetPort': target_port or None,

        }
        self._types = {
            'name': (str, None),
            'nodePort': (int, None),
            'port': (int, None),
            'protocol': (str, None),
            'targetPort': (int, None),

        }

    @property
    def name(self) -> str:
        """
        The name of this port within the service. This must be a
        DNS_LABEL. All ports within a ServiceSpec must have unique
        names. This maps to the 'Name' field in EndpointPort
        objects. Optional if only one ServicePort is defined on this
        service.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        The name of this port within the service. This must be a
        DNS_LABEL. All ports within a ServiceSpec must have unique
        names. This maps to the 'Name' field in EndpointPort
        objects. Optional if only one ServicePort is defined on this
        service.
        """
        self._properties['name'] = value

    @property
    def node_port(self) -> int:
        """
        The port on each node on which this service is exposed when
        type=NodePort or LoadBalancer. Usually assigned by the
        system. If specified, it will be allocated to the service if
        unused or else creation of the service will fail. Default is
        to auto-allocate a port if the ServiceType of this Service
        requires one. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#type-nodeport
        """
        return self._properties.get('nodePort')

    @node_port.setter
    def node_port(self, value: int):
        """
        The port on each node on which this service is exposed when
        type=NodePort or LoadBalancer. Usually assigned by the
        system. If specified, it will be allocated to the service if
        unused or else creation of the service will fail. Default is
        to auto-allocate a port if the ServiceType of this Service
        requires one. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#type-nodeport
        """
        self._properties['nodePort'] = value

    @property
    def port(self) -> int:
        """
        The port that will be exposed by this service.
        """
        return self._properties.get('port')

    @port.setter
    def port(self, value: int):
        """
        The port that will be exposed by this service.
        """
        self._properties['port'] = value

    @property
    def protocol(self) -> str:
        """
        The IP protocol for this port. Supports "TCP", "UDP", and
        "SCTP". Default is TCP.
        """
        return self._properties.get('protocol')

    @protocol.setter
    def protocol(self, value: str):
        """
        The IP protocol for this port. Supports "TCP", "UDP", and
        "SCTP". Default is TCP.
        """
        self._properties['protocol'] = value

    @property
    def target_port(self) -> typing.Optional[int]:
        """
        Number or name of the port to access on the pods targeted by
        the service. Number must be in the range 1 to 65535. Name
        must be an IANA_SVC_NAME. If this is a string, it will be
        looked up as a named port in the target Pod's container
        ports. If this is not specified, the value of the 'port'
        field is used (an identity map). This field is ignored for
        services with clusterIP=None, and should be omitted or set
        equal to the 'port' field. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#defining-a-service
        """
        value = self._properties.get('targetPort')
        return int(value) if value is not None else None

    @target_port.setter
    def target_port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Number or name of the port to access on the pods targeted by
        the service. Number must be in the range 1 to 65535. Name
        must be an IANA_SVC_NAME. If this is a string, it will be
        looked up as a named port in the target Pod's container
        ports. If this is not specified, the value of the 'port'
        field is used (an identity map). This field is ignored for
        services with clusterIP=None, and should be omitted or set
        equal to the 'port' field. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#defining-a-service
        """
        self._properties['targetPort'] = None if value is None else f'{value}'

    def __enter__(self) -> 'ServicePort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceSpec(_kuber_definitions.Definition):
    """
    ServiceSpec describes the attributes that a user creates on
    a service.
    """

    def __init__(
            self,
            cluster_ip: str = None,
            external_ips: typing.List[str] = None,
            external_name: str = None,
            external_traffic_policy: str = None,
            health_check_node_port: int = None,
            load_balancer_ip: str = None,
            load_balancer_source_ranges: typing.List[str] = None,
            ports: typing.List['ServicePort'] = None,
            publish_not_ready_addresses: bool = None,
            selector: dict = None,
            session_affinity: str = None,
            session_affinity_config: 'SessionAffinityConfig' = None,
            type_: str = None,
    ):
        """Create ServiceSpec instance."""
        super(ServiceSpec, self).__init__(
            api_version='core/v1',
            kind='ServiceSpec'
        )
        self._properties = {
            'clusterIP': cluster_ip or '',
            'externalIPs': external_ips or [],
            'externalName': external_name or '',
            'externalTrafficPolicy': external_traffic_policy or '',
            'healthCheckNodePort': health_check_node_port or None,
            'loadBalancerIP': load_balancer_ip or '',
            'loadBalancerSourceRanges': load_balancer_source_ranges or [],
            'ports': ports or [],
            'publishNotReadyAddresses': publish_not_ready_addresses or None,
            'selector': selector or {},
            'sessionAffinity': session_affinity or '',
            'sessionAffinityConfig': session_affinity_config or SessionAffinityConfig(),
            'type': type_ or '',

        }
        self._types = {
            'clusterIP': (str, None),
            'externalIPs': (list, str),
            'externalName': (str, None),
            'externalTrafficPolicy': (str, None),
            'healthCheckNodePort': (int, None),
            'loadBalancerIP': (str, None),
            'loadBalancerSourceRanges': (list, str),
            'ports': (list, ServicePort),
            'publishNotReadyAddresses': (bool, None),
            'selector': (dict, None),
            'sessionAffinity': (str, None),
            'sessionAffinityConfig': (SessionAffinityConfig, None),
            'type': (str, None),

        }

    @property
    def cluster_ip(self) -> str:
        """
        clusterIP is the IP address of the service and is usually
        assigned randomly by the master. If an address is specified
        manually and is not in use by others, it will be allocated
        to the service; otherwise, creation of the service will
        fail. This field can not be changed through updates. Valid
        values are "None", empty string (""), or a valid IP address.
        "None" can be specified for headless services when proxying
        is not required. Only applies to types ClusterIP, NodePort,
        and LoadBalancer. Ignored if type is ExternalName. More
        info: https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        return self._properties.get('clusterIP')

    @cluster_ip.setter
    def cluster_ip(self, value: str):
        """
        clusterIP is the IP address of the service and is usually
        assigned randomly by the master. If an address is specified
        manually and is not in use by others, it will be allocated
        to the service; otherwise, creation of the service will
        fail. This field can not be changed through updates. Valid
        values are "None", empty string (""), or a valid IP address.
        "None" can be specified for headless services when proxying
        is not required. Only applies to types ClusterIP, NodePort,
        and LoadBalancer. Ignored if type is ExternalName. More
        info: https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        self._properties['clusterIP'] = value

    @property
    def external_ips(self) -> typing.List[str]:
        """
        externalIPs is a list of IP addresses for which nodes in the
        cluster will also accept traffic for this service.  These
        IPs are not managed by Kubernetes.  The user is responsible
        for ensuring that traffic arrives at a node with this IP.  A
        common example is external load-balancers that are not part
        of the Kubernetes system.
        """
        return self._properties.get('externalIPs')

    @external_ips.setter
    def external_ips(self, value: typing.List[str]):
        """
        externalIPs is a list of IP addresses for which nodes in the
        cluster will also accept traffic for this service.  These
        IPs are not managed by Kubernetes.  The user is responsible
        for ensuring that traffic arrives at a node with this IP.  A
        common example is external load-balancers that are not part
        of the Kubernetes system.
        """
        self._properties['externalIPs'] = value

    @property
    def external_name(self) -> str:
        """
        externalName is the external reference that kubedns or
        equivalent will return as a CNAME record for this service.
        No proxying will be involved. Must be a valid RFC-1123
        hostname (https://tools.ietf.org/html/rfc1123) and requires
        Type to be ExternalName.
        """
        return self._properties.get('externalName')

    @external_name.setter
    def external_name(self, value: str):
        """
        externalName is the external reference that kubedns or
        equivalent will return as a CNAME record for this service.
        No proxying will be involved. Must be a valid RFC-1123
        hostname (https://tools.ietf.org/html/rfc1123) and requires
        Type to be ExternalName.
        """
        self._properties['externalName'] = value

    @property
    def external_traffic_policy(self) -> str:
        """
        externalTrafficPolicy denotes if this Service desires to
        route external traffic to node-local or cluster-wide
        endpoints. "Local" preserves the client source IP and avoids
        a second hop for LoadBalancer and Nodeport type services,
        but risks potentially imbalanced traffic spreading.
        "Cluster" obscures the client source IP and may cause a
        second hop to another node, but should have good overall
        load-spreading.
        """
        return self._properties.get('externalTrafficPolicy')

    @external_traffic_policy.setter
    def external_traffic_policy(self, value: str):
        """
        externalTrafficPolicy denotes if this Service desires to
        route external traffic to node-local or cluster-wide
        endpoints. "Local" preserves the client source IP and avoids
        a second hop for LoadBalancer and Nodeport type services,
        but risks potentially imbalanced traffic spreading.
        "Cluster" obscures the client source IP and may cause a
        second hop to another node, but should have good overall
        load-spreading.
        """
        self._properties['externalTrafficPolicy'] = value

    @property
    def health_check_node_port(self) -> int:
        """
        healthCheckNodePort specifies the healthcheck nodePort for
        the service. If not specified, HealthCheckNodePort is
        created by the service api backend with the allocated
        nodePort. Will use user-specified nodePort value if
        specified by the client. Only effects when Type is set to
        LoadBalancer and ExternalTrafficPolicy is set to Local.
        """
        return self._properties.get('healthCheckNodePort')

    @health_check_node_port.setter
    def health_check_node_port(self, value: int):
        """
        healthCheckNodePort specifies the healthcheck nodePort for
        the service. If not specified, HealthCheckNodePort is
        created by the service api backend with the allocated
        nodePort. Will use user-specified nodePort value if
        specified by the client. Only effects when Type is set to
        LoadBalancer and ExternalTrafficPolicy is set to Local.
        """
        self._properties['healthCheckNodePort'] = value

    @property
    def load_balancer_ip(self) -> str:
        """
        Only applies to Service Type: LoadBalancer LoadBalancer will
        get created with the IP specified in this field. This
        feature depends on whether the underlying cloud-provider
        supports specifying the loadBalancerIP when a load balancer
        is created. This field will be ignored if the cloud-provider
        does not support the feature.
        """
        return self._properties.get('loadBalancerIP')

    @load_balancer_ip.setter
    def load_balancer_ip(self, value: str):
        """
        Only applies to Service Type: LoadBalancer LoadBalancer will
        get created with the IP specified in this field. This
        feature depends on whether the underlying cloud-provider
        supports specifying the loadBalancerIP when a load balancer
        is created. This field will be ignored if the cloud-provider
        does not support the feature.
        """
        self._properties['loadBalancerIP'] = value

    @property
    def load_balancer_source_ranges(self) -> typing.List[str]:
        """
        If specified and supported by the platform, this will
        restrict traffic through the cloud-provider load-balancer
        will be restricted to the specified client IPs. This field
        will be ignored if the cloud-provider does not support the
        feature." More info:
        https://kubernetes.io/docs/tasks/access-application-
        cluster/configure-cloud-provider-firewall/
        """
        return self._properties.get('loadBalancerSourceRanges')

    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, value: typing.List[str]):
        """
        If specified and supported by the platform, this will
        restrict traffic through the cloud-provider load-balancer
        will be restricted to the specified client IPs. This field
        will be ignored if the cloud-provider does not support the
        feature." More info:
        https://kubernetes.io/docs/tasks/access-application-
        cluster/configure-cloud-provider-firewall/
        """
        self._properties['loadBalancerSourceRanges'] = value

    @property
    def ports(self) -> typing.List['ServicePort']:
        """
        The list of ports that are exposed by this service. More
        info: https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['ServicePort'], typing.List[dict]]
    ):
        """
        The list of ports that are exposed by this service. More
        info: https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ServicePort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    @property
    def publish_not_ready_addresses(self) -> bool:
        """
        publishNotReadyAddresses, when set to true, indicates that
        DNS implementations must publish the notReadyAddresses of
        subsets for the Endpoints associated with the Service. The
        default value is false. The primary use case for setting
        this field is to use a StatefulSet's Headless Service to
        propagate SRV records for its Pods without respect to their
        readiness for purpose of peer discovery.
        """
        return self._properties.get('publishNotReadyAddresses')

    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(self, value: bool):
        """
        publishNotReadyAddresses, when set to true, indicates that
        DNS implementations must publish the notReadyAddresses of
        subsets for the Endpoints associated with the Service. The
        default value is false. The primary use case for setting
        this field is to use a StatefulSet's Headless Service to
        propagate SRV records for its Pods without respect to their
        readiness for purpose of peer discovery.
        """
        self._properties['publishNotReadyAddresses'] = value

    @property
    def selector(self) -> dict:
        """
        Route service traffic to pods with label keys and values
        matching this selector. If empty or not present, the service
        is assumed to have an external process managing its
        endpoints, which Kubernetes will not modify. Only applies to
        types ClusterIP, NodePort, and LoadBalancer. Ignored if type
        is ExternalName. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: dict):
        """
        Route service traffic to pods with label keys and values
        matching this selector. If empty or not present, the service
        is assumed to have an external process managing its
        endpoints, which Kubernetes will not modify. Only applies to
        types ClusterIP, NodePort, and LoadBalancer. Ignored if type
        is ExternalName. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/
        """
        self._properties['selector'] = value

    @property
    def session_affinity(self) -> str:
        """
        Supports "ClientIP" and "None". Used to maintain session
        affinity. Enable client IP based session affinity. Must be
        ClientIP or None. Defaults to None. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        return self._properties.get('sessionAffinity')

    @session_affinity.setter
    def session_affinity(self, value: str):
        """
        Supports "ClientIP" and "None". Used to maintain session
        affinity. Enable client IP based session affinity. Must be
        ClientIP or None. Defaults to None. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#virtual-ips-and-service-proxies
        """
        self._properties['sessionAffinity'] = value

    @property
    def session_affinity_config(self) -> 'SessionAffinityConfig':
        """
        sessionAffinityConfig contains the configurations of session
        affinity.
        """
        return self._properties.get('sessionAffinityConfig')

    @session_affinity_config.setter
    def session_affinity_config(self, value: typing.Union['SessionAffinityConfig', dict]):
        """
        sessionAffinityConfig contains the configurations of session
        affinity.
        """
        if isinstance(value, dict):
            value = SessionAffinityConfig().from_dict(value)
        self._properties['sessionAffinityConfig'] = value

    @property
    def type_(self) -> str:
        """
        type determines how the Service is exposed. Defaults to
        ClusterIP. Valid options are ExternalName, ClusterIP,
        NodePort, and LoadBalancer. "ExternalName" maps to the
        specified externalName. "ClusterIP" allocates a cluster-
        internal IP address for load-balancing to endpoints.
        Endpoints are determined by the selector or if that is not
        specified, by manual construction of an Endpoints object. If
        clusterIP is "None", no virtual IP is allocated and the
        endpoints are published as a set of endpoints rather than a
        stable IP. "NodePort" builds on ClusterIP and allocates a
        port on every node which routes to the clusterIP.
        "LoadBalancer" builds on NodePort and creates an external
        load-balancer (if supported in the current cloud) which
        routes to the clusterIP. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#publishing-services-service-types
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        type determines how the Service is exposed. Defaults to
        ClusterIP. Valid options are ExternalName, ClusterIP,
        NodePort, and LoadBalancer. "ExternalName" maps to the
        specified externalName. "ClusterIP" allocates a cluster-
        internal IP address for load-balancing to endpoints.
        Endpoints are determined by the selector or if that is not
        specified, by manual construction of an Endpoints object. If
        clusterIP is "None", no virtual IP is allocated and the
        endpoints are published as a set of endpoints rather than a
        stable IP. "NodePort" builds on ClusterIP and allocates a
        port on every node which routes to the clusterIP.
        "LoadBalancer" builds on NodePort and creates an external
        load-balancer (if supported in the current cloud) which
        routes to the clusterIP. More info:
        https://kubernetes.io/docs/concepts/services-
        networking/service/#publishing-services-service-types
        """
        self._properties['type'] = value

    def __enter__(self) -> 'ServiceSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceStatus(_kuber_definitions.Definition):
    """
    ServiceStatus represents the current status of a service.
    """

    def __init__(
            self,
            load_balancer: 'LoadBalancerStatus' = None,
    ):
        """Create ServiceStatus instance."""
        super(ServiceStatus, self).__init__(
            api_version='core/v1',
            kind='ServiceStatus'
        )
        self._properties = {
            'loadBalancer': load_balancer or LoadBalancerStatus(),

        }
        self._types = {
            'loadBalancer': (LoadBalancerStatus, None),

        }

    @property
    def load_balancer(self) -> 'LoadBalancerStatus':
        """
        LoadBalancer contains the current status of the load-
        balancer, if one is present.
        """
        return self._properties.get('loadBalancer')

    @load_balancer.setter
    def load_balancer(self, value: typing.Union['LoadBalancerStatus', dict]):
        """
        LoadBalancer contains the current status of the load-
        balancer, if one is present.
        """
        if isinstance(value, dict):
            value = LoadBalancerStatus().from_dict(value)
        self._properties['loadBalancer'] = value

    def __enter__(self) -> 'ServiceStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SessionAffinityConfig(_kuber_definitions.Definition):
    """
    SessionAffinityConfig represents the configurations of
    session affinity.
    """

    def __init__(
            self,
            client_ip: 'ClientIPConfig' = None,
    ):
        """Create SessionAffinityConfig instance."""
        super(SessionAffinityConfig, self).__init__(
            api_version='core/v1',
            kind='SessionAffinityConfig'
        )
        self._properties = {
            'clientIP': client_ip or ClientIPConfig(),

        }
        self._types = {
            'clientIP': (ClientIPConfig, None),

        }

    @property
    def client_ip(self) -> 'ClientIPConfig':
        """
        clientIP contains the configurations of Client IP based
        session affinity.
        """
        return self._properties.get('clientIP')

    @client_ip.setter
    def client_ip(self, value: typing.Union['ClientIPConfig', dict]):
        """
        clientIP contains the configurations of Client IP based
        session affinity.
        """
        if isinstance(value, dict):
            value = ClientIPConfig().from_dict(value)
        self._properties['clientIP'] = value

    def __enter__(self) -> 'SessionAffinityConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageOSPersistentVolumeSource(_kuber_definitions.Definition):
    """
    Represents a StorageOS persistent volume resource.
    """

    def __init__(
            self,
            fs_type: str = None,
            read_only: bool = None,
            secret_ref: 'ObjectReference' = None,
            volume_name: str = None,
            volume_namespace: str = None,
    ):
        """Create StorageOSPersistentVolumeSource instance."""
        super(StorageOSPersistentVolumeSource, self).__init__(
            api_version='core/v1',
            kind='StorageOSPersistentVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or ObjectReference(),
            'volumeName': volume_name or '',
            'volumeNamespace': volume_namespace or '',

        }
        self._types = {
            'fsType': (str, None),
            'readOnly': (bool, None),
            'secretRef': (ObjectReference, None),
            'volumeName': (str, None),
            'volumeNamespace': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'ObjectReference':
        """
        SecretRef specifies the secret to use for obtaining the
        StorageOS API credentials.  If not specified, default values
        will be attempted.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['ObjectReference', dict]):
        """
        SecretRef specifies the secret to use for obtaining the
        StorageOS API credentials.  If not specified, default values
        will be attempted.
        """
        if isinstance(value, dict):
            value = ObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def volume_name(self) -> str:
        """
        VolumeName is the human-readable name of the StorageOS
        volume.  Volume names are only unique within a namespace.
        """
        return self._properties.get('volumeName')

    @volume_name.setter
    def volume_name(self, value: str):
        """
        VolumeName is the human-readable name of the StorageOS
        volume.  Volume names are only unique within a namespace.
        """
        self._properties['volumeName'] = value

    @property
    def volume_namespace(self) -> str:
        """
        VolumeNamespace specifies the scope of the volume within
        StorageOS.  If no namespace is specified then the Pod's
        namespace will be used.  This allows the Kubernetes name
        scoping to be mirrored within StorageOS for tighter
        integration. Set VolumeName to any name to override the
        default behaviour. Set to "default" if you are not using
        namespaces within StorageOS. Namespaces that do not pre-
        exist within StorageOS will be created.
        """
        return self._properties.get('volumeNamespace')

    @volume_namespace.setter
    def volume_namespace(self, value: str):
        """
        VolumeNamespace specifies the scope of the volume within
        StorageOS.  If no namespace is specified then the Pod's
        namespace will be used.  This allows the Kubernetes name
        scoping to be mirrored within StorageOS for tighter
        integration. Set VolumeName to any name to override the
        default behaviour. Set to "default" if you are not using
        namespaces within StorageOS. Namespaces that do not pre-
        exist within StorageOS will be created.
        """
        self._properties['volumeNamespace'] = value

    def __enter__(self) -> 'StorageOSPersistentVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageOSVolumeSource(_kuber_definitions.Definition):
    """
    Represents a StorageOS persistent volume resource.
    """

    def __init__(
            self,
            fs_type: str = None,
            read_only: bool = None,
            secret_ref: 'LocalObjectReference' = None,
            volume_name: str = None,
            volume_namespace: str = None,
    ):
        """Create StorageOSVolumeSource instance."""
        super(StorageOSVolumeSource, self).__init__(
            api_version='core/v1',
            kind='StorageOSVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'readOnly': read_only or None,
            'secretRef': secret_ref or LocalObjectReference(),
            'volumeName': volume_name or '',
            'volumeNamespace': volume_namespace or '',

        }
        self._types = {
            'fsType': (str, None),
            'readOnly': (bool, None),
            'secretRef': (LocalObjectReference, None),
            'volumeName': (str, None),
            'volumeNamespace': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def read_only(self) -> bool:
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Defaults to false (read/write). ReadOnly here will force the
        ReadOnly setting in VolumeMounts.
        """
        self._properties['readOnly'] = value

    @property
    def secret_ref(self) -> 'LocalObjectReference':
        """
        SecretRef specifies the secret to use for obtaining the
        StorageOS API credentials.  If not specified, default values
        will be attempted.
        """
        return self._properties.get('secretRef')

    @secret_ref.setter
    def secret_ref(self, value: typing.Union['LocalObjectReference', dict]):
        """
        SecretRef specifies the secret to use for obtaining the
        StorageOS API credentials.  If not specified, default values
        will be attempted.
        """
        if isinstance(value, dict):
            value = LocalObjectReference().from_dict(value)
        self._properties['secretRef'] = value

    @property
    def volume_name(self) -> str:
        """
        VolumeName is the human-readable name of the StorageOS
        volume.  Volume names are only unique within a namespace.
        """
        return self._properties.get('volumeName')

    @volume_name.setter
    def volume_name(self, value: str):
        """
        VolumeName is the human-readable name of the StorageOS
        volume.  Volume names are only unique within a namespace.
        """
        self._properties['volumeName'] = value

    @property
    def volume_namespace(self) -> str:
        """
        VolumeNamespace specifies the scope of the volume within
        StorageOS.  If no namespace is specified then the Pod's
        namespace will be used.  This allows the Kubernetes name
        scoping to be mirrored within StorageOS for tighter
        integration. Set VolumeName to any name to override the
        default behaviour. Set to "default" if you are not using
        namespaces within StorageOS. Namespaces that do not pre-
        exist within StorageOS will be created.
        """
        return self._properties.get('volumeNamespace')

    @volume_namespace.setter
    def volume_namespace(self, value: str):
        """
        VolumeNamespace specifies the scope of the volume within
        StorageOS.  If no namespace is specified then the Pod's
        namespace will be used.  This allows the Kubernetes name
        scoping to be mirrored within StorageOS for tighter
        integration. Set VolumeName to any name to override the
        default behaviour. Set to "default" if you are not using
        namespaces within StorageOS. Namespaces that do not pre-
        exist within StorageOS will be created.
        """
        self._properties['volumeNamespace'] = value

    def __enter__(self) -> 'StorageOSVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Sysctl(_kuber_definitions.Definition):
    """
    Sysctl defines a kernel parameter to be set
    """

    def __init__(
            self,
            name: str = None,
            value: str = None,
    ):
        """Create Sysctl instance."""
        super(Sysctl, self).__init__(
            api_version='core/v1',
            kind='Sysctl'
        )
        self._properties = {
            'name': name or '',
            'value': value or '',

        }
        self._types = {
            'name': (str, None),
            'value': (str, None),

        }

    @property
    def name(self) -> str:
        """
        Name of a property to set
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of a property to set
        """
        self._properties['name'] = value

    @property
    def value(self) -> str:
        """
        Value of a property to set
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """
        Value of a property to set
        """
        self._properties['value'] = value

    def __enter__(self) -> 'Sysctl':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TCPSocketAction(_kuber_definitions.Definition):
    """
    TCPSocketAction describes an action based on opening a
    socket
    """

    def __init__(
            self,
            host: str = None,
            port: typing.Union[str, int, None] = None,
    ):
        """Create TCPSocketAction instance."""
        super(TCPSocketAction, self).__init__(
            api_version='core/v1',
            kind='TCPSocketAction'
        )
        self._properties = {
            'host': host or '',
            'port': port or None,

        }
        self._types = {
            'host': (str, None),
            'port': (int, None),

        }

    @property
    def host(self) -> str:
        """
        Optional: Host name to connect to, defaults to the pod IP.
        """
        return self._properties.get('host')

    @host.setter
    def host(self, value: str):
        """
        Optional: Host name to connect to, defaults to the pod IP.
        """
        self._properties['host'] = value

    @property
    def port(self) -> typing.Optional[int]:
        """
        Number or name of the port to access on the container.
        Number must be in the range 1 to 65535. Name must be an
        IANA_SVC_NAME.
        """
        value = self._properties.get('port')
        return int(value) if value is not None else None

    @port.setter
    def port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Number or name of the port to access on the container.
        Number must be in the range 1 to 65535. Name must be an
        IANA_SVC_NAME.
        """
        self._properties['port'] = None if value is None else f'{value}'

    def __enter__(self) -> 'TCPSocketAction':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Taint(_kuber_definitions.Definition):
    """
    The node this Taint is attached to has the "effect" on any
    pod that does not tolerate the Taint.
    """

    def __init__(
            self,
            effect: str = None,
            key: str = None,
            time_added: str = None,
            value: str = None,
    ):
        """Create Taint instance."""
        super(Taint, self).__init__(
            api_version='core/v1',
            kind='Taint'
        )
        self._properties = {
            'effect': effect or '',
            'key': key or '',
            'timeAdded': time_added or None,
            'value': value or '',

        }
        self._types = {
            'effect': (str, None),
            'key': (str, None),
            'timeAdded': (str, None),
            'value': (str, None),

        }

    @property
    def effect(self) -> str:
        """
        Required. The effect of the taint on pods that do not
        tolerate the taint. Valid effects are NoSchedule,
        PreferNoSchedule and NoExecute.
        """
        return self._properties.get('effect')

    @effect.setter
    def effect(self, value: str):
        """
        Required. The effect of the taint on pods that do not
        tolerate the taint. Valid effects are NoSchedule,
        PreferNoSchedule and NoExecute.
        """
        self._properties['effect'] = value

    @property
    def key(self) -> str:
        """
        Required. The taint key to be applied to a node.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        Required. The taint key to be applied to a node.
        """
        self._properties['key'] = value

    @property
    def time_added(self) -> str:
        """
        TimeAdded represents the time at which the taint was added.
        It is only written for NoExecute taints.
        """
        return self._properties.get('timeAdded')

    @time_added.setter
    def time_added(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        TimeAdded represents the time at which the taint was added.
        It is only written for NoExecute taints.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['timeAdded'] = value

    @property
    def value(self) -> str:
        """
        Required. The taint value corresponding to the taint key.
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """
        Required. The taint value corresponding to the taint key.
        """
        self._properties['value'] = value

    def __enter__(self) -> 'Taint':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Toleration(_kuber_definitions.Definition):
    """
    The pod this Toleration is attached to tolerates any taint
    that matches the triple <key,value,effect> using the
    matching operator <operator>.
    """

    def __init__(
            self,
            effect: str = None,
            key: str = None,
            operator: str = None,
            toleration_seconds: int = None,
            value: str = None,
    ):
        """Create Toleration instance."""
        super(Toleration, self).__init__(
            api_version='core/v1',
            kind='Toleration'
        )
        self._properties = {
            'effect': effect or '',
            'key': key or '',
            'operator': operator or '',
            'tolerationSeconds': toleration_seconds or None,
            'value': value or '',

        }
        self._types = {
            'effect': (str, None),
            'key': (str, None),
            'operator': (str, None),
            'tolerationSeconds': (int, None),
            'value': (str, None),

        }

    @property
    def effect(self) -> str:
        """
        Effect indicates the taint effect to match. Empty means
        match all taint effects. When specified, allowed values are
        NoSchedule, PreferNoSchedule and NoExecute.
        """
        return self._properties.get('effect')

    @effect.setter
    def effect(self, value: str):
        """
        Effect indicates the taint effect to match. Empty means
        match all taint effects. When specified, allowed values are
        NoSchedule, PreferNoSchedule and NoExecute.
        """
        self._properties['effect'] = value

    @property
    def key(self) -> str:
        """
        Key is the taint key that the toleration applies to. Empty
        means match all taint keys. If the key is empty, operator
        must be Exists; this combination means to match all values
        and all keys.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        Key is the taint key that the toleration applies to. Empty
        means match all taint keys. If the key is empty, operator
        must be Exists; this combination means to match all values
        and all keys.
        """
        self._properties['key'] = value

    @property
    def operator(self) -> str:
        """
        Operator represents a key's relationship to the value. Valid
        operators are Exists and Equal. Defaults to Equal. Exists is
        equivalent to wildcard for value, so that a pod can tolerate
        all taints of a particular category.
        """
        return self._properties.get('operator')

    @operator.setter
    def operator(self, value: str):
        """
        Operator represents a key's relationship to the value. Valid
        operators are Exists and Equal. Defaults to Equal. Exists is
        equivalent to wildcard for value, so that a pod can tolerate
        all taints of a particular category.
        """
        self._properties['operator'] = value

    @property
    def toleration_seconds(self) -> int:
        """
        TolerationSeconds represents the period of time the
        toleration (which must be of effect NoExecute, otherwise
        this field is ignored) tolerates the taint. By default, it
        is not set, which means tolerate the taint forever (do not
        evict). Zero and negative values will be treated as 0 (evict
        immediately) by the system.
        """
        return self._properties.get('tolerationSeconds')

    @toleration_seconds.setter
    def toleration_seconds(self, value: int):
        """
        TolerationSeconds represents the period of time the
        toleration (which must be of effect NoExecute, otherwise
        this field is ignored) tolerates the taint. By default, it
        is not set, which means tolerate the taint forever (do not
        evict). Zero and negative values will be treated as 0 (evict
        immediately) by the system.
        """
        self._properties['tolerationSeconds'] = value

    @property
    def value(self) -> str:
        """
        Value is the taint value the toleration matches to. If the
        operator is Exists, the value should be empty, otherwise
        just a regular string.
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: str):
        """
        Value is the taint value the toleration matches to. If the
        operator is Exists, the value should be empty, otherwise
        just a regular string.
        """
        self._properties['value'] = value

    def __enter__(self) -> 'Toleration':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TopologySelectorLabelRequirement(_kuber_definitions.Definition):
    """
    A topology selector requirement is a selector that matches
    given label. This is an alpha feature and may change in the
    future.
    """

    def __init__(
            self,
            key: str = None,
            values: typing.List[str] = None,
    ):
        """Create TopologySelectorLabelRequirement instance."""
        super(TopologySelectorLabelRequirement, self).__init__(
            api_version='core/v1',
            kind='TopologySelectorLabelRequirement'
        )
        self._properties = {
            'key': key or '',
            'values': values or [],

        }
        self._types = {
            'key': (str, None),
            'values': (list, str),

        }

    @property
    def key(self) -> str:
        """
        The label key that the selector applies to.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        The label key that the selector applies to.
        """
        self._properties['key'] = value

    @property
    def values(self) -> typing.List[str]:
        """
        An array of string values. One value must match the label to
        be selected. Each entry in Values is ORed.
        """
        return self._properties.get('values')

    @values.setter
    def values(self, value: typing.List[str]):
        """
        An array of string values. One value must match the label to
        be selected. Each entry in Values is ORed.
        """
        self._properties['values'] = value

    def __enter__(self) -> 'TopologySelectorLabelRequirement':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TopologySelectorTerm(_kuber_definitions.Definition):
    """
    A topology selector term represents the result of label
    queries. A null or empty topology selector term matches no
    objects. The requirements of them are ANDed. It provides a
    subset of functionality as NodeSelectorTerm. This is an
    alpha feature and may change in the future.
    """

    def __init__(
            self,
            match_label_expressions: typing.List['TopologySelectorLabelRequirement'] = None,
    ):
        """Create TopologySelectorTerm instance."""
        super(TopologySelectorTerm, self).__init__(
            api_version='core/v1',
            kind='TopologySelectorTerm'
        )
        self._properties = {
            'matchLabelExpressions': match_label_expressions or [],

        }
        self._types = {
            'matchLabelExpressions': (list, TopologySelectorLabelRequirement),

        }

    @property
    def match_label_expressions(self) -> typing.List['TopologySelectorLabelRequirement']:
        """
        A list of topology selector requirements by labels.
        """
        return self._properties.get('matchLabelExpressions')

    @match_label_expressions.setter
    def match_label_expressions(
            self,
            value: typing.Union[typing.List['TopologySelectorLabelRequirement'], typing.List[dict]]
    ):
        """
        A list of topology selector requirements by labels.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = TopologySelectorLabelRequirement().from_dict(item)
            cleaned.append(item)
        self._properties['matchLabelExpressions'] = cleaned

    def __enter__(self) -> 'TopologySelectorTerm':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TypedLocalObjectReference(_kuber_definitions.Definition):
    """
    TypedLocalObjectReference contains enough information to let
    you locate the typed referenced object inside the same
    namespace.
    """

    def __init__(
            self,
            api_group: str = None,
            kind: str = None,
            name: str = None,
    ):
        """Create TypedLocalObjectReference instance."""
        super(TypedLocalObjectReference, self).__init__(
            api_version='core/v1',
            kind='TypedLocalObjectReference'
        )
        self._properties = {
            'apiGroup': api_group or '',
            'kind': kind or '',
            'name': name or '',

        }
        self._types = {
            'apiGroup': (str, None),
            'kind': (str, None),
            'name': (str, None),

        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. If
        APIGroup is not specified, the specified Kind must be in the
        core API group. For any other third-party types, APIGroup is
        required.
        """
        return self._properties.get('apiGroup')

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. If
        APIGroup is not specified, the specified Kind must be in the
        core API group. For any other third-party types, APIGroup is
        required.
        """
        self._properties['apiGroup'] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced
        """
        self._properties['name'] = value

    def __enter__(self) -> 'TypedLocalObjectReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Volume(_kuber_definitions.Definition):
    """
    Volume represents a named volume in a pod that may be
    accessed by any container in the pod.
    """

    def __init__(
            self,
            aws_elastic_block_store: 'AWSElasticBlockStoreVolumeSource' = None,
            azure_disk: 'AzureDiskVolumeSource' = None,
            azure_file: 'AzureFileVolumeSource' = None,
            cephfs: 'CephFSVolumeSource' = None,
            cinder: 'CinderVolumeSource' = None,
            config_map: 'ConfigMapVolumeSource' = None,
            csi: 'CSIVolumeSource' = None,
            downward_api: 'DownwardAPIVolumeSource' = None,
            empty_dir: 'EmptyDirVolumeSource' = None,
            fc: 'FCVolumeSource' = None,
            flex_volume: 'FlexVolumeSource' = None,
            flocker: 'FlockerVolumeSource' = None,
            gce_persistent_disk: 'GCEPersistentDiskVolumeSource' = None,
            git_repo: 'GitRepoVolumeSource' = None,
            glusterfs: 'GlusterfsVolumeSource' = None,
            host_path: 'HostPathVolumeSource' = None,
            iscsi: 'ISCSIVolumeSource' = None,
            name: str = None,
            nfs: 'NFSVolumeSource' = None,
            persistent_volume_claim: 'PersistentVolumeClaimVolumeSource' = None,
            photon_persistent_disk: 'PhotonPersistentDiskVolumeSource' = None,
            portworx_volume: 'PortworxVolumeSource' = None,
            projected: 'ProjectedVolumeSource' = None,
            quobyte: 'QuobyteVolumeSource' = None,
            rbd: 'RBDVolumeSource' = None,
            scale_io: 'ScaleIOVolumeSource' = None,
            secret: 'SecretVolumeSource' = None,
            storageos: 'StorageOSVolumeSource' = None,
            vsphere_volume: 'VsphereVirtualDiskVolumeSource' = None,
    ):
        """Create Volume instance."""
        super(Volume, self).__init__(
            api_version='core/v1',
            kind='Volume'
        )
        self._properties = {
            'awsElasticBlockStore': aws_elastic_block_store or AWSElasticBlockStoreVolumeSource(),
            'azureDisk': azure_disk or AzureDiskVolumeSource(),
            'azureFile': azure_file or AzureFileVolumeSource(),
            'cephfs': cephfs or CephFSVolumeSource(),
            'cinder': cinder or CinderVolumeSource(),
            'configMap': config_map or ConfigMapVolumeSource(),
            'csi': csi or CSIVolumeSource(),
            'downwardAPI': downward_api or DownwardAPIVolumeSource(),
            'emptyDir': empty_dir or EmptyDirVolumeSource(),
            'fc': fc or FCVolumeSource(),
            'flexVolume': flex_volume or FlexVolumeSource(),
            'flocker': flocker or FlockerVolumeSource(),
            'gcePersistentDisk': gce_persistent_disk or GCEPersistentDiskVolumeSource(),
            'gitRepo': git_repo or GitRepoVolumeSource(),
            'glusterfs': glusterfs or GlusterfsVolumeSource(),
            'hostPath': host_path or HostPathVolumeSource(),
            'iscsi': iscsi or ISCSIVolumeSource(),
            'name': name or '',
            'nfs': nfs or NFSVolumeSource(),
            'persistentVolumeClaim': persistent_volume_claim or PersistentVolumeClaimVolumeSource(),
            'photonPersistentDisk': photon_persistent_disk or PhotonPersistentDiskVolumeSource(),
            'portworxVolume': portworx_volume or PortworxVolumeSource(),
            'projected': projected or ProjectedVolumeSource(),
            'quobyte': quobyte or QuobyteVolumeSource(),
            'rbd': rbd or RBDVolumeSource(),
            'scaleIO': scale_io or ScaleIOVolumeSource(),
            'secret': secret or SecretVolumeSource(),
            'storageos': storageos or StorageOSVolumeSource(),
            'vsphereVolume': vsphere_volume or VsphereVirtualDiskVolumeSource(),

        }
        self._types = {
            'awsElasticBlockStore': (AWSElasticBlockStoreVolumeSource, None),
            'azureDisk': (AzureDiskVolumeSource, None),
            'azureFile': (AzureFileVolumeSource, None),
            'cephfs': (CephFSVolumeSource, None),
            'cinder': (CinderVolumeSource, None),
            'configMap': (ConfigMapVolumeSource, None),
            'csi': (CSIVolumeSource, None),
            'downwardAPI': (DownwardAPIVolumeSource, None),
            'emptyDir': (EmptyDirVolumeSource, None),
            'fc': (FCVolumeSource, None),
            'flexVolume': (FlexVolumeSource, None),
            'flocker': (FlockerVolumeSource, None),
            'gcePersistentDisk': (GCEPersistentDiskVolumeSource, None),
            'gitRepo': (GitRepoVolumeSource, None),
            'glusterfs': (GlusterfsVolumeSource, None),
            'hostPath': (HostPathVolumeSource, None),
            'iscsi': (ISCSIVolumeSource, None),
            'name': (str, None),
            'nfs': (NFSVolumeSource, None),
            'persistentVolumeClaim': (PersistentVolumeClaimVolumeSource, None),
            'photonPersistentDisk': (PhotonPersistentDiskVolumeSource, None),
            'portworxVolume': (PortworxVolumeSource, None),
            'projected': (ProjectedVolumeSource, None),
            'quobyte': (QuobyteVolumeSource, None),
            'rbd': (RBDVolumeSource, None),
            'scaleIO': (ScaleIOVolumeSource, None),
            'secret': (SecretVolumeSource, None),
            'storageos': (StorageOSVolumeSource, None),
            'vsphereVolume': (VsphereVirtualDiskVolumeSource, None),

        }

    @property
    def aws_elastic_block_store(self) -> 'AWSElasticBlockStoreVolumeSource':
        """
        AWSElasticBlockStore represents an AWS Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#awselasticblockstore
        """
        return self._properties.get('awsElasticBlockStore')

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, value: typing.Union['AWSElasticBlockStoreVolumeSource', dict]):
        """
        AWSElasticBlockStore represents an AWS Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#awselasticblockstore
        """
        if isinstance(value, dict):
            value = AWSElasticBlockStoreVolumeSource().from_dict(value)
        self._properties['awsElasticBlockStore'] = value

    @property
    def azure_disk(self) -> 'AzureDiskVolumeSource':
        """
        AzureDisk represents an Azure Data Disk mount on the host
        and bind mount to the pod.
        """
        return self._properties.get('azureDisk')

    @azure_disk.setter
    def azure_disk(self, value: typing.Union['AzureDiskVolumeSource', dict]):
        """
        AzureDisk represents an Azure Data Disk mount on the host
        and bind mount to the pod.
        """
        if isinstance(value, dict):
            value = AzureDiskVolumeSource().from_dict(value)
        self._properties['azureDisk'] = value

    @property
    def azure_file(self) -> 'AzureFileVolumeSource':
        """
        AzureFile represents an Azure File Service mount on the host
        and bind mount to the pod.
        """
        return self._properties.get('azureFile')

    @azure_file.setter
    def azure_file(self, value: typing.Union['AzureFileVolumeSource', dict]):
        """
        AzureFile represents an Azure File Service mount on the host
        and bind mount to the pod.
        """
        if isinstance(value, dict):
            value = AzureFileVolumeSource().from_dict(value)
        self._properties['azureFile'] = value

    @property
    def cephfs(self) -> 'CephFSVolumeSource':
        """
        CephFS represents a Ceph FS mount on the host that shares a
        pod's lifetime
        """
        return self._properties.get('cephfs')

    @cephfs.setter
    def cephfs(self, value: typing.Union['CephFSVolumeSource', dict]):
        """
        CephFS represents a Ceph FS mount on the host that shares a
        pod's lifetime
        """
        if isinstance(value, dict):
            value = CephFSVolumeSource().from_dict(value)
        self._properties['cephfs'] = value

    @property
    def cinder(self) -> 'CinderVolumeSource':
        """
        Cinder represents a cinder volume attached and mounted on
        kubelets host machine More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        return self._properties.get('cinder')

    @cinder.setter
    def cinder(self, value: typing.Union['CinderVolumeSource', dict]):
        """
        Cinder represents a cinder volume attached and mounted on
        kubelets host machine More info:
        https://releases.k8s.io/HEAD/examples/mysql-cinder-
        pd/README.md
        """
        if isinstance(value, dict):
            value = CinderVolumeSource().from_dict(value)
        self._properties['cinder'] = value

    @property
    def config_map(self) -> 'ConfigMapVolumeSource':
        """
        ConfigMap represents a configMap that should populate this
        volume
        """
        return self._properties.get('configMap')

    @config_map.setter
    def config_map(self, value: typing.Union['ConfigMapVolumeSource', dict]):
        """
        ConfigMap represents a configMap that should populate this
        volume
        """
        if isinstance(value, dict):
            value = ConfigMapVolumeSource().from_dict(value)
        self._properties['configMap'] = value

    @property
    def csi(self) -> 'CSIVolumeSource':
        """
        CSI (Container Storage Interface) represents storage that is
        handled by an external CSI driver (Alpha feature).
        """
        return self._properties.get('csi')

    @csi.setter
    def csi(self, value: typing.Union['CSIVolumeSource', dict]):
        """
        CSI (Container Storage Interface) represents storage that is
        handled by an external CSI driver (Alpha feature).
        """
        if isinstance(value, dict):
            value = CSIVolumeSource().from_dict(value)
        self._properties['csi'] = value

    @property
    def downward_api(self) -> 'DownwardAPIVolumeSource':
        """
        DownwardAPI represents downward API about the pod that
        should populate this volume
        """
        return self._properties.get('downwardAPI')

    @downward_api.setter
    def downward_api(self, value: typing.Union['DownwardAPIVolumeSource', dict]):
        """
        DownwardAPI represents downward API about the pod that
        should populate this volume
        """
        if isinstance(value, dict):
            value = DownwardAPIVolumeSource().from_dict(value)
        self._properties['downwardAPI'] = value

    @property
    def empty_dir(self) -> 'EmptyDirVolumeSource':
        """
        EmptyDir represents a temporary directory that shares a
        pod's lifetime. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#emptydir
        """
        return self._properties.get('emptyDir')

    @empty_dir.setter
    def empty_dir(self, value: typing.Union['EmptyDirVolumeSource', dict]):
        """
        EmptyDir represents a temporary directory that shares a
        pod's lifetime. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#emptydir
        """
        if isinstance(value, dict):
            value = EmptyDirVolumeSource().from_dict(value)
        self._properties['emptyDir'] = value

    @property
    def fc(self) -> 'FCVolumeSource':
        """
        FC represents a Fibre Channel resource that is attached to a
        kubelet's host machine and then exposed to the pod.
        """
        return self._properties.get('fc')

    @fc.setter
    def fc(self, value: typing.Union['FCVolumeSource', dict]):
        """
        FC represents a Fibre Channel resource that is attached to a
        kubelet's host machine and then exposed to the pod.
        """
        if isinstance(value, dict):
            value = FCVolumeSource().from_dict(value)
        self._properties['fc'] = value

    @property
    def flex_volume(self) -> 'FlexVolumeSource':
        """
        FlexVolume represents a generic volume resource that is
        provisioned/attached using an exec based plugin.
        """
        return self._properties.get('flexVolume')

    @flex_volume.setter
    def flex_volume(self, value: typing.Union['FlexVolumeSource', dict]):
        """
        FlexVolume represents a generic volume resource that is
        provisioned/attached using an exec based plugin.
        """
        if isinstance(value, dict):
            value = FlexVolumeSource().from_dict(value)
        self._properties['flexVolume'] = value

    @property
    def flocker(self) -> 'FlockerVolumeSource':
        """
        Flocker represents a Flocker volume attached to a kubelet's
        host machine. This depends on the Flocker control service
        being running
        """
        return self._properties.get('flocker')

    @flocker.setter
    def flocker(self, value: typing.Union['FlockerVolumeSource', dict]):
        """
        Flocker represents a Flocker volume attached to a kubelet's
        host machine. This depends on the Flocker control service
        being running
        """
        if isinstance(value, dict):
            value = FlockerVolumeSource().from_dict(value)
        self._properties['flocker'] = value

    @property
    def gce_persistent_disk(self) -> 'GCEPersistentDiskVolumeSource':
        """
        GCEPersistentDisk represents a GCE Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#gcepersistentdisk
        """
        return self._properties.get('gcePersistentDisk')

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, value: typing.Union['GCEPersistentDiskVolumeSource', dict]):
        """
        GCEPersistentDisk represents a GCE Disk resource that is
        attached to a kubelet's host machine and then exposed to the
        pod. More info: https://kubernetes.io/docs/concepts/storage/
        volumes#gcepersistentdisk
        """
        if isinstance(value, dict):
            value = GCEPersistentDiskVolumeSource().from_dict(value)
        self._properties['gcePersistentDisk'] = value

    @property
    def git_repo(self) -> 'GitRepoVolumeSource':
        """
        GitRepo represents a git repository at a particular
        revision. DEPRECATED: GitRepo is deprecated. To provision a
        container with a git repo, mount an EmptyDir into an
        InitContainer that clones the repo using git, then mount the
        EmptyDir into the Pod's container.
        """
        return self._properties.get('gitRepo')

    @git_repo.setter
    def git_repo(self, value: typing.Union['GitRepoVolumeSource', dict]):
        """
        GitRepo represents a git repository at a particular
        revision. DEPRECATED: GitRepo is deprecated. To provision a
        container with a git repo, mount an EmptyDir into an
        InitContainer that clones the repo using git, then mount the
        EmptyDir into the Pod's container.
        """
        if isinstance(value, dict):
            value = GitRepoVolumeSource().from_dict(value)
        self._properties['gitRepo'] = value

    @property
    def glusterfs(self) -> 'GlusterfsVolumeSource':
        """
        Glusterfs represents a Glusterfs mount on the host that
        shares a pod's lifetime. More info: https://releases.k8s.io/
        HEAD/examples/volumes/glusterfs/README.md
        """
        return self._properties.get('glusterfs')

    @glusterfs.setter
    def glusterfs(self, value: typing.Union['GlusterfsVolumeSource', dict]):
        """
        Glusterfs represents a Glusterfs mount on the host that
        shares a pod's lifetime. More info: https://releases.k8s.io/
        HEAD/examples/volumes/glusterfs/README.md
        """
        if isinstance(value, dict):
            value = GlusterfsVolumeSource().from_dict(value)
        self._properties['glusterfs'] = value

    @property
    def host_path(self) -> 'HostPathVolumeSource':
        """
        HostPath represents a pre-existing file or directory on the
        host machine that is directly exposed to the container. This
        is generally used for system agents or other privileged
        things that are allowed to see the host machine. Most
        containers will NOT need this. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        return self._properties.get('hostPath')

    @host_path.setter
    def host_path(self, value: typing.Union['HostPathVolumeSource', dict]):
        """
        HostPath represents a pre-existing file or directory on the
        host machine that is directly exposed to the container. This
        is generally used for system agents or other privileged
        things that are allowed to see the host machine. Most
        containers will NOT need this. More info:
        https://kubernetes.io/docs/concepts/storage/volumes#hostpath
        """
        if isinstance(value, dict):
            value = HostPathVolumeSource().from_dict(value)
        self._properties['hostPath'] = value

    @property
    def iscsi(self) -> 'ISCSIVolumeSource':
        """
        ISCSI represents an ISCSI Disk resource that is attached to
        a kubelet's host machine and then exposed to the pod. More
        info: https://releases.k8s.io/HEAD/examples/volumes/iscsi/RE
        ADME.md
        """
        return self._properties.get('iscsi')

    @iscsi.setter
    def iscsi(self, value: typing.Union['ISCSIVolumeSource', dict]):
        """
        ISCSI represents an ISCSI Disk resource that is attached to
        a kubelet's host machine and then exposed to the pod. More
        info: https://releases.k8s.io/HEAD/examples/volumes/iscsi/RE
        ADME.md
        """
        if isinstance(value, dict):
            value = ISCSIVolumeSource().from_dict(value)
        self._properties['iscsi'] = value

    @property
    def name(self) -> str:
        """
        Volume's name. Must be a DNS_LABEL and unique within the
        pod. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Volume's name. Must be a DNS_LABEL and unique within the
        pod. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/names/#names
        """
        self._properties['name'] = value

    @property
    def nfs(self) -> 'NFSVolumeSource':
        """
        NFS represents an NFS mount on the host that shares a pod's
        lifetime More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        return self._properties.get('nfs')

    @nfs.setter
    def nfs(self, value: typing.Union['NFSVolumeSource', dict]):
        """
        NFS represents an NFS mount on the host that shares a pod's
        lifetime More info:
        https://kubernetes.io/docs/concepts/storage/volumes#nfs
        """
        if isinstance(value, dict):
            value = NFSVolumeSource().from_dict(value)
        self._properties['nfs'] = value

    @property
    def persistent_volume_claim(self) -> 'PersistentVolumeClaimVolumeSource':
        """
        PersistentVolumeClaimVolumeSource represents a reference to
        a PersistentVolumeClaim in the same namespace. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        return self._properties.get('persistentVolumeClaim')

    @persistent_volume_claim.setter
    def persistent_volume_claim(self, value: typing.Union['PersistentVolumeClaimVolumeSource', dict]):
        """
        PersistentVolumeClaimVolumeSource represents a reference to
        a PersistentVolumeClaim in the same namespace. More info:
        https://kubernetes.io/docs/concepts/storage/persistent-
        volumes#persistentvolumeclaims
        """
        if isinstance(value, dict):
            value = PersistentVolumeClaimVolumeSource().from_dict(value)
        self._properties['persistentVolumeClaim'] = value

    @property
    def photon_persistent_disk(self) -> 'PhotonPersistentDiskVolumeSource':
        """
        PhotonPersistentDisk represents a PhotonController
        persistent disk attached and mounted on kubelets host
        machine
        """
        return self._properties.get('photonPersistentDisk')

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, value: typing.Union['PhotonPersistentDiskVolumeSource', dict]):
        """
        PhotonPersistentDisk represents a PhotonController
        persistent disk attached and mounted on kubelets host
        machine
        """
        if isinstance(value, dict):
            value = PhotonPersistentDiskVolumeSource().from_dict(value)
        self._properties['photonPersistentDisk'] = value

    @property
    def portworx_volume(self) -> 'PortworxVolumeSource':
        """
        PortworxVolume represents a portworx volume attached and
        mounted on kubelets host machine
        """
        return self._properties.get('portworxVolume')

    @portworx_volume.setter
    def portworx_volume(self, value: typing.Union['PortworxVolumeSource', dict]):
        """
        PortworxVolume represents a portworx volume attached and
        mounted on kubelets host machine
        """
        if isinstance(value, dict):
            value = PortworxVolumeSource().from_dict(value)
        self._properties['portworxVolume'] = value

    @property
    def projected(self) -> 'ProjectedVolumeSource':
        """
        Items for all in one resources secrets, configmaps, and
        downward API
        """
        return self._properties.get('projected')

    @projected.setter
    def projected(self, value: typing.Union['ProjectedVolumeSource', dict]):
        """
        Items for all in one resources secrets, configmaps, and
        downward API
        """
        if isinstance(value, dict):
            value = ProjectedVolumeSource().from_dict(value)
        self._properties['projected'] = value

    @property
    def quobyte(self) -> 'QuobyteVolumeSource':
        """
        Quobyte represents a Quobyte mount on the host that shares a
        pod's lifetime
        """
        return self._properties.get('quobyte')

    @quobyte.setter
    def quobyte(self, value: typing.Union['QuobyteVolumeSource', dict]):
        """
        Quobyte represents a Quobyte mount on the host that shares a
        pod's lifetime
        """
        if isinstance(value, dict):
            value = QuobyteVolumeSource().from_dict(value)
        self._properties['quobyte'] = value

    @property
    def rbd(self) -> 'RBDVolumeSource':
        """
        RBD represents a Rados Block Device mount on the host that
        shares a pod's lifetime. More info:
        https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md
        """
        return self._properties.get('rbd')

    @rbd.setter
    def rbd(self, value: typing.Union['RBDVolumeSource', dict]):
        """
        RBD represents a Rados Block Device mount on the host that
        shares a pod's lifetime. More info:
        https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md
        """
        if isinstance(value, dict):
            value = RBDVolumeSource().from_dict(value)
        self._properties['rbd'] = value

    @property
    def scale_io(self) -> 'ScaleIOVolumeSource':
        """
        ScaleIO represents a ScaleIO persistent volume attached and
        mounted on Kubernetes nodes.
        """
        return self._properties.get('scaleIO')

    @scale_io.setter
    def scale_io(self, value: typing.Union['ScaleIOVolumeSource', dict]):
        """
        ScaleIO represents a ScaleIO persistent volume attached and
        mounted on Kubernetes nodes.
        """
        if isinstance(value, dict):
            value = ScaleIOVolumeSource().from_dict(value)
        self._properties['scaleIO'] = value

    @property
    def secret(self) -> 'SecretVolumeSource':
        """
        Secret represents a secret that should populate this volume.
        More info:
        https://kubernetes.io/docs/concepts/storage/volumes#secret
        """
        return self._properties.get('secret')

    @secret.setter
    def secret(self, value: typing.Union['SecretVolumeSource', dict]):
        """
        Secret represents a secret that should populate this volume.
        More info:
        https://kubernetes.io/docs/concepts/storage/volumes#secret
        """
        if isinstance(value, dict):
            value = SecretVolumeSource().from_dict(value)
        self._properties['secret'] = value

    @property
    def storageos(self) -> 'StorageOSVolumeSource':
        """
        StorageOS represents a StorageOS volume attached and mounted
        on Kubernetes nodes.
        """
        return self._properties.get('storageos')

    @storageos.setter
    def storageos(self, value: typing.Union['StorageOSVolumeSource', dict]):
        """
        StorageOS represents a StorageOS volume attached and mounted
        on Kubernetes nodes.
        """
        if isinstance(value, dict):
            value = StorageOSVolumeSource().from_dict(value)
        self._properties['storageos'] = value

    @property
    def vsphere_volume(self) -> 'VsphereVirtualDiskVolumeSource':
        """
        VsphereVolume represents a vSphere volume attached and
        mounted on kubelets host machine
        """
        return self._properties.get('vsphereVolume')

    @vsphere_volume.setter
    def vsphere_volume(self, value: typing.Union['VsphereVirtualDiskVolumeSource', dict]):
        """
        VsphereVolume represents a vSphere volume attached and
        mounted on kubelets host machine
        """
        if isinstance(value, dict):
            value = VsphereVirtualDiskVolumeSource().from_dict(value)
        self._properties['vsphereVolume'] = value

    def __enter__(self) -> 'Volume':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeDevice(_kuber_definitions.Definition):
    """
    volumeDevice describes a mapping of a raw block device
    within a container.
    """

    def __init__(
            self,
            device_path: str = None,
            name: str = None,
    ):
        """Create VolumeDevice instance."""
        super(VolumeDevice, self).__init__(
            api_version='core/v1',
            kind='VolumeDevice'
        )
        self._properties = {
            'devicePath': device_path or '',
            'name': name or '',

        }
        self._types = {
            'devicePath': (str, None),
            'name': (str, None),

        }

    @property
    def device_path(self) -> str:
        """
        devicePath is the path inside of the container that the
        device will be mapped to.
        """
        return self._properties.get('devicePath')

    @device_path.setter
    def device_path(self, value: str):
        """
        devicePath is the path inside of the container that the
        device will be mapped to.
        """
        self._properties['devicePath'] = value

    @property
    def name(self) -> str:
        """
        name must match the name of a persistentVolumeClaim in the
        pod
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name must match the name of a persistentVolumeClaim in the
        pod
        """
        self._properties['name'] = value

    def __enter__(self) -> 'VolumeDevice':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeMount(_kuber_definitions.Definition):
    """
    VolumeMount describes a mounting of a Volume within a
    container.
    """

    def __init__(
            self,
            mount_path: str = None,
            mount_propagation: str = None,
            name: str = None,
            read_only: bool = None,
            sub_path: str = None,
            sub_path_expr: str = None,
    ):
        """Create VolumeMount instance."""
        super(VolumeMount, self).__init__(
            api_version='core/v1',
            kind='VolumeMount'
        )
        self._properties = {
            'mountPath': mount_path or '',
            'mountPropagation': mount_propagation or '',
            'name': name or '',
            'readOnly': read_only or None,
            'subPath': sub_path or '',
            'subPathExpr': sub_path_expr or '',

        }
        self._types = {
            'mountPath': (str, None),
            'mountPropagation': (str, None),
            'name': (str, None),
            'readOnly': (bool, None),
            'subPath': (str, None),
            'subPathExpr': (str, None),

        }

    @property
    def mount_path(self) -> str:
        """
        Path within the container at which the volume should be
        mounted.  Must not contain ':'.
        """
        return self._properties.get('mountPath')

    @mount_path.setter
    def mount_path(self, value: str):
        """
        Path within the container at which the volume should be
        mounted.  Must not contain ':'.
        """
        self._properties['mountPath'] = value

    @property
    def mount_propagation(self) -> str:
        """
        mountPropagation determines how mounts are propagated from
        the host to container and the other way around. When not
        set, MountPropagationNone is used. This field is beta in
        1.10.
        """
        return self._properties.get('mountPropagation')

    @mount_propagation.setter
    def mount_propagation(self, value: str):
        """
        mountPropagation determines how mounts are propagated from
        the host to container and the other way around. When not
        set, MountPropagationNone is used. This field is beta in
        1.10.
        """
        self._properties['mountPropagation'] = value

    @property
    def name(self) -> str:
        """
        This must match the Name of a Volume.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        This must match the Name of a Volume.
        """
        self._properties['name'] = value

    @property
    def read_only(self) -> bool:
        """
        Mounted read-only if true, read-write otherwise (false or
        unspecified). Defaults to false.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        Mounted read-only if true, read-write otherwise (false or
        unspecified). Defaults to false.
        """
        self._properties['readOnly'] = value

    @property
    def sub_path(self) -> str:
        """
        Path within the volume from which the container's volume
        should be mounted. Defaults to "" (volume's root).
        """
        return self._properties.get('subPath')

    @sub_path.setter
    def sub_path(self, value: str):
        """
        Path within the volume from which the container's volume
        should be mounted. Defaults to "" (volume's root).
        """
        self._properties['subPath'] = value

    @property
    def sub_path_expr(self) -> str:
        """
        Expanded path within the volume from which the container's
        volume should be mounted. Behaves similarly to SubPath but
        environment variable references $(VAR_NAME) are expanded
        using the container's environment. Defaults to "" (volume's
        root). SubPathExpr and SubPath are mutually exclusive. This
        field is alpha in 1.14.
        """
        return self._properties.get('subPathExpr')

    @sub_path_expr.setter
    def sub_path_expr(self, value: str):
        """
        Expanded path within the volume from which the container's
        volume should be mounted. Behaves similarly to SubPath but
        environment variable references $(VAR_NAME) are expanded
        using the container's environment. Defaults to "" (volume's
        root). SubPathExpr and SubPath are mutually exclusive. This
        field is alpha in 1.14.
        """
        self._properties['subPathExpr'] = value

    def __enter__(self) -> 'VolumeMount':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeNodeAffinity(_kuber_definitions.Definition):
    """
    VolumeNodeAffinity defines constraints that limit what nodes
    this volume can be accessed from.
    """

    def __init__(
            self,
            required: 'NodeSelector' = None,
    ):
        """Create VolumeNodeAffinity instance."""
        super(VolumeNodeAffinity, self).__init__(
            api_version='core/v1',
            kind='VolumeNodeAffinity'
        )
        self._properties = {
            'required': required or NodeSelector(),

        }
        self._types = {
            'required': (NodeSelector, None),

        }

    @property
    def required(self) -> 'NodeSelector':
        """
        Required specifies hard node constraints that must be met.
        """
        return self._properties.get('required')

    @required.setter
    def required(self, value: typing.Union['NodeSelector', dict]):
        """
        Required specifies hard node constraints that must be met.
        """
        if isinstance(value, dict):
            value = NodeSelector().from_dict(value)
        self._properties['required'] = value

    def __enter__(self) -> 'VolumeNodeAffinity':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeProjection(_kuber_definitions.Definition):
    """
    Projection that may be projected along with other supported
    volume types
    """

    def __init__(
            self,
            config_map: 'ConfigMapProjection' = None,
            downward_api: 'DownwardAPIProjection' = None,
            secret: 'SecretProjection' = None,
            service_account_token: 'ServiceAccountTokenProjection' = None,
    ):
        """Create VolumeProjection instance."""
        super(VolumeProjection, self).__init__(
            api_version='core/v1',
            kind='VolumeProjection'
        )
        self._properties = {
            'configMap': config_map or ConfigMapProjection(),
            'downwardAPI': downward_api or DownwardAPIProjection(),
            'secret': secret or SecretProjection(),
            'serviceAccountToken': service_account_token or ServiceAccountTokenProjection(),

        }
        self._types = {
            'configMap': (ConfigMapProjection, None),
            'downwardAPI': (DownwardAPIProjection, None),
            'secret': (SecretProjection, None),
            'serviceAccountToken': (ServiceAccountTokenProjection, None),

        }

    @property
    def config_map(self) -> 'ConfigMapProjection':
        """
        information about the configMap data to project
        """
        return self._properties.get('configMap')

    @config_map.setter
    def config_map(self, value: typing.Union['ConfigMapProjection', dict]):
        """
        information about the configMap data to project
        """
        if isinstance(value, dict):
            value = ConfigMapProjection().from_dict(value)
        self._properties['configMap'] = value

    @property
    def downward_api(self) -> 'DownwardAPIProjection':
        """
        information about the downwardAPI data to project
        """
        return self._properties.get('downwardAPI')

    @downward_api.setter
    def downward_api(self, value: typing.Union['DownwardAPIProjection', dict]):
        """
        information about the downwardAPI data to project
        """
        if isinstance(value, dict):
            value = DownwardAPIProjection().from_dict(value)
        self._properties['downwardAPI'] = value

    @property
    def secret(self) -> 'SecretProjection':
        """
        information about the secret data to project
        """
        return self._properties.get('secret')

    @secret.setter
    def secret(self, value: typing.Union['SecretProjection', dict]):
        """
        information about the secret data to project
        """
        if isinstance(value, dict):
            value = SecretProjection().from_dict(value)
        self._properties['secret'] = value

    @property
    def service_account_token(self) -> 'ServiceAccountTokenProjection':
        """
        information about the serviceAccountToken data to project
        """
        return self._properties.get('serviceAccountToken')

    @service_account_token.setter
    def service_account_token(self, value: typing.Union['ServiceAccountTokenProjection', dict]):
        """
        information about the serviceAccountToken data to project
        """
        if isinstance(value, dict):
            value = ServiceAccountTokenProjection().from_dict(value)
        self._properties['serviceAccountToken'] = value

    def __enter__(self) -> 'VolumeProjection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VsphereVirtualDiskVolumeSource(_kuber_definitions.Definition):
    """
    Represents a vSphere volume resource.
    """

    def __init__(
            self,
            fs_type: str = None,
            storage_policy_id: str = None,
            storage_policy_name: str = None,
            volume_path: str = None,
    ):
        """Create VsphereVirtualDiskVolumeSource instance."""
        super(VsphereVirtualDiskVolumeSource, self).__init__(
            api_version='core/v1',
            kind='VsphereVirtualDiskVolumeSource'
        )
        self._properties = {
            'fsType': fs_type or '',
            'storagePolicyID': storage_policy_id or '',
            'storagePolicyName': storage_policy_name or '',
            'volumePath': volume_path or '',

        }
        self._types = {
            'fsType': (str, None),
            'storagePolicyID': (str, None),
            'storagePolicyName': (str, None),
            'volumePath': (str, None),

        }

    @property
    def fs_type(self) -> str:
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        return self._properties.get('fsType')

    @fs_type.setter
    def fs_type(self, value: str):
        """
        Filesystem type to mount. Must be a filesystem type
        supported by the host operating system. Ex. "ext4", "xfs",
        "ntfs". Implicitly inferred to be "ext4" if unspecified.
        """
        self._properties['fsType'] = value

    @property
    def storage_policy_id(self) -> str:
        """
        Storage Policy Based Management (SPBM) profile ID associated
        with the StoragePolicyName.
        """
        return self._properties.get('storagePolicyID')

    @storage_policy_id.setter
    def storage_policy_id(self, value: str):
        """
        Storage Policy Based Management (SPBM) profile ID associated
        with the StoragePolicyName.
        """
        self._properties['storagePolicyID'] = value

    @property
    def storage_policy_name(self) -> str:
        """
        Storage Policy Based Management (SPBM) profile name.
        """
        return self._properties.get('storagePolicyName')

    @storage_policy_name.setter
    def storage_policy_name(self, value: str):
        """
        Storage Policy Based Management (SPBM) profile name.
        """
        self._properties['storagePolicyName'] = value

    @property
    def volume_path(self) -> str:
        """
        Path that identifies vSphere volume vmdk
        """
        return self._properties.get('volumePath')

    @volume_path.setter
    def volume_path(self, value: str):
        """
        Path that identifies vSphere volume vmdk
        """
        self._properties['volumePath'] = value

    def __enter__(self) -> 'VsphereVirtualDiskVolumeSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WeightedPodAffinityTerm(_kuber_definitions.Definition):
    """
    The weights of all of the matched WeightedPodAffinityTerm
    fields are added per-node to find the most preferred node(s)
    """

    def __init__(
            self,
            pod_affinity_term: 'PodAffinityTerm' = None,
            weight: int = None,
    ):
        """Create WeightedPodAffinityTerm instance."""
        super(WeightedPodAffinityTerm, self).__init__(
            api_version='core/v1',
            kind='WeightedPodAffinityTerm'
        )
        self._properties = {
            'podAffinityTerm': pod_affinity_term or PodAffinityTerm(),
            'weight': weight or None,

        }
        self._types = {
            'podAffinityTerm': (PodAffinityTerm, None),
            'weight': (int, None),

        }

    @property
    def pod_affinity_term(self) -> 'PodAffinityTerm':
        """
        Required. A pod affinity term, associated with the
        corresponding weight.
        """
        return self._properties.get('podAffinityTerm')

    @pod_affinity_term.setter
    def pod_affinity_term(self, value: typing.Union['PodAffinityTerm', dict]):
        """
        Required. A pod affinity term, associated with the
        corresponding weight.
        """
        if isinstance(value, dict):
            value = PodAffinityTerm().from_dict(value)
        self._properties['podAffinityTerm'] = value

    @property
    def weight(self) -> int:
        """
        weight associated with matching the corresponding
        podAffinityTerm, in the range 1-100.
        """
        return self._properties.get('weight')

    @weight.setter
    def weight(self, value: int):
        """
        weight associated with matching the corresponding
        podAffinityTerm, in the range 1-100.
        """
        self._properties['weight'] = value

    def __enter__(self) -> 'WeightedPodAffinityTerm':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

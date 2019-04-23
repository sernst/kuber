import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_12.meta_v1 import ListMeta
from kuber.v1_12.meta_v1 import ObjectMeta
from kuber.v1_12.core_v1 import TopologySelectorTerm


class StorageClass(_kuber_definitions.Resource):
    """
    StorageClass describes the parameters for a class of storage
    for which PersistentVolumes can be dynamically provisioned.
    StorageClasses are non-namespaced; the name of the storage
    class according to etcd is in ObjectMeta.Name.
    """

    def __init__(
            self,
            allow_volume_expansion: bool = None,
            allowed_topologies: typing.List['TopologySelectorTerm'] = None,
            metadata: 'ObjectMeta' = None,
            mount_options: typing.List[str] = None,
            parameters: dict = None,
            provisioner: str = None,
            reclaim_policy: str = None,
            volume_binding_mode: str = None,
    ):
        """Create StorageClass instance."""
        super(StorageClass, self).__init__(
            api_version='storage/v1',
            kind='StorageClass'
        )
        self._properties = {
            'allowVolumeExpansion': allow_volume_expansion or None,
            'allowedTopologies': allowed_topologies or [],
            'metadata': metadata or ObjectMeta(),
            'mountOptions': mount_options or [],
            'parameters': parameters or {},
            'provisioner': provisioner or '',
            'reclaimPolicy': reclaim_policy or '',
            'volumeBindingMode': volume_binding_mode or '',

        }
        self._types = {
            'allowVolumeExpansion': (bool, None),
            'allowedTopologies': (list, TopologySelectorTerm),
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'mountOptions': (list, str),
            'parameters': (dict, None),
            'provisioner': (str, None),
            'reclaimPolicy': (str, None),
            'volumeBindingMode': (str, None),

        }

    @property
    def allow_volume_expansion(self) -> bool:
        """
        AllowVolumeExpansion shows whether the storage class allow
        volume expand
        """
        return self._properties.get('allowVolumeExpansion')

    @allow_volume_expansion.setter
    def allow_volume_expansion(self, value: bool):
        """
        AllowVolumeExpansion shows whether the storage class allow
        volume expand
        """
        self._properties['allowVolumeExpansion'] = value

    @property
    def allowed_topologies(self) -> typing.List['TopologySelectorTerm']:
        """
        Restrict the node topologies where volumes can be
        dynamically provisioned. Each volume plugin defines its own
        supported topology specifications. An empty
        TopologySelectorTerm list means there is no topology
        restriction. This field is only honored by servers that
        enable the VolumeScheduling feature.
        """
        return self._properties.get('allowedTopologies')

    @allowed_topologies.setter
    def allowed_topologies(
            self,
            value: typing.Union[typing.List['TopologySelectorTerm'], typing.List[dict]]
    ):
        """
        Restrict the node topologies where volumes can be
        dynamically provisioned. Each volume plugin defines its own
        supported topology specifications. An empty
        TopologySelectorTerm list means there is no topology
        restriction. This field is only honored by servers that
        enable the VolumeScheduling feature.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = TopologySelectorTerm().from_dict(item)
            cleaned.append(item)
        self._properties['allowedTopologies'] = cleaned

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
    def mount_options(self) -> typing.List[str]:
        """
        Dynamically provisioned PersistentVolumes of this storage
        class are created with these mountOptions, e.g. ["ro",
        "soft"]. Not validated - mount of the PVs will simply fail
        if one is invalid.
        """
        return self._properties.get('mountOptions')

    @mount_options.setter
    def mount_options(self, value: typing.List[str]):
        """
        Dynamically provisioned PersistentVolumes of this storage
        class are created with these mountOptions, e.g. ["ro",
        "soft"]. Not validated - mount of the PVs will simply fail
        if one is invalid.
        """
        self._properties['mountOptions'] = value

    @property
    def parameters(self) -> dict:
        """
        Parameters holds the parameters for the provisioner that
        should create volumes of this storage class.
        """
        return self._properties.get('parameters')

    @parameters.setter
    def parameters(self, value: dict):
        """
        Parameters holds the parameters for the provisioner that
        should create volumes of this storage class.
        """
        self._properties['parameters'] = value

    @property
    def provisioner(self) -> str:
        """
        Provisioner indicates the type of the provisioner.
        """
        return self._properties.get('provisioner')

    @provisioner.setter
    def provisioner(self, value: str):
        """
        Provisioner indicates the type of the provisioner.
        """
        self._properties['provisioner'] = value

    @property
    def reclaim_policy(self) -> str:
        """
        Dynamically provisioned PersistentVolumes of this storage
        class are created with this reclaimPolicy. Defaults to
        Delete.
        """
        return self._properties.get('reclaimPolicy')

    @reclaim_policy.setter
    def reclaim_policy(self, value: str):
        """
        Dynamically provisioned PersistentVolumes of this storage
        class are created with this reclaimPolicy. Defaults to
        Delete.
        """
        self._properties['reclaimPolicy'] = value

    @property
    def volume_binding_mode(self) -> str:
        """
        VolumeBindingMode indicates how PersistentVolumeClaims
        should be provisioned and bound.  When unset,
        VolumeBindingImmediate is used. This field is only honored
        by servers that enable the VolumeScheduling feature.
        """
        return self._properties.get('volumeBindingMode')

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: str):
        """
        VolumeBindingMode indicates how PersistentVolumeClaims
        should be provisioned and bound.  When unset,
        VolumeBindingImmediate is used. This field is only honored
        by servers that enable the VolumeScheduling feature.
        """
        self._properties['volumeBindingMode'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_storage_class',
            'create_storage_class'
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
        Replaces the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_storage_class',
            'replace_storage_class'
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
        Patches the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_storage_class',
            'patch_storage_class'
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
        Reads the StorageClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_storage_class',
            'read_storage_class'
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
        Deletes the StorageClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_storage_class',
            'delete_storage_class'
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
    ) -> 'client.StorageV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> 'StorageClass':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageClassList(_kuber_definitions.Collection):
    """
    StorageClassList is a collection of storage classes.
    """

    def __init__(
            self,
            items: typing.List['StorageClass'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create StorageClassList instance."""
        super(StorageClassList, self).__init__(
            api_version='storage/v1',
            kind='StorageClassList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, StorageClass),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['StorageClass']:
        """
        Items is the list of StorageClasses
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['StorageClass'], typing.List[dict]]
    ):
        """
        Items is the list of StorageClasses
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = StorageClass().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata More info:
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
    ) -> 'client.StorageV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> 'StorageClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

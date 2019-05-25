import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_16.meta_v1 import ListMeta
from kuber.v1_16.meta_v1 import ObjectMeta
from kuber.v1_16.meta_v1 import Status
from kuber.v1_16.meta_v1 import StatusDetails
from kuber.v1_16.core_v1 import TopologySelectorTerm


class CSIDriver(_kuber_definitions.Resource):
    """
    CSIDriver captures information about a Container Storage
    Interface (CSI) volume driver deployed on the cluster. CSI
    drivers do not need to create the CSIDriver object directly.
    Instead they may use the cluster-driver-registrar sidecar
    container. When deployed with a CSI driver it automatically
    creates a CSIDriver object representing the driver.
    Kubernetes attach detach controller uses this object to
    determine whether attach is required. Kubelet uses this
    object to determine whether pod information needs to be
    passed on mount. CSIDriver objects are non-namespaced.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'CSIDriverSpec' = None,
    ):
        """Create CSIDriver instance."""
        super(CSIDriver, self).__init__(
            api_version='storage/v1beta1',
            kind='CSIDriver'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or CSIDriverSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (CSIDriverSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object metadata. metadata.Name indicates the name
        of the CSI driver that this object refers to; it MUST be the
        same name returned by the CSI GetPluginName() call for that
        driver. The driver name must be 63 characters or less,
        beginning and ending with an alphanumeric character
        ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics
        between. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata. metadata.Name indicates the name
        of the CSI driver that this object refers to; it MUST be the
        same name returned by the CSI GetPluginName() call for that
        driver. The driver name must be 63 characters or less,
        beginning and ending with an alphanumeric character
        ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics
        between. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'CSIDriverSpec':
        """
        Specification of the CSI Driver.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['CSIDriverSpec', dict]):
        """
        Specification of the CSI Driver.
        """
        if isinstance(value, dict):
            value = CSIDriverSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_csidriver',
            'create_csidriver'
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
        Replaces the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_csidriver',
            'replace_csidriver'
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
        Patches the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_csidriver',
            'patch_csidriver'
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
        Reads the CSIDriver from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_csidriver',
            'read_csidriver'
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
        Deletes the CSIDriver from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_csidriver',
            'delete_csidriver'
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'CSIDriver':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIDriverList(_kuber_definitions.Collection):
    """
    CSIDriverList is a collection of CSIDriver objects.
    """

    def __init__(
            self,
            items: typing.List['CSIDriver'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create CSIDriverList instance."""
        super(CSIDriverList, self).__init__(
            api_version='storage/v1beta1',
            kind='CSIDriverList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, CSIDriver),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['CSIDriver']:
        """
        items is the list of CSIDriver
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['CSIDriver'], typing.List[dict]]
    ):
        """
        items is the list of CSIDriver
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = CSIDriver().from_dict(item)
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'CSIDriverList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIDriverSpec(_kuber_definitions.Definition):
    """
    CSIDriverSpec is the specification of a CSIDriver.
    """

    def __init__(
            self,
            attach_required: bool = None,
            pod_info_on_mount: bool = None,
    ):
        """Create CSIDriverSpec instance."""
        super(CSIDriverSpec, self).__init__(
            api_version='storage/v1beta1',
            kind='CSIDriverSpec'
        )
        self._properties = {
            'attachRequired': attach_required or None,
            'podInfoOnMount': pod_info_on_mount or None,

        }
        self._types = {
            'attachRequired': (bool, None),
            'podInfoOnMount': (bool, None),

        }

    @property
    def attach_required(self) -> bool:
        """
        attachRequired indicates this CSI volume driver requires an
        attach operation (because it implements the CSI
        ControllerPublishVolume() method), and that the Kubernetes
        attach detach controller should call the attach volume
        interface which checks the volumeattachment status and waits
        until the volume is attached before proceeding to mounting.
        The CSI external-attacher coordinates with CSI volume driver
        and updates the volumeattachment status when the attach
        operation is complete. If the CSIDriverRegistry feature gate
        is enabled and the value is specified to false, the attach
        operation will be skipped. Otherwise the attach operation
        will be called.
        """
        return self._properties.get('attachRequired')

    @attach_required.setter
    def attach_required(self, value: bool):
        """
        attachRequired indicates this CSI volume driver requires an
        attach operation (because it implements the CSI
        ControllerPublishVolume() method), and that the Kubernetes
        attach detach controller should call the attach volume
        interface which checks the volumeattachment status and waits
        until the volume is attached before proceeding to mounting.
        The CSI external-attacher coordinates with CSI volume driver
        and updates the volumeattachment status when the attach
        operation is complete. If the CSIDriverRegistry feature gate
        is enabled and the value is specified to false, the attach
        operation will be skipped. Otherwise the attach operation
        will be called.
        """
        self._properties['attachRequired'] = value

    @property
    def pod_info_on_mount(self) -> bool:
        """
        If set to true, podInfoOnMount indicates this CSI volume
        driver requires additional pod information (like podName,
        podUID, etc.) during mount operations. If set to false, pod
        information will not be passed on mount. Default is false.
        The CSI driver specifies podInfoOnMount as part of driver
        deployment. If true, Kubelet will pass pod information as
        VolumeContext in the CSI NodePublishVolume() calls. The CSI
        driver is responsible for parsing and validating the
        information passed in as VolumeContext. The following
        VolumeConext will be passed if podInfoOnMount is set to
        true. This list might grow, but the prefix will be used.
        "csi.storage.k8s.io/pod.name": pod.Name
        "csi.storage.k8s.io/pod.namespace": pod.Namespace
        "csi.storage.k8s.io/pod.uid": string(pod.UID)
        """
        return self._properties.get('podInfoOnMount')

    @pod_info_on_mount.setter
    def pod_info_on_mount(self, value: bool):
        """
        If set to true, podInfoOnMount indicates this CSI volume
        driver requires additional pod information (like podName,
        podUID, etc.) during mount operations. If set to false, pod
        information will not be passed on mount. Default is false.
        The CSI driver specifies podInfoOnMount as part of driver
        deployment. If true, Kubelet will pass pod information as
        VolumeContext in the CSI NodePublishVolume() calls. The CSI
        driver is responsible for parsing and validating the
        information passed in as VolumeContext. The following
        VolumeConext will be passed if podInfoOnMount is set to
        true. This list might grow, but the prefix will be used.
        "csi.storage.k8s.io/pod.name": pod.Name
        "csi.storage.k8s.io/pod.namespace": pod.Namespace
        "csi.storage.k8s.io/pod.uid": string(pod.UID)
        """
        self._properties['podInfoOnMount'] = value

    def __enter__(self) -> 'CSIDriverSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINode(_kuber_definitions.Resource):
    """
    CSINode holds information about all CSI drivers installed on
    a node. CSI drivers do not need to create the CSINode object
    directly. As long as they use the node-driver-registrar
    sidecar container, the kubelet will automatically populate
    the CSINode object for the CSI driver as part of kubelet
    plugin registration. CSINode has the same name as a node. If
    the object is missing, it means either there are no CSI
    Drivers available on the node, or the Kubelet version is low
    enough that it doesn't create this object. CSINode has an
    OwnerReference that points to the corresponding node object.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'CSINodeSpec' = None,
    ):
        """Create CSINode instance."""
        super(CSINode, self).__init__(
            api_version='storage/v1beta1',
            kind='CSINode'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or CSINodeSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (CSINodeSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        metadata.name must be the Kubernetes node name.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        metadata.name must be the Kubernetes node name.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'CSINodeSpec':
        """
        spec is the specification of CSINode
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['CSINodeSpec', dict]):
        """
        spec is the specification of CSINode
        """
        if isinstance(value, dict):
            value = CSINodeSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_csinode',
            'create_csinode'
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
        Replaces the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_csinode',
            'replace_csinode'
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
        Patches the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_csinode',
            'patch_csinode'
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
        Reads the CSINode from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_csinode',
            'read_csinode'
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
        Deletes the CSINode from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_csinode',
            'delete_csinode'
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'CSINode':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeDriver(_kuber_definitions.Definition):
    """
    CSINodeDriver holds information about the specification of
    one CSI driver installed on a node
    """

    def __init__(
            self,
            name: str = None,
            node_id: str = None,
            topology_keys: typing.List[str] = None,
    ):
        """Create CSINodeDriver instance."""
        super(CSINodeDriver, self).__init__(
            api_version='storage/v1beta1',
            kind='CSINodeDriver'
        )
        self._properties = {
            'name': name or '',
            'nodeID': node_id or '',
            'topologyKeys': topology_keys or [],

        }
        self._types = {
            'name': (str, None),
            'nodeID': (str, None),
            'topologyKeys': (list, str),

        }

    @property
    def name(self) -> str:
        """
        This is the name of the CSI driver that this object refers
        to. This MUST be the same name returned by the CSI
        GetPluginName() call for that driver.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        This is the name of the CSI driver that this object refers
        to. This MUST be the same name returned by the CSI
        GetPluginName() call for that driver.
        """
        self._properties['name'] = value

    @property
    def node_id(self) -> str:
        """
        nodeID of the node from the driver point of view. This field
        enables Kubernetes to communicate with storage systems that
        do not share the same nomenclature for nodes. For example,
        Kubernetes may refer to a given node as "node1", but the
        storage system may refer to the same node as "nodeA". When
        Kubernetes issues a command to the storage system to attach
        a volume to a specific node, it can use this field to refer
        to the node name using the ID that the storage system will
        understand, e.g. "nodeA" instead of "node1". This field is
        required.
        """
        return self._properties.get('nodeID')

    @node_id.setter
    def node_id(self, value: str):
        """
        nodeID of the node from the driver point of view. This field
        enables Kubernetes to communicate with storage systems that
        do not share the same nomenclature for nodes. For example,
        Kubernetes may refer to a given node as "node1", but the
        storage system may refer to the same node as "nodeA". When
        Kubernetes issues a command to the storage system to attach
        a volume to a specific node, it can use this field to refer
        to the node name using the ID that the storage system will
        understand, e.g. "nodeA" instead of "node1". This field is
        required.
        """
        self._properties['nodeID'] = value

    @property
    def topology_keys(self) -> typing.List[str]:
        """
        topologyKeys is the list of keys supported by the driver.
        When a driver is initialized on a cluster, it provides a set
        of topology keys that it understands (e.g.
        "company.com/zone", "company.com/region"). When a driver is
        initialized on a node, it provides the same topology keys
        along with values. Kubelet will expose these topology keys
        as labels on its own node object. When Kubernetes does
        topology aware provisioning, it can use this list to
        determine which labels it should retrieve from the node
        object and pass back to the driver. It is possible for
        different nodes to use different topology keys. This can be
        empty if driver does not support topology.
        """
        return self._properties.get('topologyKeys')

    @topology_keys.setter
    def topology_keys(self, value: typing.List[str]):
        """
        topologyKeys is the list of keys supported by the driver.
        When a driver is initialized on a cluster, it provides a set
        of topology keys that it understands (e.g.
        "company.com/zone", "company.com/region"). When a driver is
        initialized on a node, it provides the same topology keys
        along with values. Kubelet will expose these topology keys
        as labels on its own node object. When Kubernetes does
        topology aware provisioning, it can use this list to
        determine which labels it should retrieve from the node
        object and pass back to the driver. It is possible for
        different nodes to use different topology keys. This can be
        empty if driver does not support topology.
        """
        self._properties['topologyKeys'] = value

    def __enter__(self) -> 'CSINodeDriver':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeList(_kuber_definitions.Collection):
    """
    CSINodeList is a collection of CSINode objects.
    """

    def __init__(
            self,
            items: typing.List['CSINode'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create CSINodeList instance."""
        super(CSINodeList, self).__init__(
            api_version='storage/v1beta1',
            kind='CSINodeList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, CSINode),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['CSINode']:
        """
        items is the list of CSINode
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['CSINode'], typing.List[dict]]
    ):
        """
        items is the list of CSINode
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = CSINode().from_dict(item)
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'CSINodeList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeSpec(_kuber_definitions.Definition):
    """
    CSINodeSpec holds information about the specification of all
    CSI drivers installed on a node
    """

    def __init__(
            self,
            drivers: typing.List['CSINodeDriver'] = None,
    ):
        """Create CSINodeSpec instance."""
        super(CSINodeSpec, self).__init__(
            api_version='storage/v1beta1',
            kind='CSINodeSpec'
        )
        self._properties = {
            'drivers': drivers or [],

        }
        self._types = {
            'drivers': (list, CSINodeDriver),

        }

    @property
    def drivers(self) -> typing.List['CSINodeDriver']:
        """
        drivers is a list of information of all CSI Drivers existing
        on a node. If all drivers in the list are uninstalled, this
        can become empty.
        """
        return self._properties.get('drivers')

    @drivers.setter
    def drivers(
            self,
            value: typing.Union[typing.List['CSINodeDriver'], typing.List[dict]]
    ):
        """
        drivers is a list of information of all CSI Drivers existing
        on a node. If all drivers in the list are uninstalled, this
        can become empty.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = CSINodeDriver().from_dict(item)
            cleaned.append(item)
        self._properties['drivers'] = cleaned

    def __enter__(self) -> 'CSINodeSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


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
            api_version='storage/v1beta1',
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

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
            api_version='storage/v1beta1',
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'StorageClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachment(_kuber_definitions.Resource):
    """
    VolumeAttachment captures the intent to attach or detach the
    specified volume to/from the specified node.
    VolumeAttachment objects are non-namespaced.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'VolumeAttachmentSpec' = None,
            status: 'VolumeAttachmentStatus' = None,
    ):
        """Create VolumeAttachment instance."""
        super(VolumeAttachment, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeAttachment'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or VolumeAttachmentSpec(),
            'status': status or VolumeAttachmentStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (VolumeAttachmentSpec, None),
            'status': (VolumeAttachmentStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'VolumeAttachmentSpec':
        """
        Specification of the desired attach/detach volume behavior.
        Populated by the Kubernetes system.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['VolumeAttachmentSpec', dict]):
        """
        Specification of the desired attach/detach volume behavior.
        Populated by the Kubernetes system.
        """
        if isinstance(value, dict):
            value = VolumeAttachmentSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'VolumeAttachmentStatus':
        """
        Status of the VolumeAttachment request. Populated by the
        entity completing the attach or detach operation, i.e. the
        external-attacher.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['VolumeAttachmentStatus', dict]):
        """
        Status of the VolumeAttachment request. Populated by the
        entity completing the attach or detach operation, i.e. the
        external-attacher.
        """
        if isinstance(value, dict):
            value = VolumeAttachmentStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'VolumeAttachmentStatus':
        """
        Creates the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_volume_attachment',
            'create_volume_attachment'
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
            VolumeAttachmentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'VolumeAttachmentStatus':
        """
        Replaces the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_volume_attachment',
            'replace_volume_attachment'
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
            VolumeAttachmentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'VolumeAttachmentStatus':
        """
        Patches the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_volume_attachment',
            'patch_volume_attachment'
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
            VolumeAttachmentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'VolumeAttachmentStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_volume_attachment',
            'read_volume_attachment'
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
            VolumeAttachmentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the VolumeAttachment from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_volume_attachment',
            'read_volume_attachment'
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
        Deletes the VolumeAttachment from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_volume_attachment',
            'delete_volume_attachment'
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'VolumeAttachment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentList(_kuber_definitions.Collection):
    """
    VolumeAttachmentList is a collection of VolumeAttachment
    objects.
    """

    def __init__(
            self,
            items: typing.List['VolumeAttachment'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create VolumeAttachmentList instance."""
        super(VolumeAttachmentList, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeAttachmentList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, VolumeAttachment),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['VolumeAttachment']:
        """
        Items is the list of VolumeAttachments
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['VolumeAttachment'], typing.List[dict]]
    ):
        """
        Items is the list of VolumeAttachments
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = VolumeAttachment().from_dict(item)
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
    ) -> 'client.StorageV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> 'VolumeAttachmentList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSource(_kuber_definitions.Definition):
    """
    VolumeAttachmentSource represents a volume that should be
    attached. Right now only PersistenVolumes can be attached
    via external attacher, in future we may allow also inline
    volumes in pods. Exactly one member can be set.
    """

    def __init__(
            self,
            persistent_volume_name: str = None,
    ):
        """Create VolumeAttachmentSource instance."""
        super(VolumeAttachmentSource, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeAttachmentSource'
        )
        self._properties = {
            'persistentVolumeName': persistent_volume_name or '',

        }
        self._types = {
            'persistentVolumeName': (str, None),

        }

    @property
    def persistent_volume_name(self) -> str:
        """
        Name of the persistent volume to attach.
        """
        return self._properties.get('persistentVolumeName')

    @persistent_volume_name.setter
    def persistent_volume_name(self, value: str):
        """
        Name of the persistent volume to attach.
        """
        self._properties['persistentVolumeName'] = value

    def __enter__(self) -> 'VolumeAttachmentSource':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSpec(_kuber_definitions.Definition):
    """
    VolumeAttachmentSpec is the specification of a
    VolumeAttachment request.
    """

    def __init__(
            self,
            attacher: str = None,
            node_name: str = None,
            source: 'VolumeAttachmentSource' = None,
    ):
        """Create VolumeAttachmentSpec instance."""
        super(VolumeAttachmentSpec, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeAttachmentSpec'
        )
        self._properties = {
            'attacher': attacher or '',
            'nodeName': node_name or '',
            'source': source or VolumeAttachmentSource(),

        }
        self._types = {
            'attacher': (str, None),
            'nodeName': (str, None),
            'source': (VolumeAttachmentSource, None),

        }

    @property
    def attacher(self) -> str:
        """
        Attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        return self._properties.get('attacher')

    @attacher.setter
    def attacher(self, value: str):
        """
        Attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        self._properties['attacher'] = value

    @property
    def node_name(self) -> str:
        """
        The node that the volume should be attached to.
        """
        return self._properties.get('nodeName')

    @node_name.setter
    def node_name(self, value: str):
        """
        The node that the volume should be attached to.
        """
        self._properties['nodeName'] = value

    @property
    def source(self) -> 'VolumeAttachmentSource':
        """
        Source represents the volume that should be attached.
        """
        return self._properties.get('source')

    @source.setter
    def source(self, value: typing.Union['VolumeAttachmentSource', dict]):
        """
        Source represents the volume that should be attached.
        """
        if isinstance(value, dict):
            value = VolumeAttachmentSource().from_dict(value)
        self._properties['source'] = value

    def __enter__(self) -> 'VolumeAttachmentSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentStatus(_kuber_definitions.Definition):
    """
    VolumeAttachmentStatus is the status of a VolumeAttachment
    request.
    """

    def __init__(
            self,
            attach_error: 'VolumeError' = None,
            attached: bool = None,
            attachment_metadata: dict = None,
            detach_error: 'VolumeError' = None,
    ):
        """Create VolumeAttachmentStatus instance."""
        super(VolumeAttachmentStatus, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeAttachmentStatus'
        )
        self._properties = {
            'attachError': attach_error or VolumeError(),
            'attached': attached or None,
            'attachmentMetadata': attachment_metadata or {},
            'detachError': detach_error or VolumeError(),

        }
        self._types = {
            'attachError': (VolumeError, None),
            'attached': (bool, None),
            'attachmentMetadata': (dict, None),
            'detachError': (VolumeError, None),

        }

    @property
    def attach_error(self) -> 'VolumeError':
        """
        The last error encountered during attach operation, if any.
        This field must only be set by the entity completing the
        attach operation, i.e. the external-attacher.
        """
        return self._properties.get('attachError')

    @attach_error.setter
    def attach_error(self, value: typing.Union['VolumeError', dict]):
        """
        The last error encountered during attach operation, if any.
        This field must only be set by the entity completing the
        attach operation, i.e. the external-attacher.
        """
        if isinstance(value, dict):
            value = VolumeError().from_dict(value)
        self._properties['attachError'] = value

    @property
    def attached(self) -> bool:
        """
        Indicates the volume is successfully attached. This field
        must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        return self._properties.get('attached')

    @attached.setter
    def attached(self, value: bool):
        """
        Indicates the volume is successfully attached. This field
        must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        self._properties['attached'] = value

    @property
    def attachment_metadata(self) -> dict:
        """
        Upon successful attach, this field is populated with any
        information returned by the attach operation that must be
        passed into subsequent WaitForAttach or Mount calls. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        return self._properties.get('attachmentMetadata')

    @attachment_metadata.setter
    def attachment_metadata(self, value: dict):
        """
        Upon successful attach, this field is populated with any
        information returned by the attach operation that must be
        passed into subsequent WaitForAttach or Mount calls. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        self._properties['attachmentMetadata'] = value

    @property
    def detach_error(self) -> 'VolumeError':
        """
        The last error encountered during detach operation, if any.
        This field must only be set by the entity completing the
        detach operation, i.e. the external-attacher.
        """
        return self._properties.get('detachError')

    @detach_error.setter
    def detach_error(self, value: typing.Union['VolumeError', dict]):
        """
        The last error encountered during detach operation, if any.
        This field must only be set by the entity completing the
        detach operation, i.e. the external-attacher.
        """
        if isinstance(value, dict):
            value = VolumeError().from_dict(value)
        self._properties['detachError'] = value

    def __enter__(self) -> 'VolumeAttachmentStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeError(_kuber_definitions.Definition):
    """
    VolumeError captures an error encountered during a volume
    operation.
    """

    def __init__(
            self,
            message: str = None,
            time: str = None,
    ):
        """Create VolumeError instance."""
        super(VolumeError, self).__init__(
            api_version='storage/v1beta1',
            kind='VolumeError'
        )
        self._properties = {
            'message': message or '',
            'time': time or None,

        }
        self._types = {
            'message': (str, None),
            'time': (str, None),

        }

    @property
    def message(self) -> str:
        """
        String detailing the error encountered during Attach or
        Detach operation. This string may be logged, so it should
        not contain sensitive information.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        String detailing the error encountered during Attach or
        Detach operation. This string may be logged, so it should
        not contain sensitive information.
        """
        self._properties['message'] = value

    @property
    def time(self) -> str:
        """
        Time the error was encountered.
        """
        return self._properties.get('time')

    @time.setter
    def time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Time the error was encountered.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['time'] = value

    def __enter__(self) -> 'VolumeError':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
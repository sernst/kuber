import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_24.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_24.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_24.meta_v1 import ObjectMeta  # noqa: F401


class CSIStorageCapacity(_kuber_definitions.Resource):
    """
    CSIStorageCapacity stores the result of one CSI GetCapacity
    call. For a given StorageClass, this describes the available
    capacity in a particular topology segment.  This can be used
    when considering where to instantiate new PersistentVolumes.

    For example this can express things like: - StorageClass
    "standard" has "1234 GiB" available in
    "topology.kubernetes.io/zone=us-east1" - StorageClass
    "localssd" has "10 GiB" available in
    "kubernetes.io/hostname=knode-abc123"

    The following three cases all imply that no capacity is
    available for a certain combination: - no object exists with
    suitable topology and storage class name - such an object
    exists, but the capacity is unset - such an object exists,
    but the capacity is zero

    The producer of these objects can decide which approach is
    more suitable.

    They are consumed by the kube-scheduler when a CSI driver
    opts into capacity-aware scheduling with
    CSIDriverSpec.StorageCapacity. The scheduler compares the
    MaximumVolumeSize against the requested size of pending
    volumes to filter out unsuitable nodes. If MaximumVolumeSize
    is unset, it falls back to a comparison against the less
    precise Capacity. If that is also unset, the scheduler
    assumes that capacity is insufficient and tries some other
    node.
    """

    def __init__(
        self,
        capacity: typing.Optional[typing.Union[str, int, None]] = None,
        maximum_volume_size: typing.Optional[typing.Union[str, int, None]] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        node_topology: typing.Optional["LabelSelector"] = None,
        storage_class_name: typing.Optional[str] = None,
    ):
        """Create CSIStorageCapacity instance."""
        super(CSIStorageCapacity, self).__init__(
            api_version="storage/v1beta1", kind="CSIStorageCapacity"
        )
        self._properties = {
            "capacity": capacity if capacity is not None else None,
            "maximumVolumeSize": (
                maximum_volume_size if maximum_volume_size is not None else None
            ),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "nodeTopology": (
                node_topology if node_topology is not None else LabelSelector()
            ),
            "storageClassName": (
                storage_class_name if storage_class_name is not None else ""
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "capacity": (_types.integer_or_string, None),
            "kind": (str, None),
            "maximumVolumeSize": (_types.integer_or_string, None),
            "metadata": (ObjectMeta, None),
            "nodeTopology": (LabelSelector, None),
            "storageClassName": (str, None),
        }

    @property
    def capacity(self) -> typing.Optional[str]:
        """
        Capacity is the value reported by the CSI driver in its
        GetCapacityResponse for a GetCapacityRequest with topology
        and parameters that match the previous fields.

        The semantic is currently (CSI spec 1.2) defined as: The
        available capacity, in bytes, of the storage that can be
        used to provision volumes. If not set, that information is
        currently unavailable.
        """
        value = self._properties.get("capacity")
        return f"{value}" if value is not None else None

    @capacity.setter
    def capacity(self, value: typing.Union[str, int, None]):
        """
        Capacity is the value reported by the CSI driver in its
        GetCapacityResponse for a GetCapacityRequest with topology
        and parameters that match the previous fields.

        The semantic is currently (CSI spec 1.2) defined as: The
        available capacity, in bytes, of the storage that can be
        used to provision volumes. If not set, that information is
        currently unavailable.
        """
        self._properties["capacity"] = _types.integer_or_string(value)

    @property
    def maximum_volume_size(self) -> typing.Optional[str]:
        """
        MaximumVolumeSize is the value reported by the CSI driver in
        its GetCapacityResponse for a GetCapacityRequest with
        topology and parameters that match the previous fields.

        This is defined since CSI spec 1.4.0 as the largest size
        that may be used in a
        CreateVolumeRequest.capacity_range.required_bytes field to
        create a volume with the same parameters as those in
        GetCapacityRequest. The corresponding value in the
        Kubernetes API is ResourceRequirements.Requests in a volume
        claim.
        """
        value = self._properties.get("maximumVolumeSize")
        return f"{value}" if value is not None else None

    @maximum_volume_size.setter
    def maximum_volume_size(self, value: typing.Union[str, int, None]):
        """
        MaximumVolumeSize is the value reported by the CSI driver in
        its GetCapacityResponse for a GetCapacityRequest with
        topology and parameters that match the previous fields.

        This is defined since CSI spec 1.4.0 as the largest size
        that may be used in a
        CreateVolumeRequest.capacity_range.required_bytes field to
        create a volume with the same parameters as those in
        GetCapacityRequest. The corresponding value in the
        Kubernetes API is ResourceRequirements.Requests in a volume
        claim.
        """
        self._properties["maximumVolumeSize"] = _types.integer_or_string(value)

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. The name has no particular
        meaning. It must be be a DNS subdomain (dots allowed, 253
        characters). To ensure that there are no conflicts with
        other CSI drivers on the cluster, the recommendation is to
        use csisc-<uuid>, a generated name, or a reverse-domain name
        which ends with the unique CSI driver name.

        Objects are namespaced.

        More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. The name has no particular
        meaning. It must be be a DNS subdomain (dots allowed, 253
        characters). To ensure that there are no conflicts with
        other CSI drivers on the cluster, the recommendation is to
        use csisc-<uuid>, a generated name, or a reverse-domain name
        which ends with the unique CSI driver name.

        Objects are namespaced.

        More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def node_topology(self) -> "LabelSelector":
        """
        NodeTopology defines which nodes have access to the storage
        for which capacity was reported. If not set, the storage is
        not accessible from any node in the cluster. If empty, the
        storage is accessible from all nodes. This field is
        immutable.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("nodeTopology"),
        )

    @node_topology.setter
    def node_topology(self, value: typing.Union["LabelSelector", dict]):
        """
        NodeTopology defines which nodes have access to the storage
        for which capacity was reported. If not set, the storage is
        not accessible from any node in the cluster. If empty, the
        storage is accessible from all nodes. This field is
        immutable.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["nodeTopology"] = value

    @property
    def storage_class_name(self) -> str:
        """
        The name of the StorageClass that the reported capacity
        applies to. It must meet the same requirements as the name
        of a StorageClass object (non-empty, DNS subdomain). If that
        object no longer exists, the CSIStorageCapacity object is
        obsolete and should be removed by its creator. This field is
        immutable.
        """
        return typing.cast(
            str,
            self._properties.get("storageClassName"),
        )

    @storage_class_name.setter
    def storage_class_name(self, value: str):
        """
        The name of the StorageClass that the reported capacity
        applies to. It must meet the same requirements as the name
        of a StorageClass object (non-empty, DNS subdomain). If that
        object no longer exists, the CSIStorageCapacity object is
        obsolete and should be removed by its creator. This field is
        immutable.
        """
        self._properties["storageClassName"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_csistorage_capacity", "create_csistorage_capacity"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: typing.Optional["str"] = None):
        """
        Replaces the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_csistorage_capacity",
            "replace_csistorage_capacity",
        ]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: typing.Optional["str"] = None):
        """
        Patches the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_csistorage_capacity", "patch_csistorage_capacity"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the CSIStorageCapacity from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_csistorage_capacity",
            "read_csistorage_capacity",
        ]
        return _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

    def delete_resource(
        self,
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the CSIStorageCapacity from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_csistorage_capacity",
            "delete_csistorage_capacity",
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds,
        )

        _kube_api.execute(
            action="delete",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name, "body": body},
        )

    @staticmethod
    def get_resource_api(
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> "CSIStorageCapacity":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIStorageCapacityList(_kuber_definitions.Collection):
    """
    CSIStorageCapacityList is a collection of CSIStorageCapacity
    objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["CSIStorageCapacity"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create CSIStorageCapacityList instance."""
        super(CSIStorageCapacityList, self).__init__(
            api_version="storage/v1beta1", kind="CSIStorageCapacityList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CSIStorageCapacity),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CSIStorageCapacity"]:
        """
        Items is the list of CSIStorageCapacity objects.
        """
        return typing.cast(
            typing.List["CSIStorageCapacity"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["CSIStorageCapacity"], typing.List[dict]]
    ):
        """
        Items is the list of CSIStorageCapacity objects.
        """
        cleaned: typing.List[CSIStorageCapacity] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CSIStorageCapacity,
                    CSIStorageCapacity().from_dict(item),
                )
            cleaned.append(typing.cast(CSIStorageCapacity, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1beta1Api(**kwargs)

    def __enter__(self) -> "CSIStorageCapacityList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401


class VolumeAttributesClass(_kuber_definitions.Resource):
    """
    VolumeAttributesClass represents a specification of mutable
    volume attributes defined by the CSI driver. The class can
    be specified during dynamic provisioning of
    PersistentVolumeClaims, and changed in the
    PersistentVolumeClaim spec after provisioning.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        parameters: typing.Optional[dict] = None,
    ):
        """Create VolumeAttributesClass instance."""
        super(VolumeAttributesClass, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttributesClass"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "parameters": parameters if parameters is not None else {},
        }
        self._types = {
            "apiVersion": (str, None),
            "driverName": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "parameters": (dict, None),
        }

    @property
    def driver_name(self) -> str:
        """
        Name of the CSI driver This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        Name of the CSI driver This field is immutable.
        """
        self._properties["driverName"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
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
        Standard object's metadata. More info:
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
    def parameters(self) -> dict:
        """
        parameters hold volume attributes defined by the CSI driver.
        These values are opaque to the Kubernetes and are passed
        directly to the CSI driver. The underlying storage provider
        supports changing these attributes on an existing volume,
        however the parameters field itself is immutable. To invoke
        a volume update, a new VolumeAttributesClass should be
        created with new parameters, and the PersistentVolumeClaim
        should be updated to reference the new
        VolumeAttributesClass.

        This field is required and must contain at least one
        key/value pair. The keys cannot be empty, and the maximum
        number of parameters is 512, with a cumulative max size of
        256K. If the CSI driver rejects invalid parameters, the
        target PersistentVolumeClaim will be set to an "Infeasible"
        state in the modifyVolumeStatus field.
        """
        return typing.cast(
            dict,
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: dict):
        """
        parameters hold volume attributes defined by the CSI driver.
        These values are opaque to the Kubernetes and are passed
        directly to the CSI driver. The underlying storage provider
        supports changing these attributes on an existing volume,
        however the parameters field itself is immutable. To invoke
        a volume update, a new VolumeAttributesClass should be
        created with new parameters, and the PersistentVolumeClaim
        should be updated to reference the new
        VolumeAttributesClass.

        This field is required and must contain at least one
        key/value pair. The keys cannot be empty, and the maximum
        number of parameters is 512, with a cumulative max size of
        256K. If the CSI driver rejects invalid parameters, the
        target PersistentVolumeClaim will be set to an "Infeasible"
        state in the modifyVolumeStatus field.
        """
        self._properties["parameters"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the VolumeAttributesClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_volume_attributes_class",
            "create_volume_attributes_class",
        ]

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
        Replaces the VolumeAttributesClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_volume_attributes_class",
            "replace_volume_attributes_class",
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
        Patches the VolumeAttributesClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_volume_attributes_class",
            "patch_volume_attributes_class",
        ]

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
        Reads the VolumeAttributesClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_volume_attributes_class",
            "read_volume_attributes_class",
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
        Deletes the VolumeAttributesClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_volume_attributes_class",
            "delete_volume_attributes_class",
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
    ) -> "client.StorageV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1alpha1Api(**kwargs)

    def __enter__(self) -> "VolumeAttributesClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttributesClassList(_kuber_definitions.Collection):
    """
    VolumeAttributesClassList is a collection of
    VolumeAttributesClass objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["VolumeAttributesClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create VolumeAttributesClassList instance."""
        super(VolumeAttributesClassList, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttributesClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, VolumeAttributesClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["VolumeAttributesClass"]:
        """
        items is the list of VolumeAttributesClass objects.
        """
        return typing.cast(
            typing.List["VolumeAttributesClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["VolumeAttributesClass"], typing.List[dict]],
    ):
        """
        items is the list of VolumeAttributesClass objects.
        """
        cleaned: typing.List[VolumeAttributesClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    VolumeAttributesClass,
                    VolumeAttributesClass().from_dict(item),
                )
            cleaned.append(typing.cast(VolumeAttributesClass, item))
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
    ) -> "client.StorageV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1alpha1Api(**kwargs)

    def __enter__(self) -> "VolumeAttributesClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

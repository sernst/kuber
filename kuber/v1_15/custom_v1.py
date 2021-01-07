import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_15.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_15.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_15.meta_v1 import Status  # noqa: F401
from kuber.v1_15.meta_v1 import StatusDetails  # noqa: F401


class CustomObjectStatus(dict):
    @classmethod
    def from_dict(cls, data: dict) -> "CustomObjectStatus":
        """Transparent pass-through method to match standard status objects."""
        return cls(**data)


class CustomObject(_kuber_definitions.Resource):
    """
    A custom object added to extend beyond the Kubernetes API.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: "ObjectMeta" = None,
        spec: dict = None,
        status: dict = None,
    ):
        """Create CustomObject instance."""
        super(CustomObject, self).__init__(
            api_version=api_version or "custom/v1",
            kind=kind or "CustomObject",
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else {},
            "status": status if status is not None else {},
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (dict, None),
            "status": (dict, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> dict:
        """
        Specification for the custom resource. The contents and
        structure differs by custom object.
        """
        return typing.cast(
            dict,
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: dict):
        """
        Specification for the custom resource. The contents and
        structure differs by custom object.
        """
        self._properties["spec"] = value

    @property
    def status(self) -> dict:
        """
        Status of the custom object, which is different for each
        custom object.
        """
        return typing.cast(
            dict,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: dict):
        """
        Status of the custom object, which is different for each
        custom object.
        """
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "CustomObjectStatus":
        """
        Creates the CustomObject in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_custom_object",
            "create_cluster_custom_object",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = CustomObjectStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "CustomObjectStatus":
        """
        Replaces the CustomObject in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_custom_object",
            "replace_cluster_custom_object",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CustomObjectStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "CustomObjectStatus":
        """
        Patches the CustomObject in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_custom_object",
            "patch_cluster_custom_object",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CustomObjectStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "CustomObjectStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_custom_object",
            "read_cluster_custom_object",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = CustomObjectStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the CustomObject from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_custom_object",
            "read_cluster_custom_object",
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
        namespace: str = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the CustomObject from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_custom_object",
            "delete_cluster_custom_object",
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
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.CustomObjectsApi":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CustomObjectsApi(**kwargs)

    def __enter__(self) -> "CustomObject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_15.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_15.meta_v1 import ObjectMeta  # noqa: F401


class RuntimeClass(_kuber_definitions.Resource):
    """
    RuntimeClass defines a class of container runtime supported
    in the cluster. The RuntimeClass is used to determine which
    container runtime is used to run all containers in a pod.
    RuntimeClasses are (currently) manually defined by a user or
    cluster provisioner, and referenced in the PodSpec. The
    Kubelet is responsible for resolving the RuntimeClassName
    reference before running the pod.  For more details, see
    https://git.k8s.io/enhancements/keps/sig-node/runtime-
    class.md
    """

    def __init__(
        self,
        handler: str = None,
        metadata: "ObjectMeta" = None,
    ):
        """Create RuntimeClass instance."""
        super(RuntimeClass, self).__init__(
            api_version="node/v1beta1", kind="RuntimeClass"
        )
        self._properties = {
            "handler": handler if handler is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "handler": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
        }

    @property
    def handler(self) -> str:
        """
        Handler specifies the underlying runtime and configuration
        that the CRI implementation will use to handle pods of this
        class. The possible values are specific to the node & CRI
        configuration.  It is assumed that all handlers are
        available on every node, and handlers of the same name are
        equivalent on every node. For example, a handler called
        "runc" might specify that the runc OCI runtime (using native
        Linux containers) will be used to run the containers in a
        pod. The Handler must conform to the DNS Label (RFC 1123)
        requirements, and is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("handler"),
        )

    @handler.setter
    def handler(self, value: str):
        """
        Handler specifies the underlying runtime and configuration
        that the CRI implementation will use to handle pods of this
        class. The possible values are specific to the node & CRI
        configuration.  It is assumed that all handlers are
        available on every node, and handlers of the same name are
        equivalent on every node. For example, a handler called
        "runc" might specify that the runc OCI runtime (using native
        Linux containers) will be used to run the containers in a
        pod. The Handler must conform to the DNS Label (RFC 1123)
        requirements, and is immutable.
        """
        self._properties["handler"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        More info:
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
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    def create_resource(self, namespace: "str" = None):
        """
        Creates the RuntimeClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_runtime_class", "create_runtime_class"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: "str" = None):
        """
        Replaces the RuntimeClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_runtime_class", "replace_runtime_class"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: "str" = None):
        """
        Patches the RuntimeClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_runtime_class", "patch_runtime_class"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: "str" = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: str = None):
        """
        Reads the RuntimeClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_runtime_class",
            "read_runtime_class",
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
        Deletes the RuntimeClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_runtime_class",
            "delete_runtime_class",
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
    ) -> "client.NodeV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NodeV1beta1Api(**kwargs)

    def __enter__(self) -> "RuntimeClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuntimeClassList(_kuber_definitions.Collection):
    """
    RuntimeClassList is a list of RuntimeClass objects.
    """

    def __init__(
        self,
        items: typing.List["RuntimeClass"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create RuntimeClassList instance."""
        super(RuntimeClassList, self).__init__(
            api_version="node/v1beta1", kind="RuntimeClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, RuntimeClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["RuntimeClass"]:
        """
        Items is a list of schema objects.
        """
        return typing.cast(
            typing.List["RuntimeClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["RuntimeClass"], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned: typing.List[RuntimeClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    RuntimeClass,
                    RuntimeClass().from_dict(item),
                )
            cleaned.append(typing.cast(RuntimeClass, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NodeV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NodeV1beta1Api(**kwargs)

    def __enter__(self) -> "RuntimeClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

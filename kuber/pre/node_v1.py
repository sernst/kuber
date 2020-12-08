import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.pre.meta_v1 import ListMeta
from kuber.pre.meta_v1 import ObjectMeta
from kuber.pre.core_v1 import Toleration


class Overhead(_kuber_definitions.Definition):
    """
    Overhead structure represents the resource overhead
    associated with running a pod.
    """

    def __init__(
        self,
        pod_fixed: dict = None,
    ):
        """Create Overhead instance."""
        super(Overhead, self).__init__(api_version="node/v1", kind="Overhead")
        self._properties = {
            "podFixed": pod_fixed if pod_fixed is not None else {},
        }
        self._types = {
            "podFixed": (dict, None),
        }

    @property
    def pod_fixed(self) -> dict:
        """
        PodFixed represents the fixed resource overhead associated
        with running a pod.
        """
        return typing.cast(
            dict,
            self._properties.get("podFixed"),
        )

    @pod_fixed.setter
    def pod_fixed(self, value: dict):
        """
        PodFixed represents the fixed resource overhead associated
        with running a pod.
        """
        self._properties["podFixed"] = value

    def __enter__(self) -> "Overhead":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuntimeClass(_kuber_definitions.Resource):
    """
    RuntimeClass defines a class of container runtime supported
    in the cluster. The RuntimeClass is used to determine which
    container runtime is used to run all containers in a pod.
    RuntimeClasses are manually defined by a user or cluster
    provisioner, and referenced in the PodSpec. The Kubelet is
    responsible for resolving the RuntimeClassName reference
    before running the pod.  For more details, see
    https://kubernetes.io/docs/concepts/containers/runtime-
    class/
    """

    def __init__(
        self,
        handler: str = None,
        metadata: "ObjectMeta" = None,
        overhead: "Overhead" = None,
        scheduling: "Scheduling" = None,
    ):
        """Create RuntimeClass instance."""
        super(RuntimeClass, self).__init__(api_version="node/v1", kind="RuntimeClass")
        self._properties = {
            "handler": handler if handler is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "overhead": overhead if overhead is not None else Overhead(),
            "scheduling": scheduling if scheduling is not None else Scheduling(),
        }
        self._types = {
            "apiVersion": (str, None),
            "handler": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "overhead": (Overhead, None),
            "scheduling": (Scheduling, None),
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
        pod. The Handler must be lowercase, conform to the DNS Label
        (RFC 1123) requirements, and is immutable.
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
        pod. The Handler must be lowercase, conform to the DNS Label
        (RFC 1123) requirements, and is immutable.
        """
        self._properties["handler"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
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
    def overhead(self) -> "Overhead":
        """
        Overhead represents the resource overhead associated with
        running a pod for a given RuntimeClass. For more details,
        see
         https://kubernetes.io/docs/concepts/scheduling-
        eviction/pod-overhead/
        This field is in beta starting v1.18 and is only honored by
        servers that enable the PodOverhead feature.
        """
        return typing.cast(
            "Overhead",
            self._properties.get("overhead"),
        )

    @overhead.setter
    def overhead(self, value: typing.Union["Overhead", dict]):
        """
        Overhead represents the resource overhead associated with
        running a pod for a given RuntimeClass. For more details,
        see
         https://kubernetes.io/docs/concepts/scheduling-
        eviction/pod-overhead/
        This field is in beta starting v1.18 and is only honored by
        servers that enable the PodOverhead feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Overhead,
                Overhead().from_dict(value),
            )
        self._properties["overhead"] = value

    @property
    def scheduling(self) -> "Scheduling":
        """
        Scheduling holds the scheduling constraints to ensure that
        pods running with this RuntimeClass are scheduled to nodes
        that support it. If scheduling is nil, this RuntimeClass is
        assumed to be supported by all nodes.
        """
        return typing.cast(
            "Scheduling",
            self._properties.get("scheduling"),
        )

    @scheduling.setter
    def scheduling(self, value: typing.Union["Scheduling", dict]):
        """
        Scheduling holds the scheduling constraints to ensure that
        pods running with this RuntimeClass are scheduled to nodes
        that support it. If scheduling is nil, this RuntimeClass is
        assumed to be supported by all nodes.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Scheduling,
                Scheduling().from_dict(value),
            )
        self._properties["scheduling"] = value

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
    ) -> "client.NodeV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NodeV1Api(**kwargs)

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
            api_version="node/v1", kind="RuntimeClassList"
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
        Standard list metadata. More info:
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
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NodeV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NodeV1Api(**kwargs)

    def __enter__(self) -> "RuntimeClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scheduling(_kuber_definitions.Definition):
    """
    Scheduling specifies the scheduling constraints for nodes
    supporting a RuntimeClass.
    """

    def __init__(
        self,
        node_selector: dict = None,
        tolerations: typing.List["Toleration"] = None,
    ):
        """Create Scheduling instance."""
        super(Scheduling, self).__init__(api_version="node/v1", kind="Scheduling")
        self._properties = {
            "nodeSelector": node_selector if node_selector is not None else {},
            "tolerations": tolerations if tolerations is not None else [],
        }
        self._types = {
            "nodeSelector": (dict, None),
            "tolerations": (list, Toleration),
        }

    @property
    def node_selector(self) -> dict:
        """
        nodeSelector lists labels that must be present on nodes that
        support this RuntimeClass. Pods using this RuntimeClass can
        only be scheduled to a node matched by this selector. The
        RuntimeClass nodeSelector is merged with a pod's existing
        nodeSelector. Any conflicts will cause the pod to be
        rejected in admission.
        """
        return typing.cast(
            dict,
            self._properties.get("nodeSelector"),
        )

    @node_selector.setter
    def node_selector(self, value: dict):
        """
        nodeSelector lists labels that must be present on nodes that
        support this RuntimeClass. Pods using this RuntimeClass can
        only be scheduled to a node matched by this selector. The
        RuntimeClass nodeSelector is merged with a pod's existing
        nodeSelector. Any conflicts will cause the pod to be
        rejected in admission.
        """
        self._properties["nodeSelector"] = value

    @property
    def tolerations(self) -> typing.List["Toleration"]:
        """
        tolerations are appended (excluding duplicates) to pods
        running with this RuntimeClass during admission, effectively
        unioning the set of nodes tolerated by the pod and the
        RuntimeClass.
        """
        return typing.cast(
            typing.List["Toleration"],
            self._properties.get("tolerations"),
        )

    @tolerations.setter
    def tolerations(
        self, value: typing.Union[typing.List["Toleration"], typing.List[dict]]
    ):
        """
        tolerations are appended (excluding duplicates) to pods
        running with this RuntimeClass during admission, effectively
        unioning the set of nodes tolerated by the pod and the
        RuntimeClass.
        """
        cleaned: typing.List[Toleration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Toleration,
                    Toleration().from_dict(item),
                )
            cleaned.append(typing.cast(Toleration, item))
        self._properties["tolerations"] = cleaned

    def __enter__(self) -> "Scheduling":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_25.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_25.core_v1 import NodeSelector  # noqa: F401
from kuber.v1_25.meta_v1 import ObjectMeta  # noqa: F401


class ClusterCIDR(_kuber_definitions.Resource):
    """
    ClusterCIDR represents a single configuration for per-Node
    Pod CIDR allocations when the MultiCIDRRangeAllocator is
    enabled (see the config for kube-controller-manager).  A
    cluster may have any number of ClusterCIDR resources, all of
    which will be considered when allocating a CIDR for a Node.
    A ClusterCIDR is eligible to be used for a given Node when
    the node selector matches the node in question and has free
    CIDRs to allocate.  In case of multiple matching ClusterCIDR
    resources, the allocator will attempt to break ties using
    internal heuristics, but any ClusterCIDR whose node selector
    matches the Node may be used.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ClusterCIDRSpec"] = None,
    ):
        """Create ClusterCIDR instance."""
        super(ClusterCIDR, self).__init__(
            api_version="networking/v1alpha1", kind="ClusterCIDR"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ClusterCIDRSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ClusterCIDRSpec, None),
        }

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
    def spec(self) -> "ClusterCIDRSpec":
        """
        Spec is the desired state of the ClusterCIDR. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "ClusterCIDRSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ClusterCIDRSpec", dict]):
        """
        Spec is the desired state of the ClusterCIDR. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                ClusterCIDRSpec,
                ClusterCIDRSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ClusterCIDR in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_cluster_cidr", "create_cluster_cidr"]

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
        Replaces the ClusterCIDR in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_cluster_cidr", "replace_cluster_cidr"]

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
        Patches the ClusterCIDR in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_cluster_cidr", "patch_cluster_cidr"]

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
        Reads the ClusterCIDR from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_cluster_cidr",
            "read_cluster_cidr",
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
        Deletes the ClusterCIDR from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_cluster_cidr",
            "delete_cluster_cidr",
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
    ) -> "client.NetworkingV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1alpha1Api(**kwargs)

    def __enter__(self) -> "ClusterCIDR":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterCIDRList(_kuber_definitions.Collection):
    """
    ClusterCIDRList contains a list of ClusterCIDR.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ClusterCIDR"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ClusterCIDRList instance."""
        super(ClusterCIDRList, self).__init__(
            api_version="networking/v1alpha1", kind="ClusterCIDRList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ClusterCIDR),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ClusterCIDR"]:
        """
        Items is the list of ClusterCIDRs.
        """
        return typing.cast(
            typing.List["ClusterCIDR"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["ClusterCIDR"], typing.List[dict]]):
        """
        Items is the list of ClusterCIDRs.
        """
        cleaned: typing.List[ClusterCIDR] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ClusterCIDR,
                    ClusterCIDR().from_dict(item),
                )
            cleaned.append(typing.cast(ClusterCIDR, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata. More info:
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
        Standard object's metadata. More info:
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
    ) -> "client.NetworkingV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1alpha1Api(**kwargs)

    def __enter__(self) -> "ClusterCIDRList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterCIDRSpec(_kuber_definitions.Definition):
    """
    ClusterCIDRSpec defines the desired state of ClusterCIDR.
    """

    def __init__(
        self,
        ipv4: typing.Optional[str] = None,
        ipv6: typing.Optional[str] = None,
        node_selector: typing.Optional["NodeSelector"] = None,
        per_node_host_bits: typing.Optional[int] = None,
    ):
        """Create ClusterCIDRSpec instance."""
        super(ClusterCIDRSpec, self).__init__(
            api_version="networking/v1alpha1", kind="ClusterCIDRSpec"
        )
        self._properties = {
            "ipv4": ipv4 if ipv4 is not None else "",
            "ipv6": ipv6 if ipv6 is not None else "",
            "nodeSelector": (
                node_selector if node_selector is not None else NodeSelector()
            ),
            "perNodeHostBits": (
                per_node_host_bits if per_node_host_bits is not None else None
            ),
        }
        self._types = {
            "ipv4": (str, None),
            "ipv6": (str, None),
            "nodeSelector": (NodeSelector, None),
            "perNodeHostBits": (int, None),
        }

    @property
    def ipv4(self) -> str:
        """
        IPv4 defines an IPv4 IP block in CIDR notation(e.g.
        "10.0.0.0/8"). At least one of IPv4 and IPv6 must be
        specified. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("ipv4"),
        )

    @ipv4.setter
    def ipv4(self, value: str):
        """
        IPv4 defines an IPv4 IP block in CIDR notation(e.g.
        "10.0.0.0/8"). At least one of IPv4 and IPv6 must be
        specified. This field is immutable.
        """
        self._properties["ipv4"] = value

    @property
    def ipv6(self) -> str:
        """
        IPv6 defines an IPv6 IP block in CIDR notation(e.g.
        "fd12:3456:789a:1::/64"). At least one of IPv4 and IPv6 must
        be specified. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("ipv6"),
        )

    @ipv6.setter
    def ipv6(self, value: str):
        """
        IPv6 defines an IPv6 IP block in CIDR notation(e.g.
        "fd12:3456:789a:1::/64"). At least one of IPv4 and IPv6 must
        be specified. This field is immutable.
        """
        self._properties["ipv6"] = value

    @property
    def node_selector(self) -> "NodeSelector":
        """
        NodeSelector defines which nodes the config is applicable
        to. An empty or nil NodeSelector selects all nodes. This
        field is immutable.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("nodeSelector"),
        )

    @node_selector.setter
    def node_selector(self, value: typing.Union["NodeSelector", dict]):
        """
        NodeSelector defines which nodes the config is applicable
        to. An empty or nil NodeSelector selects all nodes. This
        field is immutable.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["nodeSelector"] = value

    @property
    def per_node_host_bits(self) -> int:
        """
        PerNodeHostBits defines the number of host bits to be
        configured per node. A subnet mask determines how much of
        the address is used for network bits and host bits. For
        example an IPv4 address of 192.168.0.0/24, splits the
        address into 24 bits for the network portion and 8 bits for
        the host portion. To allocate 256 IPs, set this field to 8
        (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4
        (16 IPs). This field is immutable.
        """
        return typing.cast(
            int,
            self._properties.get("perNodeHostBits"),
        )

    @per_node_host_bits.setter
    def per_node_host_bits(self, value: int):
        """
        PerNodeHostBits defines the number of host bits to be
        configured per node. A subnet mask determines how much of
        the address is used for network bits and host bits. For
        example an IPv4 address of 192.168.0.0/24, splits the
        address into 24 bits for the network portion and 8 bits for
        the host portion. To allocate 256 IPs, set this field to 8
        (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4
        (16 IPs). This field is immutable.
        """
        self._properties["perNodeHostBits"] = value

    def __enter__(self) -> "ClusterCIDRSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

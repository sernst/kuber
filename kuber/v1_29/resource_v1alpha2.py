import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_29.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_29.core_v1 import NodeSelector  # noqa: F401
from kuber.v1_29.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_29.meta_v1 import Status  # noqa: F401
from kuber.v1_29.meta_v1 import StatusDetails  # noqa: F401


class AllocationResult(_kuber_definitions.Definition):
    """
    AllocationResult contains attributes of an allocated
    resource.
    """

    def __init__(
        self,
        available_on_nodes: typing.Optional["NodeSelector"] = None,
        resource_handles: typing.Optional[typing.List["ResourceHandle"]] = None,
        shareable: typing.Optional[bool] = None,
    ):
        """Create AllocationResult instance."""
        super(AllocationResult, self).__init__(
            api_version="resource/v1alpha2", kind="AllocationResult"
        )
        self._properties = {
            "availableOnNodes": (
                available_on_nodes if available_on_nodes is not None else NodeSelector()
            ),
            "resourceHandles": resource_handles if resource_handles is not None else [],
            "shareable": shareable if shareable is not None else None,
        }
        self._types = {
            "availableOnNodes": (NodeSelector, None),
            "resourceHandles": (list, ResourceHandle),
            "shareable": (bool, None),
        }

    @property
    def available_on_nodes(self) -> "NodeSelector":
        """
        This field will get set by the resource driver after it has
        allocated the resource to inform the scheduler where it can
        schedule Pods using the ResourceClaim.

        Setting this field is optional. If null, the resource is
        available everywhere.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("availableOnNodes"),
        )

    @available_on_nodes.setter
    def available_on_nodes(self, value: typing.Union["NodeSelector", dict]):
        """
        This field will get set by the resource driver after it has
        allocated the resource to inform the scheduler where it can
        schedule Pods using the ResourceClaim.

        Setting this field is optional. If null, the resource is
        available everywhere.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["availableOnNodes"] = value

    @property
    def resource_handles(self) -> typing.List["ResourceHandle"]:
        """
        ResourceHandles contain the state associated with an
        allocation that should be maintained throughout the lifetime
        of a claim. Each ResourceHandle contains data that should be
        passed to a specific kubelet plugin once it lands on a node.
        This data is returned by the driver after a successful
        allocation and is opaque to Kubernetes. Driver documentation
        may explain to users how to interpret this data if needed.

        Setting this field is optional. It has a maximum size of 32
        entries. If null (or empty), it is assumed this allocation
        will be processed by a single kubelet plugin with no
        ResourceHandle data attached. The name of the kubelet plugin
        invoked will match the DriverName set in the
        ResourceClaimStatus this AllocationResult is embedded in.
        """
        return typing.cast(
            typing.List["ResourceHandle"],
            self._properties.get("resourceHandles"),
        )

    @resource_handles.setter
    def resource_handles(
        self, value: typing.Union[typing.List["ResourceHandle"], typing.List[dict]]
    ):
        """
        ResourceHandles contain the state associated with an
        allocation that should be maintained throughout the lifetime
        of a claim. Each ResourceHandle contains data that should be
        passed to a specific kubelet plugin once it lands on a node.
        This data is returned by the driver after a successful
        allocation and is opaque to Kubernetes. Driver documentation
        may explain to users how to interpret this data if needed.

        Setting this field is optional. It has a maximum size of 32
        entries. If null (or empty), it is assumed this allocation
        will be processed by a single kubelet plugin with no
        ResourceHandle data attached. The name of the kubelet plugin
        invoked will match the DriverName set in the
        ResourceClaimStatus this AllocationResult is embedded in.
        """
        cleaned: typing.List[ResourceHandle] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceHandle,
                    ResourceHandle().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceHandle, item))
        self._properties["resourceHandles"] = cleaned

    @property
    def shareable(self) -> bool:
        """
        Shareable determines whether the resource supports more than
        one consumer at a time.
        """
        return typing.cast(
            bool,
            self._properties.get("shareable"),
        )

    @shareable.setter
    def shareable(self, value: bool):
        """
        Shareable determines whether the resource supports more than
        one consumer at a time.
        """
        self._properties["shareable"] = value

    def __enter__(self) -> "AllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContext(_kuber_definitions.Resource):
    """
    PodSchedulingContext objects hold information that is needed
    to schedule a Pod with ResourceClaims that use
    "WaitForFirstConsumer" allocation mode.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["PodSchedulingContextSpec"] = None,
        status: typing.Optional["PodSchedulingContextStatus"] = None,
    ):
        """Create PodSchedulingContext instance."""
        super(PodSchedulingContext, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContext"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else PodSchedulingContextSpec(),
            "status": status if status is not None else PodSchedulingContextStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (PodSchedulingContextSpec, None),
            "status": (PodSchedulingContextStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "PodSchedulingContextSpec":
        """
        Spec describes where resources for the Pod are needed.
        """
        return typing.cast(
            "PodSchedulingContextSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["PodSchedulingContextSpec", dict]):
        """
        Spec describes where resources for the Pod are needed.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodSchedulingContextSpec,
                PodSchedulingContextSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "PodSchedulingContextStatus":
        """
        Status describes where resources for the Pod can be
        allocated.
        """
        return typing.cast(
            "PodSchedulingContextStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["PodSchedulingContextStatus", dict]):
        """
        Status describes where resources for the Pod can be
        allocated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodSchedulingContextStatus,
                PodSchedulingContextStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Creates the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_pod_scheduling_context",
            "create_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Replaces the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_pod_scheduling_context",
            "replace_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Patches the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_pod_scheduling_context",
            "patch_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_pod_scheduling_context",
            "read_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the PodSchedulingContext from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_pod_scheduling_context",
            "read_pod_scheduling_context",
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
        Deletes the PodSchedulingContext from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_pod_scheduling_context",
            "delete_pod_scheduling_context",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "PodSchedulingContext":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextList(_kuber_definitions.Collection):
    """
    PodSchedulingContextList is a collection of Pod scheduling
    objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["PodSchedulingContext"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create PodSchedulingContextList instance."""
        super(PodSchedulingContextList, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PodSchedulingContext),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PodSchedulingContext"]:
        """
        Items is the list of PodSchedulingContext objects.
        """
        return typing.cast(
            typing.List["PodSchedulingContext"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["PodSchedulingContext"], typing.List[dict]],
    ):
        """
        Items is the list of PodSchedulingContext objects.
        """
        cleaned: typing.List[PodSchedulingContext] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodSchedulingContext,
                    PodSchedulingContext().from_dict(item),
                )
            cleaned.append(typing.cast(PodSchedulingContext, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "PodSchedulingContextList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextSpec(_kuber_definitions.Definition):
    """
    PodSchedulingContextSpec describes where resources for the
    Pod are needed.
    """

    def __init__(
        self,
        potential_nodes: typing.Optional[typing.List[str]] = None,
        selected_node: typing.Optional[str] = None,
    ):
        """Create PodSchedulingContextSpec instance."""
        super(PodSchedulingContextSpec, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextSpec"
        )
        self._properties = {
            "potentialNodes": potential_nodes if potential_nodes is not None else [],
            "selectedNode": selected_node if selected_node is not None else "",
        }
        self._types = {
            "potentialNodes": (list, str),
            "selectedNode": (str, None),
        }

    @property
    def potential_nodes(self) -> typing.List[str]:
        """
        PotentialNodes lists nodes where the Pod might be able to
        run.

        The size of this field is limited to 128. This is large
        enough for many clusters. Larger clusters may need more
        attempts to find a node that suits all pending resources.
        This may get increased in the future, but not reduced.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("potentialNodes"),
        )

    @potential_nodes.setter
    def potential_nodes(self, value: typing.List[str]):
        """
        PotentialNodes lists nodes where the Pod might be able to
        run.

        The size of this field is limited to 128. This is large
        enough for many clusters. Larger clusters may need more
        attempts to find a node that suits all pending resources.
        This may get increased in the future, but not reduced.
        """
        self._properties["potentialNodes"] = value

    @property
    def selected_node(self) -> str:
        """
        SelectedNode is the node for which allocation of
        ResourceClaims that are referenced by the Pod and that use
        "WaitForFirstConsumer" allocation is to be attempted.
        """
        return typing.cast(
            str,
            self._properties.get("selectedNode"),
        )

    @selected_node.setter
    def selected_node(self, value: str):
        """
        SelectedNode is the node for which allocation of
        ResourceClaims that are referenced by the Pod and that use
        "WaitForFirstConsumer" allocation is to be attempted.
        """
        self._properties["selectedNode"] = value

    def __enter__(self) -> "PodSchedulingContextSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextStatus(_kuber_definitions.Definition):
    """
    PodSchedulingContextStatus describes where resources for the
    Pod can be allocated.
    """

    def __init__(
        self,
        resource_claims: typing.Optional[
            typing.List["ResourceClaimSchedulingStatus"]
        ] = None,
    ):
        """Create PodSchedulingContextStatus instance."""
        super(PodSchedulingContextStatus, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextStatus"
        )
        self._properties = {
            "resourceClaims": resource_claims if resource_claims is not None else [],
        }
        self._types = {
            "resourceClaims": (list, ResourceClaimSchedulingStatus),
        }

    @property
    def resource_claims(self) -> typing.List["ResourceClaimSchedulingStatus"]:
        """
        ResourceClaims describes resource availability for each
        pod.spec.resourceClaim entry where the corresponding
        ResourceClaim uses "WaitForFirstConsumer" allocation mode.
        """
        return typing.cast(
            typing.List["ResourceClaimSchedulingStatus"],
            self._properties.get("resourceClaims"),
        )

    @resource_claims.setter
    def resource_claims(
        self,
        value: typing.Union[
            typing.List["ResourceClaimSchedulingStatus"], typing.List[dict]
        ],
    ):
        """
        ResourceClaims describes resource availability for each
        pod.spec.resourceClaim entry where the corresponding
        ResourceClaim uses "WaitForFirstConsumer" allocation mode.
        """
        cleaned: typing.List[ResourceClaimSchedulingStatus] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimSchedulingStatus,
                    ResourceClaimSchedulingStatus().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimSchedulingStatus, item))
        self._properties["resourceClaims"] = cleaned

    def __enter__(self) -> "PodSchedulingContextStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaim(_kuber_definitions.Resource):
    """
    ResourceClaim describes which resources are needed by a
    resource consumer. Its status tracks whether the resource
    has been allocated and what the resulting attributes are.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimSpec"] = None,
        status: typing.Optional["ResourceClaimStatus"] = None,
    ):
        """Create ResourceClaim instance."""
        super(ResourceClaim, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaim"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimSpec(),
            "status": status if status is not None else ResourceClaimStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimSpec, None),
            "status": (ResourceClaimStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimSpec":
        """
        Spec describes the desired attributes of a resource that
        then needs to be allocated. It can only be set once when
        creating the ResourceClaim.
        """
        return typing.cast(
            "ResourceClaimSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimSpec", dict]):
        """
        Spec describes the desired attributes of a resource that
        then needs to be allocated. It can only be set once when
        creating the ResourceClaim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimSpec,
                ResourceClaimSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ResourceClaimStatus":
        """
        Status describes whether the resource is available and with
        which attributes.
        """
        return typing.cast(
            "ResourceClaimStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ResourceClaimStatus", dict]):
        """
        Status describes whether the resource is available and with
        which attributes.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimStatus,
                ResourceClaimStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Creates the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_resource_claim", "create_resource_claim"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Replaces the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_resource_claim", "replace_resource_claim"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Patches the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_resource_claim", "patch_resource_claim"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_resource_claim",
            "read_resource_claim",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the ResourceClaim from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_claim",
            "read_resource_claim",
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
        Deletes the ResourceClaim from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_claim",
            "delete_resource_claim",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaim":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimConsumerReference(_kuber_definitions.Definition):
    """
    ResourceClaimConsumerReference contains enough information
    to let you locate the consumer of a ResourceClaim. The user
    must be a resource in the same namespace as the
    ResourceClaim.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        uid: typing.Optional[str] = None,
    ):
        """Create ResourceClaimConsumerReference instance."""
        super(ResourceClaimConsumerReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimConsumerReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "name": name if name is not None else "",
            "resource": resource if resource is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "name": (str, None),
            "resource": (str, None),
            "uid": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    @property
    def resource(self) -> str:
        """
        Resource is the type of resource being referenced, for
        example "pods".
        """
        return typing.cast(
            str,
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: str):
        """
        Resource is the type of resource being referenced, for
        example "pods".
        """
        self._properties["resource"] = value

    @property
    def uid(self) -> str:
        """
        UID identifies exactly one incarnation of the resource.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID identifies exactly one incarnation of the resource.
        """
        self._properties["uid"] = value

    def __enter__(self) -> "ResourceClaimConsumerReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimList(_kuber_definitions.Collection):
    """
    ResourceClaimList is a collection of claims.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClaim"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClaimList instance."""
        super(ResourceClaimList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClaim),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClaim"]:
        """
        Items is the list of resource claims.
        """
        return typing.cast(
            typing.List["ResourceClaim"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ResourceClaim"], typing.List[dict]]
    ):
        """
        Items is the list of resource claims.
        """
        cleaned: typing.List[ResourceClaim] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaim,
                    ResourceClaim().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaim, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimParametersReference(_kuber_definitions.Definition):
    """
    ResourceClaimParametersReference contains enough information
    to let you locate the parameters for a ResourceClaim. The
    object must be in the same namespace as the ResourceClaim.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create ResourceClaimParametersReference instance."""
        super(ResourceClaimParametersReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimParametersReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "kind": (str, None),
            "name": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata, for
        example "ConfigMap".
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata, for
        example "ConfigMap".
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    def __enter__(self) -> "ResourceClaimParametersReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimSchedulingStatus(_kuber_definitions.Definition):
    """
    ResourceClaimSchedulingStatus contains information about one
    particular ResourceClaim with "WaitForFirstConsumer"
    allocation mode.
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
        unsuitable_nodes: typing.Optional[typing.List[str]] = None,
    ):
        """Create ResourceClaimSchedulingStatus instance."""
        super(ResourceClaimSchedulingStatus, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimSchedulingStatus"
        )
        self._properties = {
            "name": name if name is not None else "",
            "unsuitableNodes": unsuitable_nodes if unsuitable_nodes is not None else [],
        }
        self._types = {
            "name": (str, None),
            "unsuitableNodes": (list, str),
        }

    @property
    def name(self) -> str:
        """
        Name matches the pod.spec.resourceClaims[*].Name field.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name matches the pod.spec.resourceClaims[*].Name field.
        """
        self._properties["name"] = value

    @property
    def unsuitable_nodes(self) -> typing.List[str]:
        """
        UnsuitableNodes lists nodes that the ResourceClaim cannot be
        allocated for.

        The size of this field is limited to 128, the same as for
        PodSchedulingSpec.PotentialNodes. This may get increased in
        the future, but not reduced.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("unsuitableNodes"),
        )

    @unsuitable_nodes.setter
    def unsuitable_nodes(self, value: typing.List[str]):
        """
        UnsuitableNodes lists nodes that the ResourceClaim cannot be
        allocated for.

        The size of this field is limited to 128, the same as for
        PodSchedulingSpec.PotentialNodes. This may get increased in
        the future, but not reduced.
        """
        self._properties["unsuitableNodes"] = value

    def __enter__(self) -> "ResourceClaimSchedulingStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimSpec(_kuber_definitions.Definition):
    """
    ResourceClaimSpec defines how a resource is to be allocated.
    """

    def __init__(
        self,
        allocation_mode: typing.Optional[str] = None,
        parameters_ref: typing.Optional["ResourceClaimParametersReference"] = None,
        resource_class_name: typing.Optional[str] = None,
    ):
        """Create ResourceClaimSpec instance."""
        super(ResourceClaimSpec, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimSpec"
        )
        self._properties = {
            "allocationMode": allocation_mode if allocation_mode is not None else "",
            "parametersRef": (
                parameters_ref
                if parameters_ref is not None
                else ResourceClaimParametersReference()
            ),
            "resourceClassName": (
                resource_class_name if resource_class_name is not None else ""
            ),
        }
        self._types = {
            "allocationMode": (str, None),
            "parametersRef": (ResourceClaimParametersReference, None),
            "resourceClassName": (str, None),
        }

    @property
    def allocation_mode(self) -> str:
        """
        Allocation can start immediately or when a Pod wants to use
        the resource. "WaitForFirstConsumer" is the default.
        """
        return typing.cast(
            str,
            self._properties.get("allocationMode"),
        )

    @allocation_mode.setter
    def allocation_mode(self, value: str):
        """
        Allocation can start immediately or when a Pod wants to use
        the resource. "WaitForFirstConsumer" is the default.
        """
        self._properties["allocationMode"] = value

    @property
    def parameters_ref(self) -> "ResourceClaimParametersReference":
        """
        ParametersRef references a separate object with arbitrary
        parameters that will be used by the driver when allocating a
        resource for the claim.

        The object must be in the same namespace as the
        ResourceClaim.
        """
        return typing.cast(
            "ResourceClaimParametersReference",
            self._properties.get("parametersRef"),
        )

    @parameters_ref.setter
    def parameters_ref(
        self, value: typing.Union["ResourceClaimParametersReference", dict]
    ):
        """
        ParametersRef references a separate object with arbitrary
        parameters that will be used by the driver when allocating a
        resource for the claim.

        The object must be in the same namespace as the
        ResourceClaim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimParametersReference,
                ResourceClaimParametersReference().from_dict(value),
            )
        self._properties["parametersRef"] = value

    @property
    def resource_class_name(self) -> str:
        """
        ResourceClassName references the driver and additional
        parameters via the name of a ResourceClass that was created
        as part of the driver deployment.
        """
        return typing.cast(
            str,
            self._properties.get("resourceClassName"),
        )

    @resource_class_name.setter
    def resource_class_name(self, value: str):
        """
        ResourceClassName references the driver and additional
        parameters via the name of a ResourceClass that was created
        as part of the driver deployment.
        """
        self._properties["resourceClassName"] = value

    def __enter__(self) -> "ResourceClaimSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimStatus(_kuber_definitions.Definition):
    """
    ResourceClaimStatus tracks whether the resource has been
    allocated and what the resulting attributes are.
    """

    def __init__(
        self,
        allocation: typing.Optional["AllocationResult"] = None,
        deallocation_requested: typing.Optional[bool] = None,
        driver_name: typing.Optional[str] = None,
        reserved_for: typing.Optional[
            typing.List["ResourceClaimConsumerReference"]
        ] = None,
    ):
        """Create ResourceClaimStatus instance."""
        super(ResourceClaimStatus, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimStatus"
        )
        self._properties = {
            "allocation": allocation if allocation is not None else AllocationResult(),
            "deallocationRequested": (
                deallocation_requested if deallocation_requested is not None else None
            ),
            "driverName": driver_name if driver_name is not None else "",
            "reservedFor": reserved_for if reserved_for is not None else [],
        }
        self._types = {
            "allocation": (AllocationResult, None),
            "deallocationRequested": (bool, None),
            "driverName": (str, None),
            "reservedFor": (list, ResourceClaimConsumerReference),
        }

    @property
    def allocation(self) -> "AllocationResult":
        """
        Allocation is set by the resource driver once a resource or
        set of resources has been allocated successfully. If this is
        not specified, the resources have not been allocated yet.
        """
        return typing.cast(
            "AllocationResult",
            self._properties.get("allocation"),
        )

    @allocation.setter
    def allocation(self, value: typing.Union["AllocationResult", dict]):
        """
        Allocation is set by the resource driver once a resource or
        set of resources has been allocated successfully. If this is
        not specified, the resources have not been allocated yet.
        """
        if isinstance(value, dict):
            value = typing.cast(
                AllocationResult,
                AllocationResult().from_dict(value),
            )
        self._properties["allocation"] = value

    @property
    def deallocation_requested(self) -> bool:
        """
        DeallocationRequested indicates that a ResourceClaim is to
        be deallocated.

        The driver then must deallocate this claim and reset the
        field together with clearing the Allocation field.

        While DeallocationRequested is set, no new consumers may be
        added to ReservedFor.
        """
        return typing.cast(
            bool,
            self._properties.get("deallocationRequested"),
        )

    @deallocation_requested.setter
    def deallocation_requested(self, value: bool):
        """
        DeallocationRequested indicates that a ResourceClaim is to
        be deallocated.

        The driver then must deallocate this claim and reset the
        field together with clearing the Allocation field.

        While DeallocationRequested is set, no new consumers may be
        added to ReservedFor.
        """
        self._properties["deallocationRequested"] = value

    @property
    def driver_name(self) -> str:
        """
        DriverName is a copy of the driver name from the
        ResourceClass at the time when allocation started.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName is a copy of the driver name from the
        ResourceClass at the time when allocation started.
        """
        self._properties["driverName"] = value

    @property
    def reserved_for(self) -> typing.List["ResourceClaimConsumerReference"]:
        """
        ReservedFor indicates which entities are currently allowed
        to use the claim. A Pod which references a ResourceClaim
        which is not reserved for that Pod will not be started.

        There can be at most 32 such reservations. This may get
        increased in the future, but not reduced.
        """
        return typing.cast(
            typing.List["ResourceClaimConsumerReference"],
            self._properties.get("reservedFor"),
        )

    @reserved_for.setter
    def reserved_for(
        self,
        value: typing.Union[
            typing.List["ResourceClaimConsumerReference"], typing.List[dict]
        ],
    ):
        """
        ReservedFor indicates which entities are currently allowed
        to use the claim. A Pod which references a ResourceClaim
        which is not reserved for that Pod will not be started.

        There can be at most 32 such reservations. This may get
        increased in the future, but not reduced.
        """
        cleaned: typing.List[ResourceClaimConsumerReference] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimConsumerReference,
                    ResourceClaimConsumerReference().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimConsumerReference, item))
        self._properties["reservedFor"] = cleaned

    def __enter__(self) -> "ResourceClaimStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplate(_kuber_definitions.Resource):
    """
    ResourceClaimTemplate is used to produce ResourceClaim
    objects.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimTemplateSpec"] = None,
    ):
        """Create ResourceClaimTemplate instance."""
        super(ResourceClaimTemplate, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplate"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimTemplateSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimTemplateSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimTemplateSpec":
        """
        Describes the ResourceClaim that is to be generated.

        This field is immutable. A ResourceClaim will get created by
        the control plane for a Pod when needed and then not get
        updated anymore.
        """
        return typing.cast(
            "ResourceClaimTemplateSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimTemplateSpec", dict]):
        """
        Describes the ResourceClaim that is to be generated.

        This field is immutable. A ResourceClaim will get created by
        the control plane for a Pod when needed and then not get
        updated anymore.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimTemplateSpec,
                ResourceClaimTemplateSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_resource_claim_template",
            "create_resource_claim_template",
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
        Replaces the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_resource_claim_template",
            "replace_resource_claim_template",
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
        Patches the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_resource_claim_template",
            "patch_resource_claim_template",
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
        Reads the ResourceClaimTemplate from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_claim_template",
            "read_resource_claim_template",
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
        Deletes the ResourceClaimTemplate from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_claim_template",
            "delete_resource_claim_template",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimTemplate":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplateList(_kuber_definitions.Collection):
    """
    ResourceClaimTemplateList is a collection of claim
    templates.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClaimTemplate"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClaimTemplateList instance."""
        super(ResourceClaimTemplateList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplateList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClaimTemplate),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClaimTemplate"]:
        """
        Items is the list of resource claim templates.
        """
        return typing.cast(
            typing.List["ResourceClaimTemplate"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["ResourceClaimTemplate"], typing.List[dict]],
    ):
        """
        Items is the list of resource claim templates.
        """
        cleaned: typing.List[ResourceClaimTemplate] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimTemplate,
                    ResourceClaimTemplate().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimTemplate, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimTemplateList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplateSpec(_kuber_definitions.Definition):
    """
    ResourceClaimTemplateSpec contains the metadata and fields
    for a ResourceClaim.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimSpec"] = None,
    ):
        """Create ResourceClaimTemplateSpec instance."""
        super(ResourceClaimTemplateSpec, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplateSpec"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimSpec(),
        }
        self._types = {
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        ObjectMeta may contain labels and annotations that will be
        copied into the PVC when creating it. No other fields are
        allowed and will be rejected during validation.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        ObjectMeta may contain labels and annotations that will be
        copied into the PVC when creating it. No other fields are
        allowed and will be rejected during validation.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimSpec":
        """
        Spec for the ResourceClaim. The entire content is copied
        unchanged into the ResourceClaim that gets created from this
        template. The same fields as in a ResourceClaim are also
        valid here.
        """
        return typing.cast(
            "ResourceClaimSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimSpec", dict]):
        """
        Spec for the ResourceClaim. The entire content is copied
        unchanged into the ResourceClaim that gets created from this
        template. The same fields as in a ResourceClaim are also
        valid here.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimSpec,
                ResourceClaimSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def __enter__(self) -> "ResourceClaimTemplateSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClass(_kuber_definitions.Resource):
    """
    ResourceClass is used by administrators to influence how
    resources are allocated.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        parameters_ref: typing.Optional["ResourceClassParametersReference"] = None,
        suitable_nodes: typing.Optional["NodeSelector"] = None,
    ):
        """Create ResourceClass instance."""
        super(ResourceClass, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClass"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "parametersRef": (
                parameters_ref
                if parameters_ref is not None
                else ResourceClassParametersReference()
            ),
            "suitableNodes": (
                suitable_nodes if suitable_nodes is not None else NodeSelector()
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "driverName": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "parametersRef": (ResourceClassParametersReference, None),
            "suitableNodes": (NodeSelector, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName defines the name of the dynamic resource driver
        that is used for allocation of a ResourceClaim that uses
        this class.

        Resource drivers have a unique name in forward domain order
        (acme.example.com).
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName defines the name of the dynamic resource driver
        that is used for allocation of a ResourceClaim that uses
        this class.

        Resource drivers have a unique name in forward domain order
        (acme.example.com).
        """
        self._properties["driverName"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def parameters_ref(self) -> "ResourceClassParametersReference":
        """
        ParametersRef references an arbitrary separate object that
        may hold parameters that will be used by the driver when
        allocating a resource that uses this class. A dynamic
        resource driver can distinguish between parameters stored
        here and and those stored in ResourceClaimSpec.
        """
        return typing.cast(
            "ResourceClassParametersReference",
            self._properties.get("parametersRef"),
        )

    @parameters_ref.setter
    def parameters_ref(
        self, value: typing.Union["ResourceClassParametersReference", dict]
    ):
        """
        ParametersRef references an arbitrary separate object that
        may hold parameters that will be used by the driver when
        allocating a resource that uses this class. A dynamic
        resource driver can distinguish between parameters stored
        here and and those stored in ResourceClaimSpec.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClassParametersReference,
                ResourceClassParametersReference().from_dict(value),
            )
        self._properties["parametersRef"] = value

    @property
    def suitable_nodes(self) -> "NodeSelector":
        """
        Only nodes matching the selector will be considered by the
        scheduler when trying to find a Node that fits a Pod when
        that Pod uses a ResourceClaim that has not been allocated
        yet.

        Setting this field is optional. If null, all nodes are
        candidates.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("suitableNodes"),
        )

    @suitable_nodes.setter
    def suitable_nodes(self, value: typing.Union["NodeSelector", dict]):
        """
        Only nodes matching the selector will be considered by the
        scheduler when trying to find a Node that fits a Pod when
        that Pod uses a ResourceClaim that has not been allocated
        yet.

        Setting this field is optional. If null, all nodes are
        candidates.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["suitableNodes"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_resource_class", "create_resource_class"]

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
        Replaces the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_resource_class", "replace_resource_class"]

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
        Patches the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_resource_class", "patch_resource_class"]

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
        Reads the ResourceClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_class",
            "read_resource_class",
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
        Deletes the ResourceClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_class",
            "delete_resource_class",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassList(_kuber_definitions.Collection):
    """
    ResourceClassList is a collection of classes.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClassList instance."""
        super(ResourceClassList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClass"]:
        """
        Items is the list of resource classes.
        """
        return typing.cast(
            typing.List["ResourceClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ResourceClass"], typing.List[dict]]
    ):
        """
        Items is the list of resource classes.
        """
        cleaned: typing.List[ResourceClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClass,
                    ResourceClass().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClass, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassParametersReference(_kuber_definitions.Definition):
    """
    ResourceClassParametersReference contains enough information
    to let you locate the parameters for a ResourceClass.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
    ):
        """Create ResourceClassParametersReference instance."""
        super(ResourceClassParametersReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassParametersReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "namespace": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata.
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace that contains the referenced resource. Must be
        empty for cluster-scoped resources and non-empty for
        namespaced resources.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace that contains the referenced resource. Must be
        empty for cluster-scoped resources and non-empty for
        namespaced resources.
        """
        self._properties["namespace"] = value

    def __enter__(self) -> "ResourceClassParametersReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceHandle(_kuber_definitions.Definition):
    """
    ResourceHandle holds opaque resource data for processing by
    a specific kubelet plugin.
    """

    def __init__(
        self,
        data: typing.Optional[str] = None,
        driver_name: typing.Optional[str] = None,
    ):
        """Create ResourceHandle instance."""
        super(ResourceHandle, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceHandle"
        )
        self._properties = {
            "data": data if data is not None else "",
            "driverName": driver_name if driver_name is not None else "",
        }
        self._types = {
            "data": (str, None),
            "driverName": (str, None),
        }

    @property
    def data(self) -> str:
        """
        Data contains the opaque data associated with this
        ResourceHandle. It is set by the controller component of the
        resource driver whose name matches the DriverName set in the
        ResourceClaimStatus this ResourceHandle is embedded in. It
        is set at allocation time and is intended for processing by
        the kubelet plugin whose name matches the DriverName set in
        this ResourceHandle.

        The maximum size of this field is 16KiB. This may get
        increased in the future, but not reduced.
        """
        return typing.cast(
            str,
            self._properties.get("data"),
        )

    @data.setter
    def data(self, value: str):
        """
        Data contains the opaque data associated with this
        ResourceHandle. It is set by the controller component of the
        resource driver whose name matches the DriverName set in the
        ResourceClaimStatus this ResourceHandle is embedded in. It
        is set at allocation time and is intended for processing by
        the kubelet plugin whose name matches the DriverName set in
        this ResourceHandle.

        The maximum size of this field is 16KiB. This may get
        increased in the future, but not reduced.
        """
        self._properties["data"] = value

    @property
    def driver_name(self) -> str:
        """
        DriverName specifies the name of the resource driver whose
        kubelet plugin should be invoked to process this
        ResourceHandle's data once it lands on a node. This may
        differ from the DriverName set in ResourceClaimStatus this
        ResourceHandle is embedded in.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName specifies the name of the resource driver whose
        kubelet plugin should be invoked to process this
        ResourceHandle's data once it lands on a node. This may
        differ from the DriverName set in ResourceClaimStatus this
        ResourceHandle is embedded in.
        """
        self._properties["driverName"] = value

    def __enter__(self) -> "ResourceHandle":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

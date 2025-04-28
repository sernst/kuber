import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import Condition  # noqa: F401
from kuber.v1_31.meta_v1 import DeleteOptions  # noqa: F401
from kuber.v1_31.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_31.meta_v1 import Status  # noqa: F401
from kuber.v1_31.meta_v1 import StatusDetails  # noqa: F401


class Eviction(_kuber_definitions.Resource):
    """
    Eviction evicts a pod from its node subject to certain
    policies and safety constraints. This is a subresource of
    Pod.  A request to cause such an eviction is created by
    POSTing to .../pods/<pod name>/evictions.
    """

    def __init__(
        self,
        delete_options: typing.Optional["DeleteOptions"] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
    ):
        """Create Eviction instance."""
        super(Eviction, self).__init__(api_version="policy/v1", kind="Eviction")
        self._properties = {
            "deleteOptions": (
                delete_options if delete_options is not None else DeleteOptions()
            ),
            "metadata": metadata if metadata is not None else ObjectMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "deleteOptions": (DeleteOptions, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
        }

    @property
    def delete_options(self) -> "DeleteOptions":
        """
        DeleteOptions may be provided
        """
        return typing.cast(
            "DeleteOptions",
            self._properties.get("deleteOptions"),
        )

    @delete_options.setter
    def delete_options(self, value: typing.Union["DeleteOptions", dict]):
        """
        DeleteOptions may be provided
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeleteOptions,
                DeleteOptions().from_dict(value),
            )
        self._properties["deleteOptions"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        ObjectMeta describes the pod that is being evicted.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        ObjectMeta describes the pod that is being evicted.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_eviction", "create_eviction"]

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
        Replaces the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_eviction", "replace_eviction"]

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
        Patches the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_eviction", "patch_eviction"]

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
        Reads the Eviction from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_eviction",
            "read_eviction",
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
        Deletes the Eviction from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_eviction",
            "delete_eviction",
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
    ) -> "client.PolicyV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.PolicyV1Api(**kwargs)

    def __enter__(self) -> "Eviction":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudget(_kuber_definitions.Resource):
    """
    PodDisruptionBudget is an object to define the max
    disruption that can be caused to a collection of pods
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["PodDisruptionBudgetSpec"] = None,
        status: typing.Optional["PodDisruptionBudgetStatus"] = None,
    ):
        """Create PodDisruptionBudget instance."""
        super(PodDisruptionBudget, self).__init__(
            api_version="policy/v1", kind="PodDisruptionBudget"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else PodDisruptionBudgetSpec(),
            "status": status if status is not None else PodDisruptionBudgetStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (PodDisruptionBudgetSpec, None),
            "status": (PodDisruptionBudgetStatus, None),
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
    def spec(self) -> "PodDisruptionBudgetSpec":
        """
        Specification of the desired behavior of the
        PodDisruptionBudget.
        """
        return typing.cast(
            "PodDisruptionBudgetSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["PodDisruptionBudgetSpec", dict]):
        """
        Specification of the desired behavior of the
        PodDisruptionBudget.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodDisruptionBudgetSpec,
                PodDisruptionBudgetSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "PodDisruptionBudgetStatus":
        """
        Most recently observed status of the PodDisruptionBudget.
        """
        return typing.cast(
            "PodDisruptionBudgetStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["PodDisruptionBudgetStatus", dict]):
        """
        Most recently observed status of the PodDisruptionBudget.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodDisruptionBudgetStatus,
                PodDisruptionBudgetStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodDisruptionBudgetStatus":
        """
        Creates the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_pod_disruption_budget",
            "create_pod_disruption_budget",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = PodDisruptionBudgetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodDisruptionBudgetStatus":
        """
        Replaces the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_pod_disruption_budget",
            "replace_pod_disruption_budget",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodDisruptionBudgetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodDisruptionBudgetStatus":
        """
        Patches the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_pod_disruption_budget",
            "patch_pod_disruption_budget",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodDisruptionBudgetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodDisruptionBudgetStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_pod_disruption_budget",
            "read_pod_disruption_budget",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = PodDisruptionBudgetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the PodDisruptionBudget from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_pod_disruption_budget",
            "read_pod_disruption_budget",
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
        Deletes the PodDisruptionBudget from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_pod_disruption_budget",
            "delete_pod_disruption_budget",
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
    ) -> "client.PolicyV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.PolicyV1Api(**kwargs)

    def __enter__(self) -> "PodDisruptionBudget":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetList(_kuber_definitions.Collection):
    """
    PodDisruptionBudgetList is a collection of
    PodDisruptionBudgets.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["PodDisruptionBudget"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create PodDisruptionBudgetList instance."""
        super(PodDisruptionBudgetList, self).__init__(
            api_version="policy/v1", kind="PodDisruptionBudgetList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PodDisruptionBudget),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PodDisruptionBudget"]:
        """
        Items is a list of PodDisruptionBudgets
        """
        return typing.cast(
            typing.List["PodDisruptionBudget"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["PodDisruptionBudget"], typing.List[dict]]
    ):
        """
        Items is a list of PodDisruptionBudgets
        """
        cleaned: typing.List[PodDisruptionBudget] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodDisruptionBudget,
                    PodDisruptionBudget().from_dict(item),
                )
            cleaned.append(typing.cast(PodDisruptionBudget, item))
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
    ) -> "client.PolicyV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.PolicyV1Api(**kwargs)

    def __enter__(self) -> "PodDisruptionBudgetList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetSpec(_kuber_definitions.Definition):
    """
    PodDisruptionBudgetSpec is a description of a
    PodDisruptionBudget.
    """

    def __init__(
        self,
        max_unavailable: typing.Optional[typing.Union[str, int, None]] = None,
        min_available: typing.Optional[typing.Union[str, int, None]] = None,
        selector: typing.Optional["LabelSelector"] = None,
        unhealthy_pod_eviction_policy: typing.Optional[str] = None,
    ):
        """Create PodDisruptionBudgetSpec instance."""
        super(PodDisruptionBudgetSpec, self).__init__(
            api_version="policy/v1", kind="PodDisruptionBudgetSpec"
        )
        self._properties = {
            "maxUnavailable": max_unavailable if max_unavailable is not None else None,
            "minAvailable": min_available if min_available is not None else None,
            "selector": selector if selector is not None else LabelSelector(),
            "unhealthyPodEvictionPolicy": (
                unhealthy_pod_eviction_policy
                if unhealthy_pod_eviction_policy is not None
                else ""
            ),
        }
        self._types = {
            "maxUnavailable": (_types.integer_or_string, None),
            "minAvailable": (_types.integer_or_string, None),
            "selector": (LabelSelector, None),
            "unhealthyPodEvictionPolicy": (str, None),
        }

    @property
    def max_unavailable(self) -> typing.Union[str, int, None]:
        """
        An eviction is allowed if at most "maxUnavailable" pods
        selected by "selector" are unavailable after the eviction,
        i.e. even in absence of the evicted pod. For example, one
        can prevent all voluntary evictions by specifying 0. This is
        a mutually exclusive setting with "minAvailable".
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxUnavailable"),
        )

    @max_unavailable.setter
    def max_unavailable(self, value: typing.Union[str, int, None]):
        """
        An eviction is allowed if at most "maxUnavailable" pods
        selected by "selector" are unavailable after the eviction,
        i.e. even in absence of the evicted pod. For example, one
        can prevent all voluntary evictions by specifying 0. This is
        a mutually exclusive setting with "minAvailable".
        """
        self._properties["maxUnavailable"] = _types.integer_or_string(value)

    @property
    def min_available(self) -> typing.Union[str, int, None]:
        """
        An eviction is allowed if at least "minAvailable" pods
        selected by "selector" will still be available after the
        eviction, i.e. even in the absence of the evicted pod.  So
        for example you can prevent all voluntary evictions by
        specifying "100%".
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("minAvailable"),
        )

    @min_available.setter
    def min_available(self, value: typing.Union[str, int, None]):
        """
        An eviction is allowed if at least "minAvailable" pods
        selected by "selector" will still be available after the
        eviction, i.e. even in the absence of the evicted pod.  So
        for example you can prevent all voluntary evictions by
        specifying "100%".
        """
        self._properties["minAvailable"] = _types.integer_or_string(value)

    @property
    def selector(self) -> "LabelSelector":
        """
        Label query over pods whose evictions are managed by the
        disruption budget. A null selector will match no pods, while
        an empty ({}) selector will select all pods within the
        namespace.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        Label query over pods whose evictions are managed by the
        disruption budget. A null selector will match no pods, while
        an empty ({}) selector will select all pods within the
        namespace.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def unhealthy_pod_eviction_policy(self) -> str:
        """
        UnhealthyPodEvictionPolicy defines the criteria for when
        unhealthy pods should be considered for eviction. Current
        implementation considers healthy pods, as pods that have
        status.conditions item with type="Ready",status="True".

        Valid policies are IfHealthyBudget and AlwaysAllow. If no
        policy is specified, the default behavior will be used,
        which corresponds to the IfHealthyBudget policy.

        IfHealthyBudget policy means that running pods
        (status.phase="Running"), but not yet healthy can be evicted
        only if the guarded application is not disrupted
        (status.currentHealthy is at least equal to
        status.desiredHealthy). Healthy pods will be subject to the
        PDB for eviction.

        AlwaysAllow policy means that all running pods
        (status.phase="Running"), but not yet healthy are considered
        disrupted and can be evicted regardless of whether the
        criteria in a PDB is met. This means perspective running
        pods of a disrupted application might not get a chance to
        become healthy. Healthy pods will be subject to the PDB for
        eviction.

        Additional policies may be added in the future. Clients
        making eviction decisions should disallow eviction of
        unhealthy pods if they encounter an unrecognized policy in
        this field.

        This field is beta-level. The eviction API uses this field
        when the feature gate PDBUnhealthyPodEvictionPolicy is
        enabled (enabled by default).
        """
        return typing.cast(
            str,
            self._properties.get("unhealthyPodEvictionPolicy"),
        )

    @unhealthy_pod_eviction_policy.setter
    def unhealthy_pod_eviction_policy(self, value: str):
        """
        UnhealthyPodEvictionPolicy defines the criteria for when
        unhealthy pods should be considered for eviction. Current
        implementation considers healthy pods, as pods that have
        status.conditions item with type="Ready",status="True".

        Valid policies are IfHealthyBudget and AlwaysAllow. If no
        policy is specified, the default behavior will be used,
        which corresponds to the IfHealthyBudget policy.

        IfHealthyBudget policy means that running pods
        (status.phase="Running"), but not yet healthy can be evicted
        only if the guarded application is not disrupted
        (status.currentHealthy is at least equal to
        status.desiredHealthy). Healthy pods will be subject to the
        PDB for eviction.

        AlwaysAllow policy means that all running pods
        (status.phase="Running"), but not yet healthy are considered
        disrupted and can be evicted regardless of whether the
        criteria in a PDB is met. This means perspective running
        pods of a disrupted application might not get a chance to
        become healthy. Healthy pods will be subject to the PDB for
        eviction.

        Additional policies may be added in the future. Clients
        making eviction decisions should disallow eviction of
        unhealthy pods if they encounter an unrecognized policy in
        this field.

        This field is beta-level. The eviction API uses this field
        when the feature gate PDBUnhealthyPodEvictionPolicy is
        enabled (enabled by default).
        """
        self._properties["unhealthyPodEvictionPolicy"] = value

    def __enter__(self) -> "PodDisruptionBudgetSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetStatus(_kuber_definitions.Definition):
    """
    PodDisruptionBudgetStatus represents information about the
    status of a PodDisruptionBudget. Status may trail the actual
    state of a system.
    """

    def __init__(
        self,
        conditions: typing.Optional[typing.List["Condition"]] = None,
        current_healthy: typing.Optional[int] = None,
        desired_healthy: typing.Optional[int] = None,
        disrupted_pods: typing.Optional[dict] = None,
        disruptions_allowed: typing.Optional[int] = None,
        expected_pods: typing.Optional[int] = None,
        observed_generation: typing.Optional[int] = None,
    ):
        """Create PodDisruptionBudgetStatus instance."""
        super(PodDisruptionBudgetStatus, self).__init__(
            api_version="policy/v1", kind="PodDisruptionBudgetStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
            "currentHealthy": current_healthy if current_healthy is not None else None,
            "desiredHealthy": desired_healthy if desired_healthy is not None else None,
            "disruptedPods": disrupted_pods if disrupted_pods is not None else {},
            "disruptionsAllowed": (
                disruptions_allowed if disruptions_allowed is not None else None
            ),
            "expectedPods": expected_pods if expected_pods is not None else None,
            "observedGeneration": (
                observed_generation if observed_generation is not None else None
            ),
        }
        self._types = {
            "conditions": (list, Condition),
            "currentHealthy": (int, None),
            "desiredHealthy": (int, None),
            "disruptedPods": (dict, None),
            "disruptionsAllowed": (int, None),
            "expectedPods": (int, None),
            "observedGeneration": (int, None),
        }

    @property
    def conditions(self) -> typing.List["Condition"]:
        """
        Conditions contain conditions for PDB. The disruption
        controller sets the DisruptionAllowed condition. The
        following are known values for the reason field (additional
        reasons could be added in the future): - SyncFailed: The
        controller encountered an error and wasn't able to compute
                      the number of allowed disruptions. Therefore
        no disruptions are
                      allowed and the status of the condition will
        be False.
        - InsufficientPods: The number of pods are either at or
        below the number
                            required by the PodDisruptionBudget. No
        disruptions are
                            allowed and the status of the condition
        will be False.
        - SufficientPods: There are more pods than required by the
        PodDisruptionBudget.
                          The condition will be True, and the number
        of allowed
                          disruptions are provided by the
        disruptionsAllowed property.
        """
        return typing.cast(
            typing.List["Condition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["Condition"], typing.List[dict]]
    ):
        """
        Conditions contain conditions for PDB. The disruption
        controller sets the DisruptionAllowed condition. The
        following are known values for the reason field (additional
        reasons could be added in the future): - SyncFailed: The
        controller encountered an error and wasn't able to compute
                      the number of allowed disruptions. Therefore
        no disruptions are
                      allowed and the status of the condition will
        be False.
        - InsufficientPods: The number of pods are either at or
        below the number
                            required by the PodDisruptionBudget. No
        disruptions are
                            allowed and the status of the condition
        will be False.
        - SufficientPods: There are more pods than required by the
        PodDisruptionBudget.
                          The condition will be True, and the number
        of allowed
                          disruptions are provided by the
        disruptionsAllowed property.
        """
        cleaned: typing.List[Condition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Condition,
                    Condition().from_dict(item),
                )
            cleaned.append(typing.cast(Condition, item))
        self._properties["conditions"] = cleaned

    @property
    def current_healthy(self) -> int:
        """
        current number of healthy pods
        """
        return typing.cast(
            int,
            self._properties.get("currentHealthy"),
        )

    @current_healthy.setter
    def current_healthy(self, value: int):
        """
        current number of healthy pods
        """
        self._properties["currentHealthy"] = value

    @property
    def desired_healthy(self) -> int:
        """
        minimum desired number of healthy pods
        """
        return typing.cast(
            int,
            self._properties.get("desiredHealthy"),
        )

    @desired_healthy.setter
    def desired_healthy(self, value: int):
        """
        minimum desired number of healthy pods
        """
        self._properties["desiredHealthy"] = value

    @property
    def disrupted_pods(self) -> dict:
        """
        DisruptedPods contains information about pods whose eviction
        was processed by the API server eviction subresource handler
        but has not yet been observed by the PodDisruptionBudget
        controller. A pod will be in this map from the time when the
        API server processed the eviction request to the time when
        the pod is seen by PDB controller as having been marked for
        deletion (or after a timeout). The key in the map is the
        name of the pod and the value is the time when the API
        server processed the eviction request. If the deletion
        didn't occur and a pod is still there it will be removed
        from the list automatically by PodDisruptionBudget
        controller after some time. If everything goes smooth this
        map should be empty for the most of the time. Large number
        of entries in the map may indicate problems with pod
        deletions.
        """
        return typing.cast(
            dict,
            self._properties.get("disruptedPods"),
        )

    @disrupted_pods.setter
    def disrupted_pods(self, value: dict):
        """
        DisruptedPods contains information about pods whose eviction
        was processed by the API server eviction subresource handler
        but has not yet been observed by the PodDisruptionBudget
        controller. A pod will be in this map from the time when the
        API server processed the eviction request to the time when
        the pod is seen by PDB controller as having been marked for
        deletion (or after a timeout). The key in the map is the
        name of the pod and the value is the time when the API
        server processed the eviction request. If the deletion
        didn't occur and a pod is still there it will be removed
        from the list automatically by PodDisruptionBudget
        controller after some time. If everything goes smooth this
        map should be empty for the most of the time. Large number
        of entries in the map may indicate problems with pod
        deletions.
        """
        self._properties["disruptedPods"] = value

    @property
    def disruptions_allowed(self) -> int:
        """
        Number of pod disruptions that are currently allowed.
        """
        return typing.cast(
            int,
            self._properties.get("disruptionsAllowed"),
        )

    @disruptions_allowed.setter
    def disruptions_allowed(self, value: int):
        """
        Number of pod disruptions that are currently allowed.
        """
        self._properties["disruptionsAllowed"] = value

    @property
    def expected_pods(self) -> int:
        """
        total number of pods counted by this disruption budget
        """
        return typing.cast(
            int,
            self._properties.get("expectedPods"),
        )

    @expected_pods.setter
    def expected_pods(self, value: int):
        """
        total number of pods counted by this disruption budget
        """
        self._properties["expectedPods"] = value

    @property
    def observed_generation(self) -> int:
        """
        Most recent generation observed when updating this PDB
        status. DisruptionsAllowed and other status information is
        valid only if observedGeneration equals to PDB's object
        generation.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        Most recent generation observed when updating this PDB
        status. DisruptionsAllowed and other status information is
        valid only if observedGeneration equals to PDB's object
        generation.
        """
        self._properties["observedGeneration"] = value

    def __enter__(self) -> "PodDisruptionBudgetStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

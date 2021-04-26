import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.pre.meta_v1 import Condition  # noqa: F401
from kuber.pre.meta_v1 import LabelSelector  # noqa: F401
from kuber.pre.meta_v1 import ListMeta  # noqa: F401
from kuber.pre.meta_v1 import ObjectMeta  # noqa: F401
from kuber.pre.meta_v1 import Status  # noqa: F401
from kuber.pre.meta_v1 import StatusDetails  # noqa: F401


class PodDisruptionBudget(_kuber_definitions.Resource):
    """
    PodDisruptionBudget is an object to define the max
    disruption that can be caused to a collection of pods
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "PodDisruptionBudgetSpec" = None,
        status: "PodDisruptionBudgetStatus" = None,
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

    def create_resource(self, namespace: "str" = None) -> "PodDisruptionBudgetStatus":
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

    def replace_resource(self, namespace: "str" = None) -> "PodDisruptionBudgetStatus":
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

    def patch_resource(self, namespace: "str" = None) -> "PodDisruptionBudgetStatus":
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
        self, namespace: "str" = None
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

    def read_resource(self, namespace: str = None):
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
        namespace: str = None,
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
        api_client: client.ApiClient = None, **kwargs
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
        items: typing.List["PodDisruptionBudget"] = None,
        metadata: "ListMeta" = None,
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
        api_client: client.ApiClient = None, **kwargs
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
        max_unavailable: typing.Union[str, int, None] = None,
        min_available: typing.Union[str, int, None] = None,
        selector: "LabelSelector" = None,
    ):
        """Create PodDisruptionBudgetSpec instance."""
        super(PodDisruptionBudgetSpec, self).__init__(
            api_version="policy/v1", kind="PodDisruptionBudgetSpec"
        )
        self._properties = {
            "maxUnavailable": max_unavailable if max_unavailable is not None else None,
            "minAvailable": min_available if min_available is not None else None,
            "selector": selector if selector is not None else LabelSelector(),
        }
        self._types = {
            "maxUnavailable": (_types.integer_or_string, None),
            "minAvailable": (_types.integer_or_string, None),
            "selector": (LabelSelector, None),
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
        conditions: typing.List["Condition"] = None,
        current_healthy: int = None,
        desired_healthy: int = None,
        disrupted_pods: dict = None,
        disruptions_allowed: int = None,
        expected_pods: int = None,
        observed_generation: int = None,
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
            "disruptionsAllowed": disruptions_allowed
            if disruptions_allowed is not None
            else None,
            "expectedPods": expected_pods if expected_pods is not None else None,
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
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

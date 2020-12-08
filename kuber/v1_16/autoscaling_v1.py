import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_16.meta_v1 import ListMeta
from kuber.v1_16.meta_v1 import ObjectMeta
from kuber.v1_16.meta_v1 import Status
from kuber.v1_16.meta_v1 import StatusDetails


class CrossVersionObjectReference(_kuber_definitions.Definition):
    """
    CrossVersionObjectReference contains enough information to
    let you identify the referred resource.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        """Create CrossVersionObjectReference instance."""
        super(CrossVersionObjectReference, self).__init__(
            api_version="autoscaling/v1", kind="CrossVersionObjectReference"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "name": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds"
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds"
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name of the referent; More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name of the referent; More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        self._properties["name"] = value

    def __enter__(self) -> "CrossVersionObjectReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscaler(_kuber_definitions.Resource):
    """
    configuration of a horizontal pod autoscaler.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "HorizontalPodAutoscalerSpec" = None,
        status: "HorizontalPodAutoscalerStatus" = None,
    ):
        """Create HorizontalPodAutoscaler instance."""
        super(HorizontalPodAutoscaler, self).__init__(
            api_version="autoscaling/v1", kind="HorizontalPodAutoscaler"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else HorizontalPodAutoscalerSpec(),
            "status": status if status is not None else HorizontalPodAutoscalerStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (HorizontalPodAutoscalerSpec, None),
            "status": (HorizontalPodAutoscalerStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata. More info:
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
        Standard object metadata. More info:
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
    def spec(self) -> "HorizontalPodAutoscalerSpec":
        """
        behaviour of autoscaler. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        return typing.cast(
            "HorizontalPodAutoscalerSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["HorizontalPodAutoscalerSpec", dict]):
        """
        behaviour of autoscaler. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        if isinstance(value, dict):
            value = typing.cast(
                HorizontalPodAutoscalerSpec,
                HorizontalPodAutoscalerSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "HorizontalPodAutoscalerStatus":
        """
        current information about the autoscaler.
        """
        return typing.cast(
            "HorizontalPodAutoscalerStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["HorizontalPodAutoscalerStatus", dict]):
        """
        current information about the autoscaler.
        """
        if isinstance(value, dict):
            value = typing.cast(
                HorizontalPodAutoscalerStatus,
                HorizontalPodAutoscalerStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: "str" = None
    ) -> "HorizontalPodAutoscalerStatus":
        """
        Creates the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_horizontal_pod_autoscaler",
            "create_horizontal_pod_autoscaler",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = HorizontalPodAutoscalerStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: "str" = None
    ) -> "HorizontalPodAutoscalerStatus":
        """
        Replaces the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_horizontal_pod_autoscaler",
            "replace_horizontal_pod_autoscaler",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = HorizontalPodAutoscalerStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: "str" = None
    ) -> "HorizontalPodAutoscalerStatus":
        """
        Patches the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_horizontal_pod_autoscaler",
            "patch_horizontal_pod_autoscaler",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = HorizontalPodAutoscalerStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: "str" = None
    ) -> "HorizontalPodAutoscalerStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_horizontal_pod_autoscaler",
            "read_horizontal_pod_autoscaler",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = HorizontalPodAutoscalerStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the HorizontalPodAutoscaler from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_horizontal_pod_autoscaler",
            "read_horizontal_pod_autoscaler",
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
        Deletes the HorizontalPodAutoscaler from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_horizontal_pod_autoscaler",
            "delete_horizontal_pod_autoscaler",
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
    ) -> "client.AutoscalingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AutoscalingV1Api(**kwargs)

    def __enter__(self) -> "HorizontalPodAutoscaler":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerList(_kuber_definitions.Collection):
    """
    list of horizontal pod autoscaler objects.
    """

    def __init__(
        self,
        items: typing.List["HorizontalPodAutoscaler"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create HorizontalPodAutoscalerList instance."""
        super(HorizontalPodAutoscalerList, self).__init__(
            api_version="autoscaling/v1", kind="HorizontalPodAutoscalerList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, HorizontalPodAutoscaler),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["HorizontalPodAutoscaler"]:
        """
        list of horizontal pod autoscaler objects.
        """
        return typing.cast(
            typing.List["HorizontalPodAutoscaler"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["HorizontalPodAutoscaler"], typing.List[dict]],
    ):
        """
        list of horizontal pod autoscaler objects.
        """
        cleaned: typing.List[HorizontalPodAutoscaler] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    HorizontalPodAutoscaler,
                    HorizontalPodAutoscaler().from_dict(item),
                )
            cleaned.append(typing.cast(HorizontalPodAutoscaler, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata.
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
    ) -> "client.AutoscalingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AutoscalingV1Api(**kwargs)

    def __enter__(self) -> "HorizontalPodAutoscalerList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerSpec(_kuber_definitions.Definition):
    """
    specification of a horizontal pod autoscaler.
    """

    def __init__(
        self,
        max_replicas: int = None,
        min_replicas: int = None,
        scale_target_ref: "CrossVersionObjectReference" = None,
        target_cpuutilization_percentage: int = None,
    ):
        """Create HorizontalPodAutoscalerSpec instance."""
        super(HorizontalPodAutoscalerSpec, self).__init__(
            api_version="autoscaling/v1", kind="HorizontalPodAutoscalerSpec"
        )
        self._properties = {
            "maxReplicas": max_replicas if max_replicas is not None else None,
            "minReplicas": min_replicas if min_replicas is not None else None,
            "scaleTargetRef": scale_target_ref
            if scale_target_ref is not None
            else CrossVersionObjectReference(),
            "targetCPUUtilizationPercentage": target_cpuutilization_percentage
            if target_cpuutilization_percentage is not None
            else None,
        }
        self._types = {
            "maxReplicas": (int, None),
            "minReplicas": (int, None),
            "scaleTargetRef": (CrossVersionObjectReference, None),
            "targetCPUUtilizationPercentage": (int, None),
        }

    @property
    def max_replicas(self) -> int:
        """
        upper limit for the number of pods that can be set by the
        autoscaler; cannot be smaller than MinReplicas.
        """
        return typing.cast(
            int,
            self._properties.get("maxReplicas"),
        )

    @max_replicas.setter
    def max_replicas(self, value: int):
        """
        upper limit for the number of pods that can be set by the
        autoscaler; cannot be smaller than MinReplicas.
        """
        self._properties["maxReplicas"] = value

    @property
    def min_replicas(self) -> int:
        """
        minReplicas is the lower limit for the number of replicas to
        which the autoscaler can scale down.  It defaults to 1 pod.
        minReplicas is allowed to be 0 if the alpha feature gate
        HPAScaleToZero is enabled and at least one Object or
        External metric is configured.  Scaling is active as long as
        at least one metric value is available.
        """
        return typing.cast(
            int,
            self._properties.get("minReplicas"),
        )

    @min_replicas.setter
    def min_replicas(self, value: int):
        """
        minReplicas is the lower limit for the number of replicas to
        which the autoscaler can scale down.  It defaults to 1 pod.
        minReplicas is allowed to be 0 if the alpha feature gate
        HPAScaleToZero is enabled and at least one Object or
        External metric is configured.  Scaling is active as long as
        at least one metric value is available.
        """
        self._properties["minReplicas"] = value

    @property
    def scale_target_ref(self) -> "CrossVersionObjectReference":
        """
        reference to scaled resource; horizontal pod autoscaler will
        learn the current resource consumption and will set the
        desired number of pods by using its Scale subresource.
        """
        return typing.cast(
            "CrossVersionObjectReference",
            self._properties.get("scaleTargetRef"),
        )

    @scale_target_ref.setter
    def scale_target_ref(
        self, value: typing.Union["CrossVersionObjectReference", dict]
    ):
        """
        reference to scaled resource; horizontal pod autoscaler will
        learn the current resource consumption and will set the
        desired number of pods by using its Scale subresource.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CrossVersionObjectReference,
                CrossVersionObjectReference().from_dict(value),
            )
        self._properties["scaleTargetRef"] = value

    @property
    def target_cpuutilization_percentage(self) -> int:
        """
        target average CPU utilization (represented as a percentage
        of requested CPU) over all the pods; if not specified the
        default autoscaling policy will be used.
        """
        return typing.cast(
            int,
            self._properties.get("targetCPUUtilizationPercentage"),
        )

    @target_cpuutilization_percentage.setter
    def target_cpuutilization_percentage(self, value: int):
        """
        target average CPU utilization (represented as a percentage
        of requested CPU) over all the pods; if not specified the
        default autoscaling policy will be used.
        """
        self._properties["targetCPUUtilizationPercentage"] = value

    def __enter__(self) -> "HorizontalPodAutoscalerSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerStatus(_kuber_definitions.Definition):
    """
    current status of a horizontal pod autoscaler
    """

    def __init__(
        self,
        current_cpuutilization_percentage: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        observed_generation: int = None,
    ):
        """Create HorizontalPodAutoscalerStatus instance."""
        super(HorizontalPodAutoscalerStatus, self).__init__(
            api_version="autoscaling/v1", kind="HorizontalPodAutoscalerStatus"
        )
        self._properties = {
            "currentCPUUtilizationPercentage": current_cpuutilization_percentage
            if current_cpuutilization_percentage is not None
            else None,
            "currentReplicas": current_replicas
            if current_replicas is not None
            else None,
            "desiredReplicas": desired_replicas
            if desired_replicas is not None
            else None,
            "lastScaleTime": last_scale_time if last_scale_time is not None else None,
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
        }
        self._types = {
            "currentCPUUtilizationPercentage": (int, None),
            "currentReplicas": (int, None),
            "desiredReplicas": (int, None),
            "lastScaleTime": (str, None),
            "observedGeneration": (int, None),
        }

    @property
    def current_cpuutilization_percentage(self) -> int:
        """
        current average CPU utilization over all pods, represented
        as a percentage of requested CPU, e.g. 70 means that an
        average pod is using now 70% of its requested CPU.
        """
        return typing.cast(
            int,
            self._properties.get("currentCPUUtilizationPercentage"),
        )

    @current_cpuutilization_percentage.setter
    def current_cpuutilization_percentage(self, value: int):
        """
        current average CPU utilization over all pods, represented
        as a percentage of requested CPU, e.g. 70 means that an
        average pod is using now 70% of its requested CPU.
        """
        self._properties["currentCPUUtilizationPercentage"] = value

    @property
    def current_replicas(self) -> int:
        """
        current number of replicas of pods managed by this
        autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("currentReplicas"),
        )

    @current_replicas.setter
    def current_replicas(self, value: int):
        """
        current number of replicas of pods managed by this
        autoscaler.
        """
        self._properties["currentReplicas"] = value

    @property
    def desired_replicas(self) -> int:
        """
        desired number of replicas of pods managed by this
        autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("desiredReplicas"),
        )

    @desired_replicas.setter
    def desired_replicas(self, value: int):
        """
        desired number of replicas of pods managed by this
        autoscaler.
        """
        self._properties["desiredReplicas"] = value

    @property
    def last_scale_time(self) -> str:
        """
        last time the HorizontalPodAutoscaler scaled the number of
        pods; used by the autoscaler to control how often the number
        of pods is changed.
        """
        return typing.cast(
            str,
            self._properties.get("lastScaleTime"),
        )

    @last_scale_time.setter
    def last_scale_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        last time the HorizontalPodAutoscaler scaled the number of
        pods; used by the autoscaler to control how often the number
        of pods is changed.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastScaleTime"] = value

    @property
    def observed_generation(self) -> int:
        """
        most recent generation observed by this autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        most recent generation observed by this autoscaler.
        """
        self._properties["observedGeneration"] = value

    def __enter__(self) -> "HorizontalPodAutoscalerStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scale(_kuber_definitions.Resource):
    """
    Scale represents a scaling request for a resource.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "ScaleSpec" = None,
        status: "ScaleStatus" = None,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(api_version="autoscaling/v1", kind="Scale")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ScaleSpec(),
            "status": status if status is not None else ScaleStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ScaleSpec, None),
            "status": (ScaleStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ScaleSpec":
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        return typing.cast(
            "ScaleSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ScaleSpec", dict]):
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ScaleSpec,
                ScaleSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ScaleStatus":
        """
        current status of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status. Read-only.
        """
        return typing.cast(
            "ScaleStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ScaleStatus", dict]):
        """
        current status of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status. Read-only.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ScaleStatus,
                ScaleStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "ScaleStatus":
        """
        Creates the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_scale", "create_scale"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ScaleStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "ScaleStatus":
        """
        Replaces the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_scale", "replace_scale"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ScaleStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "ScaleStatus":
        """
        Patches the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_scale", "patch_scale"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ScaleStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "ScaleStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_scale", "read_scale"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ScaleStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the Scale from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_scale",
            "read_scale",
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
        Deletes the Scale from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_scale",
            "delete_scale",
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
    ) -> "client.AutoscalingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AutoscalingV1Api(**kwargs)

    def __enter__(self) -> "Scale":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleSpec(_kuber_definitions.Definition):
    """
    ScaleSpec describes the attributes of a scale subresource.
    """

    def __init__(
        self,
        replicas: int = None,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(api_version="autoscaling/v1", kind="ScaleSpec")
        self._properties = {
            "replicas": replicas if replicas is not None else None,
        }
        self._types = {
            "replicas": (int, None),
        }

    @property
    def replicas(self) -> int:
        """
        desired number of instances for the scaled object.
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        desired number of instances for the scaled object.
        """
        self._properties["replicas"] = value

    def __enter__(self) -> "ScaleSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleStatus(_kuber_definitions.Definition):
    """
    ScaleStatus represents the current status of a scale
    subresource.
    """

    def __init__(
        self,
        replicas: int = None,
        selector: str = None,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version="autoscaling/v1", kind="ScaleStatus"
        )
        self._properties = {
            "replicas": replicas if replicas is not None else None,
            "selector": selector if selector is not None else "",
        }
        self._types = {
            "replicas": (int, None),
            "selector": (str, None),
        }

    @property
    def replicas(self) -> int:
        """
        actual number of observed instances of the scaled object.
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        actual number of observed instances of the scaled object.
        """
        self._properties["replicas"] = value

    @property
    def selector(self) -> str:
        """
        label query over pods that should match the replicas count.
        This is same as the label selector but in the string format
        to avoid introspection by clients. The string will be in the
        same format as the query-param syntax. More info about label
        selectors: http://kubernetes.io/docs/user-
        guide/labels#label-selectors
        """
        return typing.cast(
            str,
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: str):
        """
        label query over pods that should match the replicas count.
        This is same as the label selector but in the string format
        to avoid introspection by clients. The string will be in the
        same format as the query-param syntax. More info about label
        selectors: http://kubernetes.io/docs/user-
        guide/labels#label-selectors
        """
        self._properties["selector"] = value

    def __enter__(self) -> "ScaleStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

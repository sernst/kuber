import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_21.meta_v1 import LabelSelector
from kuber.v1_21.meta_v1 import ListMeta
from kuber.v1_21.meta_v1 import ObjectMeta
from kuber.v1_21.meta_v1 import Status
from kuber.v1_21.meta_v1 import StatusDetails


class ContainerResourceMetricSource(_kuber_definitions.Definition):
    """
    ContainerResourceMetricSource indicates how to scale on a
    resource metric known to Kubernetes, as specified in
    requests and limits, describing each pod in the current
    scale target (e.g. CPU or memory).  The values will be
    averaged together before being compared to the target.  Such
    metrics are built in to Kubernetes, and have special scaling
    options on top of those available to normal per-pod metrics
    using the "pods" source.  Only one "target" type should be
    set.
    """

    def __init__(
        self,
        container: str = None,
        name: str = None,
        target_average_utilization: int = None,
        target_average_value: typing.Union[str, int, None] = None,
    ):
        """Create ContainerResourceMetricSource instance."""
        super(ContainerResourceMetricSource, self).__init__(
            api_version="autoscaling/v2beta1", kind="ContainerResourceMetricSource"
        )
        self._properties = {
            "container": container if container is not None else "",
            "name": name if name is not None else "",
            "targetAverageUtilization": target_average_utilization
            if target_average_utilization is not None
            else None,
            "targetAverageValue": target_average_value
            if target_average_value is not None
            else None,
        }
        self._types = {
            "container": (str, None),
            "name": (str, None),
            "targetAverageUtilization": (int, None),
            "targetAverageValue": (str, None),
        }

    @property
    def container(self) -> str:
        """
        container is the name of the container in the pods of the
        scaling target
        """
        return typing.cast(
            str,
            self._properties.get("container"),
        )

    @container.setter
    def container(self, value: str):
        """
        container is the name of the container in the pods of the
        scaling target
        """
        self._properties["container"] = value

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties["name"] = value

    @property
    def target_average_utilization(self) -> int:
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        return typing.cast(
            int,
            self._properties.get("targetAverageUtilization"),
        )

    @target_average_utilization.setter
    def target_average_utilization(self, value: int):
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        self._properties["targetAverageUtilization"] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        value = self._properties.get("targetAverageValue")
        return f"{value}" if value is not None else None

    @target_average_value.setter
    def target_average_value(self, value: typing.Union[str, int, None]):
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        self._properties["targetAverageValue"] = None if value is None else f"{value}"

    def __enter__(self) -> "ContainerResourceMetricSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ContainerResourceMetricStatus(_kuber_definitions.Definition):
    """
    ContainerResourceMetricStatus indicates the current value of
    a resource metric known to Kubernetes, as specified in
    requests and limits, describing a single container in each
    pod in the current scale target (e.g. CPU or memory).  Such
    metrics are built in to Kubernetes, and have special scaling
    options on top of those available to normal per-pod metrics
    using the "pods" source.
    """

    def __init__(
        self,
        container: str = None,
        current_average_utilization: int = None,
        current_average_value: typing.Union[str, int, None] = None,
        name: str = None,
    ):
        """Create ContainerResourceMetricStatus instance."""
        super(ContainerResourceMetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="ContainerResourceMetricStatus"
        )
        self._properties = {
            "container": container if container is not None else "",
            "currentAverageUtilization": current_average_utilization
            if current_average_utilization is not None
            else None,
            "currentAverageValue": current_average_value
            if current_average_value is not None
            else None,
            "name": name if name is not None else "",
        }
        self._types = {
            "container": (str, None),
            "currentAverageUtilization": (int, None),
            "currentAverageValue": (str, None),
            "name": (str, None),
        }

    @property
    def container(self) -> str:
        """
        container is the name of the container in the pods of the
        scaling target
        """
        return typing.cast(
            str,
            self._properties.get("container"),
        )

    @container.setter
    def container(self, value: str):
        """
        container is the name of the container in the pods of the
        scaling target
        """
        self._properties["container"] = value

    @property
    def current_average_utilization(self) -> int:
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.  It will only be present if
        `targetAverageValue` was set in the corresponding metric
        specification.
        """
        return typing.cast(
            int,
            self._properties.get("currentAverageUtilization"),
        )

    @current_average_utilization.setter
    def current_average_utilization(self, value: int):
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.  It will only be present if
        `targetAverageValue` was set in the corresponding metric
        specification.
        """
        self._properties["currentAverageUtilization"] = value

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        value = self._properties.get("currentAverageValue")
        return f"{value}" if value is not None else None

    @current_average_value.setter
    def current_average_value(self, value: typing.Union[str, int, None]):
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        self._properties["currentAverageValue"] = None if value is None else f"{value}"

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties["name"] = value

    def __enter__(self) -> "ContainerResourceMetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


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
            api_version="autoscaling/v2beta1", kind="CrossVersionObjectReference"
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


class ExternalMetricSource(_kuber_definitions.Definition):
    """
    ExternalMetricSource indicates how to scale on a metric not
    associated with any Kubernetes object (for example length of
    queue in cloud messaging service, or QPS from loadbalancer
    running outside of cluster). Exactly one "target" type
    should be set.
    """

    def __init__(
        self,
        metric_name: str = None,
        metric_selector: "LabelSelector" = None,
        target_average_value: typing.Union[str, int, None] = None,
        target_value: typing.Union[str, int, None] = None,
    ):
        """Create ExternalMetricSource instance."""
        super(ExternalMetricSource, self).__init__(
            api_version="autoscaling/v2beta1", kind="ExternalMetricSource"
        )
        self._properties = {
            "metricName": metric_name if metric_name is not None else "",
            "metricSelector": metric_selector
            if metric_selector is not None
            else LabelSelector(),
            "targetAverageValue": target_average_value
            if target_average_value is not None
            else None,
            "targetValue": target_value if target_value is not None else None,
        }
        self._types = {
            "metricName": (str, None),
            "metricSelector": (LabelSelector, None),
            "targetAverageValue": (str, None),
            "targetValue": (str, None),
        }

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties["metricName"] = value

    @property
    def metric_selector(self) -> "LabelSelector":
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("metricSelector"),
        )

    @metric_selector.setter
    def metric_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["metricSelector"] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target per-pod value of global
        metric (as a quantity). Mutually exclusive with TargetValue.
        """
        value = self._properties.get("targetAverageValue")
        return f"{value}" if value is not None else None

    @target_average_value.setter
    def target_average_value(self, value: typing.Union[str, int, None]):
        """
        targetAverageValue is the target per-pod value of global
        metric (as a quantity). Mutually exclusive with TargetValue.
        """
        self._properties["targetAverageValue"] = None if value is None else f"{value}"

    @property
    def target_value(self) -> typing.Optional[str]:
        """
        targetValue is the target value of the metric (as a
        quantity). Mutually exclusive with TargetAverageValue.
        """
        value = self._properties.get("targetValue")
        return f"{value}" if value is not None else None

    @target_value.setter
    def target_value(self, value: typing.Union[str, int, None]):
        """
        targetValue is the target value of the metric (as a
        quantity). Mutually exclusive with TargetAverageValue.
        """
        self._properties["targetValue"] = None if value is None else f"{value}"

    def __enter__(self) -> "ExternalMetricSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ExternalMetricStatus(_kuber_definitions.Definition):
    """
    ExternalMetricStatus indicates the current value of a global
    metric not associated with any Kubernetes object.
    """

    def __init__(
        self,
        current_average_value: typing.Union[str, int, None] = None,
        current_value: typing.Union[str, int, None] = None,
        metric_name: str = None,
        metric_selector: "LabelSelector" = None,
    ):
        """Create ExternalMetricStatus instance."""
        super(ExternalMetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="ExternalMetricStatus"
        )
        self._properties = {
            "currentAverageValue": current_average_value
            if current_average_value is not None
            else None,
            "currentValue": current_value if current_value is not None else None,
            "metricName": metric_name if metric_name is not None else "",
            "metricSelector": metric_selector
            if metric_selector is not None
            else LabelSelector(),
        }
        self._types = {
            "currentAverageValue": (str, None),
            "currentValue": (str, None),
            "metricName": (str, None),
            "metricSelector": (LabelSelector, None),
        }

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of metric averaged
        over autoscaled pods.
        """
        value = self._properties.get("currentAverageValue")
        return f"{value}" if value is not None else None

    @current_average_value.setter
    def current_average_value(self, value: typing.Union[str, int, None]):
        """
        currentAverageValue is the current value of metric averaged
        over autoscaled pods.
        """
        self._properties["currentAverageValue"] = None if value is None else f"{value}"

    @property
    def current_value(self) -> typing.Optional[str]:
        """
        currentValue is the current value of the metric (as a
        quantity)
        """
        value = self._properties.get("currentValue")
        return f"{value}" if value is not None else None

    @current_value.setter
    def current_value(self, value: typing.Union[str, int, None]):
        """
        currentValue is the current value of the metric (as a
        quantity)
        """
        self._properties["currentValue"] = None if value is None else f"{value}"

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of a metric used for autoscaling in
        metric system.
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of a metric used for autoscaling in
        metric system.
        """
        self._properties["metricName"] = value

    @property
    def metric_selector(self) -> "LabelSelector":
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("metricSelector"),
        )

    @metric_selector.setter
    def metric_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["metricSelector"] = value

    def __enter__(self) -> "ExternalMetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscaler(_kuber_definitions.Resource):
    """
    HorizontalPodAutoscaler is the configuration for a
    horizontal pod autoscaler, which automatically manages the
    replica count of any resource implementing the scale
    subresource based on the metrics specified.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "HorizontalPodAutoscalerSpec" = None,
        status: "HorizontalPodAutoscalerStatus" = None,
    ):
        """Create HorizontalPodAutoscaler instance."""
        super(HorizontalPodAutoscaler, self).__init__(
            api_version="autoscaling/v2beta1", kind="HorizontalPodAutoscaler"
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
        metadata is the standard object metadata. More info:
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
        metadata is the standard object metadata. More info:
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
        spec is the specification for the behaviour of the
        autoscaler. More info:
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
        spec is the specification for the behaviour of the
        autoscaler. More info:
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
        status is the current information about the autoscaler.
        """
        return typing.cast(
            "HorizontalPodAutoscalerStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["HorizontalPodAutoscalerStatus", dict]):
        """
        status is the current information about the autoscaler.
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
    ) -> "client.AutoscalingV2beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AutoscalingV2beta1Api(**kwargs)

    def __enter__(self) -> "HorizontalPodAutoscaler":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerCondition(_kuber_definitions.Definition):
    """
    HorizontalPodAutoscalerCondition describes the state of a
    HorizontalPodAutoscaler at a certain point.
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create HorizontalPodAutoscalerCondition instance."""
        super(HorizontalPodAutoscalerCondition, self).__init__(
            api_version="autoscaling/v2beta1", kind="HorizontalPodAutoscalerCondition"
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        lastTransitionTime is the last time the condition
        transitioned from one status to another
        """
        return typing.cast(
            str,
            self._properties.get("lastTransitionTime"),
        )

    @last_transition_time.setter
    def last_transition_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        lastTransitionTime is the last time the condition
        transitioned from one status to another
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        message is a human-readable explanation containing details
        about the transition
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        message is a human-readable explanation containing details
        about the transition
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        reason is the reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        reason is the reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        status is the status of the condition (True, False, Unknown)
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        status is the status of the condition (True, False, Unknown)
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        type describes the current condition
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type describes the current condition
        """
        self._properties["type"] = value

    def __enter__(self) -> "HorizontalPodAutoscalerCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerList(_kuber_definitions.Collection):
    """
    HorizontalPodAutoscaler is a list of horizontal pod
    autoscaler objects.
    """

    def __init__(
        self,
        items: typing.List["HorizontalPodAutoscaler"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create HorizontalPodAutoscalerList instance."""
        super(HorizontalPodAutoscalerList, self).__init__(
            api_version="autoscaling/v2beta1", kind="HorizontalPodAutoscalerList"
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
        items is the list of horizontal pod autoscaler objects.
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
        items is the list of horizontal pod autoscaler objects.
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
        metadata is the standard list metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        metadata is the standard list metadata.
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
    ) -> "client.AutoscalingV2beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AutoscalingV2beta1Api(**kwargs)

    def __enter__(self) -> "HorizontalPodAutoscalerList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerSpec(_kuber_definitions.Definition):
    """
    HorizontalPodAutoscalerSpec describes the desired
    functionality of the HorizontalPodAutoscaler.
    """

    def __init__(
        self,
        max_replicas: int = None,
        metrics: typing.List["MetricSpec"] = None,
        min_replicas: int = None,
        scale_target_ref: "CrossVersionObjectReference" = None,
    ):
        """Create HorizontalPodAutoscalerSpec instance."""
        super(HorizontalPodAutoscalerSpec, self).__init__(
            api_version="autoscaling/v2beta1", kind="HorizontalPodAutoscalerSpec"
        )
        self._properties = {
            "maxReplicas": max_replicas if max_replicas is not None else None,
            "metrics": metrics if metrics is not None else [],
            "minReplicas": min_replicas if min_replicas is not None else None,
            "scaleTargetRef": scale_target_ref
            if scale_target_ref is not None
            else CrossVersionObjectReference(),
        }
        self._types = {
            "maxReplicas": (int, None),
            "metrics": (list, MetricSpec),
            "minReplicas": (int, None),
            "scaleTargetRef": (CrossVersionObjectReference, None),
        }

    @property
    def max_replicas(self) -> int:
        """
        maxReplicas is the upper limit for the number of replicas to
        which the autoscaler can scale up. It cannot be less that
        minReplicas.
        """
        return typing.cast(
            int,
            self._properties.get("maxReplicas"),
        )

    @max_replicas.setter
    def max_replicas(self, value: int):
        """
        maxReplicas is the upper limit for the number of replicas to
        which the autoscaler can scale up. It cannot be less that
        minReplicas.
        """
        self._properties["maxReplicas"] = value

    @property
    def metrics(self) -> typing.List["MetricSpec"]:
        """
        metrics contains the specifications for which to use to
        calculate the desired replica count (the maximum replica
        count across all metrics will be used).  The desired replica
        count is calculated multiplying the ratio between the target
        value and the current value by the current number of pods.
        Ergo, metrics used must decrease as the pod count is
        increased, and vice-versa.  See the individual metric source
        types for more information about how each type of metric
        must respond.
        """
        return typing.cast(
            typing.List["MetricSpec"],
            self._properties.get("metrics"),
        )

    @metrics.setter
    def metrics(
        self, value: typing.Union[typing.List["MetricSpec"], typing.List[dict]]
    ):
        """
        metrics contains the specifications for which to use to
        calculate the desired replica count (the maximum replica
        count across all metrics will be used).  The desired replica
        count is calculated multiplying the ratio between the target
        value and the current value by the current number of pods.
        Ergo, metrics used must decrease as the pod count is
        increased, and vice-versa.  See the individual metric source
        types for more information about how each type of metric
        must respond.
        """
        cleaned: typing.List[MetricSpec] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MetricSpec,
                    MetricSpec().from_dict(item),
                )
            cleaned.append(typing.cast(MetricSpec, item))
        self._properties["metrics"] = cleaned

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
        scaleTargetRef points to the target resource to scale, and
        is used to the pods for which metrics should be collected,
        as well as to actually change the replica count.
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
        scaleTargetRef points to the target resource to scale, and
        is used to the pods for which metrics should be collected,
        as well as to actually change the replica count.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CrossVersionObjectReference,
                CrossVersionObjectReference().from_dict(value),
            )
        self._properties["scaleTargetRef"] = value

    def __enter__(self) -> "HorizontalPodAutoscalerSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerStatus(_kuber_definitions.Definition):
    """
    HorizontalPodAutoscalerStatus describes the current status
    of a horizontal pod autoscaler.
    """

    def __init__(
        self,
        conditions: typing.List["HorizontalPodAutoscalerCondition"] = None,
        current_metrics: typing.List["MetricStatus"] = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        observed_generation: int = None,
    ):
        """Create HorizontalPodAutoscalerStatus instance."""
        super(HorizontalPodAutoscalerStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="HorizontalPodAutoscalerStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
            "currentMetrics": current_metrics if current_metrics is not None else [],
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
            "conditions": (list, HorizontalPodAutoscalerCondition),
            "currentMetrics": (list, MetricStatus),
            "currentReplicas": (int, None),
            "desiredReplicas": (int, None),
            "lastScaleTime": (str, None),
            "observedGeneration": (int, None),
        }

    @property
    def conditions(self) -> typing.List["HorizontalPodAutoscalerCondition"]:
        """
        conditions is the set of conditions required for this
        autoscaler to scale its target, and indicates whether or not
        those conditions are met.
        """
        return typing.cast(
            typing.List["HorizontalPodAutoscalerCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[
            typing.List["HorizontalPodAutoscalerCondition"], typing.List[dict]
        ],
    ):
        """
        conditions is the set of conditions required for this
        autoscaler to scale its target, and indicates whether or not
        those conditions are met.
        """
        cleaned: typing.List[HorizontalPodAutoscalerCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    HorizontalPodAutoscalerCondition,
                    HorizontalPodAutoscalerCondition().from_dict(item),
                )
            cleaned.append(typing.cast(HorizontalPodAutoscalerCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def current_metrics(self) -> typing.List["MetricStatus"]:
        """
        currentMetrics is the last read state of the metrics used by
        this autoscaler.
        """
        return typing.cast(
            typing.List["MetricStatus"],
            self._properties.get("currentMetrics"),
        )

    @current_metrics.setter
    def current_metrics(
        self, value: typing.Union[typing.List["MetricStatus"], typing.List[dict]]
    ):
        """
        currentMetrics is the last read state of the metrics used by
        this autoscaler.
        """
        cleaned: typing.List[MetricStatus] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MetricStatus,
                    MetricStatus().from_dict(item),
                )
            cleaned.append(typing.cast(MetricStatus, item))
        self._properties["currentMetrics"] = cleaned

    @property
    def current_replicas(self) -> int:
        """
        currentReplicas is current number of replicas of pods
        managed by this autoscaler, as last seen by the autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("currentReplicas"),
        )

    @current_replicas.setter
    def current_replicas(self, value: int):
        """
        currentReplicas is current number of replicas of pods
        managed by this autoscaler, as last seen by the autoscaler.
        """
        self._properties["currentReplicas"] = value

    @property
    def desired_replicas(self) -> int:
        """
        desiredReplicas is the desired number of replicas of pods
        managed by this autoscaler, as last calculated by the
        autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("desiredReplicas"),
        )

    @desired_replicas.setter
    def desired_replicas(self, value: int):
        """
        desiredReplicas is the desired number of replicas of pods
        managed by this autoscaler, as last calculated by the
        autoscaler.
        """
        self._properties["desiredReplicas"] = value

    @property
    def last_scale_time(self) -> str:
        """
        lastScaleTime is the last time the HorizontalPodAutoscaler
        scaled the number of pods, used by the autoscaler to control
        how often the number of pods is changed.
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
        lastScaleTime is the last time the HorizontalPodAutoscaler
        scaled the number of pods, used by the autoscaler to control
        how often the number of pods is changed.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastScaleTime"] = value

    @property
    def observed_generation(self) -> int:
        """
        observedGeneration is the most recent generation observed by
        this autoscaler.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        observedGeneration is the most recent generation observed by
        this autoscaler.
        """
        self._properties["observedGeneration"] = value

    def __enter__(self) -> "HorizontalPodAutoscalerStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MetricSpec(_kuber_definitions.Definition):
    """
    MetricSpec specifies how to scale based on a single metric
    (only `type` and one other matching field should be set at
    once).
    """

    def __init__(
        self,
        container_resource: "ContainerResourceMetricSource" = None,
        external: "ExternalMetricSource" = None,
        object_: "ObjectMetricSource" = None,
        pods: "PodsMetricSource" = None,
        resource: "ResourceMetricSource" = None,
        type_: str = None,
    ):
        """Create MetricSpec instance."""
        super(MetricSpec, self).__init__(
            api_version="autoscaling/v2beta1", kind="MetricSpec"
        )
        self._properties = {
            "containerResource": container_resource
            if container_resource is not None
            else ContainerResourceMetricSource(),
            "external": external if external is not None else ExternalMetricSource(),
            "object": object_ if object_ is not None else ObjectMetricSource(),
            "pods": pods if pods is not None else PodsMetricSource(),
            "resource": resource if resource is not None else ResourceMetricSource(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "containerResource": (ContainerResourceMetricSource, None),
            "external": (ExternalMetricSource, None),
            "object": (ObjectMetricSource, None),
            "pods": (PodsMetricSource, None),
            "resource": (ResourceMetricSource, None),
            "type": (str, None),
        }

    @property
    def container_resource(self) -> "ContainerResourceMetricSource":
        """
        container resource refers to a resource metric (such as
        those specified in requests and limits) known to Kubernetes
        describing a single container in each pod of the current
        scale target (e.g. CPU or memory). Such metrics are built in
        to Kubernetes, and have special scaling options on top of
        those available to normal per-pod metrics using the "pods"
        source. This is an alpha feature and can be enabled by the
        HPAContainerMetrics feature flag.
        """
        return typing.cast(
            "ContainerResourceMetricSource",
            self._properties.get("containerResource"),
        )

    @container_resource.setter
    def container_resource(
        self, value: typing.Union["ContainerResourceMetricSource", dict]
    ):
        """
        container resource refers to a resource metric (such as
        those specified in requests and limits) known to Kubernetes
        describing a single container in each pod of the current
        scale target (e.g. CPU or memory). Such metrics are built in
        to Kubernetes, and have special scaling options on top of
        those available to normal per-pod metrics using the "pods"
        source. This is an alpha feature and can be enabled by the
        HPAContainerMetrics feature flag.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ContainerResourceMetricSource,
                ContainerResourceMetricSource().from_dict(value),
            )
        self._properties["containerResource"] = value

    @property
    def external(self) -> "ExternalMetricSource":
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        return typing.cast(
            "ExternalMetricSource",
            self._properties.get("external"),
        )

    @external.setter
    def external(self, value: typing.Union["ExternalMetricSource", dict]):
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        if isinstance(value, dict):
            value = typing.cast(
                ExternalMetricSource,
                ExternalMetricSource().from_dict(value),
            )
        self._properties["external"] = value

    @property
    def object_(self) -> "ObjectMetricSource":
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        return typing.cast(
            "ObjectMetricSource",
            self._properties.get("object"),
        )

    @object_.setter
    def object_(self, value: typing.Union["ObjectMetricSource", dict]):
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMetricSource,
                ObjectMetricSource().from_dict(value),
            )
        self._properties["object"] = value

    @property
    def pods(self) -> "PodsMetricSource":
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        return typing.cast(
            "PodsMetricSource",
            self._properties.get("pods"),
        )

    @pods.setter
    def pods(self, value: typing.Union["PodsMetricSource", dict]):
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodsMetricSource,
                PodsMetricSource().from_dict(value),
            )
        self._properties["pods"] = value

    @property
    def resource(self) -> "ResourceMetricSource":
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        return typing.cast(
            "ResourceMetricSource",
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: typing.Union["ResourceMetricSource", dict]):
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceMetricSource,
                ResourceMetricSource().from_dict(value),
            )
        self._properties["resource"] = value

    @property
    def type_(self) -> str:
        """
        type is the type of metric source.  It should be one of
        "ContainerResource", "External", "Object", "Pods" or
        "Resource", each mapping to a matching field in the object.
        Note: "ContainerResource" type is available on when the
        feature-gate HPAContainerMetrics is enabled
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type is the type of metric source.  It should be one of
        "ContainerResource", "External", "Object", "Pods" or
        "Resource", each mapping to a matching field in the object.
        Note: "ContainerResource" type is available on when the
        feature-gate HPAContainerMetrics is enabled
        """
        self._properties["type"] = value

    def __enter__(self) -> "MetricSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MetricStatus(_kuber_definitions.Definition):
    """
    MetricStatus describes the last-read state of a single
    metric.
    """

    def __init__(
        self,
        container_resource: "ContainerResourceMetricStatus" = None,
        external: "ExternalMetricStatus" = None,
        object_: "ObjectMetricStatus" = None,
        pods: "PodsMetricStatus" = None,
        resource: "ResourceMetricStatus" = None,
        type_: str = None,
    ):
        """Create MetricStatus instance."""
        super(MetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="MetricStatus"
        )
        self._properties = {
            "containerResource": container_resource
            if container_resource is not None
            else ContainerResourceMetricStatus(),
            "external": external if external is not None else ExternalMetricStatus(),
            "object": object_ if object_ is not None else ObjectMetricStatus(),
            "pods": pods if pods is not None else PodsMetricStatus(),
            "resource": resource if resource is not None else ResourceMetricStatus(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "containerResource": (ContainerResourceMetricStatus, None),
            "external": (ExternalMetricStatus, None),
            "object": (ObjectMetricStatus, None),
            "pods": (PodsMetricStatus, None),
            "resource": (ResourceMetricStatus, None),
            "type": (str, None),
        }

    @property
    def container_resource(self) -> "ContainerResourceMetricStatus":
        """
        container resource refers to a resource metric (such as
        those specified in requests and limits) known to Kubernetes
        describing a single container in each pod in the current
        scale target (e.g. CPU or memory). Such metrics are built in
        to Kubernetes, and have special scaling options on top of
        those available to normal per-pod metrics using the "pods"
        source.
        """
        return typing.cast(
            "ContainerResourceMetricStatus",
            self._properties.get("containerResource"),
        )

    @container_resource.setter
    def container_resource(
        self, value: typing.Union["ContainerResourceMetricStatus", dict]
    ):
        """
        container resource refers to a resource metric (such as
        those specified in requests and limits) known to Kubernetes
        describing a single container in each pod in the current
        scale target (e.g. CPU or memory). Such metrics are built in
        to Kubernetes, and have special scaling options on top of
        those available to normal per-pod metrics using the "pods"
        source.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ContainerResourceMetricStatus,
                ContainerResourceMetricStatus().from_dict(value),
            )
        self._properties["containerResource"] = value

    @property
    def external(self) -> "ExternalMetricStatus":
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        return typing.cast(
            "ExternalMetricStatus",
            self._properties.get("external"),
        )

    @external.setter
    def external(self, value: typing.Union["ExternalMetricStatus", dict]):
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        if isinstance(value, dict):
            value = typing.cast(
                ExternalMetricStatus,
                ExternalMetricStatus().from_dict(value),
            )
        self._properties["external"] = value

    @property
    def object_(self) -> "ObjectMetricStatus":
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        return typing.cast(
            "ObjectMetricStatus",
            self._properties.get("object"),
        )

    @object_.setter
    def object_(self, value: typing.Union["ObjectMetricStatus", dict]):
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMetricStatus,
                ObjectMetricStatus().from_dict(value),
            )
        self._properties["object"] = value

    @property
    def pods(self) -> "PodsMetricStatus":
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        return typing.cast(
            "PodsMetricStatus",
            self._properties.get("pods"),
        )

    @pods.setter
    def pods(self, value: typing.Union["PodsMetricStatus", dict]):
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodsMetricStatus,
                PodsMetricStatus().from_dict(value),
            )
        self._properties["pods"] = value

    @property
    def resource(self) -> "ResourceMetricStatus":
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        return typing.cast(
            "ResourceMetricStatus",
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: typing.Union["ResourceMetricStatus", dict]):
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceMetricStatus,
                ResourceMetricStatus().from_dict(value),
            )
        self._properties["resource"] = value

    @property
    def type_(self) -> str:
        """
        type is the type of metric source.  It will be one of
        "ContainerResource", "External", "Object", "Pods" or
        "Resource", each corresponds to a matching field in the
        object. Note: "ContainerResource" type is available on when
        the feature-gate HPAContainerMetrics is enabled
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type is the type of metric source.  It will be one of
        "ContainerResource", "External", "Object", "Pods" or
        "Resource", each corresponds to a matching field in the
        object. Note: "ContainerResource" type is available on when
        the feature-gate HPAContainerMetrics is enabled
        """
        self._properties["type"] = value

    def __enter__(self) -> "MetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ObjectMetricSource(_kuber_definitions.Definition):
    """
    ObjectMetricSource indicates how to scale on a metric
    describing a kubernetes object (for example, hits-per-second
    on an Ingress object).
    """

    def __init__(
        self,
        average_value: typing.Union[str, int, None] = None,
        metric_name: str = None,
        selector: "LabelSelector" = None,
        target: "CrossVersionObjectReference" = None,
        target_value: typing.Union[str, int, None] = None,
    ):
        """Create ObjectMetricSource instance."""
        super(ObjectMetricSource, self).__init__(
            api_version="autoscaling/v2beta1", kind="ObjectMetricSource"
        )
        self._properties = {
            "averageValue": average_value if average_value is not None else None,
            "metricName": metric_name if metric_name is not None else "",
            "selector": selector if selector is not None else LabelSelector(),
            "target": target if target is not None else CrossVersionObjectReference(),
            "targetValue": target_value if target_value is not None else None,
        }
        self._types = {
            "averageValue": (str, None),
            "metricName": (str, None),
            "selector": (LabelSelector, None),
            "target": (CrossVersionObjectReference, None),
            "targetValue": (str, None),
        }

    @property
    def average_value(self) -> typing.Optional[str]:
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get("averageValue")
        return f"{value}" if value is not None else None

    @average_value.setter
    def average_value(self, value: typing.Union[str, int, None]):
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties["averageValue"] = None if value is None else f"{value}"

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties["metricName"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def target(self) -> "CrossVersionObjectReference":
        """
        target is the described Kubernetes object.
        """
        return typing.cast(
            "CrossVersionObjectReference",
            self._properties.get("target"),
        )

    @target.setter
    def target(self, value: typing.Union["CrossVersionObjectReference", dict]):
        """
        target is the described Kubernetes object.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CrossVersionObjectReference,
                CrossVersionObjectReference().from_dict(value),
            )
        self._properties["target"] = value

    @property
    def target_value(self) -> typing.Optional[str]:
        """
        targetValue is the target value of the metric (as a
        quantity).
        """
        value = self._properties.get("targetValue")
        return f"{value}" if value is not None else None

    @target_value.setter
    def target_value(self, value: typing.Union[str, int, None]):
        """
        targetValue is the target value of the metric (as a
        quantity).
        """
        self._properties["targetValue"] = None if value is None else f"{value}"

    def __enter__(self) -> "ObjectMetricSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ObjectMetricStatus(_kuber_definitions.Definition):
    """
    ObjectMetricStatus indicates the current value of a metric
    describing a kubernetes object (for example, hits-per-second
    on an Ingress object).
    """

    def __init__(
        self,
        average_value: typing.Union[str, int, None] = None,
        current_value: typing.Union[str, int, None] = None,
        metric_name: str = None,
        selector: "LabelSelector" = None,
        target: "CrossVersionObjectReference" = None,
    ):
        """Create ObjectMetricStatus instance."""
        super(ObjectMetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="ObjectMetricStatus"
        )
        self._properties = {
            "averageValue": average_value if average_value is not None else None,
            "currentValue": current_value if current_value is not None else None,
            "metricName": metric_name if metric_name is not None else "",
            "selector": selector if selector is not None else LabelSelector(),
            "target": target if target is not None else CrossVersionObjectReference(),
        }
        self._types = {
            "averageValue": (str, None),
            "currentValue": (str, None),
            "metricName": (str, None),
            "selector": (LabelSelector, None),
            "target": (CrossVersionObjectReference, None),
        }

    @property
    def average_value(self) -> typing.Optional[str]:
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get("averageValue")
        return f"{value}" if value is not None else None

    @average_value.setter
    def average_value(self, value: typing.Union[str, int, None]):
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties["averageValue"] = None if value is None else f"{value}"

    @property
    def current_value(self) -> typing.Optional[str]:
        """
        currentValue is the current value of the metric (as a
        quantity).
        """
        value = self._properties.get("currentValue")
        return f"{value}" if value is not None else None

    @current_value.setter
    def current_value(self, value: typing.Union[str, int, None]):
        """
        currentValue is the current value of the metric (as a
        quantity).
        """
        self._properties["currentValue"] = None if value is None else f"{value}"

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties["metricName"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        ObjectMetricSource, it is passed as an additional parameter
        to the metrics server for more specific metrics scoping.
        When unset, just the metricName will be used to gather
        metrics.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        ObjectMetricSource, it is passed as an additional parameter
        to the metrics server for more specific metrics scoping.
        When unset, just the metricName will be used to gather
        metrics.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def target(self) -> "CrossVersionObjectReference":
        """
        target is the described Kubernetes object.
        """
        return typing.cast(
            "CrossVersionObjectReference",
            self._properties.get("target"),
        )

    @target.setter
    def target(self, value: typing.Union["CrossVersionObjectReference", dict]):
        """
        target is the described Kubernetes object.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CrossVersionObjectReference,
                CrossVersionObjectReference().from_dict(value),
            )
        self._properties["target"] = value

    def __enter__(self) -> "ObjectMetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodsMetricSource(_kuber_definitions.Definition):
    """
    PodsMetricSource indicates how to scale on a metric
    describing each pod in the current scale target (for
    example, transactions-processed-per-second). The values will
    be averaged together before being compared to the target
    value.
    """

    def __init__(
        self,
        metric_name: str = None,
        selector: "LabelSelector" = None,
        target_average_value: typing.Union[str, int, None] = None,
    ):
        """Create PodsMetricSource instance."""
        super(PodsMetricSource, self).__init__(
            api_version="autoscaling/v2beta1", kind="PodsMetricSource"
        )
        self._properties = {
            "metricName": metric_name if metric_name is not None else "",
            "selector": selector if selector is not None else LabelSelector(),
            "targetAverageValue": target_average_value
            if target_average_value is not None
            else None,
        }
        self._types = {
            "metricName": (str, None),
            "selector": (LabelSelector, None),
            "targetAverageValue": (str, None),
        }

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question
        """
        self._properties["metricName"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get("targetAverageValue")
        return f"{value}" if value is not None else None

    @target_average_value.setter
    def target_average_value(self, value: typing.Union[str, int, None]):
        """
        targetAverageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties["targetAverageValue"] = None if value is None else f"{value}"

    def __enter__(self) -> "PodsMetricSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodsMetricStatus(_kuber_definitions.Definition):
    """
    PodsMetricStatus indicates the current value of a metric
    describing each pod in the current scale target (for
    example, transactions-processed-per-second).
    """

    def __init__(
        self,
        current_average_value: typing.Union[str, int, None] = None,
        metric_name: str = None,
        selector: "LabelSelector" = None,
    ):
        """Create PodsMetricStatus instance."""
        super(PodsMetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="PodsMetricStatus"
        )
        self._properties = {
            "currentAverageValue": current_average_value
            if current_average_value is not None
            else None,
            "metricName": metric_name if metric_name is not None else "",
            "selector": selector if selector is not None else LabelSelector(),
        }
        self._types = {
            "currentAverageValue": (str, None),
            "metricName": (str, None),
            "selector": (LabelSelector, None),
        }

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of the average of
        the metric across all relevant pods (as a quantity)
        """
        value = self._properties.get("currentAverageValue")
        return f"{value}" if value is not None else None

    @current_average_value.setter
    def current_average_value(self, value: typing.Union[str, int, None]):
        """
        currentAverageValue is the current value of the average of
        the metric across all relevant pods (as a quantity)
        """
        self._properties["currentAverageValue"] = None if value is None else f"{value}"

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question
        """
        return typing.cast(
            str,
            self._properties.get("metricName"),
        )

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question
        """
        self._properties["metricName"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        PodsMetricSource, it is passed as an additional parameter to
        the metrics server for more specific metrics scoping. When
        unset, just the metricName will be used to gather metrics.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        PodsMetricSource, it is passed as an additional parameter to
        the metrics server for more specific metrics scoping. When
        unset, just the metricName will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    def __enter__(self) -> "PodsMetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceMetricSource(_kuber_definitions.Definition):
    """
    ResourceMetricSource indicates how to scale on a resource
    metric known to Kubernetes, as specified in requests and
    limits, describing each pod in the current scale target
    (e.g. CPU or memory).  The values will be averaged together
    before being compared to the target.  Such metrics are built
    in to Kubernetes, and have special scaling options on top of
    those available to normal per-pod metrics using the "pods"
    source.  Only one "target" type should be set.
    """

    def __init__(
        self,
        name: str = None,
        target_average_utilization: int = None,
        target_average_value: typing.Union[str, int, None] = None,
    ):
        """Create ResourceMetricSource instance."""
        super(ResourceMetricSource, self).__init__(
            api_version="autoscaling/v2beta1", kind="ResourceMetricSource"
        )
        self._properties = {
            "name": name if name is not None else "",
            "targetAverageUtilization": target_average_utilization
            if target_average_utilization is not None
            else None,
            "targetAverageValue": target_average_value
            if target_average_value is not None
            else None,
        }
        self._types = {
            "name": (str, None),
            "targetAverageUtilization": (int, None),
            "targetAverageValue": (str, None),
        }

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties["name"] = value

    @property
    def target_average_utilization(self) -> int:
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        return typing.cast(
            int,
            self._properties.get("targetAverageUtilization"),
        )

    @target_average_utilization.setter
    def target_average_utilization(self, value: int):
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        self._properties["targetAverageUtilization"] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        value = self._properties.get("targetAverageValue")
        return f"{value}" if value is not None else None

    @target_average_value.setter
    def target_average_value(self, value: typing.Union[str, int, None]):
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        self._properties["targetAverageValue"] = None if value is None else f"{value}"

    def __enter__(self) -> "ResourceMetricSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceMetricStatus(_kuber_definitions.Definition):
    """
    ResourceMetricStatus indicates the current value of a
    resource metric known to Kubernetes, as specified in
    requests and limits, describing each pod in the current
    scale target (e.g. CPU or memory).  Such metrics are built
    in to Kubernetes, and have special scaling options on top of
    those available to normal per-pod metrics using the "pods"
    source.
    """

    def __init__(
        self,
        current_average_utilization: int = None,
        current_average_value: typing.Union[str, int, None] = None,
        name: str = None,
    ):
        """Create ResourceMetricStatus instance."""
        super(ResourceMetricStatus, self).__init__(
            api_version="autoscaling/v2beta1", kind="ResourceMetricStatus"
        )
        self._properties = {
            "currentAverageUtilization": current_average_utilization
            if current_average_utilization is not None
            else None,
            "currentAverageValue": current_average_value
            if current_average_value is not None
            else None,
            "name": name if name is not None else "",
        }
        self._types = {
            "currentAverageUtilization": (int, None),
            "currentAverageValue": (str, None),
            "name": (str, None),
        }

    @property
    def current_average_utilization(self) -> int:
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.  It will only be present if
        `targetAverageValue` was set in the corresponding metric
        specification.
        """
        return typing.cast(
            int,
            self._properties.get("currentAverageUtilization"),
        )

    @current_average_utilization.setter
    def current_average_utilization(self, value: int):
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.  It will only be present if
        `targetAverageValue` was set in the corresponding metric
        specification.
        """
        self._properties["currentAverageUtilization"] = value

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        value = self._properties.get("currentAverageValue")
        return f"{value}" if value is not None else None

    @current_average_value.setter
    def current_average_value(self, value: typing.Union[str, int, None]):
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        self._properties["currentAverageValue"] = None if value is None else f"{value}"

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties["name"] = value

    def __enter__(self) -> "ResourceMetricStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_14.meta_v1 import LabelSelector
from kuber.v1_14.meta_v1 import ListMeta
from kuber.v1_14.meta_v1 import ObjectMeta
from kuber.v1_14.meta_v1 import Status
from kuber.v1_14.meta_v1 import StatusDetails


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
            api_version='autoscaling/v2beta1',
            kind='CrossVersionObjectReference'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'kind': kind or '',
            'name': name or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'name': (str, None),

        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent
        """
        return self._properties.get('apiVersion')

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent
        """
        self._properties['apiVersion'] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent; More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds"
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent; More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds"
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        Name of the referent; More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent; More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        self._properties['name'] = value

    def __enter__(self) -> 'CrossVersionObjectReference':
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
            metric_selector: 'LabelSelector' = None,
            target_average_value: typing.Union[str, int, None] = None,
            target_value: typing.Union[str, int, None] = None,
    ):
        """Create ExternalMetricSource instance."""
        super(ExternalMetricSource, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='ExternalMetricSource'
        )
        self._properties = {
            'metricName': metric_name or '',
            'metricSelector': metric_selector or LabelSelector(),
            'targetAverageValue': target_average_value or None,
            'targetValue': target_value or None,

        }
        self._types = {
            'metricName': (str, None),
            'metricSelector': (LabelSelector, None),
            'targetAverageValue': (str, None),
            'targetValue': (str, None),

        }

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties['metricName'] = value

    @property
    def metric_selector(self) -> 'LabelSelector':
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        return self._properties.get('metricSelector')

    @metric_selector.setter
    def metric_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['metricSelector'] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target per-pod value of global
        metric (as a quantity). Mutually exclusive with TargetValue.
        """
        value = self._properties.get('targetAverageValue')
        return f'{value}' if value is not None else None

    @target_average_value.setter
    def target_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        targetAverageValue is the target per-pod value of global
        metric (as a quantity). Mutually exclusive with TargetValue.
        """
        self._properties['targetAverageValue'] = None if value is None else f'{value}'

    @property
    def target_value(self) -> typing.Optional[str]:
        """
        targetValue is the target value of the metric (as a
        quantity). Mutually exclusive with TargetAverageValue.
        """
        value = self._properties.get('targetValue')
        return f'{value}' if value is not None else None

    @target_value.setter
    def target_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        targetValue is the target value of the metric (as a
        quantity). Mutually exclusive with TargetAverageValue.
        """
        self._properties['targetValue'] = None if value is None else f'{value}'

    def __enter__(self) -> 'ExternalMetricSource':
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
            metric_selector: 'LabelSelector' = None,
    ):
        """Create ExternalMetricStatus instance."""
        super(ExternalMetricStatus, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='ExternalMetricStatus'
        )
        self._properties = {
            'currentAverageValue': current_average_value or None,
            'currentValue': current_value or None,
            'metricName': metric_name or '',
            'metricSelector': metric_selector or LabelSelector(),

        }
        self._types = {
            'currentAverageValue': (str, None),
            'currentValue': (str, None),
            'metricName': (str, None),
            'metricSelector': (LabelSelector, None),

        }

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of metric averaged
        over autoscaled pods.
        """
        value = self._properties.get('currentAverageValue')
        return f'{value}' if value is not None else None

    @current_average_value.setter
    def current_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        currentAverageValue is the current value of metric averaged
        over autoscaled pods.
        """
        self._properties['currentAverageValue'] = None if value is None else f'{value}'

    @property
    def current_value(self) -> typing.Optional[str]:
        """
        currentValue is the current value of the metric (as a
        quantity)
        """
        value = self._properties.get('currentValue')
        return f'{value}' if value is not None else None

    @current_value.setter
    def current_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        currentValue is the current value of the metric (as a
        quantity)
        """
        self._properties['currentValue'] = None if value is None else f'{value}'

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of a metric used for autoscaling in
        metric system.
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of a metric used for autoscaling in
        metric system.
        """
        self._properties['metricName'] = value

    @property
    def metric_selector(self) -> 'LabelSelector':
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        return self._properties.get('metricSelector')

    @metric_selector.setter
    def metric_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        metricSelector is used to identify a specific time series
        within a given metric.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['metricSelector'] = value

    def __enter__(self) -> 'ExternalMetricStatus':
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
            metadata: 'ObjectMeta' = None,
            spec: 'HorizontalPodAutoscalerSpec' = None,
            status: 'HorizontalPodAutoscalerStatus' = None,
    ):
        """Create HorizontalPodAutoscaler instance."""
        super(HorizontalPodAutoscaler, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='HorizontalPodAutoscaler'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or HorizontalPodAutoscalerSpec(),
            'status': status or HorizontalPodAutoscalerStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (HorizontalPodAutoscalerSpec, None),
            'status': (HorizontalPodAutoscalerStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        metadata is the standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        metadata is the standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'HorizontalPodAutoscalerSpec':
        """
        spec is the specification for the behaviour of the
        autoscaler. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['HorizontalPodAutoscalerSpec', dict]):
        """
        spec is the specification for the behaviour of the
        autoscaler. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status.
        """
        if isinstance(value, dict):
            value = HorizontalPodAutoscalerSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'HorizontalPodAutoscalerStatus':
        """
        status is the current information about the autoscaler.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['HorizontalPodAutoscalerStatus', dict]):
        """
        status is the current information about the autoscaler.
        """
        if isinstance(value, dict):
            value = HorizontalPodAutoscalerStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'HorizontalPodAutoscalerStatus':
        """
        Creates the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_horizontal_pod_autoscaler',
            'create_horizontal_pod_autoscaler'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            HorizontalPodAutoscalerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'HorizontalPodAutoscalerStatus':
        """
        Replaces the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_horizontal_pod_autoscaler',
            'replace_horizontal_pod_autoscaler'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            HorizontalPodAutoscalerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'HorizontalPodAutoscalerStatus':
        """
        Patches the HorizontalPodAutoscaler in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_horizontal_pod_autoscaler',
            'patch_horizontal_pod_autoscaler'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            HorizontalPodAutoscalerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'HorizontalPodAutoscalerStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_horizontal_pod_autoscaler',
            'read_horizontal_pod_autoscaler'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            HorizontalPodAutoscalerStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the HorizontalPodAutoscaler from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_horizontal_pod_autoscaler',
            'read_horizontal_pod_autoscaler'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the HorizontalPodAutoscaler from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_horizontal_pod_autoscaler',
            'delete_horizontal_pod_autoscaler'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.AutoscalingV2beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AutoscalingV2beta1Api(**kwargs)

    def __enter__(self) -> 'HorizontalPodAutoscaler':
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
            api_version='autoscaling/v2beta1',
            kind='HorizontalPodAutoscalerCondition'
        )
        self._properties = {
            'lastTransitionTime': last_transition_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastTransitionTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_transition_time(self) -> str:
        """
        lastTransitionTime is the last time the condition
        transitioned from one status to another
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        lastTransitionTime is the last time the condition
        transitioned from one status to another
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        message is a human-readable explanation containing details
        about the transition
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        message is a human-readable explanation containing details
        about the transition
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        reason is the reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        reason is the reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        status is the status of the condition (True, False, Unknown)
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        status is the status of the condition (True, False, Unknown)
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        type describes the current condition
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        type describes the current condition
        """
        self._properties['type'] = value

    def __enter__(self) -> 'HorizontalPodAutoscalerCondition':
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
            items: typing.List['HorizontalPodAutoscaler'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create HorizontalPodAutoscalerList instance."""
        super(HorizontalPodAutoscalerList, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='HorizontalPodAutoscalerList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, HorizontalPodAutoscaler),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['HorizontalPodAutoscaler']:
        """
        items is the list of horizontal pod autoscaler objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['HorizontalPodAutoscaler'], typing.List[dict]]
    ):
        """
        items is the list of horizontal pod autoscaler objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HorizontalPodAutoscaler().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        metadata is the standard list metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        metadata is the standard list metadata.
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.AutoscalingV2beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AutoscalingV2beta1Api(**kwargs)

    def __enter__(self) -> 'HorizontalPodAutoscalerList':
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
            metrics: typing.List['MetricSpec'] = None,
            min_replicas: int = None,
            scale_target_ref: 'CrossVersionObjectReference' = None,
    ):
        """Create HorizontalPodAutoscalerSpec instance."""
        super(HorizontalPodAutoscalerSpec, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='HorizontalPodAutoscalerSpec'
        )
        self._properties = {
            'maxReplicas': max_replicas or None,
            'metrics': metrics or [],
            'minReplicas': min_replicas or None,
            'scaleTargetRef': scale_target_ref or CrossVersionObjectReference(),

        }
        self._types = {
            'maxReplicas': (int, None),
            'metrics': (list, MetricSpec),
            'minReplicas': (int, None),
            'scaleTargetRef': (CrossVersionObjectReference, None),

        }

    @property
    def max_replicas(self) -> int:
        """
        maxReplicas is the upper limit for the number of replicas to
        which the autoscaler can scale up. It cannot be less that
        minReplicas.
        """
        return self._properties.get('maxReplicas')

    @max_replicas.setter
    def max_replicas(self, value: int):
        """
        maxReplicas is the upper limit for the number of replicas to
        which the autoscaler can scale up. It cannot be less that
        minReplicas.
        """
        self._properties['maxReplicas'] = value

    @property
    def metrics(self) -> typing.List['MetricSpec']:
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
        return self._properties.get('metrics')

    @metrics.setter
    def metrics(
            self,
            value: typing.Union[typing.List['MetricSpec'], typing.List[dict]]
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
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = MetricSpec().from_dict(item)
            cleaned.append(item)
        self._properties['metrics'] = cleaned

    @property
    def min_replicas(self) -> int:
        """
        minReplicas is the lower limit for the number of replicas to
        which the autoscaler can scale down. It defaults to 1 pod.
        """
        return self._properties.get('minReplicas')

    @min_replicas.setter
    def min_replicas(self, value: int):
        """
        minReplicas is the lower limit for the number of replicas to
        which the autoscaler can scale down. It defaults to 1 pod.
        """
        self._properties['minReplicas'] = value

    @property
    def scale_target_ref(self) -> 'CrossVersionObjectReference':
        """
        scaleTargetRef points to the target resource to scale, and
        is used to the pods for which metrics should be collected,
        as well as to actually change the replica count.
        """
        return self._properties.get('scaleTargetRef')

    @scale_target_ref.setter
    def scale_target_ref(self, value: typing.Union['CrossVersionObjectReference', dict]):
        """
        scaleTargetRef points to the target resource to scale, and
        is used to the pods for which metrics should be collected,
        as well as to actually change the replica count.
        """
        if isinstance(value, dict):
            value = CrossVersionObjectReference().from_dict(value)
        self._properties['scaleTargetRef'] = value

    def __enter__(self) -> 'HorizontalPodAutoscalerSpec':
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
            conditions: typing.List['HorizontalPodAutoscalerCondition'] = None,
            current_metrics: typing.List['MetricStatus'] = None,
            current_replicas: int = None,
            desired_replicas: int = None,
            last_scale_time: str = None,
            observed_generation: int = None,
    ):
        """Create HorizontalPodAutoscalerStatus instance."""
        super(HorizontalPodAutoscalerStatus, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='HorizontalPodAutoscalerStatus'
        )
        self._properties = {
            'conditions': conditions or [],
            'currentMetrics': current_metrics or [],
            'currentReplicas': current_replicas or None,
            'desiredReplicas': desired_replicas or None,
            'lastScaleTime': last_scale_time or None,
            'observedGeneration': observed_generation or None,

        }
        self._types = {
            'conditions': (list, HorizontalPodAutoscalerCondition),
            'currentMetrics': (list, MetricStatus),
            'currentReplicas': (int, None),
            'desiredReplicas': (int, None),
            'lastScaleTime': (str, None),
            'observedGeneration': (int, None),

        }

    @property
    def conditions(self) -> typing.List['HorizontalPodAutoscalerCondition']:
        """
        conditions is the set of conditions required for this
        autoscaler to scale its target, and indicates whether or not
        those conditions are met.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['HorizontalPodAutoscalerCondition'], typing.List[dict]]
    ):
        """
        conditions is the set of conditions required for this
        autoscaler to scale its target, and indicates whether or not
        those conditions are met.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HorizontalPodAutoscalerCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def current_metrics(self) -> typing.List['MetricStatus']:
        """
        currentMetrics is the last read state of the metrics used by
        this autoscaler.
        """
        return self._properties.get('currentMetrics')

    @current_metrics.setter
    def current_metrics(
            self,
            value: typing.Union[typing.List['MetricStatus'], typing.List[dict]]
    ):
        """
        currentMetrics is the last read state of the metrics used by
        this autoscaler.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = MetricStatus().from_dict(item)
            cleaned.append(item)
        self._properties['currentMetrics'] = cleaned

    @property
    def current_replicas(self) -> int:
        """
        currentReplicas is current number of replicas of pods
        managed by this autoscaler, as last seen by the autoscaler.
        """
        return self._properties.get('currentReplicas')

    @current_replicas.setter
    def current_replicas(self, value: int):
        """
        currentReplicas is current number of replicas of pods
        managed by this autoscaler, as last seen by the autoscaler.
        """
        self._properties['currentReplicas'] = value

    @property
    def desired_replicas(self) -> int:
        """
        desiredReplicas is the desired number of replicas of pods
        managed by this autoscaler, as last calculated by the
        autoscaler.
        """
        return self._properties.get('desiredReplicas')

    @desired_replicas.setter
    def desired_replicas(self, value: int):
        """
        desiredReplicas is the desired number of replicas of pods
        managed by this autoscaler, as last calculated by the
        autoscaler.
        """
        self._properties['desiredReplicas'] = value

    @property
    def last_scale_time(self) -> str:
        """
        lastScaleTime is the last time the HorizontalPodAutoscaler
        scaled the number of pods, used by the autoscaler to control
        how often the number of pods is changed.
        """
        return self._properties.get('lastScaleTime')

    @last_scale_time.setter
    def last_scale_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        lastScaleTime is the last time the HorizontalPodAutoscaler
        scaled the number of pods, used by the autoscaler to control
        how often the number of pods is changed.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastScaleTime'] = value

    @property
    def observed_generation(self) -> int:
        """
        observedGeneration is the most recent generation observed by
        this autoscaler.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        observedGeneration is the most recent generation observed by
        this autoscaler.
        """
        self._properties['observedGeneration'] = value

    def __enter__(self) -> 'HorizontalPodAutoscalerStatus':
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
            external: 'ExternalMetricSource' = None,
            object_: 'ObjectMetricSource' = None,
            pods: 'PodsMetricSource' = None,
            resource: 'ResourceMetricSource' = None,
            type_: str = None,
    ):
        """Create MetricSpec instance."""
        super(MetricSpec, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='MetricSpec'
        )
        self._properties = {
            'external': external or ExternalMetricSource(),
            'object': object_ or ObjectMetricSource(),
            'pods': pods or PodsMetricSource(),
            'resource': resource or ResourceMetricSource(),
            'type': type_ or '',

        }
        self._types = {
            'external': (ExternalMetricSource, None),
            'object': (ObjectMetricSource, None),
            'pods': (PodsMetricSource, None),
            'resource': (ResourceMetricSource, None),
            'type': (str, None),

        }

    @property
    def external(self) -> 'ExternalMetricSource':
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        return self._properties.get('external')

    @external.setter
    def external(self, value: typing.Union['ExternalMetricSource', dict]):
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        if isinstance(value, dict):
            value = ExternalMetricSource().from_dict(value)
        self._properties['external'] = value

    @property
    def object_(self) -> 'ObjectMetricSource':
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        return self._properties.get('object')

    @object_.setter
    def object_(self, value: typing.Union['ObjectMetricSource', dict]):
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        if isinstance(value, dict):
            value = ObjectMetricSource().from_dict(value)
        self._properties['object'] = value

    @property
    def pods(self) -> 'PodsMetricSource':
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        return self._properties.get('pods')

    @pods.setter
    def pods(self, value: typing.Union['PodsMetricSource', dict]):
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        if isinstance(value, dict):
            value = PodsMetricSource().from_dict(value)
        self._properties['pods'] = value

    @property
    def resource(self) -> 'ResourceMetricSource':
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        return self._properties.get('resource')

    @resource.setter
    def resource(self, value: typing.Union['ResourceMetricSource', dict]):
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        if isinstance(value, dict):
            value = ResourceMetricSource().from_dict(value)
        self._properties['resource'] = value

    @property
    def type_(self) -> str:
        """
        type is the type of metric source.  It should be one of
        "Object", "Pods" or "Resource", each mapping to a matching
        field in the object.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        type is the type of metric source.  It should be one of
        "Object", "Pods" or "Resource", each mapping to a matching
        field in the object.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'MetricSpec':
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
            external: 'ExternalMetricStatus' = None,
            object_: 'ObjectMetricStatus' = None,
            pods: 'PodsMetricStatus' = None,
            resource: 'ResourceMetricStatus' = None,
            type_: str = None,
    ):
        """Create MetricStatus instance."""
        super(MetricStatus, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='MetricStatus'
        )
        self._properties = {
            'external': external or ExternalMetricStatus(),
            'object': object_ or ObjectMetricStatus(),
            'pods': pods or PodsMetricStatus(),
            'resource': resource or ResourceMetricStatus(),
            'type': type_ or '',

        }
        self._types = {
            'external': (ExternalMetricStatus, None),
            'object': (ObjectMetricStatus, None),
            'pods': (PodsMetricStatus, None),
            'resource': (ResourceMetricStatus, None),
            'type': (str, None),

        }

    @property
    def external(self) -> 'ExternalMetricStatus':
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        return self._properties.get('external')

    @external.setter
    def external(self, value: typing.Union['ExternalMetricStatus', dict]):
        """
        external refers to a global metric that is not associated
        with any Kubernetes object. It allows autoscaling based on
        information coming from components running outside of
        cluster (for example length of queue in cloud messaging
        service, or QPS from loadbalancer running outside of
        cluster).
        """
        if isinstance(value, dict):
            value = ExternalMetricStatus().from_dict(value)
        self._properties['external'] = value

    @property
    def object_(self) -> 'ObjectMetricStatus':
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        return self._properties.get('object')

    @object_.setter
    def object_(self, value: typing.Union['ObjectMetricStatus', dict]):
        """
        object refers to a metric describing a single kubernetes
        object (for example, hits-per-second on an Ingress object).
        """
        if isinstance(value, dict):
            value = ObjectMetricStatus().from_dict(value)
        self._properties['object'] = value

    @property
    def pods(self) -> 'PodsMetricStatus':
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        return self._properties.get('pods')

    @pods.setter
    def pods(self, value: typing.Union['PodsMetricStatus', dict]):
        """
        pods refers to a metric describing each pod in the current
        scale target (for example, transactions-processed-per-
        second).  The values will be averaged together before being
        compared to the target value.
        """
        if isinstance(value, dict):
            value = PodsMetricStatus().from_dict(value)
        self._properties['pods'] = value

    @property
    def resource(self) -> 'ResourceMetricStatus':
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        return self._properties.get('resource')

    @resource.setter
    def resource(self, value: typing.Union['ResourceMetricStatus', dict]):
        """
        resource refers to a resource metric (such as those
        specified in requests and limits) known to Kubernetes
        describing each pod in the current scale target (e.g. CPU or
        memory). Such metrics are built in to Kubernetes, and have
        special scaling options on top of those available to normal
        per-pod metrics using the "pods" source.
        """
        if isinstance(value, dict):
            value = ResourceMetricStatus().from_dict(value)
        self._properties['resource'] = value

    @property
    def type_(self) -> str:
        """
        type is the type of metric source.  It will be one of
        "Object", "Pods" or "Resource", each corresponds to a
        matching field in the object.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        type is the type of metric source.  It will be one of
        "Object", "Pods" or "Resource", each corresponds to a
        matching field in the object.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'MetricStatus':
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
            selector: 'LabelSelector' = None,
            target: 'CrossVersionObjectReference' = None,
            target_value: typing.Union[str, int, None] = None,
    ):
        """Create ObjectMetricSource instance."""
        super(ObjectMetricSource, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='ObjectMetricSource'
        )
        self._properties = {
            'averageValue': average_value or None,
            'metricName': metric_name or '',
            'selector': selector or LabelSelector(),
            'target': target or CrossVersionObjectReference(),
            'targetValue': target_value or None,

        }
        self._types = {
            'averageValue': (str, None),
            'metricName': (str, None),
            'selector': (LabelSelector, None),
            'target': (CrossVersionObjectReference, None),
            'targetValue': (str, None),

        }

    @property
    def average_value(self) -> typing.Optional[str]:
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get('averageValue')
        return f'{value}' if value is not None else None

    @average_value.setter
    def average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties['averageValue'] = None if value is None else f'{value}'

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties['metricName'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def target(self) -> 'CrossVersionObjectReference':
        """
        target is the described Kubernetes object.
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['CrossVersionObjectReference', dict]):
        """
        target is the described Kubernetes object.
        """
        if isinstance(value, dict):
            value = CrossVersionObjectReference().from_dict(value)
        self._properties['target'] = value

    @property
    def target_value(self) -> typing.Optional[str]:
        """
        targetValue is the target value of the metric (as a
        quantity).
        """
        value = self._properties.get('targetValue')
        return f'{value}' if value is not None else None

    @target_value.setter
    def target_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        targetValue is the target value of the metric (as a
        quantity).
        """
        self._properties['targetValue'] = None if value is None else f'{value}'

    def __enter__(self) -> 'ObjectMetricSource':
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
            selector: 'LabelSelector' = None,
            target: 'CrossVersionObjectReference' = None,
    ):
        """Create ObjectMetricStatus instance."""
        super(ObjectMetricStatus, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='ObjectMetricStatus'
        )
        self._properties = {
            'averageValue': average_value or None,
            'currentValue': current_value or None,
            'metricName': metric_name or '',
            'selector': selector or LabelSelector(),
            'target': target or CrossVersionObjectReference(),

        }
        self._types = {
            'averageValue': (str, None),
            'currentValue': (str, None),
            'metricName': (str, None),
            'selector': (LabelSelector, None),
            'target': (CrossVersionObjectReference, None),

        }

    @property
    def average_value(self) -> typing.Optional[str]:
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get('averageValue')
        return f'{value}' if value is not None else None

    @average_value.setter
    def average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties['averageValue'] = None if value is None else f'{value}'

    @property
    def current_value(self) -> typing.Optional[str]:
        """
        currentValue is the current value of the metric (as a
        quantity).
        """
        value = self._properties.get('currentValue')
        return f'{value}' if value is not None else None

    @current_value.setter
    def current_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        currentValue is the current value of the metric (as a
        quantity).
        """
        self._properties['currentValue'] = None if value is None else f'{value}'

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question.
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question.
        """
        self._properties['metricName'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        ObjectMetricSource, it is passed as an additional parameter
        to the metrics server for more specific metrics scoping.
        When unset, just the metricName will be used to gather
        metrics.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        ObjectMetricSource, it is passed as an additional parameter
        to the metrics server for more specific metrics scoping.
        When unset, just the metricName will be used to gather
        metrics.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def target(self) -> 'CrossVersionObjectReference':
        """
        target is the described Kubernetes object.
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['CrossVersionObjectReference', dict]):
        """
        target is the described Kubernetes object.
        """
        if isinstance(value, dict):
            value = CrossVersionObjectReference().from_dict(value)
        self._properties['target'] = value

    def __enter__(self) -> 'ObjectMetricStatus':
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
            selector: 'LabelSelector' = None,
            target_average_value: typing.Union[str, int, None] = None,
    ):
        """Create PodsMetricSource instance."""
        super(PodsMetricSource, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='PodsMetricSource'
        )
        self._properties = {
            'metricName': metric_name or '',
            'selector': selector or LabelSelector(),
            'targetAverageValue': target_average_value or None,

        }
        self._types = {
            'metricName': (str, None),
            'selector': (LabelSelector, None),
            'targetAverageValue': (str, None),

        }

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question
        """
        self._properties['metricName'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping When unset, just the metricName
        will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        value = self._properties.get('targetAverageValue')
        return f'{value}' if value is not None else None

    @target_average_value.setter
    def target_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        targetAverageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        self._properties['targetAverageValue'] = None if value is None else f'{value}'

    def __enter__(self) -> 'PodsMetricSource':
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
            selector: 'LabelSelector' = None,
    ):
        """Create PodsMetricStatus instance."""
        super(PodsMetricStatus, self).__init__(
            api_version='autoscaling/v2beta1',
            kind='PodsMetricStatus'
        )
        self._properties = {
            'currentAverageValue': current_average_value or None,
            'metricName': metric_name or '',
            'selector': selector or LabelSelector(),

        }
        self._types = {
            'currentAverageValue': (str, None),
            'metricName': (str, None),
            'selector': (LabelSelector, None),

        }

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of the average of
        the metric across all relevant pods (as a quantity)
        """
        value = self._properties.get('currentAverageValue')
        return f'{value}' if value is not None else None

    @current_average_value.setter
    def current_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        currentAverageValue is the current value of the average of
        the metric across all relevant pods (as a quantity)
        """
        self._properties['currentAverageValue'] = None if value is None else f'{value}'

    @property
    def metric_name(self) -> str:
        """
        metricName is the name of the metric in question
        """
        return self._properties.get('metricName')

    @metric_name.setter
    def metric_name(self, value: str):
        """
        metricName is the name of the metric in question
        """
        self._properties['metricName'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        PodsMetricSource, it is passed as an additional parameter to
        the metrics server for more specific metrics scoping. When
        unset, just the metricName will be used to gather metrics.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set in the
        PodsMetricSource, it is passed as an additional parameter to
        the metrics server for more specific metrics scoping. When
        unset, just the metricName will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    def __enter__(self) -> 'PodsMetricStatus':
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
            api_version='autoscaling/v2beta1',
            kind='ResourceMetricSource'
        )
        self._properties = {
            'name': name or '',
            'targetAverageUtilization': target_average_utilization or None,
            'targetAverageValue': target_average_value or None,

        }
        self._types = {
            'name': (str, None),
            'targetAverageUtilization': (int, None),
            'targetAverageValue': (str, None),

        }

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties['name'] = value

    @property
    def target_average_utilization(self) -> int:
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        return self._properties.get('targetAverageUtilization')

    @target_average_utilization.setter
    def target_average_utilization(self, value: int):
        """
        targetAverageUtilization is the target value of the average
        of the resource metric across all relevant pods, represented
        as a percentage of the requested value of the resource for
        the pods.
        """
        self._properties['targetAverageUtilization'] = value

    @property
    def target_average_value(self) -> typing.Optional[str]:
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        value = self._properties.get('targetAverageValue')
        return f'{value}' if value is not None else None

    @target_average_value.setter
    def target_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        targetAverageValue is the target value of the average of the
        resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type.
        """
        self._properties['targetAverageValue'] = None if value is None else f'{value}'

    def __enter__(self) -> 'ResourceMetricSource':
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
            api_version='autoscaling/v2beta1',
            kind='ResourceMetricStatus'
        )
        self._properties = {
            'currentAverageUtilization': current_average_utilization or None,
            'currentAverageValue': current_average_value or None,
            'name': name or '',

        }
        self._types = {
            'currentAverageUtilization': (int, None),
            'currentAverageValue': (str, None),
            'name': (str, None),

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
        return self._properties.get('currentAverageUtilization')

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
        self._properties['currentAverageUtilization'] = value

    @property
    def current_average_value(self) -> typing.Optional[str]:
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        value = self._properties.get('currentAverageValue')
        return f'{value}' if value is not None else None

    @current_average_value.setter
    def current_average_value(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        currentAverageValue is the current value of the average of
        the resource metric across all relevant pods, as a raw value
        (instead of as a percentage of the request), similar to the
        "pods" metric source type. It will always be set, regardless
        of the corresponding metric specification.
        """
        self._properties['currentAverageValue'] = None if value is None else f'{value}'

    @property
    def name(self) -> str:
        """
        name is the name of the resource in question.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource in question.
        """
        self._properties['name'] = value

    def __enter__(self) -> 'ResourceMetricStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

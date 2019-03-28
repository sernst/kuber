import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import LabelSelector
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ListMeta
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ObjectMeta
from kuber.v1_13.apimachinery.pkg.api.resource import Quantity
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import Status
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import StatusDetails


class CrossVersionObjectReference(_kuber_definitions.Resource):
    """
    CrossVersionObjectReference contains enough information to
    let you identify the referred resource.
    """

    def __init__(
            self,
            name: str = None,
    ):
        """Create CrossVersionObjectReference instance."""
        super(CrossVersionObjectReference, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='CrossVersionObjectReference'
        )
        self._properties = {
            'name': name or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'name': (str, None),

        }

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

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the CrossVersionObjectReference in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_cross_version_object_reference',
            'create_cross_version_object_reference'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the CrossVersionObjectReference in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_cross_version_object_reference',
            'replace_cross_version_object_reference'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the CrossVersionObjectReference in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_cross_version_object_reference',
            'patch_cross_version_object_reference'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def delete_resource(self, namespace: 'str' = None):
        """
        Deletes the CrossVersionObjectReference from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_cross_version_object_reference',
            'delete_cross_version_object_reference'
        ]

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> client.AutoscalingV2beta2Api:
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AutoscalingV2beta2Api(**kwargs)

    def __enter__(self) -> 'CrossVersionObjectReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ExternalMetricSource(_kuber_definitions.Definition):
    """
    ExternalMetricSource indicates how to scale on a metric not
    associated with any Kubernetes object (for example length of
    queue in cloud messaging service, or QPS from loadbalancer
    running outside of cluster).
    """

    def __init__(
            self,
            metric: 'MetricIdentifier' = None,
            target: 'MetricTarget' = None,
    ):
        """Create ExternalMetricSource instance."""
        super(ExternalMetricSource, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ExternalMetricSource'
        )
        self._properties = {
            'metric': metric or MetricIdentifier(),
            'target': target or MetricTarget(),

        }
        self._types = {
            'metric': (MetricIdentifier, None),
            'target': (MetricTarget, None),

        }

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

    @property
    def target(self) -> 'MetricTarget':
        """
        target specifies the target value for the given metric
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['MetricTarget', dict]):
        """
        target specifies the target value for the given metric
        """
        if isinstance(value, dict):
            value = MetricTarget().from_dict(value)
        self._properties['target'] = value

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
            current: 'MetricValueStatus' = None,
            metric: 'MetricIdentifier' = None,
    ):
        """Create ExternalMetricStatus instance."""
        super(ExternalMetricStatus, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ExternalMetricStatus'
        )
        self._properties = {
            'current': current or MetricValueStatus(),
            'metric': metric or MetricIdentifier(),

        }
        self._types = {
            'current': (MetricValueStatus, None),
            'metric': (MetricIdentifier, None),

        }

    @property
    def current(self) -> 'MetricValueStatus':
        """
        current contains the current value for the given metric
        """
        return self._properties.get('current')

    @current.setter
    def current(self, value: typing.Union['MetricValueStatus', dict]):
        """
        current contains the current value for the given metric
        """
        if isinstance(value, dict):
            value = MetricValueStatus().from_dict(value)
        self._properties['current'] = value

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

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
    ):
        """Create HorizontalPodAutoscaler instance."""
        super(HorizontalPodAutoscaler, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='HorizontalPodAutoscaler'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or HorizontalPodAutoscalerSpec(),

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

    def delete_resource(self, namespace: 'str' = None):
        """
        Deletes the HorizontalPodAutoscaler from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_horizontal_pod_autoscaler',
            'delete_horizontal_pod_autoscaler'
        ]

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> client.AutoscalingV2beta2Api:
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AutoscalingV2beta2Api(**kwargs)

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
            api_version='autoscaling/v2beta2',
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
    HorizontalPodAutoscalerList is a list of horizontal pod
    autoscaler objects.
    """

    def __init__(
            self,
            items: typing.List['HorizontalPodAutoscaler'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create HorizontalPodAutoscalerList instance."""
        super(HorizontalPodAutoscalerList, self).__init__(
            api_version='autoscaling/v2beta2',
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
    ) -> client.AutoscalingV2beta2Api:
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AutoscalingV2beta2Api(**kwargs)

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
            api_version='autoscaling/v2beta2',
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
        must respond. If not set, the default metric will be set to
        80% average CPU utilization.
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
        must respond. If not set, the default metric will be set to
        80% average CPU utilization.
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
            api_version='autoscaling/v2beta2',
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


class MetricIdentifier(_kuber_definitions.Definition):
    """
    MetricIdentifier defines the name and optionally selector
    for a metric
    """

    def __init__(
            self,
            name: str = None,
            selector: 'LabelSelector' = None,
    ):
        """Create MetricIdentifier instance."""
        super(MetricIdentifier, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='MetricIdentifier'
        )
        self._properties = {
            'name': name or '',
            'selector': selector or LabelSelector(),

        }
        self._types = {
            'name': (str, None),
            'selector': (LabelSelector, None),

        }

    @property
    def name(self) -> str:
        """
        name is the name of the given metric
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name is the name of the given metric
        """
        self._properties['name'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping. When unset, just the metricName
        will be used to gather metrics.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is the string-encoded form of a standard kubernetes
        label selector for the given metric When set, it is passed
        as an additional parameter to the metrics server for more
        specific metrics scoping. When unset, just the metricName
        will be used to gather metrics.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    def __enter__(self) -> 'MetricIdentifier':
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
            api_version='autoscaling/v2beta2',
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
            api_version='autoscaling/v2beta2',
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


class MetricTarget(_kuber_definitions.Definition):
    """
    MetricTarget defines the target value, average value, or
    average utilization of a specific metric
    """

    def __init__(
            self,
            average_utilization: int = None,
            average_value: 'Quantity' = None,
            type_: str = None,
            value: 'Quantity' = None,
    ):
        """Create MetricTarget instance."""
        super(MetricTarget, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='MetricTarget'
        )
        self._properties = {
            'averageUtilization': average_utilization or None,
            'averageValue': average_value or Quantity(),
            'type': type_ or '',
            'value': value or Quantity(),

        }
        self._types = {
            'averageUtilization': (int, None),
            'averageValue': (Quantity, None),
            'type': (str, None),
            'value': (Quantity, None),

        }

    @property
    def average_utilization(self) -> int:
        """
        averageUtilization is the target value of the average of the
        resource metric across all relevant pods, represented as a
        percentage of the requested value of the resource for the
        pods. Currently only valid for Resource metric source type
        """
        return self._properties.get('averageUtilization')

    @average_utilization.setter
    def average_utilization(self, value: int):
        """
        averageUtilization is the target value of the average of the
        resource metric across all relevant pods, represented as a
        percentage of the requested value of the resource for the
        pods. Currently only valid for Resource metric source type
        """
        self._properties['averageUtilization'] = value

    @property
    def average_value(self) -> 'Quantity':
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        return self._properties.get('averageValue')

    @average_value.setter
    def average_value(self, value: typing.Union['Quantity', dict]):
        """
        averageValue is the target value of the average of the
        metric across all relevant pods (as a quantity)
        """
        if isinstance(value, dict):
            value = Quantity().from_dict(value)
        self._properties['averageValue'] = value

    @property
    def type_(self) -> str:
        """
        type represents whether the metric type is Utilization,
        Value, or AverageValue
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        type represents whether the metric type is Utilization,
        Value, or AverageValue
        """
        self._properties['type'] = value

    @property
    def value(self) -> 'Quantity':
        """
        value is the target value of the metric (as a quantity).
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: typing.Union['Quantity', dict]):
        """
        value is the target value of the metric (as a quantity).
        """
        if isinstance(value, dict):
            value = Quantity().from_dict(value)
        self._properties['value'] = value

    def __enter__(self) -> 'MetricTarget':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MetricValueStatus(_kuber_definitions.Definition):
    """
    MetricValueStatus holds the current value for a metric
    """

    def __init__(
            self,
            average_utilization: int = None,
            average_value: 'Quantity' = None,
            value: 'Quantity' = None,
    ):
        """Create MetricValueStatus instance."""
        super(MetricValueStatus, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='MetricValueStatus'
        )
        self._properties = {
            'averageUtilization': average_utilization or None,
            'averageValue': average_value or Quantity(),
            'value': value or Quantity(),

        }
        self._types = {
            'averageUtilization': (int, None),
            'averageValue': (Quantity, None),
            'value': (Quantity, None),

        }

    @property
    def average_utilization(self) -> int:
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.
        """
        return self._properties.get('averageUtilization')

    @average_utilization.setter
    def average_utilization(self, value: int):
        """
        currentAverageUtilization is the current value of the
        average of the resource metric across all relevant pods,
        represented as a percentage of the requested value of the
        resource for the pods.
        """
        self._properties['averageUtilization'] = value

    @property
    def average_value(self) -> 'Quantity':
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        return self._properties.get('averageValue')

    @average_value.setter
    def average_value(self, value: typing.Union['Quantity', dict]):
        """
        averageValue is the current value of the average of the
        metric across all relevant pods (as a quantity)
        """
        if isinstance(value, dict):
            value = Quantity().from_dict(value)
        self._properties['averageValue'] = value

    @property
    def value(self) -> 'Quantity':
        """
        value is the current value of the metric (as a quantity).
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: typing.Union['Quantity', dict]):
        """
        value is the current value of the metric (as a quantity).
        """
        if isinstance(value, dict):
            value = Quantity().from_dict(value)
        self._properties['value'] = value

    def __enter__(self) -> 'MetricValueStatus':
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
            described_object: 'CrossVersionObjectReference' = None,
            metric: 'MetricIdentifier' = None,
            target: 'MetricTarget' = None,
    ):
        """Create ObjectMetricSource instance."""
        super(ObjectMetricSource, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ObjectMetricSource'
        )
        self._properties = {
            'describedObject': described_object or CrossVersionObjectReference(),
            'metric': metric or MetricIdentifier(),
            'target': target or MetricTarget(),

        }
        self._types = {
            'describedObject': (CrossVersionObjectReference, None),
            'metric': (MetricIdentifier, None),
            'target': (MetricTarget, None),

        }

    @property
    def described_object(self) -> 'CrossVersionObjectReference':
        """

        """
        return self._properties.get('describedObject')

    @described_object.setter
    def described_object(self, value: typing.Union['CrossVersionObjectReference', dict]):
        """

        """
        if isinstance(value, dict):
            value = CrossVersionObjectReference().from_dict(value)
        self._properties['describedObject'] = value

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

    @property
    def target(self) -> 'MetricTarget':
        """
        target specifies the target value for the given metric
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['MetricTarget', dict]):
        """
        target specifies the target value for the given metric
        """
        if isinstance(value, dict):
            value = MetricTarget().from_dict(value)
        self._properties['target'] = value

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
            current: 'MetricValueStatus' = None,
            described_object: 'CrossVersionObjectReference' = None,
            metric: 'MetricIdentifier' = None,
    ):
        """Create ObjectMetricStatus instance."""
        super(ObjectMetricStatus, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ObjectMetricStatus'
        )
        self._properties = {
            'current': current or MetricValueStatus(),
            'describedObject': described_object or CrossVersionObjectReference(),
            'metric': metric or MetricIdentifier(),

        }
        self._types = {
            'current': (MetricValueStatus, None),
            'describedObject': (CrossVersionObjectReference, None),
            'metric': (MetricIdentifier, None),

        }

    @property
    def current(self) -> 'MetricValueStatus':
        """
        current contains the current value for the given metric
        """
        return self._properties.get('current')

    @current.setter
    def current(self, value: typing.Union['MetricValueStatus', dict]):
        """
        current contains the current value for the given metric
        """
        if isinstance(value, dict):
            value = MetricValueStatus().from_dict(value)
        self._properties['current'] = value

    @property
    def described_object(self) -> 'CrossVersionObjectReference':
        """

        """
        return self._properties.get('describedObject')

    @described_object.setter
    def described_object(self, value: typing.Union['CrossVersionObjectReference', dict]):
        """

        """
        if isinstance(value, dict):
            value = CrossVersionObjectReference().from_dict(value)
        self._properties['describedObject'] = value

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

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
            metric: 'MetricIdentifier' = None,
            target: 'MetricTarget' = None,
    ):
        """Create PodsMetricSource instance."""
        super(PodsMetricSource, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='PodsMetricSource'
        )
        self._properties = {
            'metric': metric or MetricIdentifier(),
            'target': target or MetricTarget(),

        }
        self._types = {
            'metric': (MetricIdentifier, None),
            'target': (MetricTarget, None),

        }

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

    @property
    def target(self) -> 'MetricTarget':
        """
        target specifies the target value for the given metric
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['MetricTarget', dict]):
        """
        target specifies the target value for the given metric
        """
        if isinstance(value, dict):
            value = MetricTarget().from_dict(value)
        self._properties['target'] = value

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
            current: 'MetricValueStatus' = None,
            metric: 'MetricIdentifier' = None,
    ):
        """Create PodsMetricStatus instance."""
        super(PodsMetricStatus, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='PodsMetricStatus'
        )
        self._properties = {
            'current': current or MetricValueStatus(),
            'metric': metric or MetricIdentifier(),

        }
        self._types = {
            'current': (MetricValueStatus, None),
            'metric': (MetricIdentifier, None),

        }

    @property
    def current(self) -> 'MetricValueStatus':
        """
        current contains the current value for the given metric
        """
        return self._properties.get('current')

    @current.setter
    def current(self, value: typing.Union['MetricValueStatus', dict]):
        """
        current contains the current value for the given metric
        """
        if isinstance(value, dict):
            value = MetricValueStatus().from_dict(value)
        self._properties['current'] = value

    @property
    def metric(self) -> 'MetricIdentifier':
        """
        metric identifies the target metric by name and selector
        """
        return self._properties.get('metric')

    @metric.setter
    def metric(self, value: typing.Union['MetricIdentifier', dict]):
        """
        metric identifies the target metric by name and selector
        """
        if isinstance(value, dict):
            value = MetricIdentifier().from_dict(value)
        self._properties['metric'] = value

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
            target: 'MetricTarget' = None,
    ):
        """Create ResourceMetricSource instance."""
        super(ResourceMetricSource, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ResourceMetricSource'
        )
        self._properties = {
            'name': name or '',
            'target': target or MetricTarget(),

        }
        self._types = {
            'name': (str, None),
            'target': (MetricTarget, None),

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
    def target(self) -> 'MetricTarget':
        """
        target specifies the target value for the given metric
        """
        return self._properties.get('target')

    @target.setter
    def target(self, value: typing.Union['MetricTarget', dict]):
        """
        target specifies the target value for the given metric
        """
        if isinstance(value, dict):
            value = MetricTarget().from_dict(value)
        self._properties['target'] = value

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
            current: 'MetricValueStatus' = None,
            name: str = None,
    ):
        """Create ResourceMetricStatus instance."""
        super(ResourceMetricStatus, self).__init__(
            api_version='autoscaling/v2beta2',
            kind='ResourceMetricStatus'
        )
        self._properties = {
            'current': current or MetricValueStatus(),
            'name': name or '',

        }
        self._types = {
            'current': (MetricValueStatus, None),
            'name': (str, None),

        }

    @property
    def current(self) -> 'MetricValueStatus':
        """
        current contains the current value for the given metric
        """
        return self._properties.get('current')

    @current.setter
    def current(self, value: typing.Union['MetricValueStatus', dict]):
        """
        current contains the current value for the given metric
        """
        if isinstance(value, dict):
            value = MetricValueStatus().from_dict(value)
        self._properties['current'] = value

    @property
    def name(self) -> str:
        """
        Name is the name of the resource in question.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the resource in question.
        """
        self._properties['name'] = value

    def __enter__(self) -> 'ResourceMetricStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

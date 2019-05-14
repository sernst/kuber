import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_14.meta_v1 import DeleteOptions
from kuber.v1_14.meta_v1 import LabelSelector
from kuber.v1_14.meta_v1 import ListMeta
from kuber.v1_14.meta_v1 import ObjectMeta
from kuber.v1_14.core_v1 import SELinuxOptions
from kuber.v1_14.meta_v1 import Status
from kuber.v1_14.meta_v1 import StatusDetails


class AllowedCSIDriver(_kuber_definitions.Definition):
    """
    AllowedCSIDriver represents a single inline CSI Driver that
    is allowed to be used.
    """

    def __init__(
            self,
            name: str = None,
    ):
        """Create AllowedCSIDriver instance."""
        super(AllowedCSIDriver, self).__init__(
            api_version='policy/v1beta1',
            kind='AllowedCSIDriver'
        )
        self._properties = {
            'name': name or '',

        }
        self._types = {
            'name': (str, None),

        }

    @property
    def name(self) -> str:
        """
        Name is the registered name of the CSI driver
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the registered name of the CSI driver
        """
        self._properties['name'] = value

    def __enter__(self) -> 'AllowedCSIDriver':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AllowedFlexVolume(_kuber_definitions.Definition):
    """
    AllowedFlexVolume represents a single Flexvolume that is
    allowed to be used.
    """

    def __init__(
            self,
            driver: str = None,
    ):
        """Create AllowedFlexVolume instance."""
        super(AllowedFlexVolume, self).__init__(
            api_version='policy/v1beta1',
            kind='AllowedFlexVolume'
        )
        self._properties = {
            'driver': driver or '',

        }
        self._types = {
            'driver': (str, None),

        }

    @property
    def driver(self) -> str:
        """
        driver is the name of the Flexvolume driver.
        """
        return self._properties.get('driver')

    @driver.setter
    def driver(self, value: str):
        """
        driver is the name of the Flexvolume driver.
        """
        self._properties['driver'] = value

    def __enter__(self) -> 'AllowedFlexVolume':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AllowedHostPath(_kuber_definitions.Definition):
    """
    AllowedHostPath defines the host volume conditions that will
    be enabled by a policy for pods to use. It requires the path
    prefix to be defined.
    """

    def __init__(
            self,
            path_prefix: str = None,
            read_only: bool = None,
    ):
        """Create AllowedHostPath instance."""
        super(AllowedHostPath, self).__init__(
            api_version='policy/v1beta1',
            kind='AllowedHostPath'
        )
        self._properties = {
            'pathPrefix': path_prefix or '',
            'readOnly': read_only or None,

        }
        self._types = {
            'pathPrefix': (str, None),
            'readOnly': (bool, None),

        }

    @property
    def path_prefix(self) -> str:
        """
        pathPrefix is the path prefix that the host volume must
        match. It does not support `*`. Trailing slashes are trimmed
        when validating the path prefix with a host path.

        Examples:
        `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo`
        would not allow `/food` or `/etc/foo`
        """
        return self._properties.get('pathPrefix')

    @path_prefix.setter
    def path_prefix(self, value: str):
        """
        pathPrefix is the path prefix that the host volume must
        match. It does not support `*`. Trailing slashes are trimmed
        when validating the path prefix with a host path.

        Examples:
        `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo`
        would not allow `/food` or `/etc/foo`
        """
        self._properties['pathPrefix'] = value

    @property
    def read_only(self) -> bool:
        """
        when set to true, will allow host volumes matching the
        pathPrefix only if all volume mounts are readOnly.
        """
        return self._properties.get('readOnly')

    @read_only.setter
    def read_only(self, value: bool):
        """
        when set to true, will allow host volumes matching the
        pathPrefix only if all volume mounts are readOnly.
        """
        self._properties['readOnly'] = value

    def __enter__(self) -> 'AllowedHostPath':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Eviction(_kuber_definitions.Resource):
    """
    Eviction evicts a pod from its node subject to certain
    policies and safety constraints. This is a subresource of
    Pod.  A request to cause such an eviction is created by
    POSTing to .../pods/<pod name>/evictions.
    """

    def __init__(
            self,
            delete_options: 'DeleteOptions' = None,
            metadata: 'ObjectMeta' = None,
    ):
        """Create Eviction instance."""
        super(Eviction, self).__init__(
            api_version='policy/v1beta1',
            kind='Eviction'
        )
        self._properties = {
            'deleteOptions': delete_options or DeleteOptions(),
            'metadata': metadata or ObjectMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'deleteOptions': (DeleteOptions, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),

        }

    @property
    def delete_options(self) -> 'DeleteOptions':
        """
        DeleteOptions may be provided
        """
        return self._properties.get('deleteOptions')

    @delete_options.setter
    def delete_options(self, value: typing.Union['DeleteOptions', dict]):
        """
        DeleteOptions may be provided
        """
        if isinstance(value, dict):
            value = DeleteOptions().from_dict(value)
        self._properties['deleteOptions'] = value

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        ObjectMeta describes the pod that is being evicted.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        ObjectMeta describes the pod that is being evicted.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_eviction',
            'create_eviction'
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
        Replaces the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_eviction',
            'replace_eviction'
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
        Patches the Eviction in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_eviction',
            'patch_eviction'
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

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Eviction from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_eviction',
            'read_eviction'
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
        Deletes the Eviction from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_eviction',
            'delete_eviction'
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
    ) -> 'client.PolicyV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.PolicyV1beta1Api(**kwargs)

    def __enter__(self) -> 'Eviction':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FSGroupStrategyOptions(_kuber_definitions.Definition):
    """
    FSGroupStrategyOptions defines the strategy type and options
    used to create the strategy.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create FSGroupStrategyOptions instance."""
        super(FSGroupStrategyOptions, self).__init__(
            api_version='policy/v1beta1',
            kind='FSGroupStrategyOptions'
        )
        self._properties = {
            'ranges': ranges or [],
            'rule': rule or '',

        }
        self._types = {
            'ranges': (list, IDRange),
            'rule': (str, None),

        }

    @property
    def ranges(self) -> typing.List['IDRange']:
        """
        ranges are the allowed ranges of fs groups.  If you would
        like to force a single fs group then supply a single range
        with the same start and end. Required for MustRunAs.
        """
        return self._properties.get('ranges')

    @ranges.setter
    def ranges(
            self,
            value: typing.Union[typing.List['IDRange'], typing.List[dict]]
    ):
        """
        ranges are the allowed ranges of fs groups.  If you would
        like to force a single fs group then supply a single range
        with the same start and end. Required for MustRunAs.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IDRange().from_dict(item)
            cleaned.append(item)
        self._properties['ranges'] = cleaned

    @property
    def rule(self) -> str:
        """
        rule is the strategy that will dictate what FSGroup is used
        in the SecurityContext.
        """
        return self._properties.get('rule')

    @rule.setter
    def rule(self, value: str):
        """
        rule is the strategy that will dictate what FSGroup is used
        in the SecurityContext.
        """
        self._properties['rule'] = value

    def __enter__(self) -> 'FSGroupStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HostPortRange(_kuber_definitions.Definition):
    """
    HostPortRange defines a range of host ports that will be
    enabled by a policy for pods to use.  It requires both the
    start and end to be defined.
    """

    def __init__(
            self,
            max_: int = None,
            min_: int = None,
    ):
        """Create HostPortRange instance."""
        super(HostPortRange, self).__init__(
            api_version='policy/v1beta1',
            kind='HostPortRange'
        )
        self._properties = {
            'max': max_ or None,
            'min': min_ or None,

        }
        self._types = {
            'max': (int, None),
            'min': (int, None),

        }

    @property
    def max_(self) -> int:
        """
        max is the end of the range, inclusive.
        """
        return self._properties.get('max')

    @max_.setter
    def max_(self, value: int):
        """
        max is the end of the range, inclusive.
        """
        self._properties['max'] = value

    @property
    def min_(self) -> int:
        """
        min is the start of the range, inclusive.
        """
        return self._properties.get('min')

    @min_.setter
    def min_(self, value: int):
        """
        min is the start of the range, inclusive.
        """
        self._properties['min'] = value

    def __enter__(self) -> 'HostPortRange':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IDRange(_kuber_definitions.Definition):
    """
    IDRange provides a min/max of an allowed range of IDs.
    """

    def __init__(
            self,
            max_: int = None,
            min_: int = None,
    ):
        """Create IDRange instance."""
        super(IDRange, self).__init__(
            api_version='policy/v1beta1',
            kind='IDRange'
        )
        self._properties = {
            'max': max_ or None,
            'min': min_ or None,

        }
        self._types = {
            'max': (int, None),
            'min': (int, None),

        }

    @property
    def max_(self) -> int:
        """
        max is the end of the range, inclusive.
        """
        return self._properties.get('max')

    @max_.setter
    def max_(self, value: int):
        """
        max is the end of the range, inclusive.
        """
        self._properties['max'] = value

    @property
    def min_(self) -> int:
        """
        min is the start of the range, inclusive.
        """
        return self._properties.get('min')

    @min_.setter
    def min_(self, value: int):
        """
        min is the start of the range, inclusive.
        """
        self._properties['min'] = value

    def __enter__(self) -> 'IDRange':
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
            metadata: 'ObjectMeta' = None,
            spec: 'PodDisruptionBudgetSpec' = None,
            status: 'PodDisruptionBudgetStatus' = None,
    ):
        """Create PodDisruptionBudget instance."""
        super(PodDisruptionBudget, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudget'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PodDisruptionBudgetSpec(),
            'status': status or PodDisruptionBudgetStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PodDisruptionBudgetSpec, None),
            'status': (PodDisruptionBudgetStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PodDisruptionBudgetSpec':
        """
        Specification of the desired behavior of the
        PodDisruptionBudget.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PodDisruptionBudgetSpec', dict]):
        """
        Specification of the desired behavior of the
        PodDisruptionBudget.
        """
        if isinstance(value, dict):
            value = PodDisruptionBudgetSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'PodDisruptionBudgetStatus':
        """
        Most recently observed status of the PodDisruptionBudget.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['PodDisruptionBudgetStatus', dict]):
        """
        Most recently observed status of the PodDisruptionBudget.
        """
        if isinstance(value, dict):
            value = PodDisruptionBudgetStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodDisruptionBudgetStatus':
        """
        Creates the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_pod_disruption_budget',
            'create_pod_disruption_budget'
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
            PodDisruptionBudgetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodDisruptionBudgetStatus':
        """
        Replaces the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_pod_disruption_budget',
            'replace_pod_disruption_budget'
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
            PodDisruptionBudgetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'PodDisruptionBudgetStatus':
        """
        Patches the PodDisruptionBudget in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_pod_disruption_budget',
            'patch_pod_disruption_budget'
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
            PodDisruptionBudgetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'PodDisruptionBudgetStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_pod_disruption_budget',
            'read_pod_disruption_budget'
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
            PodDisruptionBudgetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the PodDisruptionBudget from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_pod_disruption_budget',
            'read_pod_disruption_budget'
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
        Deletes the PodDisruptionBudget from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_pod_disruption_budget',
            'delete_pod_disruption_budget'
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
    ) -> 'client.PolicyV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.PolicyV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodDisruptionBudget':
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
            items: typing.List['PodDisruptionBudget'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodDisruptionBudgetList instance."""
        super(PodDisruptionBudgetList, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PodDisruptionBudget),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PodDisruptionBudget']:
        """

        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PodDisruptionBudget'], typing.List[dict]]
    ):
        """

        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodDisruptionBudget().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.PolicyV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.PolicyV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodDisruptionBudgetList':
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
            selector: 'LabelSelector' = None,
    ):
        """Create PodDisruptionBudgetSpec instance."""
        super(PodDisruptionBudgetSpec, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetSpec'
        )
        self._properties = {
            'maxUnavailable': max_unavailable or None,
            'minAvailable': min_available or None,
            'selector': selector or LabelSelector(),

        }
        self._types = {
            'maxUnavailable': (int, None),
            'minAvailable': (int, None),
            'selector': (LabelSelector, None),

        }

    @property
    def max_unavailable(self) -> typing.Optional[int]:
        """
        An eviction is allowed if at most "maxUnavailable" pods
        selected by "selector" are unavailable after the eviction,
        i.e. even in absence of the evicted pod. For example, one
        can prevent all voluntary evictions by specifying 0. This is
        a mutually exclusive setting with "minAvailable".
        """
        value = self._properties.get('maxUnavailable')
        return int(value) if value is not None else None

    @max_unavailable.setter
    def max_unavailable(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        An eviction is allowed if at most "maxUnavailable" pods
        selected by "selector" are unavailable after the eviction,
        i.e. even in absence of the evicted pod. For example, one
        can prevent all voluntary evictions by specifying 0. This is
        a mutually exclusive setting with "minAvailable".
        """
        self._properties['maxUnavailable'] = None if value is None else f'{value}'

    @property
    def min_available(self) -> typing.Optional[int]:
        """
        An eviction is allowed if at least "minAvailable" pods
        selected by "selector" will still be available after the
        eviction, i.e. even in the absence of the evicted pod.  So
        for example you can prevent all voluntary evictions by
        specifying "100%".
        """
        value = self._properties.get('minAvailable')
        return int(value) if value is not None else None

    @min_available.setter
    def min_available(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        An eviction is allowed if at least "minAvailable" pods
        selected by "selector" will still be available after the
        eviction, i.e. even in the absence of the evicted pod.  So
        for example you can prevent all voluntary evictions by
        specifying "100%".
        """
        self._properties['minAvailable'] = None if value is None else f'{value}'

    @property
    def selector(self) -> 'LabelSelector':
        """
        Label query over pods whose evictions are managed by the
        disruption budget.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Label query over pods whose evictions are managed by the
        disruption budget.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    def __enter__(self) -> 'PodDisruptionBudgetSpec':
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
            current_healthy: int = None,
            desired_healthy: int = None,
            disrupted_pods: dict = None,
            disruptions_allowed: int = None,
            expected_pods: int = None,
            observed_generation: int = None,
    ):
        """Create PodDisruptionBudgetStatus instance."""
        super(PodDisruptionBudgetStatus, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetStatus'
        )
        self._properties = {
            'currentHealthy': current_healthy or None,
            'desiredHealthy': desired_healthy or None,
            'disruptedPods': disrupted_pods or {},
            'disruptionsAllowed': disruptions_allowed or None,
            'expectedPods': expected_pods or None,
            'observedGeneration': observed_generation or None,

        }
        self._types = {
            'currentHealthy': (int, None),
            'desiredHealthy': (int, None),
            'disruptedPods': (dict, None),
            'disruptionsAllowed': (int, None),
            'expectedPods': (int, None),
            'observedGeneration': (int, None),

        }

    @property
    def current_healthy(self) -> int:
        """
        current number of healthy pods
        """
        return self._properties.get('currentHealthy')

    @current_healthy.setter
    def current_healthy(self, value: int):
        """
        current number of healthy pods
        """
        self._properties['currentHealthy'] = value

    @property
    def desired_healthy(self) -> int:
        """
        minimum desired number of healthy pods
        """
        return self._properties.get('desiredHealthy')

    @desired_healthy.setter
    def desired_healthy(self, value: int):
        """
        minimum desired number of healthy pods
        """
        self._properties['desiredHealthy'] = value

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
        return self._properties.get('disruptedPods')

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
        self._properties['disruptedPods'] = value

    @property
    def disruptions_allowed(self) -> int:
        """
        Number of pod disruptions that are currently allowed.
        """
        return self._properties.get('disruptionsAllowed')

    @disruptions_allowed.setter
    def disruptions_allowed(self, value: int):
        """
        Number of pod disruptions that are currently allowed.
        """
        self._properties['disruptionsAllowed'] = value

    @property
    def expected_pods(self) -> int:
        """
        total number of pods counted by this disruption budget
        """
        return self._properties.get('expectedPods')

    @expected_pods.setter
    def expected_pods(self, value: int):
        """
        total number of pods counted by this disruption budget
        """
        self._properties['expectedPods'] = value

    @property
    def observed_generation(self) -> int:
        """
        Most recent generation observed when updating this PDB
        status. PodDisruptionsAllowed and other status informatio is
        valid only if observedGeneration equals to PDB's object
        generation.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        Most recent generation observed when updating this PDB
        status. PodDisruptionsAllowed and other status informatio is
        valid only if observedGeneration equals to PDB's object
        generation.
        """
        self._properties['observedGeneration'] = value

    def __enter__(self) -> 'PodDisruptionBudgetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicy(_kuber_definitions.Resource):
    """
    PodSecurityPolicy governs the ability to make requests that
    affect the Security Context that will be applied to a pod
    and container.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PodSecurityPolicySpec' = None,
    ):
        """Create PodSecurityPolicy instance."""
        super(PodSecurityPolicy, self).__init__(
            api_version='policy/v1beta1',
            kind='PodSecurityPolicy'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PodSecurityPolicySpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PodSecurityPolicySpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'PodSecurityPolicySpec':
        """
        spec defines the policy enforced.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PodSecurityPolicySpec', dict]):
        """
        spec defines the policy enforced.
        """
        if isinstance(value, dict):
            value = PodSecurityPolicySpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the PodSecurityPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_pod_security_policy',
            'create_pod_security_policy'
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
        Replaces the PodSecurityPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_pod_security_policy',
            'replace_pod_security_policy'
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
        Patches the PodSecurityPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_pod_security_policy',
            'patch_pod_security_policy'
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

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the PodSecurityPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_pod_security_policy',
            'read_pod_security_policy'
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
        Deletes the PodSecurityPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_pod_security_policy',
            'delete_pod_security_policy'
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
    ) -> 'client.PolicyV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.PolicyV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodSecurityPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicyList(_kuber_definitions.Collection):
    """
    PodSecurityPolicyList is a list of PodSecurityPolicy
    objects.
    """

    def __init__(
            self,
            items: typing.List['PodSecurityPolicy'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodSecurityPolicyList instance."""
        super(PodSecurityPolicyList, self).__init__(
            api_version='policy/v1beta1',
            kind='PodSecurityPolicyList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PodSecurityPolicy),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PodSecurityPolicy']:
        """
        items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PodSecurityPolicy'], typing.List[dict]]
    ):
        """
        items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodSecurityPolicy().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.PolicyV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.PolicyV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodSecurityPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicySpec(_kuber_definitions.Definition):
    """
    PodSecurityPolicySpec defines the policy enforced.
    """

    def __init__(
            self,
            allow_privilege_escalation: bool = None,
            allowed_csidrivers: typing.List['AllowedCSIDriver'] = None,
            allowed_capabilities: typing.List[str] = None,
            allowed_flex_volumes: typing.List['AllowedFlexVolume'] = None,
            allowed_host_paths: typing.List['AllowedHostPath'] = None,
            allowed_proc_mount_types: typing.List[str] = None,
            allowed_unsafe_sysctls: typing.List[str] = None,
            default_add_capabilities: typing.List[str] = None,
            default_allow_privilege_escalation: bool = None,
            forbidden_sysctls: typing.List[str] = None,
            fs_group: 'FSGroupStrategyOptions' = None,
            host_ipc: bool = None,
            host_network: bool = None,
            host_pid: bool = None,
            host_ports: typing.List['HostPortRange'] = None,
            privileged: bool = None,
            read_only_root_filesystem: bool = None,
            required_drop_capabilities: typing.List[str] = None,
            run_as_group: 'RunAsGroupStrategyOptions' = None,
            run_as_user: 'RunAsUserStrategyOptions' = None,
            se_linux: 'SELinuxStrategyOptions' = None,
            supplemental_groups: 'SupplementalGroupsStrategyOptions' = None,
            volumes: typing.List[str] = None,
    ):
        """Create PodSecurityPolicySpec instance."""
        super(PodSecurityPolicySpec, self).__init__(
            api_version='policy/v1beta1',
            kind='PodSecurityPolicySpec'
        )
        self._properties = {
            'allowPrivilegeEscalation': allow_privilege_escalation or None,
            'allowedCSIDrivers': allowed_csidrivers or [],
            'allowedCapabilities': allowed_capabilities or [],
            'allowedFlexVolumes': allowed_flex_volumes or [],
            'allowedHostPaths': allowed_host_paths or [],
            'allowedProcMountTypes': allowed_proc_mount_types or [],
            'allowedUnsafeSysctls': allowed_unsafe_sysctls or [],
            'defaultAddCapabilities': default_add_capabilities or [],
            'defaultAllowPrivilegeEscalation': default_allow_privilege_escalation or None,
            'forbiddenSysctls': forbidden_sysctls or [],
            'fsGroup': fs_group or FSGroupStrategyOptions(),
            'hostIPC': host_ipc or None,
            'hostNetwork': host_network or None,
            'hostPID': host_pid or None,
            'hostPorts': host_ports or [],
            'privileged': privileged or None,
            'readOnlyRootFilesystem': read_only_root_filesystem or None,
            'requiredDropCapabilities': required_drop_capabilities or [],
            'runAsGroup': run_as_group or RunAsGroupStrategyOptions(),
            'runAsUser': run_as_user or RunAsUserStrategyOptions(),
            'seLinux': se_linux or SELinuxStrategyOptions(),
            'supplementalGroups': supplemental_groups or SupplementalGroupsStrategyOptions(),
            'volumes': volumes or [],

        }
        self._types = {
            'allowPrivilegeEscalation': (bool, None),
            'allowedCSIDrivers': (list, AllowedCSIDriver),
            'allowedCapabilities': (list, str),
            'allowedFlexVolumes': (list, AllowedFlexVolume),
            'allowedHostPaths': (list, AllowedHostPath),
            'allowedProcMountTypes': (list, str),
            'allowedUnsafeSysctls': (list, str),
            'defaultAddCapabilities': (list, str),
            'defaultAllowPrivilegeEscalation': (bool, None),
            'forbiddenSysctls': (list, str),
            'fsGroup': (FSGroupStrategyOptions, None),
            'hostIPC': (bool, None),
            'hostNetwork': (bool, None),
            'hostPID': (bool, None),
            'hostPorts': (list, HostPortRange),
            'privileged': (bool, None),
            'readOnlyRootFilesystem': (bool, None),
            'requiredDropCapabilities': (list, str),
            'runAsGroup': (RunAsGroupStrategyOptions, None),
            'runAsUser': (RunAsUserStrategyOptions, None),
            'seLinux': (SELinuxStrategyOptions, None),
            'supplementalGroups': (SupplementalGroupsStrategyOptions, None),
            'volumes': (list, str),

        }

    @property
    def allow_privilege_escalation(self) -> bool:
        """
        allowPrivilegeEscalation determines if a pod can request to
        allow privilege escalation. If unspecified, defaults to
        true.
        """
        return self._properties.get('allowPrivilegeEscalation')

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, value: bool):
        """
        allowPrivilegeEscalation determines if a pod can request to
        allow privilege escalation. If unspecified, defaults to
        true.
        """
        self._properties['allowPrivilegeEscalation'] = value

    @property
    def allowed_csidrivers(self) -> typing.List['AllowedCSIDriver']:
        """
        AllowedCSIDrivers is a whitelist of inline CSI drivers that
        must be explicitly set to be embedded within a pod spec. An
        empty value means no CSI drivers can run inline within a pod
        spec.
        """
        return self._properties.get('allowedCSIDrivers')

    @allowed_csidrivers.setter
    def allowed_csidrivers(
            self,
            value: typing.Union[typing.List['AllowedCSIDriver'], typing.List[dict]]
    ):
        """
        AllowedCSIDrivers is a whitelist of inline CSI drivers that
        must be explicitly set to be embedded within a pod spec. An
        empty value means no CSI drivers can run inline within a pod
        spec.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = AllowedCSIDriver().from_dict(item)
            cleaned.append(item)
        self._properties['allowedCSIDrivers'] = cleaned

    @property
    def allowed_capabilities(self) -> typing.List[str]:
        """
        allowedCapabilities is a list of capabilities that can be
        requested to add to the container. Capabilities in this
        field may be added at the pod author's discretion. You must
        not list a capability in both allowedCapabilities and
        requiredDropCapabilities.
        """
        return self._properties.get('allowedCapabilities')

    @allowed_capabilities.setter
    def allowed_capabilities(self, value: typing.List[str]):
        """
        allowedCapabilities is a list of capabilities that can be
        requested to add to the container. Capabilities in this
        field may be added at the pod author's discretion. You must
        not list a capability in both allowedCapabilities and
        requiredDropCapabilities.
        """
        self._properties['allowedCapabilities'] = value

    @property
    def allowed_flex_volumes(self) -> typing.List['AllowedFlexVolume']:
        """
        allowedFlexVolumes is a whitelist of allowed Flexvolumes.
        Empty or nil indicates that all Flexvolumes may be used.
        This parameter is effective only when the usage of the
        Flexvolumes is allowed in the "volumes" field.
        """
        return self._properties.get('allowedFlexVolumes')

    @allowed_flex_volumes.setter
    def allowed_flex_volumes(
            self,
            value: typing.Union[typing.List['AllowedFlexVolume'], typing.List[dict]]
    ):
        """
        allowedFlexVolumes is a whitelist of allowed Flexvolumes.
        Empty or nil indicates that all Flexvolumes may be used.
        This parameter is effective only when the usage of the
        Flexvolumes is allowed in the "volumes" field.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = AllowedFlexVolume().from_dict(item)
            cleaned.append(item)
        self._properties['allowedFlexVolumes'] = cleaned

    @property
    def allowed_host_paths(self) -> typing.List['AllowedHostPath']:
        """
        allowedHostPaths is a white list of allowed host paths.
        Empty indicates that all host paths may be used.
        """
        return self._properties.get('allowedHostPaths')

    @allowed_host_paths.setter
    def allowed_host_paths(
            self,
            value: typing.Union[typing.List['AllowedHostPath'], typing.List[dict]]
    ):
        """
        allowedHostPaths is a white list of allowed host paths.
        Empty indicates that all host paths may be used.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = AllowedHostPath().from_dict(item)
            cleaned.append(item)
        self._properties['allowedHostPaths'] = cleaned

    @property
    def allowed_proc_mount_types(self) -> typing.List[str]:
        """
        AllowedProcMountTypes is a whitelist of allowed
        ProcMountTypes. Empty or nil indicates that only the
        DefaultProcMountType may be used. This requires the
        ProcMountType feature flag to be enabled.
        """
        return self._properties.get('allowedProcMountTypes')

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, value: typing.List[str]):
        """
        AllowedProcMountTypes is a whitelist of allowed
        ProcMountTypes. Empty or nil indicates that only the
        DefaultProcMountType may be used. This requires the
        ProcMountType feature flag to be enabled.
        """
        self._properties['allowedProcMountTypes'] = value

    @property
    def allowed_unsafe_sysctls(self) -> typing.List[str]:
        """
        allowedUnsafeSysctls is a list of explicitly allowed unsafe
        sysctls, defaults to none. Each entry is either a plain
        sysctl name or ends in "*" in which case it is considered as
        a prefix of allowed sysctls. Single * means all unsafe
        sysctls are allowed. Kubelet has to whitelist all allowed
        unsafe sysctls explicitly to avoid rejection.

        Examples:
        e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*"
        allows "foo.bar", "foo.baz", etc.
        """
        return self._properties.get('allowedUnsafeSysctls')

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, value: typing.List[str]):
        """
        allowedUnsafeSysctls is a list of explicitly allowed unsafe
        sysctls, defaults to none. Each entry is either a plain
        sysctl name or ends in "*" in which case it is considered as
        a prefix of allowed sysctls. Single * means all unsafe
        sysctls are allowed. Kubelet has to whitelist all allowed
        unsafe sysctls explicitly to avoid rejection.

        Examples:
        e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*"
        allows "foo.bar", "foo.baz", etc.
        """
        self._properties['allowedUnsafeSysctls'] = value

    @property
    def default_add_capabilities(self) -> typing.List[str]:
        """
        defaultAddCapabilities is the default set of capabilities
        that will be added to the container unless the pod spec
        specifically drops the capability.  You may not list a
        capability in both defaultAddCapabilities and
        requiredDropCapabilities. Capabilities added here are
        implicitly allowed, and need not be included in the
        allowedCapabilities list.
        """
        return self._properties.get('defaultAddCapabilities')

    @default_add_capabilities.setter
    def default_add_capabilities(self, value: typing.List[str]):
        """
        defaultAddCapabilities is the default set of capabilities
        that will be added to the container unless the pod spec
        specifically drops the capability.  You may not list a
        capability in both defaultAddCapabilities and
        requiredDropCapabilities. Capabilities added here are
        implicitly allowed, and need not be included in the
        allowedCapabilities list.
        """
        self._properties['defaultAddCapabilities'] = value

    @property
    def default_allow_privilege_escalation(self) -> bool:
        """
        defaultAllowPrivilegeEscalation controls the default setting
        for whether a process can gain more privileges than its
        parent process.
        """
        return self._properties.get('defaultAllowPrivilegeEscalation')

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(self, value: bool):
        """
        defaultAllowPrivilegeEscalation controls the default setting
        for whether a process can gain more privileges than its
        parent process.
        """
        self._properties['defaultAllowPrivilegeEscalation'] = value

    @property
    def forbidden_sysctls(self) -> typing.List[str]:
        """
        forbiddenSysctls is a list of explicitly forbidden sysctls,
        defaults to none. Each entry is either a plain sysctl name
        or ends in "*" in which case it is considered as a prefix of
        forbidden sysctls. Single * means all sysctls are forbidden.
        Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc.
        e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.
        """
        return self._properties.get('forbiddenSysctls')

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, value: typing.List[str]):
        """
        forbiddenSysctls is a list of explicitly forbidden sysctls,
        defaults to none. Each entry is either a plain sysctl name
        or ends in "*" in which case it is considered as a prefix of
        forbidden sysctls. Single * means all sysctls are forbidden.
        Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc.
        e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.
        """
        self._properties['forbiddenSysctls'] = value

    @property
    def fs_group(self) -> 'FSGroupStrategyOptions':
        """
        fsGroup is the strategy that will dictate what fs group is
        used by the SecurityContext.
        """
        return self._properties.get('fsGroup')

    @fs_group.setter
    def fs_group(self, value: typing.Union['FSGroupStrategyOptions', dict]):
        """
        fsGroup is the strategy that will dictate what fs group is
        used by the SecurityContext.
        """
        if isinstance(value, dict):
            value = FSGroupStrategyOptions().from_dict(value)
        self._properties['fsGroup'] = value

    @property
    def host_ipc(self) -> bool:
        """
        hostIPC determines if the policy allows the use of HostIPC
        in the pod spec.
        """
        return self._properties.get('hostIPC')

    @host_ipc.setter
    def host_ipc(self, value: bool):
        """
        hostIPC determines if the policy allows the use of HostIPC
        in the pod spec.
        """
        self._properties['hostIPC'] = value

    @property
    def host_network(self) -> bool:
        """
        hostNetwork determines if the policy allows the use of
        HostNetwork in the pod spec.
        """
        return self._properties.get('hostNetwork')

    @host_network.setter
    def host_network(self, value: bool):
        """
        hostNetwork determines if the policy allows the use of
        HostNetwork in the pod spec.
        """
        self._properties['hostNetwork'] = value

    @property
    def host_pid(self) -> bool:
        """
        hostPID determines if the policy allows the use of HostPID
        in the pod spec.
        """
        return self._properties.get('hostPID')

    @host_pid.setter
    def host_pid(self, value: bool):
        """
        hostPID determines if the policy allows the use of HostPID
        in the pod spec.
        """
        self._properties['hostPID'] = value

    @property
    def host_ports(self) -> typing.List['HostPortRange']:
        """
        hostPorts determines which host port ranges are allowed to
        be exposed.
        """
        return self._properties.get('hostPorts')

    @host_ports.setter
    def host_ports(
            self,
            value: typing.Union[typing.List['HostPortRange'], typing.List[dict]]
    ):
        """
        hostPorts determines which host port ranges are allowed to
        be exposed.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HostPortRange().from_dict(item)
            cleaned.append(item)
        self._properties['hostPorts'] = cleaned

    @property
    def privileged(self) -> bool:
        """
        privileged determines if a pod can request to be run as
        privileged.
        """
        return self._properties.get('privileged')

    @privileged.setter
    def privileged(self, value: bool):
        """
        privileged determines if a pod can request to be run as
        privileged.
        """
        self._properties['privileged'] = value

    @property
    def read_only_root_filesystem(self) -> bool:
        """
        readOnlyRootFilesystem when set to true will force
        containers to run with a read only root file system.  If the
        container specifically requests to run with a non-read only
        root file system the PSP should deny the pod. If set to
        false the container may run with a read only root file
        system if it wishes but it will not be forced to.
        """
        return self._properties.get('readOnlyRootFilesystem')

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, value: bool):
        """
        readOnlyRootFilesystem when set to true will force
        containers to run with a read only root file system.  If the
        container specifically requests to run with a non-read only
        root file system the PSP should deny the pod. If set to
        false the container may run with a read only root file
        system if it wishes but it will not be forced to.
        """
        self._properties['readOnlyRootFilesystem'] = value

    @property
    def required_drop_capabilities(self) -> typing.List[str]:
        """
        requiredDropCapabilities are the capabilities that will be
        dropped from the container.  These are required to be
        dropped and cannot be added.
        """
        return self._properties.get('requiredDropCapabilities')

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, value: typing.List[str]):
        """
        requiredDropCapabilities are the capabilities that will be
        dropped from the container.  These are required to be
        dropped and cannot be added.
        """
        self._properties['requiredDropCapabilities'] = value

    @property
    def run_as_group(self) -> 'RunAsGroupStrategyOptions':
        """
        RunAsGroup is the strategy that will dictate the allowable
        RunAsGroup values that may be set. If this field is omitted,
        the pod's RunAsGroup can take any value. This field requires
        the RunAsGroup feature gate to be enabled.
        """
        return self._properties.get('runAsGroup')

    @run_as_group.setter
    def run_as_group(self, value: typing.Union['RunAsGroupStrategyOptions', dict]):
        """
        RunAsGroup is the strategy that will dictate the allowable
        RunAsGroup values that may be set. If this field is omitted,
        the pod's RunAsGroup can take any value. This field requires
        the RunAsGroup feature gate to be enabled.
        """
        if isinstance(value, dict):
            value = RunAsGroupStrategyOptions().from_dict(value)
        self._properties['runAsGroup'] = value

    @property
    def run_as_user(self) -> 'RunAsUserStrategyOptions':
        """
        runAsUser is the strategy that will dictate the allowable
        RunAsUser values that may be set.
        """
        return self._properties.get('runAsUser')

    @run_as_user.setter
    def run_as_user(self, value: typing.Union['RunAsUserStrategyOptions', dict]):
        """
        runAsUser is the strategy that will dictate the allowable
        RunAsUser values that may be set.
        """
        if isinstance(value, dict):
            value = RunAsUserStrategyOptions().from_dict(value)
        self._properties['runAsUser'] = value

    @property
    def se_linux(self) -> 'SELinuxStrategyOptions':
        """
        seLinux is the strategy that will dictate the allowable
        labels that may be set.
        """
        return self._properties.get('seLinux')

    @se_linux.setter
    def se_linux(self, value: typing.Union['SELinuxStrategyOptions', dict]):
        """
        seLinux is the strategy that will dictate the allowable
        labels that may be set.
        """
        if isinstance(value, dict):
            value = SELinuxStrategyOptions().from_dict(value)
        self._properties['seLinux'] = value

    @property
    def supplemental_groups(self) -> 'SupplementalGroupsStrategyOptions':
        """
        supplementalGroups is the strategy that will dictate what
        supplemental groups are used by the SecurityContext.
        """
        return self._properties.get('supplementalGroups')

    @supplemental_groups.setter
    def supplemental_groups(self, value: typing.Union['SupplementalGroupsStrategyOptions', dict]):
        """
        supplementalGroups is the strategy that will dictate what
        supplemental groups are used by the SecurityContext.
        """
        if isinstance(value, dict):
            value = SupplementalGroupsStrategyOptions().from_dict(value)
        self._properties['supplementalGroups'] = value

    @property
    def volumes(self) -> typing.List[str]:
        """
        volumes is a white list of allowed volume plugins. Empty
        indicates that no volumes may be used. To allow all volumes
        you may use '*'.
        """
        return self._properties.get('volumes')

    @volumes.setter
    def volumes(self, value: typing.List[str]):
        """
        volumes is a white list of allowed volume plugins. Empty
        indicates that no volumes may be used. To allow all volumes
        you may use '*'.
        """
        self._properties['volumes'] = value

    def __enter__(self) -> 'PodSecurityPolicySpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RunAsGroupStrategyOptions(_kuber_definitions.Definition):
    """
    RunAsGroupStrategyOptions defines the strategy type and any
    options used to create the strategy.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create RunAsGroupStrategyOptions instance."""
        super(RunAsGroupStrategyOptions, self).__init__(
            api_version='policy/v1beta1',
            kind='RunAsGroupStrategyOptions'
        )
        self._properties = {
            'ranges': ranges or [],
            'rule': rule or '',

        }
        self._types = {
            'ranges': (list, IDRange),
            'rule': (str, None),

        }

    @property
    def ranges(self) -> typing.List['IDRange']:
        """
        ranges are the allowed ranges of gids that may be used. If
        you would like to force a single gid then supply a single
        range with the same start and end. Required for MustRunAs.
        """
        return self._properties.get('ranges')

    @ranges.setter
    def ranges(
            self,
            value: typing.Union[typing.List['IDRange'], typing.List[dict]]
    ):
        """
        ranges are the allowed ranges of gids that may be used. If
        you would like to force a single gid then supply a single
        range with the same start and end. Required for MustRunAs.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IDRange().from_dict(item)
            cleaned.append(item)
        self._properties['ranges'] = cleaned

    @property
    def rule(self) -> str:
        """
        rule is the strategy that will dictate the allowable
        RunAsGroup values that may be set.
        """
        return self._properties.get('rule')

    @rule.setter
    def rule(self, value: str):
        """
        rule is the strategy that will dictate the allowable
        RunAsGroup values that may be set.
        """
        self._properties['rule'] = value

    def __enter__(self) -> 'RunAsGroupStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RunAsUserStrategyOptions(_kuber_definitions.Definition):
    """
    RunAsUserStrategyOptions defines the strategy type and any
    options used to create the strategy.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create RunAsUserStrategyOptions instance."""
        super(RunAsUserStrategyOptions, self).__init__(
            api_version='policy/v1beta1',
            kind='RunAsUserStrategyOptions'
        )
        self._properties = {
            'ranges': ranges or [],
            'rule': rule or '',

        }
        self._types = {
            'ranges': (list, IDRange),
            'rule': (str, None),

        }

    @property
    def ranges(self) -> typing.List['IDRange']:
        """
        ranges are the allowed ranges of uids that may be used. If
        you would like to force a single uid then supply a single
        range with the same start and end. Required for MustRunAs.
        """
        return self._properties.get('ranges')

    @ranges.setter
    def ranges(
            self,
            value: typing.Union[typing.List['IDRange'], typing.List[dict]]
    ):
        """
        ranges are the allowed ranges of uids that may be used. If
        you would like to force a single uid then supply a single
        range with the same start and end. Required for MustRunAs.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IDRange().from_dict(item)
            cleaned.append(item)
        self._properties['ranges'] = cleaned

    @property
    def rule(self) -> str:
        """
        rule is the strategy that will dictate the allowable
        RunAsUser values that may be set.
        """
        return self._properties.get('rule')

    @rule.setter
    def rule(self, value: str):
        """
        rule is the strategy that will dictate the allowable
        RunAsUser values that may be set.
        """
        self._properties['rule'] = value

    def __enter__(self) -> 'RunAsUserStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SELinuxStrategyOptions(_kuber_definitions.Definition):
    """
    SELinuxStrategyOptions defines the strategy type and any
    options used to create the strategy.
    """

    def __init__(
            self,
            rule: str = None,
            se_linux_options: 'SELinuxOptions' = None,
    ):
        """Create SELinuxStrategyOptions instance."""
        super(SELinuxStrategyOptions, self).__init__(
            api_version='policy/v1beta1',
            kind='SELinuxStrategyOptions'
        )
        self._properties = {
            'rule': rule or '',
            'seLinuxOptions': se_linux_options or SELinuxOptions(),

        }
        self._types = {
            'rule': (str, None),
            'seLinuxOptions': (SELinuxOptions, None),

        }

    @property
    def rule(self) -> str:
        """
        rule is the strategy that will dictate the allowable labels
        that may be set.
        """
        return self._properties.get('rule')

    @rule.setter
    def rule(self, value: str):
        """
        rule is the strategy that will dictate the allowable labels
        that may be set.
        """
        self._properties['rule'] = value

    @property
    def se_linux_options(self) -> 'SELinuxOptions':
        """
        seLinuxOptions required to run as; required for MustRunAs
        More info: https://kubernetes.io/docs/tasks/configure-pod-
        container/security-context/
        """
        return self._properties.get('seLinuxOptions')

    @se_linux_options.setter
    def se_linux_options(self, value: typing.Union['SELinuxOptions', dict]):
        """
        seLinuxOptions required to run as; required for MustRunAs
        More info: https://kubernetes.io/docs/tasks/configure-pod-
        container/security-context/
        """
        if isinstance(value, dict):
            value = SELinuxOptions().from_dict(value)
        self._properties['seLinuxOptions'] = value

    def __enter__(self) -> 'SELinuxStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SupplementalGroupsStrategyOptions(_kuber_definitions.Definition):
    """
    SupplementalGroupsStrategyOptions defines the strategy type
    and options used to create the strategy.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create SupplementalGroupsStrategyOptions instance."""
        super(SupplementalGroupsStrategyOptions, self).__init__(
            api_version='policy/v1beta1',
            kind='SupplementalGroupsStrategyOptions'
        )
        self._properties = {
            'ranges': ranges or [],
            'rule': rule or '',

        }
        self._types = {
            'ranges': (list, IDRange),
            'rule': (str, None),

        }

    @property
    def ranges(self) -> typing.List['IDRange']:
        """
        ranges are the allowed ranges of supplemental groups.  If
        you would like to force a single supplemental group then
        supply a single range with the same start and end. Required
        for MustRunAs.
        """
        return self._properties.get('ranges')

    @ranges.setter
    def ranges(
            self,
            value: typing.Union[typing.List['IDRange'], typing.List[dict]]
    ):
        """
        ranges are the allowed ranges of supplemental groups.  If
        you would like to force a single supplemental group then
        supply a single range with the same start and end. Required
        for MustRunAs.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IDRange().from_dict(item)
            cleaned.append(item)
        self._properties['ranges'] = cleaned

    @property
    def rule(self) -> str:
        """
        rule is the strategy that will dictate what supplemental
        groups is used in the SecurityContext.
        """
        return self._properties.get('rule')

    @rule.setter
    def rule(self, value: str):
        """
        rule is the strategy that will dictate what supplemental
        groups is used in the SecurityContext.
        """
        self._properties['rule'] = value

    def __enter__(self) -> 'SupplementalGroupsStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

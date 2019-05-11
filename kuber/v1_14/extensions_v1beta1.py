import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_14.core_v1 import Container
from kuber.v1_14.core_v1 import ContainerPort
from kuber.v1_14.core_v1 import EnvFromSource
from kuber.v1_14.core_v1 import EnvVar
from kuber.v1_14.meta_v1 import LabelSelector
from kuber.v1_14.core_v1 import Lifecycle
from kuber.v1_14.meta_v1 import ListMeta
from kuber.v1_14.core_v1 import LoadBalancerStatus
from kuber.v1_14.meta_v1 import ObjectMeta
from kuber.v1_14.core_v1 import PodTemplateSpec
from kuber.v1_14.core_v1 import Probe
from kuber.v1_14.core_v1 import ResourceRequirements
from kuber.v1_14.core_v1 import SELinuxOptions
from kuber.v1_14.core_v1 import SecurityContext
from kuber.v1_14.meta_v1 import Status
from kuber.v1_14.meta_v1 import StatusDetails
from kuber.v1_14.core_v1 import VolumeDevice
from kuber.v1_14.core_v1 import VolumeMount


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
            api_version='extensions/v1beta1',
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
    allowed to be used. Deprecated: use AllowedFlexVolume from
    policy API Group instead.
    """

    def __init__(
            self,
            driver: str = None,
    ):
        """Create AllowedFlexVolume instance."""
        super(AllowedFlexVolume, self).__init__(
            api_version='extensions/v1beta1',
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
    prefix to be defined. Deprecated: use AllowedHostPath from
    policy API Group instead.
    """

    def __init__(
            self,
            path_prefix: str = None,
            read_only: bool = None,
    ):
        """Create AllowedHostPath instance."""
        super(AllowedHostPath, self).__init__(
            api_version='extensions/v1beta1',
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


class DaemonSet(_kuber_definitions.Resource):
    """
    DEPRECATED - This group version of DaemonSet is deprecated
    by apps/v1beta2/DaemonSet. See the release notes for more
    information. DaemonSet represents the configuration of a
    daemon set.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'DaemonSetSpec' = None,
    ):
        """Create DaemonSet instance."""
        super(DaemonSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSet'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or DaemonSetSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (DaemonSetSpec, None),
            'status': (DaemonSetStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'DaemonSetSpec':
        """
        The desired behavior of this daemon set. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['DaemonSetSpec', dict]):
        """
        The desired behavior of this daemon set. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = DaemonSetSpec().from_dict(value)
        self._properties['spec'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'DaemonSet':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.template.spec.containers if c.name == name), None)

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'DaemonSetStatus':
        """
        Creates the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_daemon_set',
            'create_daemon_set'
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
            DaemonSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'DaemonSetStatus':
        """
        Replaces the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_daemon_set',
            'replace_daemon_set'
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
            DaemonSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'DaemonSetStatus':
        """
        Patches the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_daemon_set',
            'patch_daemon_set'
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
            DaemonSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'DaemonSetStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_daemon_set',
            'read_daemon_set'
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
            DaemonSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the DaemonSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_daemon_set',
            'read_daemon_set'
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
        Deletes the DaemonSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_daemon_set',
            'delete_daemon_set'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'DaemonSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetCondition(_kuber_definitions.Definition):
    """
    DaemonSetCondition describes the state of a DaemonSet at a
    certain point.
    """

    def __init__(
            self,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create DaemonSetCondition instance."""
        super(DaemonSetCondition, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetCondition'
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
        Last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of DaemonSet condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of DaemonSet condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'DaemonSetCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetList(_kuber_definitions.Collection):
    """
    DaemonSetList is a collection of daemon sets.
    """

    def __init__(
            self,
            items: typing.List['DaemonSet'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create DaemonSetList instance."""
        super(DaemonSetList, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, DaemonSet),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['DaemonSet']:
        """
        A list of daemon sets.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['DaemonSet'], typing.List[dict]]
    ):
        """
        A list of daemon sets.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = DaemonSet().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'DaemonSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetSpec(_kuber_definitions.Definition):
    """
    DaemonSetSpec is the specification of a daemon set.
    """

    def __init__(
            self,
            min_ready_seconds: int = None,
            revision_history_limit: int = None,
            selector: 'LabelSelector' = None,
            template: 'PodTemplateSpec' = None,
            template_generation: int = None,
            update_strategy: 'DaemonSetUpdateStrategy' = None,
    ):
        """Create DaemonSetSpec instance."""
        super(DaemonSetSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetSpec'
        )
        self._properties = {
            'minReadySeconds': min_ready_seconds or None,
            'revisionHistoryLimit': revision_history_limit or None,
            'selector': selector or LabelSelector(),
            'template': template or PodTemplateSpec(),
            'templateGeneration': template_generation or None,
            'updateStrategy': update_strategy or DaemonSetUpdateStrategy(),

        }
        self._types = {
            'minReadySeconds': (int, None),
            'revisionHistoryLimit': (int, None),
            'selector': (LabelSelector, None),
            'template': (PodTemplateSpec, None),
            'templateGeneration': (int, None),
            'updateStrategy': (DaemonSetUpdateStrategy, None),

        }

    @property
    def min_ready_seconds(self) -> int:
        """
        The minimum number of seconds for which a newly created
        DaemonSet pod should be ready without any of its container
        crashing, for it to be considered available. Defaults to 0
        (pod will be considered available as soon as it is ready).
        """
        return self._properties.get('minReadySeconds')

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        The minimum number of seconds for which a newly created
        DaemonSet pod should be ready without any of its container
        crashing, for it to be considered available. Defaults to 0
        (pod will be considered available as soon as it is ready).
        """
        self._properties['minReadySeconds'] = value

    @property
    def revision_history_limit(self) -> int:
        """
        The number of old history to retain to allow rollback. This
        is a pointer to distinguish between explicit zero and not
        specified. Defaults to 10.
        """
        return self._properties.get('revisionHistoryLimit')

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        The number of old history to retain to allow rollback. This
        is a pointer to distinguish between explicit zero and not
        specified. Defaults to 10.
        """
        self._properties['revisionHistoryLimit'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        A label query over pods that are managed by the daemon set.
        Must match in order to be controlled. If empty, defaulted to
        labels on Pod template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        A label query over pods that are managed by the daemon set.
        Must match in order to be controlled. If empty, defaulted to
        labels on Pod template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        An object that describes the pod that will be created. The
        DaemonSet will create exactly one copy of this pod on every
        node that matches the template's node selector (or on every
        node if no node selector is specified). More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/replication
        controller#pod-template
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        An object that describes the pod that will be created. The
        DaemonSet will create exactly one copy of this pod on every
        node that matches the template's node selector (or on every
        node if no node selector is specified). More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/replication
        controller#pod-template
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    @property
    def template_generation(self) -> int:
        """
        DEPRECATED. A sequence number representing a specific
        generation of the template. Populated by the system. It can
        be set only during the creation.
        """
        return self._properties.get('templateGeneration')

    @template_generation.setter
    def template_generation(self, value: int):
        """
        DEPRECATED. A sequence number representing a specific
        generation of the template. Populated by the system. It can
        be set only during the creation.
        """
        self._properties['templateGeneration'] = value

    @property
    def update_strategy(self) -> 'DaemonSetUpdateStrategy':
        """
        An update strategy to replace existing DaemonSet pods with
        new pods.
        """
        return self._properties.get('updateStrategy')

    @update_strategy.setter
    def update_strategy(self, value: typing.Union['DaemonSetUpdateStrategy', dict]):
        """
        An update strategy to replace existing DaemonSet pods with
        new pods.
        """
        if isinstance(value, dict):
            value = DaemonSetUpdateStrategy().from_dict(value)
        self._properties['updateStrategy'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'DaemonSetSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def __enter__(self) -> 'DaemonSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetStatus(_kuber_definitions.Definition):
    """
    DaemonSetStatus represents the current status of a daemon
    set.
    """

    def __init__(
            self,
            collision_count: int = None,
            conditions: typing.List['DaemonSetCondition'] = None,
            current_number_scheduled: int = None,
            desired_number_scheduled: int = None,
            number_available: int = None,
            number_misscheduled: int = None,
            number_ready: int = None,
            number_unavailable: int = None,
            observed_generation: int = None,
            updated_number_scheduled: int = None,
    ):
        """Create DaemonSetStatus instance."""
        super(DaemonSetStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetStatus'
        )
        self._properties = {
            'collisionCount': collision_count or None,
            'conditions': conditions or [],
            'currentNumberScheduled': current_number_scheduled or None,
            'desiredNumberScheduled': desired_number_scheduled or None,
            'numberAvailable': number_available or None,
            'numberMisscheduled': number_misscheduled or None,
            'numberReady': number_ready or None,
            'numberUnavailable': number_unavailable or None,
            'observedGeneration': observed_generation or None,
            'updatedNumberScheduled': updated_number_scheduled or None,

        }
        self._types = {
            'collisionCount': (int, None),
            'conditions': (list, DaemonSetCondition),
            'currentNumberScheduled': (int, None),
            'desiredNumberScheduled': (int, None),
            'numberAvailable': (int, None),
            'numberMisscheduled': (int, None),
            'numberReady': (int, None),
            'numberUnavailable': (int, None),
            'observedGeneration': (int, None),
            'updatedNumberScheduled': (int, None),

        }

    @property
    def collision_count(self) -> int:
        """
        Count of hash collisions for the DaemonSet. The DaemonSet
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ControllerRevision.
        """
        return self._properties.get('collisionCount')

    @collision_count.setter
    def collision_count(self, value: int):
        """
        Count of hash collisions for the DaemonSet. The DaemonSet
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ControllerRevision.
        """
        self._properties['collisionCount'] = value

    @property
    def conditions(self) -> typing.List['DaemonSetCondition']:
        """
        Represents the latest available observations of a
        DaemonSet's current state.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['DaemonSetCondition'], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        DaemonSet's current state.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = DaemonSetCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def current_number_scheduled(self) -> int:
        """
        The number of nodes that are running at least 1 daemon pod
        and are supposed to run the daemon pod. More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/daemonset/
        """
        return self._properties.get('currentNumberScheduled')

    @current_number_scheduled.setter
    def current_number_scheduled(self, value: int):
        """
        The number of nodes that are running at least 1 daemon pod
        and are supposed to run the daemon pod. More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/daemonset/
        """
        self._properties['currentNumberScheduled'] = value

    @property
    def desired_number_scheduled(self) -> int:
        """
        The total number of nodes that should be running the daemon
        pod (including nodes correctly running the daemon pod). More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/daemonset/
        """
        return self._properties.get('desiredNumberScheduled')

    @desired_number_scheduled.setter
    def desired_number_scheduled(self, value: int):
        """
        The total number of nodes that should be running the daemon
        pod (including nodes correctly running the daemon pod). More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/daemonset/
        """
        self._properties['desiredNumberScheduled'] = value

    @property
    def number_available(self) -> int:
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and available
        (ready for at least spec.minReadySeconds)
        """
        return self._properties.get('numberAvailable')

    @number_available.setter
    def number_available(self, value: int):
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and available
        (ready for at least spec.minReadySeconds)
        """
        self._properties['numberAvailable'] = value

    @property
    def number_misscheduled(self) -> int:
        """
        The number of nodes that are running the daemon pod, but are
        not supposed to run the daemon pod. More info: https://kuber
        netes.io/docs/concepts/workloads/controllers/daemonset/
        """
        return self._properties.get('numberMisscheduled')

    @number_misscheduled.setter
    def number_misscheduled(self, value: int):
        """
        The number of nodes that are running the daemon pod, but are
        not supposed to run the daemon pod. More info: https://kuber
        netes.io/docs/concepts/workloads/controllers/daemonset/
        """
        self._properties['numberMisscheduled'] = value

    @property
    def number_ready(self) -> int:
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and ready.
        """
        return self._properties.get('numberReady')

    @number_ready.setter
    def number_ready(self, value: int):
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and ready.
        """
        self._properties['numberReady'] = value

    @property
    def number_unavailable(self) -> int:
        """
        The number of nodes that should be running the daemon pod
        and have none of the daemon pod running and available (ready
        for at least spec.minReadySeconds)
        """
        return self._properties.get('numberUnavailable')

    @number_unavailable.setter
    def number_unavailable(self, value: int):
        """
        The number of nodes that should be running the daemon pod
        and have none of the daemon pod running and available (ready
        for at least spec.minReadySeconds)
        """
        self._properties['numberUnavailable'] = value

    @property
    def observed_generation(self) -> int:
        """
        The most recent generation observed by the daemon set
        controller.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        The most recent generation observed by the daemon set
        controller.
        """
        self._properties['observedGeneration'] = value

    @property
    def updated_number_scheduled(self) -> int:
        """
        The total number of nodes that are running updated daemon
        pod
        """
        return self._properties.get('updatedNumberScheduled')

    @updated_number_scheduled.setter
    def updated_number_scheduled(self, value: int):
        """
        The total number of nodes that are running updated daemon
        pod
        """
        self._properties['updatedNumberScheduled'] = value

    def __enter__(self) -> 'DaemonSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetUpdateStrategy(_kuber_definitions.Definition):
    """

    """

    def __init__(
            self,
            rolling_update: 'RollingUpdateDaemonSet' = None,
            type_: str = None,
    ):
        """Create DaemonSetUpdateStrategy instance."""
        super(DaemonSetUpdateStrategy, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetUpdateStrategy'
        )
        self._properties = {
            'rollingUpdate': rolling_update or RollingUpdateDaemonSet(),
            'type': type_ or '',

        }
        self._types = {
            'rollingUpdate': (RollingUpdateDaemonSet, None),
            'type': (str, None),

        }

    @property
    def rolling_update(self) -> 'RollingUpdateDaemonSet':
        """
        Rolling update config params. Present only if type =
        "RollingUpdate".
        """
        return self._properties.get('rollingUpdate')

    @rolling_update.setter
    def rolling_update(self, value: typing.Union['RollingUpdateDaemonSet', dict]):
        """
        Rolling update config params. Present only if type =
        "RollingUpdate".
        """
        if isinstance(value, dict):
            value = RollingUpdateDaemonSet().from_dict(value)
        self._properties['rollingUpdate'] = value

    @property
    def type_(self) -> str:
        """
        Type of daemon set update. Can be "RollingUpdate" or
        "OnDelete". Default is OnDelete.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of daemon set update. Can be "RollingUpdate" or
        "OnDelete". Default is OnDelete.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'DaemonSetUpdateStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Deployment(_kuber_definitions.Resource):
    """
    DEPRECATED - This group version of Deployment is deprecated
    by apps/v1beta2/Deployment. See the release notes for more
    information. Deployment enables declarative updates for Pods
    and ReplicaSets.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'DeploymentSpec' = None,
    ):
        """Create Deployment instance."""
        super(Deployment, self).__init__(
            api_version='extensions/v1beta1',
            kind='Deployment'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or DeploymentSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (DeploymentSpec, None),
            'status': (DeploymentStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'DeploymentSpec':
        """
        Specification of the desired behavior of the Deployment.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['DeploymentSpec', dict]):
        """
        Specification of the desired behavior of the Deployment.
        """
        if isinstance(value, dict):
            value = DeploymentSpec().from_dict(value)
        self._properties['spec'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'Deployment':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.template.spec.containers if c.name == name), None)

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'DeploymentStatus':
        """
        Creates the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_deployment',
            'create_deployment'
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
            DeploymentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'DeploymentStatus':
        """
        Replaces the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_deployment',
            'replace_deployment'
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
            DeploymentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'DeploymentStatus':
        """
        Patches the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_deployment',
            'patch_deployment'
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
            DeploymentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'DeploymentStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_deployment',
            'read_deployment'
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
            DeploymentStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Deployment from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_deployment',
            'read_deployment'
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
        Deletes the Deployment from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_deployment',
            'delete_deployment'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'Deployment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentCondition(_kuber_definitions.Definition):
    """
    DeploymentCondition describes the state of a deployment at a
    certain point.
    """

    def __init__(
            self,
            last_transition_time: str = None,
            last_update_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create DeploymentCondition instance."""
        super(DeploymentCondition, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentCondition'
        )
        self._properties = {
            'lastTransitionTime': last_transition_time or None,
            'lastUpdateTime': last_update_time or None,
            'message': message or '',
            'reason': reason or '',
            'status': status or '',
            'type': type_ or '',

        }
        self._types = {
            'lastTransitionTime': (str, None),
            'lastUpdateTime': (str, None),
            'message': (str, None),
            'reason': (str, None),
            'status': (str, None),
            'type': (str, None),

        }

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def last_update_time(self) -> str:
        """
        The last time this condition was updated.
        """
        return self._properties.get('lastUpdateTime')

    @last_update_time.setter
    def last_update_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The last time this condition was updated.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastUpdateTime'] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of deployment condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of deployment condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'DeploymentCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentList(_kuber_definitions.Collection):
    """
    DeploymentList is a list of Deployments.
    """

    def __init__(
            self,
            items: typing.List['Deployment'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create DeploymentList instance."""
        super(DeploymentList, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Deployment),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Deployment']:
        """
        Items is the list of Deployments.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Deployment'], typing.List[dict]]
    ):
        """
        Items is the list of Deployments.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Deployment().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata.
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'DeploymentList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentRollback(_kuber_definitions.Definition):
    """
    DEPRECATED. DeploymentRollback stores the information
    required to rollback a deployment.
    """

    def __init__(
            self,
            api_version: str = None,
            kind: str = None,
            name: str = None,
            rollback_to: 'RollbackConfig' = None,
            updated_annotations: dict = None,
    ):
        """Create DeploymentRollback instance."""
        super(DeploymentRollback, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentRollback'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'kind': kind or '',
            'name': name or '',
            'rollbackTo': rollback_to or RollbackConfig(),
            'updatedAnnotations': updated_annotations or {},

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'name': (str, None),
            'rollbackTo': (RollbackConfig, None),
            'updatedAnnotations': (dict, None),

        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return self._properties.get('apiVersion')

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties['apiVersion'] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        Required: This must match the Name of a deployment.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Required: This must match the Name of a deployment.
        """
        self._properties['name'] = value

    @property
    def rollback_to(self) -> 'RollbackConfig':
        """
        The config of this deployment rollback.
        """
        return self._properties.get('rollbackTo')

    @rollback_to.setter
    def rollback_to(self, value: typing.Union['RollbackConfig', dict]):
        """
        The config of this deployment rollback.
        """
        if isinstance(value, dict):
            value = RollbackConfig().from_dict(value)
        self._properties['rollbackTo'] = value

    @property
    def updated_annotations(self) -> dict:
        """
        The annotations to be updated to a deployment
        """
        return self._properties.get('updatedAnnotations')

    @updated_annotations.setter
    def updated_annotations(self, value: dict):
        """
        The annotations to be updated to a deployment
        """
        self._properties['updatedAnnotations'] = value

    def __enter__(self) -> 'DeploymentRollback':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentSpec(_kuber_definitions.Definition):
    """
    DeploymentSpec is the specification of the desired behavior
    of the Deployment.
    """

    def __init__(
            self,
            min_ready_seconds: int = None,
            paused: bool = None,
            progress_deadline_seconds: int = None,
            replicas: int = None,
            revision_history_limit: int = None,
            rollback_to: 'RollbackConfig' = None,
            selector: 'LabelSelector' = None,
            strategy: 'DeploymentStrategy' = None,
            template: 'PodTemplateSpec' = None,
    ):
        """Create DeploymentSpec instance."""
        super(DeploymentSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentSpec'
        )
        self._properties = {
            'minReadySeconds': min_ready_seconds or None,
            'paused': paused or None,
            'progressDeadlineSeconds': progress_deadline_seconds or None,
            'replicas': replicas or None,
            'revisionHistoryLimit': revision_history_limit or None,
            'rollbackTo': rollback_to or RollbackConfig(),
            'selector': selector or LabelSelector(),
            'strategy': strategy or DeploymentStrategy(),
            'template': template or PodTemplateSpec(),

        }
        self._types = {
            'minReadySeconds': (int, None),
            'paused': (bool, None),
            'progressDeadlineSeconds': (int, None),
            'replicas': (int, None),
            'revisionHistoryLimit': (int, None),
            'rollbackTo': (RollbackConfig, None),
            'selector': (LabelSelector, None),
            'strategy': (DeploymentStrategy, None),
            'template': (PodTemplateSpec, None),

        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        return self._properties.get('minReadySeconds')

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        self._properties['minReadySeconds'] = value

    @property
    def paused(self) -> bool:
        """
        Indicates that the deployment is paused and will not be
        processed by the deployment controller.
        """
        return self._properties.get('paused')

    @paused.setter
    def paused(self, value: bool):
        """
        Indicates that the deployment is paused and will not be
        processed by the deployment controller.
        """
        self._properties['paused'] = value

    @property
    def progress_deadline_seconds(self) -> int:
        """
        The maximum time in seconds for a deployment to make
        progress before it is considered to be failed. The
        deployment controller will continue to process failed
        deployments and a condition with a ProgressDeadlineExceeded
        reason will be surfaced in the deployment status. Note that
        progress will not be estimated during the time a deployment
        is paused. This is set to the max value of int32 (i.e.
        2147483647) by default, which means "no deadline".
        """
        return self._properties.get('progressDeadlineSeconds')

    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, value: int):
        """
        The maximum time in seconds for a deployment to make
        progress before it is considered to be failed. The
        deployment controller will continue to process failed
        deployments and a condition with a ProgressDeadlineExceeded
        reason will be surfaced in the deployment status. Note that
        progress will not be estimated during the time a deployment
        is paused. This is set to the max value of int32 (i.e.
        2147483647) by default, which means "no deadline".
        """
        self._properties['progressDeadlineSeconds'] = value

    @property
    def replicas(self) -> int:
        """
        Number of desired pods. This is a pointer to distinguish
        between explicit zero and not specified. Defaults to 1.
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Number of desired pods. This is a pointer to distinguish
        between explicit zero and not specified. Defaults to 1.
        """
        self._properties['replicas'] = value

    @property
    def revision_history_limit(self) -> int:
        """
        The number of old ReplicaSets to retain to allow rollback.
        This is a pointer to distinguish between explicit zero and
        not specified. This is set to the max value of int32 (i.e.
        2147483647) by default, which means "retaining all old
        RelicaSets".
        """
        return self._properties.get('revisionHistoryLimit')

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        The number of old ReplicaSets to retain to allow rollback.
        This is a pointer to distinguish between explicit zero and
        not specified. This is set to the max value of int32 (i.e.
        2147483647) by default, which means "retaining all old
        RelicaSets".
        """
        self._properties['revisionHistoryLimit'] = value

    @property
    def rollback_to(self) -> 'RollbackConfig':
        """
        DEPRECATED. The config this deployment is rolling back to.
        Will be cleared after rollback is done.
        """
        return self._properties.get('rollbackTo')

    @rollback_to.setter
    def rollback_to(self, value: typing.Union['RollbackConfig', dict]):
        """
        DEPRECATED. The config this deployment is rolling back to.
        Will be cleared after rollback is done.
        """
        if isinstance(value, dict):
            value = RollbackConfig().from_dict(value)
        self._properties['rollbackTo'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        Label selector for pods. Existing ReplicaSets whose pods are
        selected by this will be the ones affected by this
        deployment.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Label selector for pods. Existing ReplicaSets whose pods are
        selected by this will be the ones affected by this
        deployment.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def strategy(self) -> 'DeploymentStrategy':
        """
        The deployment strategy to use to replace existing pods with
        new ones.
        """
        return self._properties.get('strategy')

    @strategy.setter
    def strategy(self, value: typing.Union['DeploymentStrategy', dict]):
        """
        The deployment strategy to use to replace existing pods with
        new ones.
        """
        if isinstance(value, dict):
            value = DeploymentStrategy().from_dict(value)
        self._properties['strategy'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        Template describes the pods that will be created.
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        Template describes the pods that will be created.
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'DeploymentSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def __enter__(self) -> 'DeploymentSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentStatus(_kuber_definitions.Definition):
    """
    DeploymentStatus is the most recently observed status of the
    Deployment.
    """

    def __init__(
            self,
            available_replicas: int = None,
            collision_count: int = None,
            conditions: typing.List['DeploymentCondition'] = None,
            observed_generation: int = None,
            ready_replicas: int = None,
            replicas: int = None,
            unavailable_replicas: int = None,
            updated_replicas: int = None,
    ):
        """Create DeploymentStatus instance."""
        super(DeploymentStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentStatus'
        )
        self._properties = {
            'availableReplicas': available_replicas or None,
            'collisionCount': collision_count or None,
            'conditions': conditions or [],
            'observedGeneration': observed_generation or None,
            'readyReplicas': ready_replicas or None,
            'replicas': replicas or None,
            'unavailableReplicas': unavailable_replicas or None,
            'updatedReplicas': updated_replicas or None,

        }
        self._types = {
            'availableReplicas': (int, None),
            'collisionCount': (int, None),
            'conditions': (list, DeploymentCondition),
            'observedGeneration': (int, None),
            'readyReplicas': (int, None),
            'replicas': (int, None),
            'unavailableReplicas': (int, None),
            'updatedReplicas': (int, None),

        }

    @property
    def available_replicas(self) -> int:
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this deployment.
        """
        return self._properties.get('availableReplicas')

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this deployment.
        """
        self._properties['availableReplicas'] = value

    @property
    def collision_count(self) -> int:
        """
        Count of hash collisions for the Deployment. The Deployment
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ReplicaSet.
        """
        return self._properties.get('collisionCount')

    @collision_count.setter
    def collision_count(self, value: int):
        """
        Count of hash collisions for the Deployment. The Deployment
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ReplicaSet.
        """
        self._properties['collisionCount'] = value

    @property
    def conditions(self) -> typing.List['DeploymentCondition']:
        """
        Represents the latest available observations of a
        deployment's current state.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['DeploymentCondition'], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        deployment's current state.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = DeploymentCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def observed_generation(self) -> int:
        """
        The generation observed by the deployment controller.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        The generation observed by the deployment controller.
        """
        self._properties['observedGeneration'] = value

    @property
    def ready_replicas(self) -> int:
        """
        Total number of ready pods targeted by this deployment.
        """
        return self._properties.get('readyReplicas')

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        Total number of ready pods targeted by this deployment.
        """
        self._properties['readyReplicas'] = value

    @property
    def replicas(self) -> int:
        """
        Total number of non-terminated pods targeted by this
        deployment (their labels match the selector).
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Total number of non-terminated pods targeted by this
        deployment (their labels match the selector).
        """
        self._properties['replicas'] = value

    @property
    def unavailable_replicas(self) -> int:
        """
        Total number of unavailable pods targeted by this
        deployment. This is the total number of pods that are still
        required for the deployment to have 100% available capacity.
        They may either be pods that are running but not yet
        available or pods that still have not been created.
        """
        return self._properties.get('unavailableReplicas')

    @unavailable_replicas.setter
    def unavailable_replicas(self, value: int):
        """
        Total number of unavailable pods targeted by this
        deployment. This is the total number of pods that are still
        required for the deployment to have 100% available capacity.
        They may either be pods that are running but not yet
        available or pods that still have not been created.
        """
        self._properties['unavailableReplicas'] = value

    @property
    def updated_replicas(self) -> int:
        """
        Total number of non-terminated pods targeted by this
        deployment that have the desired template spec.
        """
        return self._properties.get('updatedReplicas')

    @updated_replicas.setter
    def updated_replicas(self, value: int):
        """
        Total number of non-terminated pods targeted by this
        deployment that have the desired template spec.
        """
        self._properties['updatedReplicas'] = value

    def __enter__(self) -> 'DeploymentStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentStrategy(_kuber_definitions.Definition):
    """
    DeploymentStrategy describes how to replace existing pods
    with new ones.
    """

    def __init__(
            self,
            rolling_update: 'RollingUpdateDeployment' = None,
            type_: str = None,
    ):
        """Create DeploymentStrategy instance."""
        super(DeploymentStrategy, self).__init__(
            api_version='extensions/v1beta1',
            kind='DeploymentStrategy'
        )
        self._properties = {
            'rollingUpdate': rolling_update or RollingUpdateDeployment(),
            'type': type_ or '',

        }
        self._types = {
            'rollingUpdate': (RollingUpdateDeployment, None),
            'type': (str, None),

        }

    @property
    def rolling_update(self) -> 'RollingUpdateDeployment':
        """
        Rolling update config params. Present only if
        DeploymentStrategyType = RollingUpdate.
        """
        return self._properties.get('rollingUpdate')

    @rolling_update.setter
    def rolling_update(self, value: typing.Union['RollingUpdateDeployment', dict]):
        """
        Rolling update config params. Present only if
        DeploymentStrategyType = RollingUpdate.
        """
        if isinstance(value, dict):
            value = RollingUpdateDeployment().from_dict(value)
        self._properties['rollingUpdate'] = value

    @property
    def type_(self) -> str:
        """
        Type of deployment. Can be "Recreate" or "RollingUpdate".
        Default is RollingUpdate.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of deployment. Can be "Recreate" or "RollingUpdate".
        Default is RollingUpdate.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'DeploymentStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FSGroupStrategyOptions(_kuber_definitions.Definition):
    """
    FSGroupStrategyOptions defines the strategy type and options
    used to create the strategy. Deprecated: use
    FSGroupStrategyOptions from policy API Group instead.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create FSGroupStrategyOptions instance."""
        super(FSGroupStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
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


class HTTPIngressPath(_kuber_definitions.Definition):
    """
    HTTPIngressPath associates a path regex with a backend.
    Incoming urls matching the path are forwarded to the
    backend.
    """

    def __init__(
            self,
            backend: 'IngressBackend' = None,
            path: str = None,
    ):
        """Create HTTPIngressPath instance."""
        super(HTTPIngressPath, self).__init__(
            api_version='extensions/v1beta1',
            kind='HTTPIngressPath'
        )
        self._properties = {
            'backend': backend or IngressBackend(),
            'path': path or '',

        }
        self._types = {
            'backend': (IngressBackend, None),
            'path': (str, None),

        }

    @property
    def backend(self) -> 'IngressBackend':
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        return self._properties.get('backend')

    @backend.setter
    def backend(self, value: typing.Union['IngressBackend', dict]):
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        if isinstance(value, dict):
            value = IngressBackend().from_dict(value)
        self._properties['backend'] = value

    @property
    def path(self) -> str:
        """
        Path is an extended POSIX regex as defined by IEEE Std
        1003.1, (i.e this follows the egrep/unix syntax, not the
        perl syntax) matched against the path of an incoming
        request. Currently it can contain characters disallowed from
        the conventional "path" part of a URL as defined by RFC
        3986. Paths must begin with a '/'. If unspecified, the path
        defaults to a catch all sending traffic to the backend.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is an extended POSIX regex as defined by IEEE Std
        1003.1, (i.e this follows the egrep/unix syntax, not the
        perl syntax) matched against the path of an incoming
        request. Currently it can contain characters disallowed from
        the conventional "path" part of a URL as defined by RFC
        3986. Paths must begin with a '/'. If unspecified, the path
        defaults to a catch all sending traffic to the backend.
        """
        self._properties['path'] = value

    def __enter__(self) -> 'HTTPIngressPath':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPIngressRuleValue(_kuber_definitions.Definition):
    """
    HTTPIngressRuleValue is a list of http selectors pointing to
    backends. In the example: http://<host>/<path>?<searchpart>
    -> backend where where parts of the url correspond to RFC
    3986, this resource will be used to match against everything
    after the last '/' and before the first '?' or '#'.
    """

    def __init__(
            self,
            paths: typing.List['HTTPIngressPath'] = None,
    ):
        """Create HTTPIngressRuleValue instance."""
        super(HTTPIngressRuleValue, self).__init__(
            api_version='extensions/v1beta1',
            kind='HTTPIngressRuleValue'
        )
        self._properties = {
            'paths': paths or [],

        }
        self._types = {
            'paths': (list, HTTPIngressPath),

        }

    @property
    def paths(self) -> typing.List['HTTPIngressPath']:
        """
        A collection of paths that map requests to backends.
        """
        return self._properties.get('paths')

    @paths.setter
    def paths(
            self,
            value: typing.Union[typing.List['HTTPIngressPath'], typing.List[dict]]
    ):
        """
        A collection of paths that map requests to backends.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HTTPIngressPath().from_dict(item)
            cleaned.append(item)
        self._properties['paths'] = cleaned

    def __enter__(self) -> 'HTTPIngressRuleValue':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HostPortRange(_kuber_definitions.Definition):
    """
    HostPortRange defines a range of host ports that will be
    enabled by a policy for pods to use.  It requires both the
    start and end to be defined. Deprecated: use HostPortRange
    from policy API Group instead.
    """

    def __init__(
            self,
            max_: int = None,
            min_: int = None,
    ):
        """Create HostPortRange instance."""
        super(HostPortRange, self).__init__(
            api_version='extensions/v1beta1',
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
    Deprecated: use IDRange from policy API Group instead.
    """

    def __init__(
            self,
            max_: int = None,
            min_: int = None,
    ):
        """Create IDRange instance."""
        super(IDRange, self).__init__(
            api_version='extensions/v1beta1',
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


class IPBlock(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of IPBlock is deprecated
    by networking/v1/IPBlock. IPBlock describes a particular
    CIDR (Ex. "192.168.1.1/24") that is allowed to the pods
    matched by a NetworkPolicySpec's podSelector. The except
    entry describes CIDRs that should not be included within
    this rule.
    """

    def __init__(
            self,
            cidr: str = None,
            except_: typing.List[str] = None,
    ):
        """Create IPBlock instance."""
        super(IPBlock, self).__init__(
            api_version='extensions/v1beta1',
            kind='IPBlock'
        )
        self._properties = {
            'cidr': cidr or '',
            'except': except_ or [],

        }
        self._types = {
            'cidr': (str, None),
            'except': (list, str),

        }

    @property
    def cidr(self) -> str:
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24"
        """
        return self._properties.get('cidr')

    @cidr.setter
    def cidr(self, value: str):
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24"
        """
        self._properties['cidr'] = value

    @property
    def except_(self) -> typing.List[str]:
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24"
        Except values will be rejected if they are outside the CIDR
        range
        """
        return self._properties.get('except')

    @except_.setter
    def except_(self, value: typing.List[str]):
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24"
        Except values will be rejected if they are outside the CIDR
        range
        """
        self._properties['except'] = value

    def __enter__(self) -> 'IPBlock':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Ingress(_kuber_definitions.Resource):
    """
    Ingress is a collection of rules that allow inbound
    connections to reach the endpoints defined by a backend. An
    Ingress can be configured to give services externally-
    reachable urls, load balance traffic, terminate SSL, offer
    name based virtual hosting etc. DEPRECATED - This group
    version of Ingress is deprecated by
    networking.k8s.io/v1beta1 Ingress. See the release notes for
    more information.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'IngressSpec' = None,
    ):
        """Create Ingress instance."""
        super(Ingress, self).__init__(
            api_version='extensions/v1beta1',
            kind='Ingress'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or IngressSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (IngressSpec, None),
            'status': (IngressStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'IngressSpec':
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['IngressSpec', dict]):
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = IngressSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Creates the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_ingress',
            'create_ingress'
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
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Replaces the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_ingress',
            'replace_ingress'
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
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Patches the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_ingress',
            'patch_ingress'
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
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_ingress',
            'read_ingress'
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
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Ingress from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_ingress',
            'read_ingress'
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
        Deletes the Ingress from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_ingress',
            'delete_ingress'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'Ingress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressBackend(_kuber_definitions.Definition):
    """
    IngressBackend describes all endpoints for a given service
    and port.
    """

    def __init__(
            self,
            service_name: str = None,
            service_port: typing.Union[str, int, None] = None,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressBackend'
        )
        self._properties = {
            'serviceName': service_name or '',
            'servicePort': service_port or None,

        }
        self._types = {
            'serviceName': (str, None),
            'servicePort': (int, None),

        }

    @property
    def service_name(self) -> str:
        """
        Specifies the name of the referenced service.
        """
        return self._properties.get('serviceName')

    @service_name.setter
    def service_name(self, value: str):
        """
        Specifies the name of the referenced service.
        """
        self._properties['serviceName'] = value

    @property
    def service_port(self) -> typing.Optional[int]:
        """
        Specifies the port of the referenced service.
        """
        value = self._properties.get('servicePort')
        return int(value) if value is not None else None

    @service_port.setter
    def service_port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Specifies the port of the referenced service.
        """
        self._properties['servicePort'] = None if value is None else f'{value}'

    def __enter__(self) -> 'IngressBackend':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressList(_kuber_definitions.Collection):
    """
    IngressList is a collection of Ingress.
    """

    def __init__(
            self,
            items: typing.List['Ingress'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create IngressList instance."""
        super(IngressList, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Ingress),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Ingress']:
        """
        Items is the list of Ingress.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Ingress'], typing.List[dict]]
    ):
        """
        Items is the list of Ingress.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Ingress().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'IngressList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressRule(_kuber_definitions.Definition):
    """
    IngressRule represents the rules mapping the paths under a
    specified host to the related backend services. Incoming
    requests are first evaluated for a host match, then routed
    to the backend associated with the matching
    IngressRuleValue.
    """

    def __init__(
            self,
            host: str = None,
            http: 'HTTPIngressRuleValue' = None,
    ):
        """Create IngressRule instance."""
        super(IngressRule, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressRule'
        )
        self._properties = {
            'host': host or '',
            'http': http or HTTPIngressRuleValue(),

        }
        self._types = {
            'host': (str, None),
            'http': (HTTPIngressRuleValue, None),

        }

    @property
    def host(self) -> str:
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in the RFC: 1. IPs are
        not allowed. Currently an IngressRuleValue can only apply to
        the
        	  IP in the Spec of the parent Ingress.
        2. The `:`
        delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http
        and
        	  :443 for https.
        Both these may change in the future.
        Incoming requests are matched against the host before the
        IngressRuleValue. If the host is unspecified, the Ingress
        routes all traffic based on the specified IngressRuleValue.
        """
        return self._properties.get('host')

    @host.setter
    def host(self, value: str):
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in the RFC: 1. IPs are
        not allowed. Currently an IngressRuleValue can only apply to
        the
        	  IP in the Spec of the parent Ingress.
        2. The `:`
        delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http
        and
        	  :443 for https.
        Both these may change in the future.
        Incoming requests are matched against the host before the
        IngressRuleValue. If the host is unspecified, the Ingress
        routes all traffic based on the specified IngressRuleValue.
        """
        self._properties['host'] = value

    @property
    def http(self) -> 'HTTPIngressRuleValue':
        """

        """
        return self._properties.get('http')

    @http.setter
    def http(self, value: typing.Union['HTTPIngressRuleValue', dict]):
        """

        """
        if isinstance(value, dict):
            value = HTTPIngressRuleValue().from_dict(value)
        self._properties['http'] = value

    def __enter__(self) -> 'IngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressSpec(_kuber_definitions.Definition):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """

    def __init__(
            self,
            backend: 'IngressBackend' = None,
            rules: typing.List['IngressRule'] = None,
            tls: typing.List['IngressTLS'] = None,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressSpec'
        )
        self._properties = {
            'backend': backend or IngressBackend(),
            'rules': rules or [],
            'tls': tls or [],

        }
        self._types = {
            'backend': (IngressBackend, None),
            'rules': (list, IngressRule),
            'tls': (list, IngressTLS),

        }

    @property
    def backend(self) -> 'IngressBackend':
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        return self._properties.get('backend')

    @backend.setter
    def backend(self, value: typing.Union['IngressBackend', dict]):
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        if isinstance(value, dict):
            value = IngressBackend().from_dict(value)
        self._properties['backend'] = value

    @property
    def rules(self) -> typing.List['IngressRule']:
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        return self._properties.get('rules')

    @rules.setter
    def rules(
            self,
            value: typing.Union[typing.List['IngressRule'], typing.List[dict]]
    ):
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IngressRule().from_dict(item)
            cleaned.append(item)
        self._properties['rules'] = cleaned

    @property
    def tls(self) -> typing.List['IngressTLS']:
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        return self._properties.get('tls')

    @tls.setter
    def tls(
            self,
            value: typing.Union[typing.List['IngressTLS'], typing.List[dict]]
    ):
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IngressTLS().from_dict(item)
            cleaned.append(item)
        self._properties['tls'] = cleaned

    def __enter__(self) -> 'IngressSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressStatus(_kuber_definitions.Definition):
    """
    IngressStatus describe the current state of the Ingress.
    """

    def __init__(
            self,
            load_balancer: 'LoadBalancerStatus' = None,
    ):
        """Create IngressStatus instance."""
        super(IngressStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressStatus'
        )
        self._properties = {
            'loadBalancer': load_balancer or LoadBalancerStatus(),

        }
        self._types = {
            'loadBalancer': (LoadBalancerStatus, None),

        }

    @property
    def load_balancer(self) -> 'LoadBalancerStatus':
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        return self._properties.get('loadBalancer')

    @load_balancer.setter
    def load_balancer(self, value: typing.Union['LoadBalancerStatus', dict]):
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        if isinstance(value, dict):
            value = LoadBalancerStatus().from_dict(value)
        self._properties['loadBalancer'] = value

    def __enter__(self) -> 'IngressStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressTLS(_kuber_definitions.Definition):
    """
    IngressTLS describes the transport layer security associated
    with an Ingress.
    """

    def __init__(
            self,
            hosts: typing.List[str] = None,
            secret_name: str = None,
    ):
        """Create IngressTLS instance."""
        super(IngressTLS, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressTLS'
        )
        self._properties = {
            'hosts': hosts or [],
            'secretName': secret_name or '',

        }
        self._types = {
            'hosts': (list, str),
            'secretName': (str, None),

        }

    @property
    def hosts(self) -> typing.List[str]:
        """
        Hosts are a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        return self._properties.get('hosts')

    @hosts.setter
    def hosts(self, value: typing.List[str]):
        """
        Hosts are a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        self._properties['hosts'] = value

    @property
    def secret_name(self) -> str:
        """
        SecretName is the name of the secret used to terminate SSL
        traffic on 443. Field is left optional to allow SSL routing
        based on SNI hostname alone. If the SNI host in a listener
        conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        return self._properties.get('secretName')

    @secret_name.setter
    def secret_name(self, value: str):
        """
        SecretName is the name of the secret used to terminate SSL
        traffic on 443. Field is left optional to allow SSL routing
        based on SNI hostname alone. If the SNI host in a listener
        conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        self._properties['secretName'] = value

    def __enter__(self) -> 'IngressTLS':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicy(_kuber_definitions.Resource):
    """
    DEPRECATED 1.9 - This group version of NetworkPolicy is
    deprecated by networking/v1/NetworkPolicy. NetworkPolicy
    describes what network traffic is allowed for a set of Pods
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'NetworkPolicySpec' = None,
    ):
        """Create NetworkPolicy instance."""
        super(NetworkPolicy, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicy'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or NetworkPolicySpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (NetworkPolicySpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'NetworkPolicySpec':
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['NetworkPolicySpec', dict]):
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        if isinstance(value, dict):
            value = NetworkPolicySpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_network_policy',
            'create_network_policy'
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
        Replaces the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_network_policy',
            'replace_network_policy'
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
        Patches the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_network_policy',
            'patch_network_policy'
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
        Reads the NetworkPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_network_policy',
            'read_network_policy'
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
        Deletes the NetworkPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_network_policy',
            'delete_network_policy'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'NetworkPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyEgressRule(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of
    NetworkPolicyEgressRule is deprecated by
    networking/v1/NetworkPolicyEgressRule.
    NetworkPolicyEgressRule describes a particular set of
    traffic that is allowed out of pods matched by a
    NetworkPolicySpec's podSelector. The traffic must match both
    ports and to. This type is beta-level in 1.8
    """

    def __init__(
            self,
            ports: typing.List['NetworkPolicyPort'] = None,
            to: typing.List['NetworkPolicyPeer'] = None,
    ):
        """Create NetworkPolicyEgressRule instance."""
        super(NetworkPolicyEgressRule, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicyEgressRule'
        )
        self._properties = {
            'ports': ports or [],
            'to': to or [],

        }
        self._types = {
            'ports': (list, NetworkPolicyPort),
            'to': (list, NetworkPolicyPeer),

        }

    @property
    def ports(self) -> typing.List['NetworkPolicyPort']:
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['NetworkPolicyPort'], typing.List[dict]]
    ):
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    @property
    def to(self) -> typing.List['NetworkPolicyPeer']:
        """
        List of destinations for outgoing traffic of pods selected
        for this rule. Items in this list are combined using a
        logical OR operation. If this field is empty or missing,
        this rule matches all destinations (traffic not restricted
        by destination). If this field is present and contains at
        least one item, this rule allows traffic only if the traffic
        matches at least one item in the to list.
        """
        return self._properties.get('to')

    @to.setter
    def to(
            self,
            value: typing.Union[typing.List['NetworkPolicyPeer'], typing.List[dict]]
    ):
        """
        List of destinations for outgoing traffic of pods selected
        for this rule. Items in this list are combined using a
        logical OR operation. If this field is empty or missing,
        this rule matches all destinations (traffic not restricted
        by destination). If this field is present and contains at
        least one item, this rule allows traffic only if the traffic
        matches at least one item in the to list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPeer().from_dict(item)
            cleaned.append(item)
        self._properties['to'] = cleaned

    def __enter__(self) -> 'NetworkPolicyEgressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyIngressRule(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of
    NetworkPolicyIngressRule is deprecated by
    networking/v1/NetworkPolicyIngressRule. This
    NetworkPolicyIngressRule matches traffic if and only if the
    traffic matches both ports AND from.
    """

    def __init__(
            self,
            from_: typing.List['NetworkPolicyPeer'] = None,
            ports: typing.List['NetworkPolicyPort'] = None,
    ):
        """Create NetworkPolicyIngressRule instance."""
        super(NetworkPolicyIngressRule, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicyIngressRule'
        )
        self._properties = {
            'from': from_ or [],
            'ports': ports or [],

        }
        self._types = {
            'from': (list, NetworkPolicyPeer),
            'ports': (list, NetworkPolicyPort),

        }

    @property
    def from_(self) -> typing.List['NetworkPolicyPeer']:
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least on item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        return self._properties.get('from')

    @from_.setter
    def from_(
            self,
            value: typing.Union[typing.List['NetworkPolicyPeer'], typing.List[dict]]
    ):
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least on item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPeer().from_dict(item)
            cleaned.append(item)
        self._properties['from'] = cleaned

    @property
    def ports(self) -> typing.List['NetworkPolicyPort']:
        """
        List of ports which should be made accessible on the pods
        selected for this rule. Each item in this list is combined
        using a logical OR. If this field is empty or missing, this
        rule matches all ports (traffic not restricted by port). If
        this field is present and contains at least one item, then
        this rule allows traffic only if the traffic matches at
        least one port in the list.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['NetworkPolicyPort'], typing.List[dict]]
    ):
        """
        List of ports which should be made accessible on the pods
        selected for this rule. Each item in this list is combined
        using a logical OR. If this field is empty or missing, this
        rule matches all ports (traffic not restricted by port). If
        this field is present and contains at least one item, then
        this rule allows traffic only if the traffic matches at
        least one port in the list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    def __enter__(self) -> 'NetworkPolicyIngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyList(_kuber_definitions.Collection):
    """
    DEPRECATED 1.9 - This group version of NetworkPolicyList is
    deprecated by networking/v1/NetworkPolicyList. Network
    Policy List is a list of NetworkPolicy objects.
    """

    def __init__(
            self,
            items: typing.List['NetworkPolicy'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create NetworkPolicyList instance."""
        super(NetworkPolicyList, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicyList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, NetworkPolicy),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['NetworkPolicy']:
        """
        Items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['NetworkPolicy'], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicy().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'NetworkPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPeer(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of NetworkPolicyPeer is
    deprecated by networking/v1/NetworkPolicyPeer.
    """

    def __init__(
            self,
            ip_block: 'IPBlock' = None,
            namespace_selector: 'LabelSelector' = None,
            pod_selector: 'LabelSelector' = None,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicyPeer'
        )
        self._properties = {
            'ipBlock': ip_block or IPBlock(),
            'namespaceSelector': namespace_selector or LabelSelector(),
            'podSelector': pod_selector or LabelSelector(),

        }
        self._types = {
            'ipBlock': (IPBlock, None),
            'namespaceSelector': (LabelSelector, None),
            'podSelector': (LabelSelector, None),

        }

    @property
    def ip_block(self) -> 'IPBlock':
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        return self._properties.get('ipBlock')

    @ip_block.setter
    def ip_block(self, value: typing.Union['IPBlock', dict]):
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        if isinstance(value, dict):
            value = IPBlock().from_dict(value)
        self._properties['ipBlock'] = value

    @property
    def namespace_selector(self) -> 'LabelSelector':
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects all Pods in the
        Namespaces selected by NamespaceSelector.
        """
        return self._properties.get('namespaceSelector')

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects all Pods in the
        Namespaces selected by NamespaceSelector.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['namespaceSelector'] = value

    @property
    def pod_selector(self) -> 'LabelSelector':
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects the Pods matching
        PodSelector in the policy's own Namespace.
        """
        return self._properties.get('podSelector')

    @pod_selector.setter
    def pod_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects the Pods matching
        PodSelector in the policy's own Namespace.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['podSelector'] = value

    def __enter__(self) -> 'NetworkPolicyPeer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPort(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of NetworkPolicyPort is
    deprecated by networking/v1/NetworkPolicyPort.
    """

    def __init__(
            self,
            port: typing.Union[str, int, None] = None,
            protocol: str = None,
    ):
        """Create NetworkPolicyPort instance."""
        super(NetworkPolicyPort, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicyPort'
        )
        self._properties = {
            'port': port or None,
            'protocol': protocol or '',

        }
        self._types = {
            'port': (int, None),
            'protocol': (str, None),

        }

    @property
    def port(self) -> typing.Optional[int]:
        """
        If specified, the port on the given protocol.  This can
        either be a numerical or named port on a pod.  If this field
        is not provided, this matches all port names and numbers. If
        present, only traffic on the specified protocol AND port
        will be matched.
        """
        value = self._properties.get('port')
        return int(value) if value is not None else None

    @port.setter
    def port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        If specified, the port on the given protocol.  This can
        either be a numerical or named port on a pod.  If this field
        is not provided, this matches all port names and numbers. If
        present, only traffic on the specified protocol AND port
        will be matched.
        """
        self._properties['port'] = None if value is None else f'{value}'

    @property
    def protocol(self) -> str:
        """
        Optional.  The protocol (TCP, UDP, or SCTP) which traffic
        must match. If not specified, this field defaults to TCP.
        """
        return self._properties.get('protocol')

    @protocol.setter
    def protocol(self, value: str):
        """
        Optional.  The protocol (TCP, UDP, or SCTP) which traffic
        must match. If not specified, this field defaults to TCP.
        """
        self._properties['protocol'] = value

    def __enter__(self) -> 'NetworkPolicyPort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicySpec(_kuber_definitions.Definition):
    """
    DEPRECATED 1.9 - This group version of NetworkPolicySpec is
    deprecated by networking/v1/NetworkPolicySpec.
    """

    def __init__(
            self,
            egress: typing.List['NetworkPolicyEgressRule'] = None,
            ingress: typing.List['NetworkPolicyIngressRule'] = None,
            pod_selector: 'LabelSelector' = None,
            policy_types: typing.List[str] = None,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='NetworkPolicySpec'
        )
        self._properties = {
            'egress': egress or [],
            'ingress': ingress or [],
            'podSelector': pod_selector or LabelSelector(),
            'policyTypes': policy_types or [],

        }
        self._types = {
            'egress': (list, NetworkPolicyEgressRule),
            'ingress': (list, NetworkPolicyIngressRule),
            'podSelector': (LabelSelector, None),
            'policyTypes': (list, str),

        }

    @property
    def egress(self) -> typing.List['NetworkPolicyEgressRule']:
        """
        List of egress rules to be applied to the selected pods.
        Outgoing traffic is allowed if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic matches at least one egress rule
        across all of the NetworkPolicy objects whose podSelector
        matches the pod. If this field is empty then this
        NetworkPolicy limits all outgoing traffic (and serves solely
        to ensure that the pods it selects are isolated by default).
        This field is beta-level in 1.8
        """
        return self._properties.get('egress')

    @egress.setter
    def egress(
            self,
            value: typing.Union[typing.List['NetworkPolicyEgressRule'], typing.List[dict]]
    ):
        """
        List of egress rules to be applied to the selected pods.
        Outgoing traffic is allowed if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic matches at least one egress rule
        across all of the NetworkPolicy objects whose podSelector
        matches the pod. If this field is empty then this
        NetworkPolicy limits all outgoing traffic (and serves solely
        to ensure that the pods it selects are isolated by default).
        This field is beta-level in 1.8
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyEgressRule().from_dict(item)
            cleaned.append(item)
        self._properties['egress'] = cleaned

    @property
    def ingress(self) -> typing.List['NetworkPolicyIngressRule']:
        """
        List of ingress rules to be applied to the selected pods.
        Traffic is allowed to a pod if there are no NetworkPolicies
        selecting the pod OR if the traffic source is the pod's
        local node, OR if the traffic matches at least one ingress
        rule across all of the NetworkPolicy objects whose
        podSelector matches the pod. If this field is empty then
        this NetworkPolicy does not allow any traffic (and serves
        solely to ensure that the pods it selects are isolated by
        default).
        """
        return self._properties.get('ingress')

    @ingress.setter
    def ingress(
            self,
            value: typing.Union[typing.List['NetworkPolicyIngressRule'], typing.List[dict]]
    ):
        """
        List of ingress rules to be applied to the selected pods.
        Traffic is allowed to a pod if there are no NetworkPolicies
        selecting the pod OR if the traffic source is the pod's
        local node, OR if the traffic matches at least one ingress
        rule across all of the NetworkPolicy objects whose
        podSelector matches the pod. If this field is empty then
        this NetworkPolicy does not allow any traffic (and serves
        solely to ensure that the pods it selects are isolated by
        default).
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyIngressRule().from_dict(item)
            cleaned.append(item)
        self._properties['ingress'] = cleaned

    @property
    def pod_selector(self) -> 'LabelSelector':
        """
        Selects the pods to which this NetworkPolicy object applies.
        The array of ingress rules is applied to any pods selected
        by this field. Multiple network policies can select the same
        set of pods.  In this case, the ingress rules for each are
        combined additively. This field is NOT optional and follows
        standard label selector semantics. An empty podSelector
        matches all pods in this namespace.
        """
        return self._properties.get('podSelector')

    @pod_selector.setter
    def pod_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selects the pods to which this NetworkPolicy object applies.
        The array of ingress rules is applied to any pods selected
        by this field. Multiple network policies can select the same
        set of pods.  In this case, the ingress rules for each are
        combined additively. This field is NOT optional and follows
        standard label selector semantics. An empty podSelector
        matches all pods in this namespace.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['podSelector'] = value

    @property
    def policy_types(self) -> typing.List[str]:
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are "Ingress", "Egress", or "Ingress,Egress". If
        this field is not specified, it will default based on the
        existence of Ingress or Egress rules; policies that contain
        an Egress section are assumed to affect Egress, and all
        policies (whether or not they contain an Ingress section)
        are assumed to affect Ingress. If you want to write an
        egress-only policy, you must explicitly specify policyTypes
        [ "Egress" ]. Likewise, if you want to write a policy that
        specifies that no egress is allowed, you must specify a
        policyTypes value that include "Egress" (since such a policy
        would not include an Egress section and would otherwise
        default to just [ "Ingress" ]). This field is beta-level in
        1.8
        """
        return self._properties.get('policyTypes')

    @policy_types.setter
    def policy_types(self, value: typing.List[str]):
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are "Ingress", "Egress", or "Ingress,Egress". If
        this field is not specified, it will default based on the
        existence of Ingress or Egress rules; policies that contain
        an Egress section are assumed to affect Egress, and all
        policies (whether or not they contain an Ingress section)
        are assumed to affect Ingress. If you want to write an
        egress-only policy, you must explicitly specify policyTypes
        [ "Egress" ]. Likewise, if you want to write a policy that
        specifies that no egress is allowed, you must specify a
        policyTypes value that include "Egress" (since such a policy
        would not include an Egress section and would otherwise
        default to just [ "Ingress" ]). This field is beta-level in
        1.8
        """
        self._properties['policyTypes'] = value

    def __enter__(self) -> 'NetworkPolicySpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicy(_kuber_definitions.Resource):
    """
    PodSecurityPolicy governs the ability to make requests that
    affect the Security Context that will be applied to a pod
    and container. Deprecated: use PodSecurityPolicy from policy
    API Group instead.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PodSecurityPolicySpec' = None,
    ):
        """Create PodSecurityPolicy instance."""
        super(PodSecurityPolicy, self).__init__(
            api_version='extensions/v1beta1',
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
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodSecurityPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicyList(_kuber_definitions.Collection):
    """
    PodSecurityPolicyList is a list of PodSecurityPolicy
    objects. Deprecated: use PodSecurityPolicyList from policy
    API Group instead.
    """

    def __init__(
            self,
            items: typing.List['PodSecurityPolicy'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodSecurityPolicyList instance."""
        super(PodSecurityPolicyList, self).__init__(
            api_version='extensions/v1beta1',
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
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'PodSecurityPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicySpec(_kuber_definitions.Definition):
    """
    PodSecurityPolicySpec defines the policy enforced.
    Deprecated: use PodSecurityPolicySpec from policy API Group
    instead.
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
            api_version='extensions/v1beta1',
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


class ReplicaSet(_kuber_definitions.Resource):
    """
    DEPRECATED - This group version of ReplicaSet is deprecated
    by apps/v1beta2/ReplicaSet. See the release notes for more
    information. ReplicaSet ensures that a specified number of
    pod replicas are running at any given time.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ReplicaSetSpec' = None,
    ):
        """Create ReplicaSet instance."""
        super(ReplicaSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSet'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ReplicaSetSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (ReplicaSetSpec, None),
            'status': (ReplicaSetStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        If the Labels of a ReplicaSet are empty, they are defaulted
        to be the same as the Pod(s) that the ReplicaSet manages.
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        If the Labels of a ReplicaSet are empty, they are defaulted
        to be the same as the Pod(s) that the ReplicaSet manages.
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ReplicaSetSpec':
        """
        Spec defines the specification of the desired behavior of
        the ReplicaSet. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ReplicaSetSpec', dict]):
        """
        Spec defines the specification of the desired behavior of
        the ReplicaSet. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = ReplicaSetSpec().from_dict(value)
        self._properties['spec'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'ReplicaSet':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.spec.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.spec.template.spec.containers if c.name == name), None)

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicaSetStatus':
        """
        Creates the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_replica_set',
            'create_replica_set'
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
            ReplicaSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicaSetStatus':
        """
        Replaces the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_replica_set',
            'replace_replica_set'
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
            ReplicaSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'ReplicaSetStatus':
        """
        Patches the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_replica_set',
            'patch_replica_set'
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
            ReplicaSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'ReplicaSetStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_replica_set',
            'read_replica_set'
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
            ReplicaSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the ReplicaSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_replica_set',
            'read_replica_set'
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
        Deletes the ReplicaSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_replica_set',
            'delete_replica_set'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'ReplicaSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetCondition(_kuber_definitions.Definition):
    """
    ReplicaSetCondition describes the state of a replica set at
    a certain point.
    """

    def __init__(
            self,
            last_transition_time: str = None,
            message: str = None,
            reason: str = None,
            status: str = None,
            type_: str = None,
    ):
        """Create ReplicaSetCondition instance."""
        super(ReplicaSetCondition, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetCondition'
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
        The last time the condition transitioned from one status to
        another.
        """
        return self._properties.get('lastTransitionTime')

    @last_transition_time.setter
    def last_transition_time(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['lastTransitionTime'] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties['status'] = value

    @property
    def type_(self) -> str:
        """
        Type of replica set condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of replica set condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'ReplicaSetCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetList(_kuber_definitions.Collection):
    """
    ReplicaSetList is a collection of ReplicaSets.
    """

    def __init__(
            self,
            items: typing.List['ReplicaSet'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ReplicaSetList instance."""
        super(ReplicaSetList, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ReplicaSet),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ReplicaSet']:
        """
        List of ReplicaSets. More info: https://kubernetes.io/docs/c
        oncepts/workloads/controllers/replicationcontroller
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ReplicaSet'], typing.List[dict]]
    ):
        """
        List of ReplicaSets. More info: https://kubernetes.io/docs/c
        oncepts/workloads/controllers/replicationcontroller
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ReplicaSet().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'ReplicaSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetSpec(_kuber_definitions.Definition):
    """
    ReplicaSetSpec is the specification of a ReplicaSet.
    """

    def __init__(
            self,
            min_ready_seconds: int = None,
            replicas: int = None,
            selector: 'LabelSelector' = None,
            template: 'PodTemplateSpec' = None,
    ):
        """Create ReplicaSetSpec instance."""
        super(ReplicaSetSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetSpec'
        )
        self._properties = {
            'minReadySeconds': min_ready_seconds or None,
            'replicas': replicas or None,
            'selector': selector or LabelSelector(),
            'template': template or PodTemplateSpec(),

        }
        self._types = {
            'minReadySeconds': (int, None),
            'replicas': (int, None),
            'selector': (LabelSelector, None),
            'template': (PodTemplateSpec, None),

        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        return self._properties.get('minReadySeconds')

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        self._properties['minReadySeconds'] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller/#
        what-is-a-replicationcontroller
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller/#
        what-is-a-replicationcontroller
        """
        self._properties['replicas'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        Selector is a label query over pods that should match the
        replica count. If the selector is empty, it is defaulted to
        the labels present on the pod template. Label keys and
        values that must match in order to be controlled by this
        replica set. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selector is a label query over pods that should match the
        replica count. If the selector is empty, it is defaulted to
        the labels present on the pod template. Label keys and
        values that must match in order to be controlled by this
        replica set. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. More info: ht
        tps://kubernetes.io/docs/concepts/workloads/controllers/repl
        icationcontroller#pod-template
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. More info: ht
        tps://kubernetes.io/docs/concepts/workloads/controllers/repl
        icationcontroller#pod-template
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    def append_container(
        self,
        args: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.List[str] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.List['EnvVar'] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.List['EnvFromSource'] = _kuber_definitions.UNCHANGED_VALUE,
        image: str = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: 'Lifecycle' = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        name: str = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.List['ContainerPort'] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: 'Probe' = _kuber_definitions.UNCHANGED_VALUE,
        resources: 'ResourceRequirements' = _kuber_definitions.UNCHANGED_VALUE,
        security_context: 'SecurityContext' = _kuber_definitions.UNCHANGED_VALUE,
        stdin: bool = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: bool = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: str = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: str = _kuber_definitions.UNCHANGED_VALUE,
        tty: bool = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.List['VolumeDevice'] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.List['VolumeMount'] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: str = _kuber_definitions.UNCHANGED_VALUE,
    ) -> 'ReplicaSetSpec':
        """Adds a container object within the specified resource."""
        values = {
            'args': args,
            'command': command,
            'env': env,
            'env_from': env_from,
            'image': image,
            'image_pull_policy': image_pull_policy,
            'lifecycle': lifecycle,
            'liveness_probe': liveness_probe,
            'name': name,
            'ports': ports,
            'readiness_probe': readiness_probe,
            'resources': resources,
            'security_context': security_context,
            'stdin': stdin,
            'stdin_once': stdin_once,
            'termination_message_path': termination_message_path,
            'termination_message_policy': termination_message_policy,
            'tty': tty,
            'volume_devices': volume_devices,
            'volume_mounts': volume_mounts,
            'working_dir': working_dir,
        }
        self.template.spec.containers.append(Container(**{
            k: v
            for k, v in values.items()
            if v != _kuber_definitions.UNCHANGED_VALUE
        }))
        return self

    def get_container(self, name: str) -> typing.Optional['Container']:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def __enter__(self) -> 'ReplicaSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetStatus(_kuber_definitions.Definition):
    """
    ReplicaSetStatus represents the current status of a
    ReplicaSet.
    """

    def __init__(
            self,
            available_replicas: int = None,
            conditions: typing.List['ReplicaSetCondition'] = None,
            fully_labeled_replicas: int = None,
            observed_generation: int = None,
            ready_replicas: int = None,
            replicas: int = None,
    ):
        """Create ReplicaSetStatus instance."""
        super(ReplicaSetStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetStatus'
        )
        self._properties = {
            'availableReplicas': available_replicas or None,
            'conditions': conditions or [],
            'fullyLabeledReplicas': fully_labeled_replicas or None,
            'observedGeneration': observed_generation or None,
            'readyReplicas': ready_replicas or None,
            'replicas': replicas or None,

        }
        self._types = {
            'availableReplicas': (int, None),
            'conditions': (list, ReplicaSetCondition),
            'fullyLabeledReplicas': (int, None),
            'observedGeneration': (int, None),
            'readyReplicas': (int, None),
            'replicas': (int, None),

        }

    @property
    def available_replicas(self) -> int:
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replica set.
        """
        return self._properties.get('availableReplicas')

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replica set.
        """
        self._properties['availableReplicas'] = value

    @property
    def conditions(self) -> typing.List['ReplicaSetCondition']:
        """
        Represents the latest available observations of a replica
        set's current state.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['ReplicaSetCondition'], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a replica
        set's current state.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ReplicaSetCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def fully_labeled_replicas(self) -> int:
        """
        The number of pods that have labels matching the labels of
        the pod template of the replicaset.
        """
        return self._properties.get('fullyLabeledReplicas')

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, value: int):
        """
        The number of pods that have labels matching the labels of
        the pod template of the replicaset.
        """
        self._properties['fullyLabeledReplicas'] = value

    @property
    def observed_generation(self) -> int:
        """
        ObservedGeneration reflects the generation of the most
        recently observed ReplicaSet.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        ObservedGeneration reflects the generation of the most
        recently observed ReplicaSet.
        """
        self._properties['observedGeneration'] = value

    @property
    def ready_replicas(self) -> int:
        """
        The number of ready replicas for this replica set.
        """
        return self._properties.get('readyReplicas')

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        The number of ready replicas for this replica set.
        """
        self._properties['readyReplicas'] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller/#what-is-a-
        replicationcontroller
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller/#what-is-a-
        replicationcontroller
        """
        self._properties['replicas'] = value

    def __enter__(self) -> 'ReplicaSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollbackConfig(_kuber_definitions.Definition):
    """
    DEPRECATED.
    """

    def __init__(
            self,
            revision: int = None,
    ):
        """Create RollbackConfig instance."""
        super(RollbackConfig, self).__init__(
            api_version='extensions/v1beta1',
            kind='RollbackConfig'
        )
        self._properties = {
            'revision': revision or None,

        }
        self._types = {
            'revision': (int, None),

        }

    @property
    def revision(self) -> int:
        """
        The revision to rollback to. If set to 0, rollback to the
        last revision.
        """
        return self._properties.get('revision')

    @revision.setter
    def revision(self, value: int):
        """
        The revision to rollback to. If set to 0, rollback to the
        last revision.
        """
        self._properties['revision'] = value

    def __enter__(self) -> 'RollbackConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateDaemonSet(_kuber_definitions.Definition):
    """
    Spec to control the desired behavior of daemon set rolling
    update.
    """

    def __init__(
            self,
            max_unavailable: typing.Union[str, int, None] = None,
    ):
        """Create RollingUpdateDaemonSet instance."""
        super(RollingUpdateDaemonSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='RollingUpdateDaemonSet'
        )
        self._properties = {
            'maxUnavailable': max_unavailable or None,

        }
        self._types = {
            'maxUnavailable': (int, None),

        }

    @property
    def max_unavailable(self) -> typing.Optional[int]:
        """
        The maximum number of DaemonSet pods that can be unavailable
        during the update. Value can be an absolute number (ex: 5)
        or a percentage of total number of DaemonSet pods at the
        start of the update (ex: 10%). Absolute number is calculated
        from percentage by rounding up. This cannot be 0. Default
        value is 1. Example: when this is set to 30%, at most 30% of
        the total number of nodes that should be running the daemon
        pod (i.e. status.desiredNumberScheduled) can have their pods
        stopped for an update at any given time. The update starts
        by stopping at most 30% of those DaemonSet pods and then
        brings up new DaemonSet pods in their place. Once the new
        pods are available, it then proceeds onto other DaemonSet
        pods, thus ensuring that at least 70% of original number of
        DaemonSet pods are available at all times during the update.
        """
        value = self._properties.get('maxUnavailable')
        return int(value) if value is not None else None

    @max_unavailable.setter
    def max_unavailable(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        The maximum number of DaemonSet pods that can be unavailable
        during the update. Value can be an absolute number (ex: 5)
        or a percentage of total number of DaemonSet pods at the
        start of the update (ex: 10%). Absolute number is calculated
        from percentage by rounding up. This cannot be 0. Default
        value is 1. Example: when this is set to 30%, at most 30% of
        the total number of nodes that should be running the daemon
        pod (i.e. status.desiredNumberScheduled) can have their pods
        stopped for an update at any given time. The update starts
        by stopping at most 30% of those DaemonSet pods and then
        brings up new DaemonSet pods in their place. Once the new
        pods are available, it then proceeds onto other DaemonSet
        pods, thus ensuring that at least 70% of original number of
        DaemonSet pods are available at all times during the update.
        """
        self._properties['maxUnavailable'] = None if value is None else f'{value}'

    def __enter__(self) -> 'RollingUpdateDaemonSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateDeployment(_kuber_definitions.Definition):
    """
    Spec to control the desired behavior of rolling update.
    """

    def __init__(
            self,
            max_surge: typing.Union[str, int, None] = None,
            max_unavailable: typing.Union[str, int, None] = None,
    ):
        """Create RollingUpdateDeployment instance."""
        super(RollingUpdateDeployment, self).__init__(
            api_version='extensions/v1beta1',
            kind='RollingUpdateDeployment'
        )
        self._properties = {
            'maxSurge': max_surge or None,
            'maxUnavailable': max_unavailable or None,

        }
        self._types = {
            'maxSurge': (int, None),
            'maxUnavailable': (int, None),

        }

    @property
    def max_surge(self) -> typing.Optional[int]:
        """
        The maximum number of pods that can be scheduled above the
        desired number of pods. Value can be an absolute number (ex:
        5) or a percentage of desired pods (ex: 10%). This can not
        be 0 if MaxUnavailable is 0. Absolute number is calculated
        from percentage by rounding up. By default, a value of 1 is
        used. Example: when this is set to 30%, the new RC can be
        scaled up immediately when the rolling update starts, such
        that the total number of old and new pods do not exceed 130%
        of desired pods. Once old pods have been killed, new RC can
        be scaled up further, ensuring that total number of pods
        running at any time during the update is at most 130% of
        desired pods.
        """
        value = self._properties.get('maxSurge')
        return int(value) if value is not None else None

    @max_surge.setter
    def max_surge(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        The maximum number of pods that can be scheduled above the
        desired number of pods. Value can be an absolute number (ex:
        5) or a percentage of desired pods (ex: 10%). This can not
        be 0 if MaxUnavailable is 0. Absolute number is calculated
        from percentage by rounding up. By default, a value of 1 is
        used. Example: when this is set to 30%, the new RC can be
        scaled up immediately when the rolling update starts, such
        that the total number of old and new pods do not exceed 130%
        of desired pods. Once old pods have been killed, new RC can
        be scaled up further, ensuring that total number of pods
        running at any time during the update is at most 130% of
        desired pods.
        """
        self._properties['maxSurge'] = None if value is None else f'{value}'

    @property
    def max_unavailable(self) -> typing.Optional[int]:
        """
        The maximum number of pods that can be unavailable during
        the update. Value can be an absolute number (ex: 5) or a
        percentage of desired pods (ex: 10%). Absolute number is
        calculated from percentage by rounding down. This can not be
        0 if MaxSurge is 0. By default, a fixed value of 1 is used.
        Example: when this is set to 30%, the old RC can be scaled
        down to 70% of desired pods immediately when the rolling
        update starts. Once new pods are ready, old RC can be scaled
        down further, followed by scaling up the new RC, ensuring
        that the total number of pods available at all times during
        the update is at least 70% of desired pods.
        """
        value = self._properties.get('maxUnavailable')
        return int(value) if value is not None else None

    @max_unavailable.setter
    def max_unavailable(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        The maximum number of pods that can be unavailable during
        the update. Value can be an absolute number (ex: 5) or a
        percentage of desired pods (ex: 10%). Absolute number is
        calculated from percentage by rounding down. This can not be
        0 if MaxSurge is 0. By default, a fixed value of 1 is used.
        Example: when this is set to 30%, the old RC can be scaled
        down to 70% of desired pods immediately when the rolling
        update starts. Once new pods are ready, old RC can be scaled
        down further, followed by scaling up the new RC, ensuring
        that the total number of pods available at all times during
        the update is at least 70% of desired pods.
        """
        self._properties['maxUnavailable'] = None if value is None else f'{value}'

    def __enter__(self) -> 'RollingUpdateDeployment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RunAsGroupStrategyOptions(_kuber_definitions.Definition):
    """
    RunAsGroupStrategyOptions defines the strategy type and any
    options used to create the strategy. Deprecated: use
    RunAsGroupStrategyOptions from policy API Group instead.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create RunAsGroupStrategyOptions instance."""
        super(RunAsGroupStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
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
    options used to create the strategy. Deprecated: use
    RunAsUserStrategyOptions from policy API Group instead.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create RunAsUserStrategyOptions instance."""
        super(RunAsUserStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
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
    options used to create the strategy. Deprecated: use
    SELinuxStrategyOptions from policy API Group instead.
    """

    def __init__(
            self,
            rule: str = None,
            se_linux_options: 'SELinuxOptions' = None,
    ):
        """Create SELinuxStrategyOptions instance."""
        super(SELinuxStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
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


class Scale(_kuber_definitions.Resource):
    """
    represents a scaling request for a resource.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ScaleSpec' = None,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(
            api_version='extensions/v1beta1',
            kind='Scale'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ScaleSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (ScaleSpec, None),
            'status': (ScaleStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ScaleSpec':
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ScaleSpec', dict]):
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status.
        """
        if isinstance(value, dict):
            value = ScaleSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'ScaleStatus':
        """
        Creates the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_scale',
            'create_scale'
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
            ScaleStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'ScaleStatus':
        """
        Replaces the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_scale',
            'replace_scale'
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
            ScaleStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'ScaleStatus':
        """
        Patches the Scale in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_scale',
            'patch_scale'
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
            ScaleStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'ScaleStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_scale',
            'read_scale'
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
            ScaleStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Scale from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_scale',
            'read_scale'
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
        Deletes the Scale from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_scale',
            'delete_scale'
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
    ) -> 'client.ExtensionsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.ExtensionsV1beta1Api(**kwargs)

    def __enter__(self) -> 'Scale':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleSpec(_kuber_definitions.Definition):
    """
    describes the attributes of a scale subresource
    """

    def __init__(
            self,
            replicas: int = None,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='ScaleSpec'
        )
        self._properties = {
            'replicas': replicas or None,

        }
        self._types = {
            'replicas': (int, None),

        }

    @property
    def replicas(self) -> int:
        """
        desired number of instances for the scaled object.
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        desired number of instances for the scaled object.
        """
        self._properties['replicas'] = value

    def __enter__(self) -> 'ScaleSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleStatus(_kuber_definitions.Definition):
    """
    represents the current status of a scale subresource.
    """

    def __init__(
            self,
            replicas: int = None,
            selector: dict = None,
            target_selector: str = None,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='ScaleStatus'
        )
        self._properties = {
            'replicas': replicas or None,
            'selector': selector or {},
            'targetSelector': target_selector or '',

        }
        self._types = {
            'replicas': (int, None),
            'selector': (dict, None),
            'targetSelector': (str, None),

        }

    @property
    def replicas(self) -> int:
        """
        actual number of observed instances of the scaled object.
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        actual number of observed instances of the scaled object.
        """
        self._properties['replicas'] = value

    @property
    def selector(self) -> dict:
        """
        label query over pods that should match the replicas count.
        More info: http://kubernetes.io/docs/user-
        guide/labels#label-selectors
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: dict):
        """
        label query over pods that should match the replicas count.
        More info: http://kubernetes.io/docs/user-
        guide/labels#label-selectors
        """
        self._properties['selector'] = value

    @property
    def target_selector(self) -> str:
        """
        label selector for pods that should match the replicas
        count. This is a serializated version of both map-based and
        more expressive set-based selectors. This is done to avoid
        introspection in the clients. The string will be in the same
        format as the query-param syntax. If the target type only
        supports map-based selectors, both this field and map-based
        selector field are populated. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return self._properties.get('targetSelector')

    @target_selector.setter
    def target_selector(self, value: str):
        """
        label selector for pods that should match the replicas
        count. This is a serializated version of both map-based and
        more expressive set-based selectors. This is done to avoid
        introspection in the clients. The string will be in the same
        format as the query-param syntax. If the target type only
        supports map-based selectors, both this field and map-based
        selector field are populated. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        self._properties['targetSelector'] = value

    def __enter__(self) -> 'ScaleStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SupplementalGroupsStrategyOptions(_kuber_definitions.Definition):
    """
    SupplementalGroupsStrategyOptions defines the strategy type
    and options used to create the strategy. Deprecated: use
    SupplementalGroupsStrategyOptions from policy API Group
    instead.
    """

    def __init__(
            self,
            ranges: typing.List['IDRange'] = None,
            rule: str = None,
    ):
        """Create SupplementalGroupsStrategyOptions instance."""
        super(SupplementalGroupsStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
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

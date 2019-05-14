import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_11.core_v1 import Container
from kuber.v1_11.core_v1 import ContainerPort
from kuber.v1_11.core_v1 import EnvFromSource
from kuber.v1_11.core_v1 import EnvVar
from kuber.v1_11.meta_v1 import LabelSelector
from kuber.v1_11.core_v1 import Lifecycle
from kuber.v1_11.meta_v1 import ListMeta
from kuber.v1_11.meta_v1 import ObjectMeta
from kuber.v1_11.core_v1 import PersistentVolumeClaim
from kuber.v1_11.core_v1 import PodTemplateSpec
from kuber.v1_11.core_v1 import Probe
from kuber.v1_11.apimachinery_runtime import RawExtension
from kuber.v1_11.core_v1 import ResourceRequirements
from kuber.v1_11.core_v1 import SecurityContext
from kuber.v1_11.meta_v1 import Status
from kuber.v1_11.meta_v1 import StatusDetails
from kuber.v1_11.core_v1 import VolumeDevice
from kuber.v1_11.core_v1 import VolumeMount


class ControllerRevision(_kuber_definitions.Resource):
    """
    DEPRECATED - This group version of ControllerRevision is
    deprecated by apps/v1beta2/ControllerRevision. See the
    release notes for more information. ControllerRevision
    implements an immutable snapshot of state data. Clients are
    responsible for serializing and deserializing the objects
    that contain their internal state. Once a ControllerRevision
    has been successfully created, it can not be updated. The
    API Server will fail validation of all requests that attempt
    to mutate the Data field. ControllerRevisions may, however,
    be deleted. Note that, due to its use by both the DaemonSet
    and StatefulSet controllers for update and rollback, this
    object is beta. However, it may be subject to name and
    representation changes in future releases, and clients
    should not depend on its stability. It is primarily for
    internal use by controllers.
    """

    def __init__(
            self,
            data: 'RawExtension' = None,
            metadata: 'ObjectMeta' = None,
            revision: int = None,
    ):
        """Create ControllerRevision instance."""
        super(ControllerRevision, self).__init__(
            api_version='apps/v1beta1',
            kind='ControllerRevision'
        )
        self._properties = {
            'data': data or RawExtension(),
            'metadata': metadata or ObjectMeta(),
            'revision': revision or None,

        }
        self._types = {
            'apiVersion': (str, None),
            'data': (RawExtension, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'revision': (int, None),

        }

    @property
    def data(self) -> 'RawExtension':
        """
        Data is the serialized representation of the state.
        """
        return self._properties.get('data')

    @data.setter
    def data(self, value: typing.Union['RawExtension', dict]):
        """
        Data is the serialized representation of the state.
        """
        if isinstance(value, dict):
            value = RawExtension().from_dict(value)
        self._properties['data'] = value

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
    def revision(self) -> int:
        """
        Revision indicates the revision of the state represented by
        Data.
        """
        return self._properties.get('revision')

    @revision.setter
    def revision(self, value: int):
        """
        Revision indicates the revision of the state represented by
        Data.
        """
        self._properties['revision'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_controller_revision',
            'create_controller_revision'
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
        Replaces the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_controller_revision',
            'replace_controller_revision'
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
        Patches the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_controller_revision',
            'patch_controller_revision'
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
        Reads the ControllerRevision from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_controller_revision',
            'read_controller_revision'
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
        Deletes the ControllerRevision from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_controller_revision',
            'delete_controller_revision'
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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

    def __enter__(self) -> 'ControllerRevision':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ControllerRevisionList(_kuber_definitions.Collection):
    """
    ControllerRevisionList is a resource containing a list of
    ControllerRevision objects.
    """

    def __init__(
            self,
            items: typing.List['ControllerRevision'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ControllerRevisionList instance."""
        super(ControllerRevisionList, self).__init__(
            api_version='apps/v1beta1',
            kind='ControllerRevisionList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ControllerRevision),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ControllerRevision']:
        """
        Items is the list of ControllerRevisions
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ControllerRevision'], typing.List[dict]]
    ):
        """
        Items is the list of ControllerRevisions
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ControllerRevision().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        More info:
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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

    def __enter__(self) -> 'ControllerRevisionList':
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
            status: 'DeploymentStatus' = None,
    ):
        """Create Deployment instance."""
        super(Deployment, self).__init__(
            api_version='apps/v1beta1',
            kind='Deployment'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or DeploymentSpec(),
            'status': status or DeploymentStatus(),

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

    @property
    def status(self) -> 'DeploymentStatus':
        """
        Most recently observed status of the Deployment.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['DeploymentStatus', dict]):
        """
        Most recently observed status of the Deployment.
        """
        if isinstance(value, dict):
            value = DeploymentStatus().from_dict(value)
        self._properties['status'] = value

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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

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
            api_version='apps/v1beta1',
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
            api_version='apps/v1beta1',
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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

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
            api_version='apps/v1beta1',
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
            api_version='apps/v1beta1',
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
        Indicates that the deployment is paused.
        """
        return self._properties.get('paused')

    @paused.setter
    def paused(self, value: bool):
        """
        Indicates that the deployment is paused.
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
        is paused. Defaults to 600s.
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
        is paused. Defaults to 600s.
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
        not specified. Defaults to 2.
        """
        return self._properties.get('revisionHistoryLimit')

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        The number of old ReplicaSets to retain to allow rollback.
        This is a pointer to distinguish between explicit zero and
        not specified. Defaults to 2.
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
            api_version='apps/v1beta1',
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
            api_version='apps/v1beta1',
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
            api_version='apps/v1beta1',
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
            api_version='apps/v1beta1',
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
        from percentage by rounding up. Defaults to 25%. Example:
        when this is set to 30%, the new ReplicaSet can be scaled up
        immediately when the rolling update starts, such that the
        total number of old and new pods do not exceed 130% of
        desired pods. Once old pods have been killed, new ReplicaSet
        can be scaled up further, ensuring that total number of pods
        running at any time during the update is atmost 130% of
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
        from percentage by rounding up. Defaults to 25%. Example:
        when this is set to 30%, the new ReplicaSet can be scaled up
        immediately when the rolling update starts, such that the
        total number of old and new pods do not exceed 130% of
        desired pods. Once old pods have been killed, new ReplicaSet
        can be scaled up further, ensuring that total number of pods
        running at any time during the update is atmost 130% of
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
        0 if MaxSurge is 0. Defaults to 25%. Example: when this is
        set to 30%, the old ReplicaSet can be scaled down to 70% of
        desired pods immediately when the rolling update starts.
        Once new pods are ready, old ReplicaSet can be scaled down
        further, followed by scaling up the new ReplicaSet, ensuring
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
        0 if MaxSurge is 0. Defaults to 25%. Example: when this is
        set to 30%, the old ReplicaSet can be scaled down to 70% of
        desired pods immediately when the rolling update starts.
        Once new pods are ready, old ReplicaSet can be scaled down
        further, followed by scaling up the new ReplicaSet, ensuring
        that the total number of pods available at all times during
        the update is at least 70% of desired pods.
        """
        self._properties['maxUnavailable'] = None if value is None else f'{value}'

    def __enter__(self) -> 'RollingUpdateDeployment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateStatefulSetStrategy(_kuber_definitions.Definition):
    """
    RollingUpdateStatefulSetStrategy is used to communicate
    parameter for RollingUpdateStatefulSetStrategyType.
    """

    def __init__(
            self,
            partition: int = None,
    ):
        """Create RollingUpdateStatefulSetStrategy instance."""
        super(RollingUpdateStatefulSetStrategy, self).__init__(
            api_version='apps/v1beta1',
            kind='RollingUpdateStatefulSetStrategy'
        )
        self._properties = {
            'partition': partition or None,

        }
        self._types = {
            'partition': (int, None),

        }

    @property
    def partition(self) -> int:
        """
        Partition indicates the ordinal at which the StatefulSet
        should be partitioned.
        """
        return self._properties.get('partition')

    @partition.setter
    def partition(self, value: int):
        """
        Partition indicates the ordinal at which the StatefulSet
        should be partitioned.
        """
        self._properties['partition'] = value

    def __enter__(self) -> 'RollingUpdateStatefulSetStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scale(_kuber_definitions.Resource):
    """
    Scale represents a scaling request for a resource.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'ScaleSpec' = None,
            status: 'ScaleStatus' = None,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(
            api_version='apps/v1beta1',
            kind='Scale'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or ScaleSpec(),
            'status': status or ScaleStatus(),

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
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'ScaleSpec':
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['ScaleSpec', dict]):
        """
        defines the behavior of the scale. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status.
        """
        if isinstance(value, dict):
            value = ScaleSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'ScaleStatus':
        """
        current status of the scale. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status. Read-only.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['ScaleStatus', dict]):
        """
        current status of the scale. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status. Read-only.
        """
        if isinstance(value, dict):
            value = ScaleStatus().from_dict(value)
        self._properties['status'] = value

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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

    def __enter__(self) -> 'Scale':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleSpec(_kuber_definitions.Definition):
    """
    ScaleSpec describes the attributes of a scale subresource
    """

    def __init__(
            self,
            replicas: int = None,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(
            api_version='apps/v1beta1',
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
    ScaleStatus represents the current status of a scale
    subresource.
    """

    def __init__(
            self,
            replicas: int = None,
            selector: dict = None,
            target_selector: str = None,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version='apps/v1beta1',
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


class StatefulSet(_kuber_definitions.Resource):
    """
    DEPRECATED - This group version of StatefulSet is deprecated
    by apps/v1beta2/StatefulSet. See the release notes for more
    information. StatefulSet represents a set of pods with
    consistent identities. Identities are defined as:
     -
    Network: A single stable DNS and hostname.
     - Storage: As
    many VolumeClaims as requested.
    The StatefulSet guarantees
    that a given network identity will always map to the same
    storage identity.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'StatefulSetSpec' = None,
            status: 'StatefulSetStatus' = None,
    ):
        """Create StatefulSet instance."""
        super(StatefulSet, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSet'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or StatefulSetSpec(),
            'status': status or StatefulSetStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (StatefulSetSpec, None),
            'status': (StatefulSetStatus, None),

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
    def spec(self) -> 'StatefulSetSpec':
        """
        Spec defines the desired identities of pods in this set.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['StatefulSetSpec', dict]):
        """
        Spec defines the desired identities of pods in this set.
        """
        if isinstance(value, dict):
            value = StatefulSetSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'StatefulSetStatus':
        """
        Status is the current status of Pods in this StatefulSet.
        This data may be out of date by some window of time.
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['StatefulSetStatus', dict]):
        """
        Status is the current status of Pods in this StatefulSet.
        This data may be out of date by some window of time.
        """
        if isinstance(value, dict):
            value = StatefulSetStatus().from_dict(value)
        self._properties['status'] = value

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
    ) -> 'StatefulSet':
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
    ) -> 'StatefulSetStatus':
        """
        Creates the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_stateful_set',
            'create_stateful_set'
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
            StatefulSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'StatefulSetStatus':
        """
        Replaces the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_stateful_set',
            'replace_stateful_set'
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
            StatefulSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'StatefulSetStatus':
        """
        Patches the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_stateful_set',
            'patch_stateful_set'
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
            StatefulSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'StatefulSetStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_stateful_set',
            'read_stateful_set'
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
            StatefulSetStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the StatefulSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_stateful_set',
            'read_stateful_set'
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
        Deletes the StatefulSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_stateful_set',
            'delete_stateful_set'
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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

    def __enter__(self) -> 'StatefulSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetCondition(_kuber_definitions.Definition):
    """
    StatefulSetCondition describes the state of a statefulset at
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
        """Create StatefulSetCondition instance."""
        super(StatefulSetCondition, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetCondition'
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
        Type of statefulset condition.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type of statefulset condition.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'StatefulSetCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetList(_kuber_definitions.Collection):
    """
    StatefulSetList is a collection of StatefulSets.
    """

    def __init__(
            self,
            items: typing.List['StatefulSet'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create StatefulSetList instance."""
        super(StatefulSetList, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, StatefulSet),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['StatefulSet']:
        """

        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['StatefulSet'], typing.List[dict]]
    ):
        """

        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = StatefulSet().from_dict(item)
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
    ) -> 'client.AppsV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AppsV1beta1Api(**kwargs)

    def __enter__(self) -> 'StatefulSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetSpec(_kuber_definitions.Definition):
    """
    A StatefulSetSpec is the specification of a StatefulSet.
    """

    def __init__(
            self,
            pod_management_policy: str = None,
            replicas: int = None,
            revision_history_limit: int = None,
            selector: 'LabelSelector' = None,
            service_name: str = None,
            template: 'PodTemplateSpec' = None,
            update_strategy: 'StatefulSetUpdateStrategy' = None,
            volume_claim_templates: typing.List['PersistentVolumeClaim'] = None,
    ):
        """Create StatefulSetSpec instance."""
        super(StatefulSetSpec, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetSpec'
        )
        self._properties = {
            'podManagementPolicy': pod_management_policy or '',
            'replicas': replicas or None,
            'revisionHistoryLimit': revision_history_limit or None,
            'selector': selector or LabelSelector(),
            'serviceName': service_name or '',
            'template': template or PodTemplateSpec(),
            'updateStrategy': update_strategy or StatefulSetUpdateStrategy(),
            'volumeClaimTemplates': volume_claim_templates or [],

        }
        self._types = {
            'podManagementPolicy': (str, None),
            'replicas': (int, None),
            'revisionHistoryLimit': (int, None),
            'selector': (LabelSelector, None),
            'serviceName': (str, None),
            'template': (PodTemplateSpec, None),
            'updateStrategy': (StatefulSetUpdateStrategy, None),
            'volumeClaimTemplates': (list, PersistentVolumeClaim),

        }

    @property
    def pod_management_policy(self) -> str:
        """
        podManagementPolicy controls how pods are created during
        initial scale up, when replacing pods on nodes, or when
        scaling down. The default policy is `OrderedReady`, where
        pods are created in increasing order (pod-0, then pod-1,
        etc) and the controller will wait until each pod is ready
        before continuing. When scaling down, the pods are removed
        in the opposite order. The alternative policy is `Parallel`
        which will create pods in parallel to match the desired
        scale without waiting, and on scale down will delete all
        pods at once.
        """
        return self._properties.get('podManagementPolicy')

    @pod_management_policy.setter
    def pod_management_policy(self, value: str):
        """
        podManagementPolicy controls how pods are created during
        initial scale up, when replacing pods on nodes, or when
        scaling down. The default policy is `OrderedReady`, where
        pods are created in increasing order (pod-0, then pod-1,
        etc) and the controller will wait until each pod is ready
        before continuing. When scaling down, the pods are removed
        in the opposite order. The alternative policy is `Parallel`
        which will create pods in parallel to match the desired
        scale without waiting, and on scale down will delete all
        pods at once.
        """
        self._properties['podManagementPolicy'] = value

    @property
    def replicas(self) -> int:
        """
        replicas is the desired number of replicas of the given
        Template. These are replicas in the sense that they are
        instantiations of the same Template, but individual replicas
        also have a consistent identity. If unspecified, defaults to
        1.
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        replicas is the desired number of replicas of the given
        Template. These are replicas in the sense that they are
        instantiations of the same Template, but individual replicas
        also have a consistent identity. If unspecified, defaults to
        1.
        """
        self._properties['replicas'] = value

    @property
    def revision_history_limit(self) -> int:
        """
        revisionHistoryLimit is the maximum number of revisions that
        will be maintained in the StatefulSet's revision history.
        The revision history consists of all revisions not
        represented by a currently applied StatefulSetSpec version.
        The default value is 10.
        """
        return self._properties.get('revisionHistoryLimit')

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        revisionHistoryLimit is the maximum number of revisions that
        will be maintained in the StatefulSet's revision history.
        The revision history consists of all revisions not
        represented by a currently applied StatefulSetSpec version.
        The default value is 10.
        """
        self._properties['revisionHistoryLimit'] = value

    @property
    def selector(self) -> 'LabelSelector':
        """
        selector is a label query over pods that should match the
        replica count. If empty, defaulted to labels on the pod
        template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        selector is a label query over pods that should match the
        replica count. If empty, defaulted to labels on the pod
        template. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def service_name(self) -> str:
        """
        serviceName is the name of the service that governs this
        StatefulSet. This service must exist before the StatefulSet,
        and is responsible for the network identity of the set. Pods
        get DNS/hostnames that follow the pattern: pod-specific-
        string.serviceName.default.svc.cluster.local where "pod-
        specific-string" is managed by the StatefulSet controller.
        """
        return self._properties.get('serviceName')

    @service_name.setter
    def service_name(self, value: str):
        """
        serviceName is the name of the service that governs this
        StatefulSet. This service must exist before the StatefulSet,
        and is responsible for the network identity of the set. Pods
        get DNS/hostnames that follow the pattern: pod-specific-
        string.serviceName.default.svc.cluster.local where "pod-
        specific-string" is managed by the StatefulSet controller.
        """
        self._properties['serviceName'] = value

    @property
    def template(self) -> 'PodTemplateSpec':
        """
        template is the object that describes the pod that will be
        created if insufficient replicas are detected. Each pod
        stamped out by the StatefulSet will fulfill this Template,
        but have a unique identity from the rest of the StatefulSet.
        """
        return self._properties.get('template')

    @template.setter
    def template(self, value: typing.Union['PodTemplateSpec', dict]):
        """
        template is the object that describes the pod that will be
        created if insufficient replicas are detected. Each pod
        stamped out by the StatefulSet will fulfill this Template,
        but have a unique identity from the rest of the StatefulSet.
        """
        if isinstance(value, dict):
            value = PodTemplateSpec().from_dict(value)
        self._properties['template'] = value

    @property
    def update_strategy(self) -> 'StatefulSetUpdateStrategy':
        """
        updateStrategy indicates the StatefulSetUpdateStrategy that
        will be employed to update Pods in the StatefulSet when a
        revision is made to Template.
        """
        return self._properties.get('updateStrategy')

    @update_strategy.setter
    def update_strategy(self, value: typing.Union['StatefulSetUpdateStrategy', dict]):
        """
        updateStrategy indicates the StatefulSetUpdateStrategy that
        will be employed to update Pods in the StatefulSet when a
        revision is made to Template.
        """
        if isinstance(value, dict):
            value = StatefulSetUpdateStrategy().from_dict(value)
        self._properties['updateStrategy'] = value

    @property
    def volume_claim_templates(self) -> typing.List['PersistentVolumeClaim']:
        """
        volumeClaimTemplates is a list of claims that pods are
        allowed to reference. The StatefulSet controller is
        responsible for mapping network identities to claims in a
        way that maintains the identity of a pod. Every claim in
        this list must have at least one matching (by name)
        volumeMount in one container in the template. A claim in
        this list takes precedence over any volumes in the template,
        with the same name.
        """
        return self._properties.get('volumeClaimTemplates')

    @volume_claim_templates.setter
    def volume_claim_templates(
            self,
            value: typing.Union[typing.List['PersistentVolumeClaim'], typing.List[dict]]
    ):
        """
        volumeClaimTemplates is a list of claims that pods are
        allowed to reference. The StatefulSet controller is
        responsible for mapping network identities to claims in a
        way that maintains the identity of a pod. Every claim in
        this list must have at least one matching (by name)
        volumeMount in one container in the template. A claim in
        this list takes precedence over any volumes in the template,
        with the same name.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PersistentVolumeClaim().from_dict(item)
            cleaned.append(item)
        self._properties['volumeClaimTemplates'] = cleaned

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
    ) -> 'StatefulSetSpec':
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

    def __enter__(self) -> 'StatefulSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetStatus(_kuber_definitions.Definition):
    """
    StatefulSetStatus represents the current state of a
    StatefulSet.
    """

    def __init__(
            self,
            collision_count: int = None,
            conditions: typing.List['StatefulSetCondition'] = None,
            current_replicas: int = None,
            current_revision: str = None,
            observed_generation: int = None,
            ready_replicas: int = None,
            replicas: int = None,
            update_revision: str = None,
            updated_replicas: int = None,
    ):
        """Create StatefulSetStatus instance."""
        super(StatefulSetStatus, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetStatus'
        )
        self._properties = {
            'collisionCount': collision_count or None,
            'conditions': conditions or [],
            'currentReplicas': current_replicas or None,
            'currentRevision': current_revision or '',
            'observedGeneration': observed_generation or None,
            'readyReplicas': ready_replicas or None,
            'replicas': replicas or None,
            'updateRevision': update_revision or '',
            'updatedReplicas': updated_replicas or None,

        }
        self._types = {
            'collisionCount': (int, None),
            'conditions': (list, StatefulSetCondition),
            'currentReplicas': (int, None),
            'currentRevision': (str, None),
            'observedGeneration': (int, None),
            'readyReplicas': (int, None),
            'replicas': (int, None),
            'updateRevision': (str, None),
            'updatedReplicas': (int, None),

        }

    @property
    def collision_count(self) -> int:
        """
        collisionCount is the count of hash collisions for the
        StatefulSet. The StatefulSet controller uses this field as a
        collision avoidance mechanism when it needs to create the
        name for the newest ControllerRevision.
        """
        return self._properties.get('collisionCount')

    @collision_count.setter
    def collision_count(self, value: int):
        """
        collisionCount is the count of hash collisions for the
        StatefulSet. The StatefulSet controller uses this field as a
        collision avoidance mechanism when it needs to create the
        name for the newest ControllerRevision.
        """
        self._properties['collisionCount'] = value

    @property
    def conditions(self) -> typing.List['StatefulSetCondition']:
        """
        Represents the latest available observations of a
        statefulset's current state.
        """
        return self._properties.get('conditions')

    @conditions.setter
    def conditions(
            self,
            value: typing.Union[typing.List['StatefulSetCondition'], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        statefulset's current state.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = StatefulSetCondition().from_dict(item)
            cleaned.append(item)
        self._properties['conditions'] = cleaned

    @property
    def current_replicas(self) -> int:
        """
        currentReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by currentRevision.
        """
        return self._properties.get('currentReplicas')

    @current_replicas.setter
    def current_replicas(self, value: int):
        """
        currentReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by currentRevision.
        """
        self._properties['currentReplicas'] = value

    @property
    def current_revision(self) -> str:
        """
        currentRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence
        [0,currentReplicas).
        """
        return self._properties.get('currentRevision')

    @current_revision.setter
    def current_revision(self, value: str):
        """
        currentRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence
        [0,currentReplicas).
        """
        self._properties['currentRevision'] = value

    @property
    def observed_generation(self) -> int:
        """
        observedGeneration is the most recent generation observed
        for this StatefulSet. It corresponds to the StatefulSet's
        generation, which is updated on mutation by the API Server.
        """
        return self._properties.get('observedGeneration')

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        observedGeneration is the most recent generation observed
        for this StatefulSet. It corresponds to the StatefulSet's
        generation, which is updated on mutation by the API Server.
        """
        self._properties['observedGeneration'] = value

    @property
    def ready_replicas(self) -> int:
        """
        readyReplicas is the number of Pods created by the
        StatefulSet controller that have a Ready Condition.
        """
        return self._properties.get('readyReplicas')

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        readyReplicas is the number of Pods created by the
        StatefulSet controller that have a Ready Condition.
        """
        self._properties['readyReplicas'] = value

    @property
    def replicas(self) -> int:
        """
        replicas is the number of Pods created by the StatefulSet
        controller.
        """
        return self._properties.get('replicas')

    @replicas.setter
    def replicas(self, value: int):
        """
        replicas is the number of Pods created by the StatefulSet
        controller.
        """
        self._properties['replicas'] = value

    @property
    def update_revision(self) -> str:
        """
        updateRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence [replicas-
        updatedReplicas,replicas)
        """
        return self._properties.get('updateRevision')

    @update_revision.setter
    def update_revision(self, value: str):
        """
        updateRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence [replicas-
        updatedReplicas,replicas)
        """
        self._properties['updateRevision'] = value

    @property
    def updated_replicas(self) -> int:
        """
        updatedReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by updateRevision.
        """
        return self._properties.get('updatedReplicas')

    @updated_replicas.setter
    def updated_replicas(self, value: int):
        """
        updatedReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by updateRevision.
        """
        self._properties['updatedReplicas'] = value

    def __enter__(self) -> 'StatefulSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetUpdateStrategy(_kuber_definitions.Definition):
    """
    StatefulSetUpdateStrategy indicates the strategy that the
    StatefulSet controller will use to perform updates. It
    includes any additional parameters necessary to perform the
    update for the indicated strategy.
    """

    def __init__(
            self,
            rolling_update: 'RollingUpdateStatefulSetStrategy' = None,
            type_: str = None,
    ):
        """Create StatefulSetUpdateStrategy instance."""
        super(StatefulSetUpdateStrategy, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetUpdateStrategy'
        )
        self._properties = {
            'rollingUpdate': rolling_update or RollingUpdateStatefulSetStrategy(),
            'type': type_ or '',

        }
        self._types = {
            'rollingUpdate': (RollingUpdateStatefulSetStrategy, None),
            'type': (str, None),

        }

    @property
    def rolling_update(self) -> 'RollingUpdateStatefulSetStrategy':
        """
        RollingUpdate is used to communicate parameters when Type is
        RollingUpdateStatefulSetStrategyType.
        """
        return self._properties.get('rollingUpdate')

    @rolling_update.setter
    def rolling_update(self, value: typing.Union['RollingUpdateStatefulSetStrategy', dict]):
        """
        RollingUpdate is used to communicate parameters when Type is
        RollingUpdateStatefulSetStrategyType.
        """
        if isinstance(value, dict):
            value = RollingUpdateStatefulSetStrategy().from_dict(value)
        self._properties['rollingUpdate'] = value

    @property
    def type_(self) -> str:
        """
        Type indicates the type of the StatefulSetUpdateStrategy.
        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """
        Type indicates the type of the StatefulSetUpdateStrategy.
        """
        self._properties['type'] = value

    def __enter__(self) -> 'StatefulSetUpdateStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

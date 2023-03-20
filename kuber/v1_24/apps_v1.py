import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_24.core_v1 import Container  # noqa: F401
from kuber.v1_24.core_v1 import ContainerPort  # noqa: F401
from kuber.v1_24.core_v1 import EnvFromSource  # noqa: F401
from kuber.v1_24.core_v1 import EnvVar  # noqa: F401
from kuber.v1_24.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_24.core_v1 import Lifecycle  # noqa: F401
from kuber.v1_24.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_24.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_24.core_v1 import PersistentVolumeClaim  # noqa: F401
from kuber.v1_24.core_v1 import PodTemplateSpec  # noqa: F401
from kuber.v1_24.core_v1 import Probe  # noqa: F401
from kuber.v1_24.apimachinery_runtime import RawExtension  # noqa: F401
from kuber.v1_24.core_v1 import ResourceRequirements  # noqa: F401
from kuber.v1_24.core_v1 import SecurityContext  # noqa: F401
from kuber.v1_24.meta_v1 import Status  # noqa: F401
from kuber.v1_24.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_24.core_v1 import VolumeDevice  # noqa: F401
from kuber.v1_24.core_v1 import VolumeMount  # noqa: F401


class ControllerRevision(_kuber_definitions.Resource):
    """
    ControllerRevision implements an immutable snapshot of state
    data. Clients are responsible for serializing and
    deserializing the objects that contain their internal state.
    Once a ControllerRevision has been successfully created, it
    can not be updated. The API Server will fail validation of
    all requests that attempt to mutate the Data field.
    ControllerRevisions may, however, be deleted. Note that, due
    to its use by both the DaemonSet and StatefulSet controllers
    for update and rollback, this object is beta. However, it
    may be subject to name and representation changes in future
    releases, and clients should not depend on its stability. It
    is primarily for internal use by controllers.
    """

    def __init__(
        self,
        data: typing.Optional["RawExtension"] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        revision: typing.Optional[int] = None,
    ):
        """Create ControllerRevision instance."""
        super(ControllerRevision, self).__init__(
            api_version="apps/v1", kind="ControllerRevision"
        )
        self._properties = {
            "data": data if data is not None else RawExtension(),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "revision": revision if revision is not None else None,
        }
        self._types = {
            "apiVersion": (str, None),
            "data": (RawExtension, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "revision": (int, None),
        }

    @property
    def data(self) -> "RawExtension":
        """
        Data is the serialized representation of the state.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("data"),
        )

    @data.setter
    def data(self, value: typing.Union["RawExtension", dict]):
        """
        Data is the serialized representation of the state.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["data"] = value

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
    def revision(self) -> int:
        """
        Revision indicates the revision of the state represented by
        Data.
        """
        return typing.cast(
            int,
            self._properties.get("revision"),
        )

    @revision.setter
    def revision(self, value: int):
        """
        Revision indicates the revision of the state represented by
        Data.
        """
        self._properties["revision"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_controller_revision", "create_controller_revision"]

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
        Replaces the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_controller_revision",
            "replace_controller_revision",
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
        Patches the ControllerRevision in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_controller_revision", "patch_controller_revision"]

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
        Reads the ControllerRevision from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_controller_revision",
            "read_controller_revision",
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
        Deletes the ControllerRevision from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_controller_revision",
            "delete_controller_revision",
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "ControllerRevision":
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
        items: typing.Optional[typing.List["ControllerRevision"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ControllerRevisionList instance."""
        super(ControllerRevisionList, self).__init__(
            api_version="apps/v1", kind="ControllerRevisionList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ControllerRevision),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ControllerRevision"]:
        """
        Items is the list of ControllerRevisions
        """
        return typing.cast(
            typing.List["ControllerRevision"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ControllerRevision"], typing.List[dict]]
    ):
        """
        Items is the list of ControllerRevisions
        """
        cleaned: typing.List[ControllerRevision] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ControllerRevision,
                    ControllerRevision().from_dict(item),
                )
            cleaned.append(typing.cast(ControllerRevision, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        More info:
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
        More info:
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "ControllerRevisionList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSet(_kuber_definitions.Resource):
    """
    DaemonSet represents the configuration of a daemon set.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["DaemonSetSpec"] = None,
        status: typing.Optional["DaemonSetStatus"] = None,
    ):
        """Create DaemonSet instance."""
        super(DaemonSet, self).__init__(api_version="apps/v1", kind="DaemonSet")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else DaemonSetSpec(),
            "status": status if status is not None else DaemonSetStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (DaemonSetSpec, None),
            "status": (DaemonSetStatus, None),
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
    def spec(self) -> "DaemonSetSpec":
        """
        The desired behavior of this daemon set. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "DaemonSetSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["DaemonSetSpec", dict]):
        """
        The desired behavior of this daemon set. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                DaemonSetSpec,
                DaemonSetSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "DaemonSetStatus":
        """
        The current status of this daemon set. This data may be out
        of date by some window of time. Populated by the system.
        Read-only. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "DaemonSetStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["DaemonSetStatus", dict]):
        """
        The current status of this daemon set. This data may be out
        of date by some window of time. Populated by the system.
        Read-only. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                DaemonSetStatus,
                DaemonSetStatus().from_dict(value),
            )
        self._properties["status"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "DaemonSet":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (c for c in self.spec.template.spec.containers if c.name == name), None
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.template.spec.containers

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DaemonSetStatus":
        """
        Creates the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_daemon_set", "create_daemon_set"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = DaemonSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DaemonSetStatus":
        """
        Replaces the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_daemon_set", "replace_daemon_set"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = DaemonSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DaemonSetStatus":
        """
        Patches the DaemonSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_daemon_set", "patch_daemon_set"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = DaemonSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "DaemonSetStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_daemon_set",
            "read_daemon_set",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = DaemonSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the DaemonSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_daemon_set",
            "read_daemon_set",
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
        Deletes the DaemonSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_daemon_set",
            "delete_daemon_set",
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "DaemonSet":
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
        last_transition_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create DaemonSetCondition instance."""
        super(DaemonSetCondition, self).__init__(
            api_version="apps/v1", kind="DaemonSetCondition"
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
        Last time the condition transitioned from one status to
        another.
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
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type of DaemonSet condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of DaemonSet condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "DaemonSetCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetList(_kuber_definitions.Collection):
    """
    DaemonSetList is a collection of daemon sets.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["DaemonSet"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create DaemonSetList instance."""
        super(DaemonSetList, self).__init__(api_version="apps/v1", kind="DaemonSetList")
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, DaemonSet),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["DaemonSet"]:
        """
        A list of daemon sets.
        """
        return typing.cast(
            typing.List["DaemonSet"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["DaemonSet"], typing.List[dict]]):
        """
        A list of daemon sets.
        """
        cleaned: typing.List[DaemonSet] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DaemonSet,
                    DaemonSet().from_dict(item),
                )
            cleaned.append(typing.cast(DaemonSet, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
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
        Standard list metadata. More info:
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "DaemonSetList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetSpec(_kuber_definitions.Definition):
    """
    DaemonSetSpec is the specification of a daemon set.
    """

    def __init__(
        self,
        min_ready_seconds: typing.Optional[int] = None,
        revision_history_limit: typing.Optional[int] = None,
        selector: typing.Optional["LabelSelector"] = None,
        template: typing.Optional["PodTemplateSpec"] = None,
        update_strategy: typing.Optional["DaemonSetUpdateStrategy"] = None,
    ):
        """Create DaemonSetSpec instance."""
        super(DaemonSetSpec, self).__init__(api_version="apps/v1", kind="DaemonSetSpec")
        self._properties = {
            "minReadySeconds": min_ready_seconds
            if min_ready_seconds is not None
            else None,
            "revisionHistoryLimit": revision_history_limit
            if revision_history_limit is not None
            else None,
            "selector": selector if selector is not None else LabelSelector(),
            "template": template if template is not None else PodTemplateSpec(),
            "updateStrategy": update_strategy
            if update_strategy is not None
            else DaemonSetUpdateStrategy(),
        }
        self._types = {
            "minReadySeconds": (int, None),
            "revisionHistoryLimit": (int, None),
            "selector": (LabelSelector, None),
            "template": (PodTemplateSpec, None),
            "updateStrategy": (DaemonSetUpdateStrategy, None),
        }

    @property
    def min_ready_seconds(self) -> int:
        """
        The minimum number of seconds for which a newly created
        DaemonSet pod should be ready without any of its container
        crashing, for it to be considered available. Defaults to 0
        (pod will be considered available as soon as it is ready).
        """
        return typing.cast(
            int,
            self._properties.get("minReadySeconds"),
        )

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        The minimum number of seconds for which a newly created
        DaemonSet pod should be ready without any of its container
        crashing, for it to be considered available. Defaults to 0
        (pod will be considered available as soon as it is ready).
        """
        self._properties["minReadySeconds"] = value

    @property
    def revision_history_limit(self) -> int:
        """
        The number of old history to retain to allow rollback. This
        is a pointer to distinguish between explicit zero and not
        specified. Defaults to 10.
        """
        return typing.cast(
            int,
            self._properties.get("revisionHistoryLimit"),
        )

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        The number of old history to retain to allow rollback. This
        is a pointer to distinguish between explicit zero and not
        specified. Defaults to 10.
        """
        self._properties["revisionHistoryLimit"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        A label query over pods that are managed by the daemon set.
        Must match in order to be controlled. It must match the pod
        template's labels. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        A label query over pods that are managed by the daemon set.
        Must match in order to be controlled. It must match the pod
        template's labels. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def template(self) -> "PodTemplateSpec":
        """
        An object that describes the pod that will be created. The
        DaemonSet will create exactly one copy of this pod on every
        node that matches the template's node selector (or on every
        node if no node selector is specified). More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/replication
        controller#pod-template
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        An object that describes the pod that will be created. The
        DaemonSet will create exactly one copy of this pod on every
        node that matches the template's node selector (or on every
        node if no node selector is specified). More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/replication
        controller#pod-template
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodTemplateSpec,
                PodTemplateSpec().from_dict(value),
            )
        self._properties["template"] = value

    @property
    def update_strategy(self) -> "DaemonSetUpdateStrategy":
        """
        An update strategy to replace existing DaemonSet pods with
        new pods.
        """
        return typing.cast(
            "DaemonSetUpdateStrategy",
            self._properties.get("updateStrategy"),
        )

    @update_strategy.setter
    def update_strategy(self, value: typing.Union["DaemonSetUpdateStrategy", dict]):
        """
        An update strategy to replace existing DaemonSet pods with
        new pods.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DaemonSetUpdateStrategy,
                DaemonSetUpdateStrategy().from_dict(value),
            )
        self._properties["updateStrategy"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "DaemonSetSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.template.spec.containers

    def __enter__(self) -> "DaemonSetSpec":
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
        collision_count: typing.Optional[int] = None,
        conditions: typing.Optional[typing.List["DaemonSetCondition"]] = None,
        current_number_scheduled: typing.Optional[int] = None,
        desired_number_scheduled: typing.Optional[int] = None,
        number_available: typing.Optional[int] = None,
        number_misscheduled: typing.Optional[int] = None,
        number_ready: typing.Optional[int] = None,
        number_unavailable: typing.Optional[int] = None,
        observed_generation: typing.Optional[int] = None,
        updated_number_scheduled: typing.Optional[int] = None,
    ):
        """Create DaemonSetStatus instance."""
        super(DaemonSetStatus, self).__init__(
            api_version="apps/v1", kind="DaemonSetStatus"
        )
        self._properties = {
            "collisionCount": collision_count if collision_count is not None else None,
            "conditions": conditions if conditions is not None else [],
            "currentNumberScheduled": current_number_scheduled
            if current_number_scheduled is not None
            else None,
            "desiredNumberScheduled": desired_number_scheduled
            if desired_number_scheduled is not None
            else None,
            "numberAvailable": number_available
            if number_available is not None
            else None,
            "numberMisscheduled": number_misscheduled
            if number_misscheduled is not None
            else None,
            "numberReady": number_ready if number_ready is not None else None,
            "numberUnavailable": number_unavailable
            if number_unavailable is not None
            else None,
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
            "updatedNumberScheduled": updated_number_scheduled
            if updated_number_scheduled is not None
            else None,
        }
        self._types = {
            "collisionCount": (int, None),
            "conditions": (list, DaemonSetCondition),
            "currentNumberScheduled": (int, None),
            "desiredNumberScheduled": (int, None),
            "numberAvailable": (int, None),
            "numberMisscheduled": (int, None),
            "numberReady": (int, None),
            "numberUnavailable": (int, None),
            "observedGeneration": (int, None),
            "updatedNumberScheduled": (int, None),
        }

    @property
    def collision_count(self) -> int:
        """
        Count of hash collisions for the DaemonSet. The DaemonSet
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ControllerRevision.
        """
        return typing.cast(
            int,
            self._properties.get("collisionCount"),
        )

    @collision_count.setter
    def collision_count(self, value: int):
        """
        Count of hash collisions for the DaemonSet. The DaemonSet
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ControllerRevision.
        """
        self._properties["collisionCount"] = value

    @property
    def conditions(self) -> typing.List["DaemonSetCondition"]:
        """
        Represents the latest available observations of a
        DaemonSet's current state.
        """
        return typing.cast(
            typing.List["DaemonSetCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["DaemonSetCondition"], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        DaemonSet's current state.
        """
        cleaned: typing.List[DaemonSetCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DaemonSetCondition,
                    DaemonSetCondition().from_dict(item),
                )
            cleaned.append(typing.cast(DaemonSetCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def current_number_scheduled(self) -> int:
        """
        The number of nodes that are running at least 1 daemon pod
        and are supposed to run the daemon pod. More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/daemonset/
        """
        return typing.cast(
            int,
            self._properties.get("currentNumberScheduled"),
        )

    @current_number_scheduled.setter
    def current_number_scheduled(self, value: int):
        """
        The number of nodes that are running at least 1 daemon pod
        and are supposed to run the daemon pod. More info: https://k
        ubernetes.io/docs/concepts/workloads/controllers/daemonset/
        """
        self._properties["currentNumberScheduled"] = value

    @property
    def desired_number_scheduled(self) -> int:
        """
        The total number of nodes that should be running the daemon
        pod (including nodes correctly running the daemon pod). More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/daemonset/
        """
        return typing.cast(
            int,
            self._properties.get("desiredNumberScheduled"),
        )

    @desired_number_scheduled.setter
    def desired_number_scheduled(self, value: int):
        """
        The total number of nodes that should be running the daemon
        pod (including nodes correctly running the daemon pod). More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/daemonset/
        """
        self._properties["desiredNumberScheduled"] = value

    @property
    def number_available(self) -> int:
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and available
        (ready for at least spec.minReadySeconds)
        """
        return typing.cast(
            int,
            self._properties.get("numberAvailable"),
        )

    @number_available.setter
    def number_available(self, value: int):
        """
        The number of nodes that should be running the daemon pod
        and have one or more of the daemon pod running and available
        (ready for at least spec.minReadySeconds)
        """
        self._properties["numberAvailable"] = value

    @property
    def number_misscheduled(self) -> int:
        """
        The number of nodes that are running the daemon pod, but are
        not supposed to run the daemon pod. More info: https://kuber
        netes.io/docs/concepts/workloads/controllers/daemonset/
        """
        return typing.cast(
            int,
            self._properties.get("numberMisscheduled"),
        )

    @number_misscheduled.setter
    def number_misscheduled(self, value: int):
        """
        The number of nodes that are running the daemon pod, but are
        not supposed to run the daemon pod. More info: https://kuber
        netes.io/docs/concepts/workloads/controllers/daemonset/
        """
        self._properties["numberMisscheduled"] = value

    @property
    def number_ready(self) -> int:
        """
        numberReady is the number of nodes that should be running
        the daemon pod and have one or more of the daemon pod
        running with a Ready Condition.
        """
        return typing.cast(
            int,
            self._properties.get("numberReady"),
        )

    @number_ready.setter
    def number_ready(self, value: int):
        """
        numberReady is the number of nodes that should be running
        the daemon pod and have one or more of the daemon pod
        running with a Ready Condition.
        """
        self._properties["numberReady"] = value

    @property
    def number_unavailable(self) -> int:
        """
        The number of nodes that should be running the daemon pod
        and have none of the daemon pod running and available (ready
        for at least spec.minReadySeconds)
        """
        return typing.cast(
            int,
            self._properties.get("numberUnavailable"),
        )

    @number_unavailable.setter
    def number_unavailable(self, value: int):
        """
        The number of nodes that should be running the daemon pod
        and have none of the daemon pod running and available (ready
        for at least spec.minReadySeconds)
        """
        self._properties["numberUnavailable"] = value

    @property
    def observed_generation(self) -> int:
        """
        The most recent generation observed by the daemon set
        controller.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        The most recent generation observed by the daemon set
        controller.
        """
        self._properties["observedGeneration"] = value

    @property
    def updated_number_scheduled(self) -> int:
        """
        The total number of nodes that are running updated daemon
        pod
        """
        return typing.cast(
            int,
            self._properties.get("updatedNumberScheduled"),
        )

    @updated_number_scheduled.setter
    def updated_number_scheduled(self, value: int):
        """
        The total number of nodes that are running updated daemon
        pod
        """
        self._properties["updatedNumberScheduled"] = value

    def __enter__(self) -> "DaemonSetStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetUpdateStrategy(_kuber_definitions.Definition):
    """
    DaemonSetUpdateStrategy is a struct used to control the
    update strategy for a DaemonSet.
    """

    def __init__(
        self,
        rolling_update: typing.Optional["RollingUpdateDaemonSet"] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create DaemonSetUpdateStrategy instance."""
        super(DaemonSetUpdateStrategy, self).__init__(
            api_version="apps/v1", kind="DaemonSetUpdateStrategy"
        )
        self._properties = {
            "rollingUpdate": rolling_update
            if rolling_update is not None
            else RollingUpdateDaemonSet(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "rollingUpdate": (RollingUpdateDaemonSet, None),
            "type": (str, None),
        }

    @property
    def rolling_update(self) -> "RollingUpdateDaemonSet":
        """
        Rolling update config params. Present only if type =
        "RollingUpdate".
        """
        return typing.cast(
            "RollingUpdateDaemonSet",
            self._properties.get("rollingUpdate"),
        )

    @rolling_update.setter
    def rolling_update(self, value: typing.Union["RollingUpdateDaemonSet", dict]):
        """
        Rolling update config params. Present only if type =
        "RollingUpdate".
        """
        if isinstance(value, dict):
            value = typing.cast(
                RollingUpdateDaemonSet,
                RollingUpdateDaemonSet().from_dict(value),
            )
        self._properties["rollingUpdate"] = value

    @property
    def type_(self) -> str:
        """
        Type of daemon set update. Can be "RollingUpdate" or
        "OnDelete". Default is RollingUpdate.

        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of daemon set update. Can be "RollingUpdate" or
        "OnDelete". Default is RollingUpdate.

        """
        self._properties["type"] = value

    def __enter__(self) -> "DaemonSetUpdateStrategy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Deployment(_kuber_definitions.Resource):
    """
    Deployment enables declarative updates for Pods and
    ReplicaSets.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["DeploymentSpec"] = None,
        status: typing.Optional["DeploymentStatus"] = None,
    ):
        """Create Deployment instance."""
        super(Deployment, self).__init__(api_version="apps/v1", kind="Deployment")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else DeploymentSpec(),
            "status": status if status is not None else DeploymentStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (DeploymentSpec, None),
            "status": (DeploymentStatus, None),
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
    def spec(self) -> "DeploymentSpec":
        """
        Specification of the desired behavior of the Deployment.
        """
        return typing.cast(
            "DeploymentSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["DeploymentSpec", dict]):
        """
        Specification of the desired behavior of the Deployment.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeploymentSpec,
                DeploymentSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "DeploymentStatus":
        """
        Most recently observed status of the Deployment.
        """
        return typing.cast(
            "DeploymentStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["DeploymentStatus", dict]):
        """
        Most recently observed status of the Deployment.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeploymentStatus,
                DeploymentStatus().from_dict(value),
            )
        self._properties["status"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "Deployment":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (c for c in self.spec.template.spec.containers if c.name == name), None
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.template.spec.containers

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DeploymentStatus":
        """
        Creates the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_deployment", "create_deployment"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = DeploymentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DeploymentStatus":
        """
        Replaces the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_deployment", "replace_deployment"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = DeploymentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "DeploymentStatus":
        """
        Patches the Deployment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_deployment", "patch_deployment"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = DeploymentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "DeploymentStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_deployment",
            "read_deployment",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = DeploymentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the Deployment from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_deployment",
            "read_deployment",
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
        Deletes the Deployment from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_deployment",
            "delete_deployment",
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "Deployment":
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
        last_transition_time: typing.Optional[str] = None,
        last_update_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create DeploymentCondition instance."""
        super(DeploymentCondition, self).__init__(
            api_version="apps/v1", kind="DeploymentCondition"
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "lastUpdateTime": last_update_time
            if last_update_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "lastUpdateTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transitioned from one status to
        another.
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
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def last_update_time(self) -> str:
        """
        The last time this condition was updated.
        """
        return typing.cast(
            str,
            self._properties.get("lastUpdateTime"),
        )

    @last_update_time.setter
    def last_update_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        The last time this condition was updated.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastUpdateTime"] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type of deployment condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of deployment condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "DeploymentCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentList(_kuber_definitions.Collection):
    """
    DeploymentList is a list of Deployments.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["Deployment"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create DeploymentList instance."""
        super(DeploymentList, self).__init__(
            api_version="apps/v1", kind="DeploymentList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Deployment),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Deployment"]:
        """
        Items is the list of Deployments.
        """
        return typing.cast(
            typing.List["Deployment"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Deployment"], typing.List[dict]]):
        """
        Items is the list of Deployments.
        """
        cleaned: typing.List[Deployment] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Deployment,
                    Deployment().from_dict(item),
                )
            cleaned.append(typing.cast(Deployment, item))
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "DeploymentList":
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
        min_ready_seconds: typing.Optional[int] = None,
        paused: typing.Optional[bool] = None,
        progress_deadline_seconds: typing.Optional[int] = None,
        replicas: typing.Optional[int] = None,
        revision_history_limit: typing.Optional[int] = None,
        selector: typing.Optional["LabelSelector"] = None,
        strategy: typing.Optional["DeploymentStrategy"] = None,
        template: typing.Optional["PodTemplateSpec"] = None,
    ):
        """Create DeploymentSpec instance."""
        super(DeploymentSpec, self).__init__(
            api_version="apps/v1", kind="DeploymentSpec"
        )
        self._properties = {
            "minReadySeconds": min_ready_seconds
            if min_ready_seconds is not None
            else None,
            "paused": paused if paused is not None else None,
            "progressDeadlineSeconds": progress_deadline_seconds
            if progress_deadline_seconds is not None
            else None,
            "replicas": replicas if replicas is not None else None,
            "revisionHistoryLimit": revision_history_limit
            if revision_history_limit is not None
            else None,
            "selector": selector if selector is not None else LabelSelector(),
            "strategy": strategy if strategy is not None else DeploymentStrategy(),
            "template": template if template is not None else PodTemplateSpec(),
        }
        self._types = {
            "minReadySeconds": (int, None),
            "paused": (bool, None),
            "progressDeadlineSeconds": (int, None),
            "replicas": (int, None),
            "revisionHistoryLimit": (int, None),
            "selector": (LabelSelector, None),
            "strategy": (DeploymentStrategy, None),
            "template": (PodTemplateSpec, None),
        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        return typing.cast(
            int,
            self._properties.get("minReadySeconds"),
        )

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        self._properties["minReadySeconds"] = value

    @property
    def paused(self) -> bool:
        """
        Indicates that the deployment is paused.
        """
        return typing.cast(
            bool,
            self._properties.get("paused"),
        )

    @paused.setter
    def paused(self, value: bool):
        """
        Indicates that the deployment is paused.
        """
        self._properties["paused"] = value

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
        return typing.cast(
            int,
            self._properties.get("progressDeadlineSeconds"),
        )

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
        self._properties["progressDeadlineSeconds"] = value

    @property
    def replicas(self) -> int:
        """
        Number of desired pods. This is a pointer to distinguish
        between explicit zero and not specified. Defaults to 1.
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        Number of desired pods. This is a pointer to distinguish
        between explicit zero and not specified. Defaults to 1.
        """
        self._properties["replicas"] = value

    @property
    def revision_history_limit(self) -> int:
        """
        The number of old ReplicaSets to retain to allow rollback.
        This is a pointer to distinguish between explicit zero and
        not specified. Defaults to 10.
        """
        return typing.cast(
            int,
            self._properties.get("revisionHistoryLimit"),
        )

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        The number of old ReplicaSets to retain to allow rollback.
        This is a pointer to distinguish between explicit zero and
        not specified. Defaults to 10.
        """
        self._properties["revisionHistoryLimit"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        Label selector for pods. Existing ReplicaSets whose pods are
        selected by this will be the ones affected by this
        deployment. It must match the pod template's labels.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        Label selector for pods. Existing ReplicaSets whose pods are
        selected by this will be the ones affected by this
        deployment. It must match the pod template's labels.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def strategy(self) -> "DeploymentStrategy":
        """
        The deployment strategy to use to replace existing pods with
        new ones.
        """
        return typing.cast(
            "DeploymentStrategy",
            self._properties.get("strategy"),
        )

    @strategy.setter
    def strategy(self, value: typing.Union["DeploymentStrategy", dict]):
        """
        The deployment strategy to use to replace existing pods with
        new ones.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeploymentStrategy,
                DeploymentStrategy().from_dict(value),
            )
        self._properties["strategy"] = value

    @property
    def template(self) -> "PodTemplateSpec":
        """
        Template describes the pods that will be created.
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        Template describes the pods that will be created.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodTemplateSpec,
                PodTemplateSpec().from_dict(value),
            )
        self._properties["template"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "DeploymentSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.template.spec.containers

    def __enter__(self) -> "DeploymentSpec":
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
        available_replicas: typing.Optional[int] = None,
        collision_count: typing.Optional[int] = None,
        conditions: typing.Optional[typing.List["DeploymentCondition"]] = None,
        observed_generation: typing.Optional[int] = None,
        ready_replicas: typing.Optional[int] = None,
        replicas: typing.Optional[int] = None,
        unavailable_replicas: typing.Optional[int] = None,
        updated_replicas: typing.Optional[int] = None,
    ):
        """Create DeploymentStatus instance."""
        super(DeploymentStatus, self).__init__(
            api_version="apps/v1", kind="DeploymentStatus"
        )
        self._properties = {
            "availableReplicas": available_replicas
            if available_replicas is not None
            else None,
            "collisionCount": collision_count if collision_count is not None else None,
            "conditions": conditions if conditions is not None else [],
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
            "readyReplicas": ready_replicas if ready_replicas is not None else None,
            "replicas": replicas if replicas is not None else None,
            "unavailableReplicas": unavailable_replicas
            if unavailable_replicas is not None
            else None,
            "updatedReplicas": updated_replicas
            if updated_replicas is not None
            else None,
        }
        self._types = {
            "availableReplicas": (int, None),
            "collisionCount": (int, None),
            "conditions": (list, DeploymentCondition),
            "observedGeneration": (int, None),
            "readyReplicas": (int, None),
            "replicas": (int, None),
            "unavailableReplicas": (int, None),
            "updatedReplicas": (int, None),
        }

    @property
    def available_replicas(self) -> int:
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this deployment.
        """
        return typing.cast(
            int,
            self._properties.get("availableReplicas"),
        )

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this deployment.
        """
        self._properties["availableReplicas"] = value

    @property
    def collision_count(self) -> int:
        """
        Count of hash collisions for the Deployment. The Deployment
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ReplicaSet.
        """
        return typing.cast(
            int,
            self._properties.get("collisionCount"),
        )

    @collision_count.setter
    def collision_count(self, value: int):
        """
        Count of hash collisions for the Deployment. The Deployment
        controller uses this field as a collision avoidance
        mechanism when it needs to create the name for the newest
        ReplicaSet.
        """
        self._properties["collisionCount"] = value

    @property
    def conditions(self) -> typing.List["DeploymentCondition"]:
        """
        Represents the latest available observations of a
        deployment's current state.
        """
        return typing.cast(
            typing.List["DeploymentCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["DeploymentCondition"], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a
        deployment's current state.
        """
        cleaned: typing.List[DeploymentCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeploymentCondition,
                    DeploymentCondition().from_dict(item),
                )
            cleaned.append(typing.cast(DeploymentCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def observed_generation(self) -> int:
        """
        The generation observed by the deployment controller.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        The generation observed by the deployment controller.
        """
        self._properties["observedGeneration"] = value

    @property
    def ready_replicas(self) -> int:
        """
        readyReplicas is the number of pods targeted by this
        Deployment with a Ready Condition.
        """
        return typing.cast(
            int,
            self._properties.get("readyReplicas"),
        )

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        readyReplicas is the number of pods targeted by this
        Deployment with a Ready Condition.
        """
        self._properties["readyReplicas"] = value

    @property
    def replicas(self) -> int:
        """
        Total number of non-terminated pods targeted by this
        deployment (their labels match the selector).
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        Total number of non-terminated pods targeted by this
        deployment (their labels match the selector).
        """
        self._properties["replicas"] = value

    @property
    def unavailable_replicas(self) -> int:
        """
        Total number of unavailable pods targeted by this
        deployment. This is the total number of pods that are still
        required for the deployment to have 100% available capacity.
        They may either be pods that are running but not yet
        available or pods that still have not been created.
        """
        return typing.cast(
            int,
            self._properties.get("unavailableReplicas"),
        )

    @unavailable_replicas.setter
    def unavailable_replicas(self, value: int):
        """
        Total number of unavailable pods targeted by this
        deployment. This is the total number of pods that are still
        required for the deployment to have 100% available capacity.
        They may either be pods that are running but not yet
        available or pods that still have not been created.
        """
        self._properties["unavailableReplicas"] = value

    @property
    def updated_replicas(self) -> int:
        """
        Total number of non-terminated pods targeted by this
        deployment that have the desired template spec.
        """
        return typing.cast(
            int,
            self._properties.get("updatedReplicas"),
        )

    @updated_replicas.setter
    def updated_replicas(self, value: int):
        """
        Total number of non-terminated pods targeted by this
        deployment that have the desired template spec.
        """
        self._properties["updatedReplicas"] = value

    def __enter__(self) -> "DeploymentStatus":
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
        rolling_update: typing.Optional["RollingUpdateDeployment"] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create DeploymentStrategy instance."""
        super(DeploymentStrategy, self).__init__(
            api_version="apps/v1", kind="DeploymentStrategy"
        )
        self._properties = {
            "rollingUpdate": rolling_update
            if rolling_update is not None
            else RollingUpdateDeployment(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "rollingUpdate": (RollingUpdateDeployment, None),
            "type": (str, None),
        }

    @property
    def rolling_update(self) -> "RollingUpdateDeployment":
        """
        Rolling update config params. Present only if
        DeploymentStrategyType = RollingUpdate.
        """
        return typing.cast(
            "RollingUpdateDeployment",
            self._properties.get("rollingUpdate"),
        )

    @rolling_update.setter
    def rolling_update(self, value: typing.Union["RollingUpdateDeployment", dict]):
        """
        Rolling update config params. Present only if
        DeploymentStrategyType = RollingUpdate.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RollingUpdateDeployment,
                RollingUpdateDeployment().from_dict(value),
            )
        self._properties["rollingUpdate"] = value

    @property
    def type_(self) -> str:
        """
        Type of deployment. Can be "Recreate" or "RollingUpdate".
        Default is RollingUpdate.

        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of deployment. Can be "Recreate" or "RollingUpdate".
        Default is RollingUpdate.

        """
        self._properties["type"] = value

    def __enter__(self) -> "DeploymentStrategy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSet(_kuber_definitions.Resource):
    """
    ReplicaSet ensures that a specified number of pod replicas
    are running at any given time.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ReplicaSetSpec"] = None,
        status: typing.Optional["ReplicaSetStatus"] = None,
    ):
        """Create ReplicaSet instance."""
        super(ReplicaSet, self).__init__(api_version="apps/v1", kind="ReplicaSet")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ReplicaSetSpec(),
            "status": status if status is not None else ReplicaSetStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ReplicaSetSpec, None),
            "status": (ReplicaSetStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        If the Labels of a ReplicaSet are empty, they are defaulted
        to be the same as the Pod(s) that the ReplicaSet manages.
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
        If the Labels of a ReplicaSet are empty, they are defaulted
        to be the same as the Pod(s) that the ReplicaSet manages.
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
    def spec(self) -> "ReplicaSetSpec":
        """
        Spec defines the specification of the desired behavior of
        the ReplicaSet. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "ReplicaSetSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ReplicaSetSpec", dict]):
        """
        Spec defines the specification of the desired behavior of
        the ReplicaSet. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                ReplicaSetSpec,
                ReplicaSetSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ReplicaSetStatus":
        """
        Status is the most recently observed status of the
        ReplicaSet. This data may be out of date by some window of
        time. Populated by the system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "ReplicaSetStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ReplicaSetStatus", dict]):
        """
        Status is the most recently observed status of the
        ReplicaSet. This data may be out of date by some window of
        time. Populated by the system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                ReplicaSetStatus,
                ReplicaSetStatus().from_dict(value),
            )
        self._properties["status"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "ReplicaSet":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (c for c in self.spec.template.spec.containers if c.name == name), None
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.template.spec.containers

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ReplicaSetStatus":
        """
        Creates the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_replica_set", "create_replica_set"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ReplicaSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ReplicaSetStatus":
        """
        Replaces the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_replica_set", "replace_replica_set"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ReplicaSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ReplicaSetStatus":
        """
        Patches the ReplicaSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_replica_set", "patch_replica_set"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ReplicaSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "ReplicaSetStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_replica_set",
            "read_replica_set",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ReplicaSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the ReplicaSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_replica_set",
            "read_replica_set",
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
        Deletes the ReplicaSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_replica_set",
            "delete_replica_set",
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "ReplicaSet":
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
        last_transition_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create ReplicaSetCondition instance."""
        super(ReplicaSetCondition, self).__init__(
            api_version="apps/v1", kind="ReplicaSetCondition"
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
        The last time the condition transitioned from one status to
        another.
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
        The last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type of replica set condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of replica set condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "ReplicaSetCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetList(_kuber_definitions.Collection):
    """
    ReplicaSetList is a collection of ReplicaSets.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ReplicaSet"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ReplicaSetList instance."""
        super(ReplicaSetList, self).__init__(
            api_version="apps/v1", kind="ReplicaSetList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ReplicaSet),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ReplicaSet"]:
        """
        List of ReplicaSets. More info: https://kubernetes.io/docs/c
        oncepts/workloads/controllers/replicationcontroller
        """
        return typing.cast(
            typing.List["ReplicaSet"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["ReplicaSet"], typing.List[dict]]):
        """
        List of ReplicaSets. More info: https://kubernetes.io/docs/c
        oncepts/workloads/controllers/replicationcontroller
        """
        cleaned: typing.List[ReplicaSet] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ReplicaSet,
                    ReplicaSet().from_dict(item),
                )
            cleaned.append(typing.cast(ReplicaSet, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "ReplicaSetList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetSpec(_kuber_definitions.Definition):
    """
    ReplicaSetSpec is the specification of a ReplicaSet.
    """

    def __init__(
        self,
        min_ready_seconds: typing.Optional[int] = None,
        replicas: typing.Optional[int] = None,
        selector: typing.Optional["LabelSelector"] = None,
        template: typing.Optional["PodTemplateSpec"] = None,
    ):
        """Create ReplicaSetSpec instance."""
        super(ReplicaSetSpec, self).__init__(
            api_version="apps/v1", kind="ReplicaSetSpec"
        )
        self._properties = {
            "minReadySeconds": min_ready_seconds
            if min_ready_seconds is not None
            else None,
            "replicas": replicas if replicas is not None else None,
            "selector": selector if selector is not None else LabelSelector(),
            "template": template if template is not None else PodTemplateSpec(),
        }
        self._types = {
            "minReadySeconds": (int, None),
            "replicas": (int, None),
            "selector": (LabelSelector, None),
            "template": (PodTemplateSpec, None),
        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        return typing.cast(
            int,
            self._properties.get("minReadySeconds"),
        )

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing, for
        it to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready)
        """
        self._properties["minReadySeconds"] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller/#
        what-is-a-replicationcontroller
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the number of desired replicas. This is a
        pointer to distinguish between explicit zero and
        unspecified. Defaults to 1. More info: https://kubernetes.io
        /docs/concepts/workloads/controllers/replicationcontroller/#
        what-is-a-replicationcontroller
        """
        self._properties["replicas"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        Selector is a label query over pods that should match the
        replica count. Label keys and values that must match in
        order to be controlled by this replica set. It must match
        the pod template's labels. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        Selector is a label query over pods that should match the
        replica count. Label keys and values that must match in
        order to be controlled by this replica set. It must match
        the pod template's labels. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def template(self) -> "PodTemplateSpec":
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. More info: ht
        tps://kubernetes.io/docs/concepts/workloads/controllers/repl
        icationcontroller#pod-template
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        Template is the object that describes the pod that will be
        created if insufficient replicas are detected. More info: ht
        tps://kubernetes.io/docs/concepts/workloads/controllers/repl
        icationcontroller#pod-template
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodTemplateSpec,
                PodTemplateSpec().from_dict(value),
            )
        self._properties["template"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "ReplicaSetSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.template.spec.containers

    def __enter__(self) -> "ReplicaSetSpec":
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
        available_replicas: typing.Optional[int] = None,
        conditions: typing.Optional[typing.List["ReplicaSetCondition"]] = None,
        fully_labeled_replicas: typing.Optional[int] = None,
        observed_generation: typing.Optional[int] = None,
        ready_replicas: typing.Optional[int] = None,
        replicas: typing.Optional[int] = None,
    ):
        """Create ReplicaSetStatus instance."""
        super(ReplicaSetStatus, self).__init__(
            api_version="apps/v1", kind="ReplicaSetStatus"
        )
        self._properties = {
            "availableReplicas": available_replicas
            if available_replicas is not None
            else None,
            "conditions": conditions if conditions is not None else [],
            "fullyLabeledReplicas": fully_labeled_replicas
            if fully_labeled_replicas is not None
            else None,
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
            "readyReplicas": ready_replicas if ready_replicas is not None else None,
            "replicas": replicas if replicas is not None else None,
        }
        self._types = {
            "availableReplicas": (int, None),
            "conditions": (list, ReplicaSetCondition),
            "fullyLabeledReplicas": (int, None),
            "observedGeneration": (int, None),
            "readyReplicas": (int, None),
            "replicas": (int, None),
        }

    @property
    def available_replicas(self) -> int:
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replica set.
        """
        return typing.cast(
            int,
            self._properties.get("availableReplicas"),
        )

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        The number of available replicas (ready for at least
        minReadySeconds) for this replica set.
        """
        self._properties["availableReplicas"] = value

    @property
    def conditions(self) -> typing.List["ReplicaSetCondition"]:
        """
        Represents the latest available observations of a replica
        set's current state.
        """
        return typing.cast(
            typing.List["ReplicaSetCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["ReplicaSetCondition"], typing.List[dict]]
    ):
        """
        Represents the latest available observations of a replica
        set's current state.
        """
        cleaned: typing.List[ReplicaSetCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ReplicaSetCondition,
                    ReplicaSetCondition().from_dict(item),
                )
            cleaned.append(typing.cast(ReplicaSetCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def fully_labeled_replicas(self) -> int:
        """
        The number of pods that have labels matching the labels of
        the pod template of the replicaset.
        """
        return typing.cast(
            int,
            self._properties.get("fullyLabeledReplicas"),
        )

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, value: int):
        """
        The number of pods that have labels matching the labels of
        the pod template of the replicaset.
        """
        self._properties["fullyLabeledReplicas"] = value

    @property
    def observed_generation(self) -> int:
        """
        ObservedGeneration reflects the generation of the most
        recently observed ReplicaSet.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        ObservedGeneration reflects the generation of the most
        recently observed ReplicaSet.
        """
        self._properties["observedGeneration"] = value

    @property
    def ready_replicas(self) -> int:
        """
        readyReplicas is the number of pods targeted by this
        ReplicaSet with a Ready Condition.
        """
        return typing.cast(
            int,
            self._properties.get("readyReplicas"),
        )

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        readyReplicas is the number of pods targeted by this
        ReplicaSet with a Ready Condition.
        """
        self._properties["readyReplicas"] = value

    @property
    def replicas(self) -> int:
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller/#what-is-a-
        replicationcontroller
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        Replicas is the most recently oberved number of replicas.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/replicationcontroller/#what-is-a-
        replicationcontroller
        """
        self._properties["replicas"] = value

    def __enter__(self) -> "ReplicaSetStatus":
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
        max_surge: typing.Optional[typing.Union[str, int, None]] = None,
        max_unavailable: typing.Optional[typing.Union[str, int, None]] = None,
    ):
        """Create RollingUpdateDaemonSet instance."""
        super(RollingUpdateDaemonSet, self).__init__(
            api_version="apps/v1", kind="RollingUpdateDaemonSet"
        )
        self._properties = {
            "maxSurge": max_surge if max_surge is not None else None,
            "maxUnavailable": max_unavailable if max_unavailable is not None else None,
        }
        self._types = {
            "maxSurge": (_types.integer_or_string, None),
            "maxUnavailable": (_types.integer_or_string, None),
        }

    @property
    def max_surge(self) -> typing.Union[str, int, None]:
        """
        The maximum number of nodes with an existing available
        DaemonSet pod that can have an updated DaemonSet pod during
        during an update. Value can be an absolute number (ex: 5) or
        a percentage of desired pods (ex: 10%). This can not be 0 if
        MaxUnavailable is 0. Absolute number is calculated from
        percentage by rounding up to a minimum of 1. Default value
        is 0. Example: when this is set to 30%, at most 30% of the
        total number of nodes that should be running the daemon pod
        (i.e. status.desiredNumberScheduled) can have their a new
        pod created before the old pod is marked as deleted. The
        update starts by launching new pods on 30% of nodes. Once an
        updated pod is available (Ready for at least
        minReadySeconds) the old DaemonSet pod on that node is
        marked deleted. If the old pod becomes unavailable for any
        reason (Ready transitions to false, is evicted, or is
        drained) an updated pod is immediatedly created on that node
        without considering surge limits. Allowing surge implies the
        possibility that the resources consumed by the daemonset on
        any given node can double if the readiness check fails, and
        so resource intensive daemonsets should take into account
        that they may cause evictions during disruption. This is
        beta field and enabled/disabled by DaemonSetUpdateSurge
        feature gate.
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxSurge"),
        )

    @max_surge.setter
    def max_surge(self, value: typing.Union[str, int, None]):
        """
        The maximum number of nodes with an existing available
        DaemonSet pod that can have an updated DaemonSet pod during
        during an update. Value can be an absolute number (ex: 5) or
        a percentage of desired pods (ex: 10%). This can not be 0 if
        MaxUnavailable is 0. Absolute number is calculated from
        percentage by rounding up to a minimum of 1. Default value
        is 0. Example: when this is set to 30%, at most 30% of the
        total number of nodes that should be running the daemon pod
        (i.e. status.desiredNumberScheduled) can have their a new
        pod created before the old pod is marked as deleted. The
        update starts by launching new pods on 30% of nodes. Once an
        updated pod is available (Ready for at least
        minReadySeconds) the old DaemonSet pod on that node is
        marked deleted. If the old pod becomes unavailable for any
        reason (Ready transitions to false, is evicted, or is
        drained) an updated pod is immediatedly created on that node
        without considering surge limits. Allowing surge implies the
        possibility that the resources consumed by the daemonset on
        any given node can double if the readiness check fails, and
        so resource intensive daemonsets should take into account
        that they may cause evictions during disruption. This is
        beta field and enabled/disabled by DaemonSetUpdateSurge
        feature gate.
        """
        self._properties["maxSurge"] = _types.integer_or_string(value)

    @property
    def max_unavailable(self) -> typing.Union[str, int, None]:
        """
        The maximum number of DaemonSet pods that can be unavailable
        during the update. Value can be an absolute number (ex: 5)
        or a percentage of total number of DaemonSet pods at the
        start of the update (ex: 10%). Absolute number is calculated
        from percentage by rounding up. This cannot be 0 if MaxSurge
        is 0 Default value is 1. Example: when this is set to 30%,
        at most 30% of the total number of nodes that should be
        running the daemon pod (i.e. status.desiredNumberScheduled)
        can have their pods stopped for an update at any given time.
        The update starts by stopping at most 30% of those DaemonSet
        pods and then brings up new DaemonSet pods in their place.
        Once the new pods are available, it then proceeds onto other
        DaemonSet pods, thus ensuring that at least 70% of original
        number of DaemonSet pods are available at all times during
        the update.
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxUnavailable"),
        )

    @max_unavailable.setter
    def max_unavailable(self, value: typing.Union[str, int, None]):
        """
        The maximum number of DaemonSet pods that can be unavailable
        during the update. Value can be an absolute number (ex: 5)
        or a percentage of total number of DaemonSet pods at the
        start of the update (ex: 10%). Absolute number is calculated
        from percentage by rounding up. This cannot be 0 if MaxSurge
        is 0 Default value is 1. Example: when this is set to 30%,
        at most 30% of the total number of nodes that should be
        running the daemon pod (i.e. status.desiredNumberScheduled)
        can have their pods stopped for an update at any given time.
        The update starts by stopping at most 30% of those DaemonSet
        pods and then brings up new DaemonSet pods in their place.
        Once the new pods are available, it then proceeds onto other
        DaemonSet pods, thus ensuring that at least 70% of original
        number of DaemonSet pods are available at all times during
        the update.
        """
        self._properties["maxUnavailable"] = _types.integer_or_string(value)

    def __enter__(self) -> "RollingUpdateDaemonSet":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateDeployment(_kuber_definitions.Definition):
    """
    Spec to control the desired behavior of rolling update.
    """

    def __init__(
        self,
        max_surge: typing.Optional[typing.Union[str, int, None]] = None,
        max_unavailable: typing.Optional[typing.Union[str, int, None]] = None,
    ):
        """Create RollingUpdateDeployment instance."""
        super(RollingUpdateDeployment, self).__init__(
            api_version="apps/v1", kind="RollingUpdateDeployment"
        )
        self._properties = {
            "maxSurge": max_surge if max_surge is not None else None,
            "maxUnavailable": max_unavailable if max_unavailable is not None else None,
        }
        self._types = {
            "maxSurge": (_types.integer_or_string, None),
            "maxUnavailable": (_types.integer_or_string, None),
        }

    @property
    def max_surge(self) -> typing.Union[str, int, None]:
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
        running at any time during the update is at most 130% of
        desired pods.
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxSurge"),
        )

    @max_surge.setter
    def max_surge(self, value: typing.Union[str, int, None]):
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
        running at any time during the update is at most 130% of
        desired pods.
        """
        self._properties["maxSurge"] = _types.integer_or_string(value)

    @property
    def max_unavailable(self) -> typing.Union[str, int, None]:
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
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxUnavailable"),
        )

    @max_unavailable.setter
    def max_unavailable(self, value: typing.Union[str, int, None]):
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
        self._properties["maxUnavailable"] = _types.integer_or_string(value)

    def __enter__(self) -> "RollingUpdateDeployment":
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
        max_unavailable: typing.Optional[typing.Union[str, int, None]] = None,
        partition: typing.Optional[int] = None,
    ):
        """Create RollingUpdateStatefulSetStrategy instance."""
        super(RollingUpdateStatefulSetStrategy, self).__init__(
            api_version="apps/v1", kind="RollingUpdateStatefulSetStrategy"
        )
        self._properties = {
            "maxUnavailable": max_unavailable if max_unavailable is not None else None,
            "partition": partition if partition is not None else None,
        }
        self._types = {
            "maxUnavailable": (_types.integer_or_string, None),
            "partition": (int, None),
        }

    @property
    def max_unavailable(self) -> typing.Union[str, int, None]:
        """
        The maximum number of pods that can be unavailable during
        the update. Value can be an absolute number (ex: 5) or a
        percentage of desired pods (ex: 10%). Absolute number is
        calculated from percentage by rounding up. This can not be
        0. Defaults to 1. This field is alpha-level and is only
        honored by servers that enable the MaxUnavailableStatefulSet
        feature. The field applies to all pods in the range 0 to
        Replicas-1. That means if there is any unavailable pod in
        the range 0 to Replicas-1, it will be counted towards
        MaxUnavailable.
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("maxUnavailable"),
        )

    @max_unavailable.setter
    def max_unavailable(self, value: typing.Union[str, int, None]):
        """
        The maximum number of pods that can be unavailable during
        the update. Value can be an absolute number (ex: 5) or a
        percentage of desired pods (ex: 10%). Absolute number is
        calculated from percentage by rounding up. This can not be
        0. Defaults to 1. This field is alpha-level and is only
        honored by servers that enable the MaxUnavailableStatefulSet
        feature. The field applies to all pods in the range 0 to
        Replicas-1. That means if there is any unavailable pod in
        the range 0 to Replicas-1, it will be counted towards
        MaxUnavailable.
        """
        self._properties["maxUnavailable"] = _types.integer_or_string(value)

    @property
    def partition(self) -> int:
        """
        Partition indicates the ordinal at which the StatefulSet
        should be partitioned for updates. During a rolling update,
        all pods from ordinal Replicas-1 to Partition are updated.
        All pods from ordinal Partition-1 to 0 remain untouched.
        This is helpful in being able to do a canary based
        deployment. The default value is 0.
        """
        return typing.cast(
            int,
            self._properties.get("partition"),
        )

    @partition.setter
    def partition(self, value: int):
        """
        Partition indicates the ordinal at which the StatefulSet
        should be partitioned for updates. During a rolling update,
        all pods from ordinal Replicas-1 to Partition are updated.
        All pods from ordinal Partition-1 to 0 remain untouched.
        This is helpful in being able to do a canary based
        deployment. The default value is 0.
        """
        self._properties["partition"] = value

    def __enter__(self) -> "RollingUpdateStatefulSetStrategy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSet(_kuber_definitions.Resource):
    """
    StatefulSet represents a set of pods with consistent
    identities. Identities are defined as:
      - Network: A single stable DNS and hostname.
      - Storage: As many VolumeClaims as requested.

    The StatefulSet guarantees that a given network identity
    will always map to the same storage identity.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["StatefulSetSpec"] = None,
        status: typing.Optional["StatefulSetStatus"] = None,
    ):
        """Create StatefulSet instance."""
        super(StatefulSet, self).__init__(api_version="apps/v1", kind="StatefulSet")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else StatefulSetSpec(),
            "status": status if status is not None else StatefulSetStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (StatefulSetSpec, None),
            "status": (StatefulSetStatus, None),
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
    def spec(self) -> "StatefulSetSpec":
        """
        Spec defines the desired identities of pods in this set.
        """
        return typing.cast(
            "StatefulSetSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["StatefulSetSpec", dict]):
        """
        Spec defines the desired identities of pods in this set.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StatefulSetSpec,
                StatefulSetSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "StatefulSetStatus":
        """
        Status is the current status of Pods in this StatefulSet.
        This data may be out of date by some window of time.
        """
        return typing.cast(
            "StatefulSetStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["StatefulSetStatus", dict]):
        """
        Status is the current status of Pods in this StatefulSet.
        This data may be out of date by some window of time.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StatefulSetStatus,
                StatefulSetStatus().from_dict(value),
            )
        self._properties["status"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "StatefulSet":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (c for c in self.spec.template.spec.containers if c.name == name), None
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.template.spec.containers

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StatefulSetStatus":
        """
        Creates the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_stateful_set", "create_stateful_set"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = StatefulSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StatefulSetStatus":
        """
        Replaces the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_stateful_set", "replace_stateful_set"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StatefulSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StatefulSetStatus":
        """
        Patches the StatefulSet in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_stateful_set", "patch_stateful_set"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StatefulSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "StatefulSetStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_stateful_set",
            "read_stateful_set",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = StatefulSetStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the StatefulSet from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_stateful_set",
            "read_stateful_set",
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
        Deletes the StatefulSet from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_stateful_set",
            "delete_stateful_set",
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "StatefulSet":
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
        last_transition_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create StatefulSetCondition instance."""
        super(StatefulSetCondition, self).__init__(
            api_version="apps/v1", kind="StatefulSetCondition"
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
        Last time the condition transitioned from one status to
        another.
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
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        A human readable message indicating details about the
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human readable message indicating details about the
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        The reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        The reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type of statefulset condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of statefulset condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "StatefulSetCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetList(_kuber_definitions.Collection):
    """
    StatefulSetList is a collection of StatefulSets.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["StatefulSet"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create StatefulSetList instance."""
        super(StatefulSetList, self).__init__(
            api_version="apps/v1", kind="StatefulSetList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, StatefulSet),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["StatefulSet"]:
        """
        Items is the list of stateful sets.
        """
        return typing.cast(
            typing.List["StatefulSet"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["StatefulSet"], typing.List[dict]]):
        """
        Items is the list of stateful sets.
        """
        cleaned: typing.List[StatefulSet] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StatefulSet,
                    StatefulSet().from_dict(item),
                )
            cleaned.append(typing.cast(StatefulSet, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list's metadata. More info:
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
        Standard list's metadata. More info:
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
    ) -> "client.AppsV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AppsV1Api(**kwargs)

    def __enter__(self) -> "StatefulSetList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetPersistentVolumeClaimRetentionPolicy(_kuber_definitions.Definition):
    """
    StatefulSetPersistentVolumeClaimRetentionPolicy describes
    the policy used for PVCs created from the StatefulSet
    VolumeClaimTemplates.
    """

    def __init__(
        self,
        when_deleted: typing.Optional[str] = None,
        when_scaled: typing.Optional[str] = None,
    ):
        """Create StatefulSetPersistentVolumeClaimRetentionPolicy instance."""
        super(StatefulSetPersistentVolumeClaimRetentionPolicy, self).__init__(
            api_version="apps/v1",
            kind="StatefulSetPersistentVolumeClaimRetentionPolicy",
        )
        self._properties = {
            "whenDeleted": when_deleted if when_deleted is not None else "",
            "whenScaled": when_scaled if when_scaled is not None else "",
        }
        self._types = {
            "whenDeleted": (str, None),
            "whenScaled": (str, None),
        }

    @property
    def when_deleted(self) -> str:
        """
        WhenDeleted specifies what happens to PVCs created from
        StatefulSet VolumeClaimTemplates when the StatefulSet is
        deleted. The default policy of `Retain` causes PVCs to not
        be affected by StatefulSet deletion. The `Delete` policy
        causes those PVCs to be deleted.
        """
        return typing.cast(
            str,
            self._properties.get("whenDeleted"),
        )

    @when_deleted.setter
    def when_deleted(self, value: str):
        """
        WhenDeleted specifies what happens to PVCs created from
        StatefulSet VolumeClaimTemplates when the StatefulSet is
        deleted. The default policy of `Retain` causes PVCs to not
        be affected by StatefulSet deletion. The `Delete` policy
        causes those PVCs to be deleted.
        """
        self._properties["whenDeleted"] = value

    @property
    def when_scaled(self) -> str:
        """
        WhenScaled specifies what happens to PVCs created from
        StatefulSet VolumeClaimTemplates when the StatefulSet is
        scaled down. The default policy of `Retain` causes PVCs to
        not be affected by a scaledown. The `Delete` policy causes
        the associated PVCs for any excess pods above the replica
        count to be deleted.
        """
        return typing.cast(
            str,
            self._properties.get("whenScaled"),
        )

    @when_scaled.setter
    def when_scaled(self, value: str):
        """
        WhenScaled specifies what happens to PVCs created from
        StatefulSet VolumeClaimTemplates when the StatefulSet is
        scaled down. The default policy of `Retain` causes PVCs to
        not be affected by a scaledown. The `Delete` policy causes
        the associated PVCs for any excess pods above the replica
        count to be deleted.
        """
        self._properties["whenScaled"] = value

    def __enter__(self) -> "StatefulSetPersistentVolumeClaimRetentionPolicy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetSpec(_kuber_definitions.Definition):
    """
    A StatefulSetSpec is the specification of a StatefulSet.
    """

    def __init__(
        self,
        min_ready_seconds: typing.Optional[int] = None,
        persistent_volume_claim_retention_policy: typing.Optional[
            "StatefulSetPersistentVolumeClaimRetentionPolicy"
        ] = None,
        pod_management_policy: typing.Optional[str] = None,
        replicas: typing.Optional[int] = None,
        revision_history_limit: typing.Optional[int] = None,
        selector: typing.Optional["LabelSelector"] = None,
        service_name: typing.Optional[str] = None,
        template: typing.Optional["PodTemplateSpec"] = None,
        update_strategy: typing.Optional["StatefulSetUpdateStrategy"] = None,
        volume_claim_templates: typing.Optional[
            typing.List["PersistentVolumeClaim"]
        ] = None,
    ):
        """Create StatefulSetSpec instance."""
        super(StatefulSetSpec, self).__init__(
            api_version="apps/v1", kind="StatefulSetSpec"
        )
        self._properties = {
            "minReadySeconds": min_ready_seconds
            if min_ready_seconds is not None
            else None,
            "persistentVolumeClaimRetentionPolicy": persistent_volume_claim_retention_policy
            if persistent_volume_claim_retention_policy is not None
            else StatefulSetPersistentVolumeClaimRetentionPolicy(),
            "podManagementPolicy": pod_management_policy
            if pod_management_policy is not None
            else "",
            "replicas": replicas if replicas is not None else None,
            "revisionHistoryLimit": revision_history_limit
            if revision_history_limit is not None
            else None,
            "selector": selector if selector is not None else LabelSelector(),
            "serviceName": service_name if service_name is not None else "",
            "template": template if template is not None else PodTemplateSpec(),
            "updateStrategy": update_strategy
            if update_strategy is not None
            else StatefulSetUpdateStrategy(),
            "volumeClaimTemplates": volume_claim_templates
            if volume_claim_templates is not None
            else [],
        }
        self._types = {
            "minReadySeconds": (int, None),
            "persistentVolumeClaimRetentionPolicy": (
                StatefulSetPersistentVolumeClaimRetentionPolicy,
                None,
            ),
            "podManagementPolicy": (str, None),
            "replicas": (int, None),
            "revisionHistoryLimit": (int, None),
            "selector": (LabelSelector, None),
            "serviceName": (str, None),
            "template": (PodTemplateSpec, None),
            "updateStrategy": (StatefulSetUpdateStrategy, None),
            "volumeClaimTemplates": (list, PersistentVolumeClaim),
        }

    @property
    def min_ready_seconds(self) -> int:
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing for it
        to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready) This is an
        alpha field and requires enabling StatefulSetMinReadySeconds
        feature gate.
        """
        return typing.cast(
            int,
            self._properties.get("minReadySeconds"),
        )

    @min_ready_seconds.setter
    def min_ready_seconds(self, value: int):
        """
        Minimum number of seconds for which a newly created pod
        should be ready without any of its container crashing for it
        to be considered available. Defaults to 0 (pod will be
        considered available as soon as it is ready) This is an
        alpha field and requires enabling StatefulSetMinReadySeconds
        feature gate.
        """
        self._properties["minReadySeconds"] = value

    @property
    def persistent_volume_claim_retention_policy(
        self,
    ) -> "StatefulSetPersistentVolumeClaimRetentionPolicy":
        """
        persistentVolumeClaimRetentionPolicy describes the lifecycle
        of persistent volume claims created from
        volumeClaimTemplates. By default, all persistent volume
        claims are created as needed and retained until manually
        deleted. This policy allows the lifecycle to be altered, for
        example by deleting persistent volume claims when their
        stateful set is deleted, or when their pod is scaled down.
        This requires the StatefulSetAutoDeletePVC feature gate to
        be enabled, which is alpha.  +optional
        """
        return typing.cast(
            "StatefulSetPersistentVolumeClaimRetentionPolicy",
            self._properties.get("persistentVolumeClaimRetentionPolicy"),
        )

    @persistent_volume_claim_retention_policy.setter
    def persistent_volume_claim_retention_policy(
        self,
        value: typing.Union["StatefulSetPersistentVolumeClaimRetentionPolicy", dict],
    ):
        """
        persistentVolumeClaimRetentionPolicy describes the lifecycle
        of persistent volume claims created from
        volumeClaimTemplates. By default, all persistent volume
        claims are created as needed and retained until manually
        deleted. This policy allows the lifecycle to be altered, for
        example by deleting persistent volume claims when their
        stateful set is deleted, or when their pod is scaled down.
        This requires the StatefulSetAutoDeletePVC feature gate to
        be enabled, which is alpha.  +optional
        """
        if isinstance(value, dict):
            value = typing.cast(
                StatefulSetPersistentVolumeClaimRetentionPolicy,
                StatefulSetPersistentVolumeClaimRetentionPolicy().from_dict(value),
            )
        self._properties["persistentVolumeClaimRetentionPolicy"] = value

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
        return typing.cast(
            str,
            self._properties.get("podManagementPolicy"),
        )

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
        self._properties["podManagementPolicy"] = value

    @property
    def replicas(self) -> int:
        """
        replicas is the desired number of replicas of the given
        Template. These are replicas in the sense that they are
        instantiations of the same Template, but individual replicas
        also have a consistent identity. If unspecified, defaults to
        1.
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        replicas is the desired number of replicas of the given
        Template. These are replicas in the sense that they are
        instantiations of the same Template, but individual replicas
        also have a consistent identity. If unspecified, defaults to
        1.
        """
        self._properties["replicas"] = value

    @property
    def revision_history_limit(self) -> int:
        """
        revisionHistoryLimit is the maximum number of revisions that
        will be maintained in the StatefulSet's revision history.
        The revision history consists of all revisions not
        represented by a currently applied StatefulSetSpec version.
        The default value is 10.
        """
        return typing.cast(
            int,
            self._properties.get("revisionHistoryLimit"),
        )

    @revision_history_limit.setter
    def revision_history_limit(self, value: int):
        """
        revisionHistoryLimit is the maximum number of revisions that
        will be maintained in the StatefulSet's revision history.
        The revision history consists of all revisions not
        represented by a currently applied StatefulSetSpec version.
        The default value is 10.
        """
        self._properties["revisionHistoryLimit"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector is a label query over pods that should match the
        replica count. It must match the pod template's labels. More
        info: https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/#label-selectors
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector is a label query over pods that should match the
        replica count. It must match the pod template's labels. More
        info: https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

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
        return typing.cast(
            str,
            self._properties.get("serviceName"),
        )

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
        self._properties["serviceName"] = value

    @property
    def template(self) -> "PodTemplateSpec":
        """
        template is the object that describes the pod that will be
        created if insufficient replicas are detected. Each pod
        stamped out by the StatefulSet will fulfill this Template,
        but have a unique identity from the rest of the StatefulSet.
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        template is the object that describes the pod that will be
        created if insufficient replicas are detected. Each pod
        stamped out by the StatefulSet will fulfill this Template,
        but have a unique identity from the rest of the StatefulSet.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodTemplateSpec,
                PodTemplateSpec().from_dict(value),
            )
        self._properties["template"] = value

    @property
    def update_strategy(self) -> "StatefulSetUpdateStrategy":
        """
        updateStrategy indicates the StatefulSetUpdateStrategy that
        will be employed to update Pods in the StatefulSet when a
        revision is made to Template.
        """
        return typing.cast(
            "StatefulSetUpdateStrategy",
            self._properties.get("updateStrategy"),
        )

    @update_strategy.setter
    def update_strategy(self, value: typing.Union["StatefulSetUpdateStrategy", dict]):
        """
        updateStrategy indicates the StatefulSetUpdateStrategy that
        will be employed to update Pods in the StatefulSet when a
        revision is made to Template.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StatefulSetUpdateStrategy,
                StatefulSetUpdateStrategy().from_dict(value),
            )
        self._properties["updateStrategy"] = value

    @property
    def volume_claim_templates(self) -> typing.List["PersistentVolumeClaim"]:
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
        return typing.cast(
            typing.List["PersistentVolumeClaim"],
            self._properties.get("volumeClaimTemplates"),
        )

    @volume_claim_templates.setter
    def volume_claim_templates(
        self,
        value: typing.Union[typing.List["PersistentVolumeClaim"], typing.List[dict]],
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
        cleaned: typing.List[PersistentVolumeClaim] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PersistentVolumeClaim,
                    PersistentVolumeClaim().from_dict(item),
                )
            cleaned.append(typing.cast(PersistentVolumeClaim, item))
        self._properties["volumeClaimTemplates"] = cleaned

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "StatefulSetSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.template.spec.containers

    def __enter__(self) -> "StatefulSetSpec":
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
        available_replicas: typing.Optional[int] = None,
        collision_count: typing.Optional[int] = None,
        conditions: typing.Optional[typing.List["StatefulSetCondition"]] = None,
        current_replicas: typing.Optional[int] = None,
        current_revision: typing.Optional[str] = None,
        observed_generation: typing.Optional[int] = None,
        ready_replicas: typing.Optional[int] = None,
        replicas: typing.Optional[int] = None,
        update_revision: typing.Optional[str] = None,
        updated_replicas: typing.Optional[int] = None,
    ):
        """Create StatefulSetStatus instance."""
        super(StatefulSetStatus, self).__init__(
            api_version="apps/v1", kind="StatefulSetStatus"
        )
        self._properties = {
            "availableReplicas": available_replicas
            if available_replicas is not None
            else None,
            "collisionCount": collision_count if collision_count is not None else None,
            "conditions": conditions if conditions is not None else [],
            "currentReplicas": current_replicas
            if current_replicas is not None
            else None,
            "currentRevision": current_revision if current_revision is not None else "",
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
            "readyReplicas": ready_replicas if ready_replicas is not None else None,
            "replicas": replicas if replicas is not None else None,
            "updateRevision": update_revision if update_revision is not None else "",
            "updatedReplicas": updated_replicas
            if updated_replicas is not None
            else None,
        }
        self._types = {
            "availableReplicas": (int, None),
            "collisionCount": (int, None),
            "conditions": (list, StatefulSetCondition),
            "currentReplicas": (int, None),
            "currentRevision": (str, None),
            "observedGeneration": (int, None),
            "readyReplicas": (int, None),
            "replicas": (int, None),
            "updateRevision": (str, None),
            "updatedReplicas": (int, None),
        }

    @property
    def available_replicas(self) -> int:
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this statefulset. This is a
        beta field and enabled/disabled by
        StatefulSetMinReadySeconds feature gate.
        """
        return typing.cast(
            int,
            self._properties.get("availableReplicas"),
        )

    @available_replicas.setter
    def available_replicas(self, value: int):
        """
        Total number of available pods (ready for at least
        minReadySeconds) targeted by this statefulset. This is a
        beta field and enabled/disabled by
        StatefulSetMinReadySeconds feature gate.
        """
        self._properties["availableReplicas"] = value

    @property
    def collision_count(self) -> int:
        """
        collisionCount is the count of hash collisions for the
        StatefulSet. The StatefulSet controller uses this field as a
        collision avoidance mechanism when it needs to create the
        name for the newest ControllerRevision.
        """
        return typing.cast(
            int,
            self._properties.get("collisionCount"),
        )

    @collision_count.setter
    def collision_count(self, value: int):
        """
        collisionCount is the count of hash collisions for the
        StatefulSet. The StatefulSet controller uses this field as a
        collision avoidance mechanism when it needs to create the
        name for the newest ControllerRevision.
        """
        self._properties["collisionCount"] = value

    @property
    def conditions(self) -> typing.List["StatefulSetCondition"]:
        """
        Represents the latest available observations of a
        statefulset's current state.
        """
        return typing.cast(
            typing.List["StatefulSetCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[typing.List["StatefulSetCondition"], typing.List[dict]],
    ):
        """
        Represents the latest available observations of a
        statefulset's current state.
        """
        cleaned: typing.List[StatefulSetCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StatefulSetCondition,
                    StatefulSetCondition().from_dict(item),
                )
            cleaned.append(typing.cast(StatefulSetCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def current_replicas(self) -> int:
        """
        currentReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by currentRevision.
        """
        return typing.cast(
            int,
            self._properties.get("currentReplicas"),
        )

    @current_replicas.setter
    def current_replicas(self, value: int):
        """
        currentReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by currentRevision.
        """
        self._properties["currentReplicas"] = value

    @property
    def current_revision(self) -> str:
        """
        currentRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence
        [0,currentReplicas).
        """
        return typing.cast(
            str,
            self._properties.get("currentRevision"),
        )

    @current_revision.setter
    def current_revision(self, value: str):
        """
        currentRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence
        [0,currentReplicas).
        """
        self._properties["currentRevision"] = value

    @property
    def observed_generation(self) -> int:
        """
        observedGeneration is the most recent generation observed
        for this StatefulSet. It corresponds to the StatefulSet's
        generation, which is updated on mutation by the API Server.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        observedGeneration is the most recent generation observed
        for this StatefulSet. It corresponds to the StatefulSet's
        generation, which is updated on mutation by the API Server.
        """
        self._properties["observedGeneration"] = value

    @property
    def ready_replicas(self) -> int:
        """
        readyReplicas is the number of pods created for this
        StatefulSet with a Ready Condition.
        """
        return typing.cast(
            int,
            self._properties.get("readyReplicas"),
        )

    @ready_replicas.setter
    def ready_replicas(self, value: int):
        """
        readyReplicas is the number of pods created for this
        StatefulSet with a Ready Condition.
        """
        self._properties["readyReplicas"] = value

    @property
    def replicas(self) -> int:
        """
        replicas is the number of Pods created by the StatefulSet
        controller.
        """
        return typing.cast(
            int,
            self._properties.get("replicas"),
        )

    @replicas.setter
    def replicas(self, value: int):
        """
        replicas is the number of Pods created by the StatefulSet
        controller.
        """
        self._properties["replicas"] = value

    @property
    def update_revision(self) -> str:
        """
        updateRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence [replicas-
        updatedReplicas,replicas)
        """
        return typing.cast(
            str,
            self._properties.get("updateRevision"),
        )

    @update_revision.setter
    def update_revision(self, value: str):
        """
        updateRevision, if not empty, indicates the version of the
        StatefulSet used to generate Pods in the sequence [replicas-
        updatedReplicas,replicas)
        """
        self._properties["updateRevision"] = value

    @property
    def updated_replicas(self) -> int:
        """
        updatedReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by updateRevision.
        """
        return typing.cast(
            int,
            self._properties.get("updatedReplicas"),
        )

    @updated_replicas.setter
    def updated_replicas(self, value: int):
        """
        updatedReplicas is the number of Pods created by the
        StatefulSet controller from the StatefulSet version
        indicated by updateRevision.
        """
        self._properties["updatedReplicas"] = value

    def __enter__(self) -> "StatefulSetStatus":
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
        rolling_update: typing.Optional["RollingUpdateStatefulSetStrategy"] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create StatefulSetUpdateStrategy instance."""
        super(StatefulSetUpdateStrategy, self).__init__(
            api_version="apps/v1", kind="StatefulSetUpdateStrategy"
        )
        self._properties = {
            "rollingUpdate": rolling_update
            if rolling_update is not None
            else RollingUpdateStatefulSetStrategy(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "rollingUpdate": (RollingUpdateStatefulSetStrategy, None),
            "type": (str, None),
        }

    @property
    def rolling_update(self) -> "RollingUpdateStatefulSetStrategy":
        """
        RollingUpdate is used to communicate parameters when Type is
        RollingUpdateStatefulSetStrategyType.
        """
        return typing.cast(
            "RollingUpdateStatefulSetStrategy",
            self._properties.get("rollingUpdate"),
        )

    @rolling_update.setter
    def rolling_update(
        self, value: typing.Union["RollingUpdateStatefulSetStrategy", dict]
    ):
        """
        RollingUpdate is used to communicate parameters when Type is
        RollingUpdateStatefulSetStrategyType.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RollingUpdateStatefulSetStrategy,
                RollingUpdateStatefulSetStrategy().from_dict(value),
            )
        self._properties["rollingUpdate"] = value

    @property
    def type_(self) -> str:
        """
        Type indicates the type of the StatefulSetUpdateStrategy.
        Default is RollingUpdate.

        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type indicates the type of the StatefulSetUpdateStrategy.
        Default is RollingUpdate.

        """
        self._properties["type"] = value

    def __enter__(self) -> "StatefulSetUpdateStrategy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

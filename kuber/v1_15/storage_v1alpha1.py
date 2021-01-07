import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_15.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_15.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_15.core_v1 import PersistentVolumeSpec  # noqa: F401
from kuber.v1_15.meta_v1 import Status  # noqa: F401
from kuber.v1_15.meta_v1 import StatusDetails  # noqa: F401


class VolumeAttachment(_kuber_definitions.Resource):
    """
    VolumeAttachment captures the intent to attach or detach the
    specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "VolumeAttachmentSpec" = None,
        status: "VolumeAttachmentStatus" = None,
    ):
        """Create VolumeAttachment instance."""
        super(VolumeAttachment, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttachment"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else VolumeAttachmentSpec(),
            "status": status if status is not None else VolumeAttachmentStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (VolumeAttachmentSpec, None),
            "status": (VolumeAttachmentStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "VolumeAttachmentSpec":
        """
        Specification of the desired attach/detach volume behavior.
        Populated by the Kubernetes system.
        """
        return typing.cast(
            "VolumeAttachmentSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["VolumeAttachmentSpec", dict]):
        """
        Specification of the desired attach/detach volume behavior.
        Populated by the Kubernetes system.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentSpec,
                VolumeAttachmentSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "VolumeAttachmentStatus":
        """
        Status of the VolumeAttachment request. Populated by the
        entity completing the attach or detach operation, i.e. the
        external-attacher.
        """
        return typing.cast(
            "VolumeAttachmentStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["VolumeAttachmentStatus", dict]):
        """
        Status of the VolumeAttachment request. Populated by the
        entity completing the attach or detach operation, i.e. the
        external-attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentStatus,
                VolumeAttachmentStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "VolumeAttachmentStatus":
        """
        Creates the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_volume_attachment", "create_volume_attachment"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "VolumeAttachmentStatus":
        """
        Replaces the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_volume_attachment", "replace_volume_attachment"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "VolumeAttachmentStatus":
        """
        Patches the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_volume_attachment", "patch_volume_attachment"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "VolumeAttachmentStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_volume_attachment",
            "read_volume_attachment",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the VolumeAttachment from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_volume_attachment",
            "read_volume_attachment",
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
        Deletes the VolumeAttachment from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_volume_attachment",
            "delete_volume_attachment",
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
    ) -> "client.StorageV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1alpha1Api(**kwargs)

    def __enter__(self) -> "VolumeAttachment":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentList(_kuber_definitions.Collection):
    """
    VolumeAttachmentList is a collection of VolumeAttachment
    objects.
    """

    def __init__(
        self,
        items: typing.List["VolumeAttachment"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create VolumeAttachmentList instance."""
        super(VolumeAttachmentList, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttachmentList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, VolumeAttachment),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["VolumeAttachment"]:
        """
        Items is the list of VolumeAttachments
        """
        return typing.cast(
            typing.List["VolumeAttachment"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["VolumeAttachment"], typing.List[dict]]
    ):
        """
        Items is the list of VolumeAttachments
        """
        cleaned: typing.List[VolumeAttachment] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    VolumeAttachment,
                    VolumeAttachment().from_dict(item),
                )
            cleaned.append(typing.cast(VolumeAttachment, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
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
    ) -> "client.StorageV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1alpha1Api(**kwargs)

    def __enter__(self) -> "VolumeAttachmentList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSource(_kuber_definitions.Definition):
    """
    VolumeAttachmentSource represents a volume that should be
    attached. Right now only PersistenVolumes can be attached
    via external attacher, in future we may allow also inline
    volumes in pods. Exactly one member can be set.
    """

    def __init__(
        self,
        inline_volume_spec: "PersistentVolumeSpec" = None,
        persistent_volume_name: str = None,
    ):
        """Create VolumeAttachmentSource instance."""
        super(VolumeAttachmentSource, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttachmentSource"
        )
        self._properties = {
            "inlineVolumeSpec": inline_volume_spec
            if inline_volume_spec is not None
            else PersistentVolumeSpec(),
            "persistentVolumeName": persistent_volume_name
            if persistent_volume_name is not None
            else "",
        }
        self._types = {
            "inlineVolumeSpec": (PersistentVolumeSpec, None),
            "persistentVolumeName": (str, None),
        }

    @property
    def inline_volume_spec(self) -> "PersistentVolumeSpec":
        """
        inlineVolumeSpec contains all the information necessary to
        attach a persistent volume defined by a pod's inline
        VolumeSource. This field is populated only for the
        CSIMigration feature. It contains translated fields from a
        pod's inline VolumeSource to a PersistentVolumeSpec. This
        field is alpha-level and is only honored by servers that
        enabled the CSIMigration feature.
        """
        return typing.cast(
            "PersistentVolumeSpec",
            self._properties.get("inlineVolumeSpec"),
        )

    @inline_volume_spec.setter
    def inline_volume_spec(self, value: typing.Union["PersistentVolumeSpec", dict]):
        """
        inlineVolumeSpec contains all the information necessary to
        attach a persistent volume defined by a pod's inline
        VolumeSource. This field is populated only for the
        CSIMigration feature. It contains translated fields from a
        pod's inline VolumeSource to a PersistentVolumeSpec. This
        field is alpha-level and is only honored by servers that
        enabled the CSIMigration feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PersistentVolumeSpec,
                PersistentVolumeSpec().from_dict(value),
            )
        self._properties["inlineVolumeSpec"] = value

    @property
    def persistent_volume_name(self) -> str:
        """
        Name of the persistent volume to attach.
        """
        return typing.cast(
            str,
            self._properties.get("persistentVolumeName"),
        )

    @persistent_volume_name.setter
    def persistent_volume_name(self, value: str):
        """
        Name of the persistent volume to attach.
        """
        self._properties["persistentVolumeName"] = value

    def __enter__(self) -> "VolumeAttachmentSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSpec(_kuber_definitions.Definition):
    """
    VolumeAttachmentSpec is the specification of a
    VolumeAttachment request.
    """

    def __init__(
        self,
        attacher: str = None,
        node_name: str = None,
        source: "VolumeAttachmentSource" = None,
    ):
        """Create VolumeAttachmentSpec instance."""
        super(VolumeAttachmentSpec, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttachmentSpec"
        )
        self._properties = {
            "attacher": attacher if attacher is not None else "",
            "nodeName": node_name if node_name is not None else "",
            "source": source if source is not None else VolumeAttachmentSource(),
        }
        self._types = {
            "attacher": (str, None),
            "nodeName": (str, None),
            "source": (VolumeAttachmentSource, None),
        }

    @property
    def attacher(self) -> str:
        """
        Attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        return typing.cast(
            str,
            self._properties.get("attacher"),
        )

    @attacher.setter
    def attacher(self, value: str):
        """
        Attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        self._properties["attacher"] = value

    @property
    def node_name(self) -> str:
        """
        The node that the volume should be attached to.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        The node that the volume should be attached to.
        """
        self._properties["nodeName"] = value

    @property
    def source(self) -> "VolumeAttachmentSource":
        """
        Source represents the volume that should be attached.
        """
        return typing.cast(
            "VolumeAttachmentSource",
            self._properties.get("source"),
        )

    @source.setter
    def source(self, value: typing.Union["VolumeAttachmentSource", dict]):
        """
        Source represents the volume that should be attached.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentSource,
                VolumeAttachmentSource().from_dict(value),
            )
        self._properties["source"] = value

    def __enter__(self) -> "VolumeAttachmentSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentStatus(_kuber_definitions.Definition):
    """
    VolumeAttachmentStatus is the status of a VolumeAttachment
    request.
    """

    def __init__(
        self,
        attach_error: "VolumeError" = None,
        attached: bool = None,
        attachment_metadata: dict = None,
        detach_error: "VolumeError" = None,
    ):
        """Create VolumeAttachmentStatus instance."""
        super(VolumeAttachmentStatus, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeAttachmentStatus"
        )
        self._properties = {
            "attachError": attach_error if attach_error is not None else VolumeError(),
            "attached": attached if attached is not None else None,
            "attachmentMetadata": attachment_metadata
            if attachment_metadata is not None
            else {},
            "detachError": detach_error if detach_error is not None else VolumeError(),
        }
        self._types = {
            "attachError": (VolumeError, None),
            "attached": (bool, None),
            "attachmentMetadata": (dict, None),
            "detachError": (VolumeError, None),
        }

    @property
    def attach_error(self) -> "VolumeError":
        """
        The last error encountered during attach operation, if any.
        This field must only be set by the entity completing the
        attach operation, i.e. the external-attacher.
        """
        return typing.cast(
            "VolumeError",
            self._properties.get("attachError"),
        )

    @attach_error.setter
    def attach_error(self, value: typing.Union["VolumeError", dict]):
        """
        The last error encountered during attach operation, if any.
        This field must only be set by the entity completing the
        attach operation, i.e. the external-attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeError,
                VolumeError().from_dict(value),
            )
        self._properties["attachError"] = value

    @property
    def attached(self) -> bool:
        """
        Indicates the volume is successfully attached. This field
        must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        return typing.cast(
            bool,
            self._properties.get("attached"),
        )

    @attached.setter
    def attached(self, value: bool):
        """
        Indicates the volume is successfully attached. This field
        must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        self._properties["attached"] = value

    @property
    def attachment_metadata(self) -> dict:
        """
        Upon successful attach, this field is populated with any
        information returned by the attach operation that must be
        passed into subsequent WaitForAttach or Mount calls. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        return typing.cast(
            dict,
            self._properties.get("attachmentMetadata"),
        )

    @attachment_metadata.setter
    def attachment_metadata(self, value: dict):
        """
        Upon successful attach, this field is populated with any
        information returned by the attach operation that must be
        passed into subsequent WaitForAttach or Mount calls. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        self._properties["attachmentMetadata"] = value

    @property
    def detach_error(self) -> "VolumeError":
        """
        The last error encountered during detach operation, if any.
        This field must only be set by the entity completing the
        detach operation, i.e. the external-attacher.
        """
        return typing.cast(
            "VolumeError",
            self._properties.get("detachError"),
        )

    @detach_error.setter
    def detach_error(self, value: typing.Union["VolumeError", dict]):
        """
        The last error encountered during detach operation, if any.
        This field must only be set by the entity completing the
        detach operation, i.e. the external-attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeError,
                VolumeError().from_dict(value),
            )
        self._properties["detachError"] = value

    def __enter__(self) -> "VolumeAttachmentStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeError(_kuber_definitions.Definition):
    """
    VolumeError captures an error encountered during a volume
    operation.
    """

    def __init__(
        self,
        message: str = None,
        time: str = None,
    ):
        """Create VolumeError instance."""
        super(VolumeError, self).__init__(
            api_version="storage/v1alpha1", kind="VolumeError"
        )
        self._properties = {
            "message": message if message is not None else "",
            "time": time if time is not None else None,
        }
        self._types = {
            "message": (str, None),
            "time": (str, None),
        }

    @property
    def message(self) -> str:
        """
        String detailing the error encountered during Attach or
        Detach operation. This string maybe logged, so it should not
        contain sensitive information.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        String detailing the error encountered during Attach or
        Detach operation. This string maybe logged, so it should not
        contain sensitive information.
        """
        self._properties["message"] = value

    @property
    def time(self) -> str:
        """
        Time the error was encountered.
        """
        return typing.cast(
            str,
            self._properties.get("time"),
        )

    @time.setter
    def time(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        Time the error was encountered.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["time"] = value

    def __enter__(self) -> "VolumeError":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

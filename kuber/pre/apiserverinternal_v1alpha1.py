import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.pre.meta_v1 import ListMeta
from kuber.pre.meta_v1 import ObjectMeta
from kuber.pre.meta_v1 import Status
from kuber.pre.meta_v1 import StatusDetails


class ServerStorageVersion(_kuber_definitions.Definition):
    """
    An API server instance reports the version it can decode and
    the version it encodes objects to when persisting objects in
    the backend.
    """

    def __init__(
        self,
        api_server_id: str = None,
        decodable_versions: typing.List[str] = None,
        encoding_version: str = None,
    ):
        """Create ServerStorageVersion instance."""
        super(ServerStorageVersion, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="ServerStorageVersion"
        )
        self._properties = {
            "apiServerID": api_server_id if api_server_id is not None else "",
            "decodableVersions": decodable_versions
            if decodable_versions is not None
            else [],
            "encodingVersion": encoding_version if encoding_version is not None else "",
        }
        self._types = {
            "apiServerID": (str, None),
            "decodableVersions": (list, str),
            "encodingVersion": (str, None),
        }

    @property
    def api_server_id(self) -> str:
        """
        The ID of the reporting API server.
        """
        return typing.cast(
            str,
            self._properties.get("apiServerID"),
        )

    @api_server_id.setter
    def api_server_id(self, value: str):
        """
        The ID of the reporting API server.
        """
        self._properties["apiServerID"] = value

    @property
    def decodable_versions(self) -> typing.List[str]:
        """
        The API server can decode objects encoded in these versions.
        The encodingVersion must be included in the
        decodableVersions.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("decodableVersions"),
        )

    @decodable_versions.setter
    def decodable_versions(self, value: typing.List[str]):
        """
        The API server can decode objects encoded in these versions.
        The encodingVersion must be included in the
        decodableVersions.
        """
        self._properties["decodableVersions"] = value

    @property
    def encoding_version(self) -> str:
        """
        The API server encodes the object to this version when
        persisting it in the backend (e.g., etcd).
        """
        return typing.cast(
            str,
            self._properties.get("encodingVersion"),
        )

    @encoding_version.setter
    def encoding_version(self, value: str):
        """
        The API server encodes the object to this version when
        persisting it in the backend (e.g., etcd).
        """
        self._properties["encodingVersion"] = value

    def __enter__(self) -> "ServerStorageVersion":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersion(_kuber_definitions.Resource):
    """

    Storage version of a specific resource.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "StorageVersionSpec" = None,
        status: "StorageVersionStatus" = None,
    ):
        """Create StorageVersion instance."""
        super(StorageVersion, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="StorageVersion"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else StorageVersionSpec(),
            "status": status if status is not None else StorageVersionStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (StorageVersionSpec, None),
            "status": (StorageVersionStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        The name is <group>.<resource>.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        The name is <group>.<resource>.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "StorageVersionSpec":
        """
        Spec is an empty spec. It is here to comply with Kubernetes
        API style.
        """
        return typing.cast(
            "StorageVersionSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["StorageVersionSpec", dict]):
        """
        Spec is an empty spec. It is here to comply with Kubernetes
        API style.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StorageVersionSpec,
                StorageVersionSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "StorageVersionStatus":
        """
        API server instances report the version they can decode and
        the version they encode objects to when persisting objects
        in the backend.
        """
        return typing.cast(
            "StorageVersionStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["StorageVersionStatus", dict]):
        """
        API server instances report the version they can decode and
        the version they encode objects to when persisting objects
        in the backend.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StorageVersionStatus,
                StorageVersionStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "StorageVersionStatus":
        """
        Creates the StorageVersion in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_storage_version", "create_storage_version"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = StorageVersionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "StorageVersionStatus":
        """
        Replaces the StorageVersion in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_storage_version", "replace_storage_version"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StorageVersionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "StorageVersionStatus":
        """
        Patches the StorageVersion in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_storage_version", "patch_storage_version"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StorageVersionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "StorageVersionStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_storage_version", "read_storage_version"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = StorageVersionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the StorageVersion from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_storage_version",
            "read_storage_version",
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
        Deletes the StorageVersion from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_storage_version",
            "delete_storage_version",
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
    ) -> "client.ApiserverinternalV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiserverinternalV1alpha1Api(**kwargs)

    def __enter__(self) -> "StorageVersion":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionCondition(_kuber_definitions.Definition):
    """
    Describes the state of the storageVersion at a certain
    point.
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        observed_generation: int = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create StorageVersionCondition instance."""
        super(StorageVersionCondition, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="StorageVersionCondition"
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "message": message if message is not None else "",
            "observedGeneration": observed_generation
            if observed_generation is not None
            else None,
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "observedGeneration": (int, None),
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
    def observed_generation(self) -> int:
        """
        If set, this represents the .metadata.generation that the
        condition was set based upon.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        If set, this represents the .metadata.generation that the
        condition was set based upon.
        """
        self._properties["observedGeneration"] = value

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
        Type of the condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of the condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "StorageVersionCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionList(_kuber_definitions.Collection):
    """
    A list of StorageVersions.
    """

    def __init__(
        self,
        items: typing.List["StorageVersion"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create StorageVersionList instance."""
        super(StorageVersionList, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="StorageVersionList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, StorageVersion),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["StorageVersion"]:
        """"""
        return typing.cast(
            typing.List["StorageVersion"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["StorageVersion"], typing.List[dict]]
    ):
        """"""
        cleaned: typing.List[StorageVersion] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StorageVersion,
                    StorageVersion().from_dict(item),
                )
            cleaned.append(typing.cast(StorageVersion, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """"""
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.ApiserverinternalV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiserverinternalV1alpha1Api(**kwargs)

    def __enter__(self) -> "StorageVersionList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionSpec(_kuber_definitions.Definition):
    """
    StorageVersionSpec is an empty spec.
    """

    def __init__(
        self,
    ):
        """Create StorageVersionSpec instance."""
        super(StorageVersionSpec, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="StorageVersionSpec"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "StorageVersionSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionStatus(_kuber_definitions.Definition):
    """
    API server instances report the versions they can decode and
    the version they encode objects to when persisting objects
    in the backend.
    """

    def __init__(
        self,
        common_encoding_version: str = None,
        conditions: typing.List["StorageVersionCondition"] = None,
        storage_versions: typing.List["ServerStorageVersion"] = None,
    ):
        """Create StorageVersionStatus instance."""
        super(StorageVersionStatus, self).__init__(
            api_version="apiserverinternal/v1alpha1", kind="StorageVersionStatus"
        )
        self._properties = {
            "commonEncodingVersion": common_encoding_version
            if common_encoding_version is not None
            else "",
            "conditions": conditions if conditions is not None else [],
            "storageVersions": storage_versions if storage_versions is not None else [],
        }
        self._types = {
            "commonEncodingVersion": (str, None),
            "conditions": (list, StorageVersionCondition),
            "storageVersions": (list, ServerStorageVersion),
        }

    @property
    def common_encoding_version(self) -> str:
        """
        If all API server instances agree on the same encoding
        storage version, then this field is set to that version.
        Otherwise this field is left empty. API servers should
        finish updating its storageVersionStatus entry before
        serving write operations, so that this field will be in sync
        with the reality.
        """
        return typing.cast(
            str,
            self._properties.get("commonEncodingVersion"),
        )

    @common_encoding_version.setter
    def common_encoding_version(self, value: str):
        """
        If all API server instances agree on the same encoding
        storage version, then this field is set to that version.
        Otherwise this field is left empty. API servers should
        finish updating its storageVersionStatus entry before
        serving write operations, so that this field will be in sync
        with the reality.
        """
        self._properties["commonEncodingVersion"] = value

    @property
    def conditions(self) -> typing.List["StorageVersionCondition"]:
        """
        The latest available observations of the storageVersion's
        state.
        """
        return typing.cast(
            typing.List["StorageVersionCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[typing.List["StorageVersionCondition"], typing.List[dict]],
    ):
        """
        The latest available observations of the storageVersion's
        state.
        """
        cleaned: typing.List[StorageVersionCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StorageVersionCondition,
                    StorageVersionCondition().from_dict(item),
                )
            cleaned.append(typing.cast(StorageVersionCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def storage_versions(self) -> typing.List["ServerStorageVersion"]:
        """
        The reported versions per API server instance.
        """
        return typing.cast(
            typing.List["ServerStorageVersion"],
            self._properties.get("storageVersions"),
        )

    @storage_versions.setter
    def storage_versions(
        self,
        value: typing.Union[typing.List["ServerStorageVersion"], typing.List[dict]],
    ):
        """
        The reported versions per API server instance.
        """
        cleaned: typing.List[ServerStorageVersion] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ServerStorageVersion,
                    ServerStorageVersion().from_dict(item),
                )
            cleaned.append(typing.cast(ServerStorageVersion, item))
        self._properties["storageVersions"] = cleaned

    def __enter__(self) -> "StorageVersionStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

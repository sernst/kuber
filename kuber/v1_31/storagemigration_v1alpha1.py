import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_31.meta_v1 import Status  # noqa: F401
from kuber.v1_31.meta_v1 import StatusDetails  # noqa: F401


class GroupVersionResource(_kuber_definitions.Definition):
    """
    The names of the group, the version, and the resource.
    """

    def __init__(
        self,
        group: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
    ):
        """Create GroupVersionResource instance."""
        super(GroupVersionResource, self).__init__(
            api_version="storagemigration/v1alpha1", kind="GroupVersionResource"
        )
        self._properties = {
            "group": group if group is not None else "",
            "resource": resource if resource is not None else "",
            "version": version if version is not None else "",
        }
        self._types = {
            "group": (str, None),
            "resource": (str, None),
            "version": (str, None),
        }

    @property
    def group(self) -> str:
        """
        The name of the group.
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        The name of the group.
        """
        self._properties["group"] = value

    @property
    def resource(self) -> str:
        """
        The name of the resource.
        """
        return typing.cast(
            str,
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: str):
        """
        The name of the resource.
        """
        self._properties["resource"] = value

    @property
    def version(self) -> str:
        """
        The name of the version.
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        The name of the version.
        """
        self._properties["version"] = value

    def __enter__(self) -> "GroupVersionResource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MigrationCondition(_kuber_definitions.Definition):
    """
    Describes the state of a migration at a certain point.
    """

    def __init__(
        self,
        last_update_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create MigrationCondition instance."""
        super(MigrationCondition, self).__init__(
            api_version="storagemigration/v1alpha1", kind="MigrationCondition"
        )
        self._properties = {
            "lastUpdateTime": (
                last_update_time if last_update_time is not None else None
            ),
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastUpdateTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

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

    def __enter__(self) -> "MigrationCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionMigration(_kuber_definitions.Resource):
    """
    StorageVersionMigration represents a migration of stored
    data to the latest storage version.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["StorageVersionMigrationSpec"] = None,
        status: typing.Optional["StorageVersionMigrationStatus"] = None,
    ):
        """Create StorageVersionMigration instance."""
        super(StorageVersionMigration, self).__init__(
            api_version="storagemigration/v1alpha1", kind="StorageVersionMigration"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else StorageVersionMigrationSpec(),
            "status": status if status is not None else StorageVersionMigrationStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (StorageVersionMigrationSpec, None),
            "status": (StorageVersionMigrationStatus, None),
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
    def spec(self) -> "StorageVersionMigrationSpec":
        """
        Specification of the migration.
        """
        return typing.cast(
            "StorageVersionMigrationSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["StorageVersionMigrationSpec", dict]):
        """
        Specification of the migration.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StorageVersionMigrationSpec,
                StorageVersionMigrationSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "StorageVersionMigrationStatus":
        """
        Status of the migration.
        """
        return typing.cast(
            "StorageVersionMigrationStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["StorageVersionMigrationStatus", dict]):
        """
        Status of the migration.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StorageVersionMigrationStatus,
                StorageVersionMigrationStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StorageVersionMigrationStatus":
        """
        Creates the StorageVersionMigration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_storage_version_migration",
            "create_storage_version_migration",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = StorageVersionMigrationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StorageVersionMigrationStatus":
        """
        Replaces the StorageVersionMigration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_storage_version_migration",
            "replace_storage_version_migration",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StorageVersionMigrationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "StorageVersionMigrationStatus":
        """
        Patches the StorageVersionMigration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_storage_version_migration",
            "patch_storage_version_migration",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = StorageVersionMigrationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "StorageVersionMigrationStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_storage_version_migration",
            "read_storage_version_migration",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = StorageVersionMigrationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the StorageVersionMigration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_storage_version_migration",
            "read_storage_version_migration",
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
        Deletes the StorageVersionMigration from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_storage_version_migration",
            "delete_storage_version_migration",
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
    ) -> "client.StoragemigrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StoragemigrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "StorageVersionMigration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionMigrationList(_kuber_definitions.Collection):
    """
    StorageVersionMigrationList is a collection of storage
    version migrations.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["StorageVersionMigration"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create StorageVersionMigrationList instance."""
        super(StorageVersionMigrationList, self).__init__(
            api_version="storagemigration/v1alpha1", kind="StorageVersionMigrationList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, StorageVersionMigration),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["StorageVersionMigration"]:
        """
        Items is the list of StorageVersionMigration
        """
        return typing.cast(
            typing.List["StorageVersionMigration"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["StorageVersionMigration"], typing.List[dict]],
    ):
        """
        Items is the list of StorageVersionMigration
        """
        cleaned: typing.List[StorageVersionMigration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StorageVersionMigration,
                    StorageVersionMigration().from_dict(item),
                )
            cleaned.append(typing.cast(StorageVersionMigration, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
    ) -> "client.StoragemigrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StoragemigrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "StorageVersionMigrationList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionMigrationSpec(_kuber_definitions.Definition):
    """
    Spec of the storage version migration.
    """

    def __init__(
        self,
        continue_token: typing.Optional[str] = None,
        resource: typing.Optional["GroupVersionResource"] = None,
    ):
        """Create StorageVersionMigrationSpec instance."""
        super(StorageVersionMigrationSpec, self).__init__(
            api_version="storagemigration/v1alpha1", kind="StorageVersionMigrationSpec"
        )
        self._properties = {
            "continueToken": continue_token if continue_token is not None else "",
            "resource": resource if resource is not None else GroupVersionResource(),
        }
        self._types = {
            "continueToken": (str, None),
            "resource": (GroupVersionResource, None),
        }

    @property
    def continue_token(self) -> str:
        """
        The token used in the list options to get the next chunk of
        objects to migrate. When the .status.conditions indicates
        the migration is "Running", users can use this token to
        check the progress of the migration.
        """
        return typing.cast(
            str,
            self._properties.get("continueToken"),
        )

    @continue_token.setter
    def continue_token(self, value: str):
        """
        The token used in the list options to get the next chunk of
        objects to migrate. When the .status.conditions indicates
        the migration is "Running", users can use this token to
        check the progress of the migration.
        """
        self._properties["continueToken"] = value

    @property
    def resource(self) -> "GroupVersionResource":
        """
        The resource that is being migrated. The migrator sends
        requests to the endpoint serving the resource. Immutable.
        """
        return typing.cast(
            "GroupVersionResource",
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: typing.Union["GroupVersionResource", dict]):
        """
        The resource that is being migrated. The migrator sends
        requests to the endpoint serving the resource. Immutable.
        """
        if isinstance(value, dict):
            value = typing.cast(
                GroupVersionResource,
                GroupVersionResource().from_dict(value),
            )
        self._properties["resource"] = value

    def __enter__(self) -> "StorageVersionMigrationSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageVersionMigrationStatus(_kuber_definitions.Definition):
    """
    Status of the storage version migration.
    """

    def __init__(
        self,
        conditions: typing.Optional[typing.List["MigrationCondition"]] = None,
        resource_version: typing.Optional[str] = None,
    ):
        """Create StorageVersionMigrationStatus instance."""
        super(StorageVersionMigrationStatus, self).__init__(
            api_version="storagemigration/v1alpha1",
            kind="StorageVersionMigrationStatus",
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
            "resourceVersion": resource_version if resource_version is not None else "",
        }
        self._types = {
            "conditions": (list, MigrationCondition),
            "resourceVersion": (str, None),
        }

    @property
    def conditions(self) -> typing.List["MigrationCondition"]:
        """
        The latest available observations of the migration's current
        state.
        """
        return typing.cast(
            typing.List["MigrationCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["MigrationCondition"], typing.List[dict]]
    ):
        """
        The latest available observations of the migration's current
        state.
        """
        cleaned: typing.List[MigrationCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MigrationCondition,
                    MigrationCondition().from_dict(item),
                )
            cleaned.append(typing.cast(MigrationCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def resource_version(self) -> str:
        """
        ResourceVersion to compare with the GC cache for performing
        the migration. This is the current resource version of given
        group, version and resource when kube-controller-manager
        first observes this StorageVersionMigration resource.
        """
        return typing.cast(
            str,
            self._properties.get("resourceVersion"),
        )

    @resource_version.setter
    def resource_version(self, value: str):
        """
        ResourceVersion to compare with the GC cache for performing
        the migration. This is the current resource version of given
        group, version and resource when kube-controller-manager
        first observes this StorageVersionMigration resource.
        """
        self._properties["resourceVersion"] = value

    def __enter__(self) -> "StorageVersionMigrationStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

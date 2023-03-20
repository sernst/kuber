import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_24.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_24.meta_v1 import ObjectMeta  # noqa: F401


class PriorityClass(_kuber_definitions.Resource):
    """
    PriorityClass defines mapping from a priority class name to
    the priority integer value. The value can be any valid
    integer.
    """

    def __init__(
        self,
        description: typing.Optional[str] = None,
        global_default: typing.Optional[bool] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        preemption_policy: typing.Optional[str] = None,
        value: typing.Optional[int] = None,
    ):
        """Create PriorityClass instance."""
        super(PriorityClass, self).__init__(
            api_version="scheduling/v1", kind="PriorityClass"
        )
        self._properties = {
            "description": description if description is not None else "",
            "globalDefault": global_default if global_default is not None else None,
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "preemptionPolicy": preemption_policy
            if preemption_policy is not None
            else "",
            "value": value if value is not None else None,
        }
        self._types = {
            "apiVersion": (str, None),
            "description": (str, None),
            "globalDefault": (bool, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "preemptionPolicy": (str, None),
            "value": (int, None),
        }

    @property
    def description(self) -> str:
        """
        description is an arbitrary string that usually provides
        guidelines on when this priority class should be used.
        """
        return typing.cast(
            str,
            self._properties.get("description"),
        )

    @description.setter
    def description(self, value: str):
        """
        description is an arbitrary string that usually provides
        guidelines on when this priority class should be used.
        """
        self._properties["description"] = value

    @property
    def global_default(self) -> bool:
        """
        globalDefault specifies whether this PriorityClass should be
        considered as the default priority for pods that do not have
        any priority class. Only one PriorityClass can be marked as
        `globalDefault`. However, if more than one PriorityClasses
        exists with their `globalDefault` field set to true, the
        smallest value of such global default PriorityClasses will
        be used as the default priority.
        """
        return typing.cast(
            bool,
            self._properties.get("globalDefault"),
        )

    @global_default.setter
    def global_default(self, value: bool):
        """
        globalDefault specifies whether this PriorityClass should be
        considered as the default priority for pods that do not have
        any priority class. Only one PriorityClass can be marked as
        `globalDefault`. However, if more than one PriorityClasses
        exists with their `globalDefault` field set to true, the
        smallest value of such global default PriorityClasses will
        be used as the default priority.
        """
        self._properties["globalDefault"] = value

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
    def preemption_policy(self) -> str:
        """
        PreemptionPolicy is the Policy for preempting pods with
        lower priority. One of Never, PreemptLowerPriority. Defaults
        to PreemptLowerPriority if unset.
        """
        return typing.cast(
            str,
            self._properties.get("preemptionPolicy"),
        )

    @preemption_policy.setter
    def preemption_policy(self, value: str):
        """
        PreemptionPolicy is the Policy for preempting pods with
        lower priority. One of Never, PreemptLowerPriority. Defaults
        to PreemptLowerPriority if unset.
        """
        self._properties["preemptionPolicy"] = value

    @property
    def value(self) -> int:
        """
        The value of this priority class. This is the actual
        priority that pods receive when they have the name of this
        class in their pod spec.
        """
        return typing.cast(
            int,
            self._properties.get("value"),
        )

    @value.setter
    def value(self, value: int):
        """
        The value of this priority class. This is the actual
        priority that pods receive when they have the name of this
        class in their pod spec.
        """
        self._properties["value"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_priority_class", "create_priority_class"]

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
        Replaces the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_priority_class", "replace_priority_class"]

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
        Patches the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_priority_class", "patch_priority_class"]

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
        Reads the PriorityClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_priority_class",
            "read_priority_class",
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
        Deletes the PriorityClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_priority_class",
            "delete_priority_class",
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
    ) -> "client.SchedulingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.SchedulingV1Api(**kwargs)

    def __enter__(self) -> "PriorityClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityClassList(_kuber_definitions.Collection):
    """
    PriorityClassList is a collection of priority classes.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["PriorityClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create PriorityClassList instance."""
        super(PriorityClassList, self).__init__(
            api_version="scheduling/v1", kind="PriorityClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PriorityClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PriorityClass"]:
        """
        items is the list of PriorityClasses
        """
        return typing.cast(
            typing.List["PriorityClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["PriorityClass"], typing.List[dict]]
    ):
        """
        items is the list of PriorityClasses
        """
        cleaned: typing.List[PriorityClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PriorityClass,
                    PriorityClass().from_dict(item),
                )
            cleaned.append(typing.cast(PriorityClass, item))
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
    ) -> "client.SchedulingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.SchedulingV1Api(**kwargs)

    def __enter__(self) -> "PriorityClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

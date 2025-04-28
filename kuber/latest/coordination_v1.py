import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.latest.meta_v1 import ListMeta  # noqa: F401
from kuber.latest.meta_v1 import MicroTime  # noqa: F401
from kuber.latest.meta_v1 import ObjectMeta  # noqa: F401


class Lease(_kuber_definitions.Resource):
    """
    Lease defines a lease concept.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["LeaseSpec"] = None,
    ):
        """Create Lease instance."""
        super(Lease, self).__init__(api_version="coordination/v1", kind="Lease")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else LeaseSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (LeaseSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        More info:
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
        More info:
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
    def spec(self) -> "LeaseSpec":
        """
        spec contains the specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "LeaseSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["LeaseSpec", dict]):
        """
        spec contains the specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                LeaseSpec,
                LeaseSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the Lease in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_lease", "create_lease"]

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
        Replaces the Lease in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_lease", "replace_lease"]

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
        Patches the Lease in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_lease", "patch_lease"]

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
        Reads the Lease from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_lease",
            "read_lease",
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
        Deletes the Lease from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_lease",
            "delete_lease",
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
    ) -> "client.CoordinationApi":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CoordinationApi(**kwargs)

    def __enter__(self) -> "Lease":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseList(_kuber_definitions.Collection):
    """
    LeaseList is a list of Lease objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["Lease"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create LeaseList instance."""
        super(LeaseList, self).__init__(api_version="coordination/v1", kind="LeaseList")
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Lease),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Lease"]:
        """
        items is a list of schema objects.
        """
        return typing.cast(
            typing.List["Lease"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Lease"], typing.List[dict]]):
        """
        items is a list of schema objects.
        """
        cleaned: typing.List[Lease] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Lease,
                    Lease().from_dict(item),
                )
            cleaned.append(typing.cast(Lease, item))
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
    ) -> "client.CoordinationApi":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CoordinationApi(**kwargs)

    def __enter__(self) -> "LeaseList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseSpec(_kuber_definitions.Definition):
    """
    LeaseSpec is a specification of a Lease.
    """

    def __init__(
        self,
        acquire_time: typing.Optional["MicroTime"] = None,
        holder_identity: typing.Optional[str] = None,
        lease_duration_seconds: typing.Optional[int] = None,
        lease_transitions: typing.Optional[int] = None,
        preferred_holder: typing.Optional[str] = None,
        renew_time: typing.Optional["MicroTime"] = None,
        strategy: typing.Optional[str] = None,
    ):
        """Create LeaseSpec instance."""
        super(LeaseSpec, self).__init__(api_version="coordination/v1", kind="LeaseSpec")
        self._properties = {
            "acquireTime": acquire_time if acquire_time is not None else MicroTime(),
            "holderIdentity": holder_identity if holder_identity is not None else "",
            "leaseDurationSeconds": (
                lease_duration_seconds if lease_duration_seconds is not None else None
            ),
            "leaseTransitions": (
                lease_transitions if lease_transitions is not None else None
            ),
            "preferredHolder": preferred_holder if preferred_holder is not None else "",
            "renewTime": renew_time if renew_time is not None else MicroTime(),
            "strategy": strategy if strategy is not None else "",
        }
        self._types = {
            "acquireTime": (MicroTime, None),
            "holderIdentity": (str, None),
            "leaseDurationSeconds": (int, None),
            "leaseTransitions": (int, None),
            "preferredHolder": (str, None),
            "renewTime": (MicroTime, None),
            "strategy": (str, None),
        }

    @property
    def acquire_time(self) -> "MicroTime":
        """
        acquireTime is a time when the current lease was acquired.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("acquireTime"),
        )

    @acquire_time.setter
    def acquire_time(self, value: typing.Union["MicroTime", dict]):
        """
        acquireTime is a time when the current lease was acquired.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["acquireTime"] = value

    @property
    def holder_identity(self) -> str:
        """
        holderIdentity contains the identity of the holder of a
        current lease. If Coordinated Leader Election is used, the
        holder identity must be equal to the elected
        LeaseCandidate.metadata.name field.
        """
        return typing.cast(
            str,
            self._properties.get("holderIdentity"),
        )

    @holder_identity.setter
    def holder_identity(self, value: str):
        """
        holderIdentity contains the identity of the holder of a
        current lease. If Coordinated Leader Election is used, the
        holder identity must be equal to the elected
        LeaseCandidate.metadata.name field.
        """
        self._properties["holderIdentity"] = value

    @property
    def lease_duration_seconds(self) -> int:
        """
        leaseDurationSeconds is a duration that candidates for a
        lease need to wait to force acquire it. This is measured
        against the time of last observed renewTime.
        """
        return typing.cast(
            int,
            self._properties.get("leaseDurationSeconds"),
        )

    @lease_duration_seconds.setter
    def lease_duration_seconds(self, value: int):
        """
        leaseDurationSeconds is a duration that candidates for a
        lease need to wait to force acquire it. This is measured
        against the time of last observed renewTime.
        """
        self._properties["leaseDurationSeconds"] = value

    @property
    def lease_transitions(self) -> int:
        """
        leaseTransitions is the number of transitions of a lease
        between holders.
        """
        return typing.cast(
            int,
            self._properties.get("leaseTransitions"),
        )

    @lease_transitions.setter
    def lease_transitions(self, value: int):
        """
        leaseTransitions is the number of transitions of a lease
        between holders.
        """
        self._properties["leaseTransitions"] = value

    @property
    def preferred_holder(self) -> str:
        """
        PreferredHolder signals to a lease holder that the lease has
        a more optimal holder and should be given up. This field can
        only be set if Strategy is also set.
        """
        return typing.cast(
            str,
            self._properties.get("preferredHolder"),
        )

    @preferred_holder.setter
    def preferred_holder(self, value: str):
        """
        PreferredHolder signals to a lease holder that the lease has
        a more optimal holder and should be given up. This field can
        only be set if Strategy is also set.
        """
        self._properties["preferredHolder"] = value

    @property
    def renew_time(self) -> "MicroTime":
        """
        renewTime is a time when the current holder of a lease has
        last updated the lease.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("renewTime"),
        )

    @renew_time.setter
    def renew_time(self, value: typing.Union["MicroTime", dict]):
        """
        renewTime is a time when the current holder of a lease has
        last updated the lease.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["renewTime"] = value

    @property
    def strategy(self) -> str:
        """
        Strategy indicates the strategy for picking the leader for
        coordinated leader election. If the field is not specified,
        there is no active coordination for this lease. (Alpha)
        Using this field requires the CoordinatedLeaderElection
        feature gate to be enabled.
        """
        return typing.cast(
            str,
            self._properties.get("strategy"),
        )

    @strategy.setter
    def strategy(self, value: str):
        """
        Strategy indicates the strategy for picking the leader for
        coordinated leader election. If the field is not specified,
        there is no active coordination for this lease. (Alpha)
        Using this field requires the CoordinatedLeaderElection
        feature gate to be enabled.
        """
        self._properties["strategy"] = value

    def __enter__(self) -> "LeaseSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

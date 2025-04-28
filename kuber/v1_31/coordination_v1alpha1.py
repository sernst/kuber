import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.meta_v1 import MicroTime  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401


class LeaseCandidate(_kuber_definitions.Resource):
    """
    LeaseCandidate defines a candidate for a Lease object.
    Candidates are created such that coordinated leader election
    will pick the best leader from the list of candidates.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["LeaseCandidateSpec"] = None,
    ):
        """Create LeaseCandidate instance."""
        super(LeaseCandidate, self).__init__(
            api_version="coordination/v1alpha1", kind="LeaseCandidate"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else LeaseCandidateSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (LeaseCandidateSpec, None),
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
    def spec(self) -> "LeaseCandidateSpec":
        """
        spec contains the specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "LeaseCandidateSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["LeaseCandidateSpec", dict]):
        """
        spec contains the specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                LeaseCandidateSpec,
                LeaseCandidateSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the LeaseCandidate in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_lease_candidate", "create_lease_candidate"]

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
        Replaces the LeaseCandidate in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_lease_candidate", "replace_lease_candidate"]

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
        Patches the LeaseCandidate in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_lease_candidate", "patch_lease_candidate"]

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
        Reads the LeaseCandidate from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_lease_candidate",
            "read_lease_candidate",
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
        Deletes the LeaseCandidate from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_lease_candidate",
            "delete_lease_candidate",
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
    ) -> "client.CoordinationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CoordinationV1alpha1Api(**kwargs)

    def __enter__(self) -> "LeaseCandidate":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseCandidateList(_kuber_definitions.Collection):
    """
    LeaseCandidateList is a list of Lease objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["LeaseCandidate"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create LeaseCandidateList instance."""
        super(LeaseCandidateList, self).__init__(
            api_version="coordination/v1alpha1", kind="LeaseCandidateList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, LeaseCandidate),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["LeaseCandidate"]:
        """
        items is a list of schema objects.
        """
        return typing.cast(
            typing.List["LeaseCandidate"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["LeaseCandidate"], typing.List[dict]]
    ):
        """
        items is a list of schema objects.
        """
        cleaned: typing.List[LeaseCandidate] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    LeaseCandidate,
                    LeaseCandidate().from_dict(item),
                )
            cleaned.append(typing.cast(LeaseCandidate, item))
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
    ) -> "client.CoordinationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CoordinationV1alpha1Api(**kwargs)

    def __enter__(self) -> "LeaseCandidateList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseCandidateSpec(_kuber_definitions.Definition):
    """
    LeaseCandidateSpec is a specification of a Lease.
    """

    def __init__(
        self,
        binary_version: typing.Optional[str] = None,
        emulation_version: typing.Optional[str] = None,
        lease_name: typing.Optional[str] = None,
        ping_time: typing.Optional["MicroTime"] = None,
        preferred_strategies: typing.Optional[typing.List[str]] = None,
        renew_time: typing.Optional["MicroTime"] = None,
    ):
        """Create LeaseCandidateSpec instance."""
        super(LeaseCandidateSpec, self).__init__(
            api_version="coordination/v1alpha1", kind="LeaseCandidateSpec"
        )
        self._properties = {
            "binaryVersion": binary_version if binary_version is not None else "",
            "emulationVersion": (
                emulation_version if emulation_version is not None else ""
            ),
            "leaseName": lease_name if lease_name is not None else "",
            "pingTime": ping_time if ping_time is not None else MicroTime(),
            "preferredStrategies": (
                preferred_strategies if preferred_strategies is not None else []
            ),
            "renewTime": renew_time if renew_time is not None else MicroTime(),
        }
        self._types = {
            "binaryVersion": (str, None),
            "emulationVersion": (str, None),
            "leaseName": (str, None),
            "pingTime": (MicroTime, None),
            "preferredStrategies": (list, str),
            "renewTime": (MicroTime, None),
        }

    @property
    def binary_version(self) -> str:
        """
        BinaryVersion is the binary version. It must be in a semver
        format without leading `v`. This field is required when
        strategy is "OldestEmulationVersion"
        """
        return typing.cast(
            str,
            self._properties.get("binaryVersion"),
        )

    @binary_version.setter
    def binary_version(self, value: str):
        """
        BinaryVersion is the binary version. It must be in a semver
        format without leading `v`. This field is required when
        strategy is "OldestEmulationVersion"
        """
        self._properties["binaryVersion"] = value

    @property
    def emulation_version(self) -> str:
        """
        EmulationVersion is the emulation version. It must be in a
        semver format without leading `v`. EmulationVersion must be
        less than or equal to BinaryVersion. This field is required
        when strategy is "OldestEmulationVersion"
        """
        return typing.cast(
            str,
            self._properties.get("emulationVersion"),
        )

    @emulation_version.setter
    def emulation_version(self, value: str):
        """
        EmulationVersion is the emulation version. It must be in a
        semver format without leading `v`. EmulationVersion must be
        less than or equal to BinaryVersion. This field is required
        when strategy is "OldestEmulationVersion"
        """
        self._properties["emulationVersion"] = value

    @property
    def lease_name(self) -> str:
        """
        LeaseName is the name of the lease for which this candidate
        is contending. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("leaseName"),
        )

    @lease_name.setter
    def lease_name(self, value: str):
        """
        LeaseName is the name of the lease for which this candidate
        is contending. This field is immutable.
        """
        self._properties["leaseName"] = value

    @property
    def ping_time(self) -> "MicroTime":
        """
        PingTime is the last time that the server has requested the
        LeaseCandidate to renew. It is only done during leader
        election to check if any LeaseCandidates have become
        ineligible. When PingTime is updated, the LeaseCandidate
        will respond by updating RenewTime.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("pingTime"),
        )

    @ping_time.setter
    def ping_time(self, value: typing.Union["MicroTime", dict]):
        """
        PingTime is the last time that the server has requested the
        LeaseCandidate to renew. It is only done during leader
        election to check if any LeaseCandidates have become
        ineligible. When PingTime is updated, the LeaseCandidate
        will respond by updating RenewTime.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["pingTime"] = value

    @property
    def preferred_strategies(self) -> typing.List[str]:
        """
        PreferredStrategies indicates the list of strategies for
        picking the leader for coordinated leader election. The list
        is ordered, and the first strategy supersedes all other
        strategies. The list is used by coordinated leader election
        to make a decision about the final election strategy. This
        follows as - If all clients have strategy X as the first
        element in this list, strategy X will be used. - If a
        candidate has strategy [X] and another candidate has
        strategy [Y, X], Y supersedes X and strategy Y
          will be used.
        - If a candidate has strategy [X, Y] and another candidate
        has strategy [Y, X], this is a user error and leader
          election will not operate the Lease until resolved.
        (Alpha) Using this field requires the
        CoordinatedLeaderElection feature gate to be enabled.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("preferredStrategies"),
        )

    @preferred_strategies.setter
    def preferred_strategies(self, value: typing.List[str]):
        """
        PreferredStrategies indicates the list of strategies for
        picking the leader for coordinated leader election. The list
        is ordered, and the first strategy supersedes all other
        strategies. The list is used by coordinated leader election
        to make a decision about the final election strategy. This
        follows as - If all clients have strategy X as the first
        element in this list, strategy X will be used. - If a
        candidate has strategy [X] and another candidate has
        strategy [Y, X], Y supersedes X and strategy Y
          will be used.
        - If a candidate has strategy [X, Y] and another candidate
        has strategy [Y, X], this is a user error and leader
          election will not operate the Lease until resolved.
        (Alpha) Using this field requires the
        CoordinatedLeaderElection feature gate to be enabled.
        """
        self._properties["preferredStrategies"] = value

    @property
    def renew_time(self) -> "MicroTime":
        """
        RenewTime is the time that the LeaseCandidate was last
        updated. Any time a Lease needs to do leader election, the
        PingTime field is updated to signal to the LeaseCandidate
        that they should update the RenewTime. Old LeaseCandidate
        objects are also garbage collected if it has been hours
        since the last renew. The PingTime field is updated
        regularly to prevent garbage collection for still active
        LeaseCandidates.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("renewTime"),
        )

    @renew_time.setter
    def renew_time(self, value: typing.Union["MicroTime", dict]):
        """
        RenewTime is the time that the LeaseCandidate was last
        updated. Any time a Lease needs to do leader election, the
        PingTime field is updated to signal to the LeaseCandidate
        that they should update the RenewTime. Old LeaseCandidate
        objects are also garbage collected if it has been hours
        since the last renew. The PingTime field is updated
        regularly to prevent garbage collection for still active
        LeaseCandidates.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["renewTime"] = value

    def __enter__(self) -> "LeaseCandidateSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

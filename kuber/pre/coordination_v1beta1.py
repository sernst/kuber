import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.pre.meta_v1 import ListMeta
from kuber.pre.meta_v1 import MicroTime
from kuber.pre.meta_v1 import ObjectMeta


class Lease(_kuber_definitions.Resource):
    """
    Lease defines a lease concept.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'LeaseSpec' = None,
    ):
        """Create Lease instance."""
        super(Lease, self).__init__(
            api_version='coordination/v1beta1',
            kind='Lease'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or LeaseSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (LeaseSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'LeaseSpec':
        """
        Specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['LeaseSpec', dict]):
        """
        Specification of the Lease. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = LeaseSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the Lease in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_lease',
            'create_lease'
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
        Replaces the Lease in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_lease',
            'replace_lease'
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
        Patches the Lease in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_lease',
            'patch_lease'
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
        Reads the Lease from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_lease',
            'read_lease'
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
        Deletes the Lease from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_lease',
            'delete_lease'
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
    ) -> 'client.CoordinationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoordinationV1beta1Api(**kwargs)

    def __enter__(self) -> 'Lease':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseList(_kuber_definitions.Collection):
    """
    LeaseList is a list of Lease objects.
    """

    def __init__(
            self,
            items: typing.List['Lease'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create LeaseList instance."""
        super(LeaseList, self).__init__(
            api_version='coordination/v1beta1',
            kind='LeaseList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Lease),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Lease']:
        """
        Items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Lease'], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Lease().from_dict(item)
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
    ) -> 'client.CoordinationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.CoordinationV1beta1Api(**kwargs)

    def __enter__(self) -> 'LeaseList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LeaseSpec(_kuber_definitions.Definition):
    """
    LeaseSpec is a specification of a Lease.
    """

    def __init__(
            self,
            acquire_time: 'MicroTime' = None,
            holder_identity: str = None,
            lease_duration_seconds: int = None,
            lease_transitions: int = None,
            renew_time: 'MicroTime' = None,
    ):
        """Create LeaseSpec instance."""
        super(LeaseSpec, self).__init__(
            api_version='coordination/v1beta1',
            kind='LeaseSpec'
        )
        self._properties = {
            'acquireTime': acquire_time or MicroTime(),
            'holderIdentity': holder_identity or '',
            'leaseDurationSeconds': lease_duration_seconds or None,
            'leaseTransitions': lease_transitions or None,
            'renewTime': renew_time or MicroTime(),

        }
        self._types = {
            'acquireTime': (MicroTime, None),
            'holderIdentity': (str, None),
            'leaseDurationSeconds': (int, None),
            'leaseTransitions': (int, None),
            'renewTime': (MicroTime, None),

        }

    @property
    def acquire_time(self) -> 'MicroTime':
        """
        acquireTime is a time when the current lease was acquired.
        """
        return self._properties.get('acquireTime')

    @acquire_time.setter
    def acquire_time(self, value: typing.Union['MicroTime', dict]):
        """
        acquireTime is a time when the current lease was acquired.
        """
        if isinstance(value, dict):
            value = MicroTime().from_dict(value)
        self._properties['acquireTime'] = value

    @property
    def holder_identity(self) -> str:
        """
        holderIdentity contains the identity of the holder of a
        current lease.
        """
        return self._properties.get('holderIdentity')

    @holder_identity.setter
    def holder_identity(self, value: str):
        """
        holderIdentity contains the identity of the holder of a
        current lease.
        """
        self._properties['holderIdentity'] = value

    @property
    def lease_duration_seconds(self) -> int:
        """
        leaseDurationSeconds is a duration that candidates for a
        lease need to wait to force acquire it. This is measure
        against time of last observed RenewTime.
        """
        return self._properties.get('leaseDurationSeconds')

    @lease_duration_seconds.setter
    def lease_duration_seconds(self, value: int):
        """
        leaseDurationSeconds is a duration that candidates for a
        lease need to wait to force acquire it. This is measure
        against time of last observed RenewTime.
        """
        self._properties['leaseDurationSeconds'] = value

    @property
    def lease_transitions(self) -> int:
        """
        leaseTransitions is the number of transitions of a lease
        between holders.
        """
        return self._properties.get('leaseTransitions')

    @lease_transitions.setter
    def lease_transitions(self, value: int):
        """
        leaseTransitions is the number of transitions of a lease
        between holders.
        """
        self._properties['leaseTransitions'] = value

    @property
    def renew_time(self) -> 'MicroTime':
        """
        renewTime is a time when the current holder of a lease has
        last updated the lease.
        """
        return self._properties.get('renewTime')

    @renew_time.setter
    def renew_time(self, value: typing.Union['MicroTime', dict]):
        """
        renewTime is a time when the current holder of a lease has
        last updated the lease.
        """
        if isinstance(value, dict):
            value = MicroTime().from_dict(value)
        self._properties['renewTime'] = value

    def __enter__(self) -> 'LeaseSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

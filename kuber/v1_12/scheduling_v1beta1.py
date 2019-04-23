import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_12.meta_v1 import ListMeta
from kuber.v1_12.meta_v1 import ObjectMeta


class PriorityClass(_kuber_definitions.Resource):
    """
    PriorityClass defines mapping from a priority class name to
    the priority integer value. The value can be any valid
    integer.
    """

    def __init__(
            self,
            description: str = None,
            global_default: bool = None,
            metadata: 'ObjectMeta' = None,
            value: int = None,
    ):
        """Create PriorityClass instance."""
        super(PriorityClass, self).__init__(
            api_version='scheduling/v1beta1',
            kind='PriorityClass'
        )
        self._properties = {
            'description': description or '',
            'globalDefault': global_default or None,
            'metadata': metadata or ObjectMeta(),
            'value': value or None,

        }
        self._types = {
            'apiVersion': (str, None),
            'description': (str, None),
            'globalDefault': (bool, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'value': (int, None),

        }

    @property
    def description(self) -> str:
        """
        description is an arbitrary string that usually provides
        guidelines on when this priority class should be used.
        """
        return self._properties.get('description')

    @description.setter
    def description(self, value: str):
        """
        description is an arbitrary string that usually provides
        guidelines on when this priority class should be used.
        """
        self._properties['description'] = value

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
        return self._properties.get('globalDefault')

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
        self._properties['globalDefault'] = value

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
    def value(self) -> int:
        """
        The value of this priority class. This is the actual
        priority that pods receive when they have the name of this
        class in their pod spec.
        """
        return self._properties.get('value')

    @value.setter
    def value(self, value: int):
        """
        The value of this priority class. This is the actual
        priority that pods receive when they have the name of this
        class in their pod spec.
        """
        self._properties['value'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_priority_class',
            'create_priority_class'
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
        Replaces the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_priority_class',
            'replace_priority_class'
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
        Patches the PriorityClass in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_priority_class',
            'patch_priority_class'
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
        Reads the PriorityClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_priority_class',
            'read_priority_class'
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
        Deletes the PriorityClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_priority_class',
            'delete_priority_class'
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
    ) -> 'client.SchedulingV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.SchedulingV1beta1Api(**kwargs)

    def __enter__(self) -> 'PriorityClass':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityClassList(_kuber_definitions.Collection):
    """
    PriorityClassList is a collection of priority classes.
    """

    def __init__(
            self,
            items: typing.List['PriorityClass'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PriorityClassList instance."""
        super(PriorityClassList, self).__init__(
            api_version='scheduling/v1beta1',
            kind='PriorityClassList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PriorityClass),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PriorityClass']:
        """
        items is the list of PriorityClasses
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PriorityClass'], typing.List[dict]]
    ):
        """
        items is the list of PriorityClasses
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PriorityClass().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata More info:
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
    ) -> 'client.SchedulingV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.SchedulingV1beta1Api(**kwargs)

    def __enter__(self) -> 'PriorityClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

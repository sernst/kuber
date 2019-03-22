import typing

from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ListMeta
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ObjectMeta


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
            api_version='scheduling/v1',
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

    def create_resource(self, namespace: 'str' = None) -> bool:
        """
        Creates the PriorityClass in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PriorityClass was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the PriorityClass in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PriorityClass was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the PriorityClass from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'PriorityClass':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityClassList(_kuber_definitions.Resource):
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
            api_version='scheduling/v1',
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

    def create_resource(self, namespace: 'str' = None) -> bool:
        """
        Creates the PriorityClassList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PriorityClassList was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the PriorityClassList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PriorityClassList was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the PriorityClassList from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'PriorityClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

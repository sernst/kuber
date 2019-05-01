import typing

from kuber import management
from kuber.management import creation


class ResourceKindArray:
    """
    A flexible accessor class for interacting with Kubernetes resources
    within a bundle that have been filtered by kind from a parent
    ResourceArray.
    """

    def __init__(self, array: 'ResourceArray', kind: str):
        """
        Creates a ResourceKindArray instance that filters on the specified
        Kubernetes resource kind.
        """
        self._kind = _to_pascal_case(kind)
        self._array = array

    @property
    def _resources(self) -> typing.Tuple['creation.ResourceSubclass', ...]:
        """Internal dynamic resource filtering based on the source array."""
        return tuple([
            r
            for r in getattr(self._array, '_resources')
            if r.kind == self._kind
        ])

    def to_list(self) -> typing.List['creation.ResourceSubclass']:
        """Returns the resources in this object as a standard Python list."""
        return list(self._resources)

    def _get_resources(self, name: str):
        """Internal filtering function to retrieve matching resources."""
        value = _to_kebab_case(name)
        matches = [r for r in self._resources if r.metadata.name == value]
        if len(matches) == 0:
            raise ValueError(f'Not found {self._kind}/{value}')

        return matches

    def __len__(self) -> int:
        """Number of matching resources."""
        return len(self._resources)

    def __getitem__(self, item: typing.Union[str, int]) -> typing.Union[
            'creation.ResourceSubclass',
            typing.Tuple['creation.ResourceSubclass', ...]
    ]:
        """
        Retrieves either a single resource of a tuple of resources
        with the matching name depending on the number of matches found if
        the item argument is a string. If the item argument is an integer,
        the matching resource with that index will be returned.
        """
        if isinstance(item, int):
            return self._resources[item]

        resources = self._get_resources(item)
        return tuple(resources) if len(resources) > 1 else resources[0]

    def __getattr__(self, item: str) -> typing.Union[
            'creation.ResourceSubclass',
            typing.Tuple['creation.ResourceSubclass', ...]
    ]:
        """
        Retrieves either a single resource of a tuple of resources
        with the matching name depending on the number of matches found.
        """
        resources = self._get_resources(item)
        return tuple(resources) if len(resources) > 1 else resources[0]


class ResourceArray:
    """
    A flexible accessor class for interacting with Kubernetes resources
    within a bundle.
    """

    def __init__(
            self,
            bundle: 'management.ResourceBundle',
            namespace: str = None
    ):
        """
        Creates a ResourceArray for the given bundle and with an optional
        namespace filter.
        """
        self._bundle = bundle
        self._namespace = namespace

    @property
    def _resources(self) -> typing.Tuple['creation.ResourceSubclass', ...]:
        """Internal dynamic resource filtering based on the source bundle."""
        namespace = self._namespace
        resources = getattr(self._bundle, '_resources')
        return tuple([
            r
            for r in resources
            if not namespace or r.metadata.namespace == namespace
        ])

    def to_list(self) -> typing.List['creation.ResourceSubclass']:
        """Returns the resources in this object as a standard Python list."""
        return list(self._resources)

    def within(self, namespace: str) -> 'ResourceArray':
        """
        Filters this array down to only include resources of the specified
        kind.
        """
        return ResourceArray(self._bundle, namespace)

    def __len__(self):
        """Number of resources in this array."""
        return len(self._resources)

    def __getitem__(self, item: typing.Union[int, str]):
        """
        If the item is an int, it will return that resource from the filtered
        list. If a string, it will return a ResourceKindArray that is
        constrained by the type of resource identified by the item argument.
        """
        if isinstance(item, int):
            return self._resources[item]

        return ResourceKindArray(self, item)

    def __getattr__(self, item: str):
        """A filtered array of resources of the matching kind."""
        return ResourceKindArray(self, item)


def _to_pascal_case(value: str) -> str:
    """Converts a snake_case string into a PascalCase one."""
    value = value.replace('-', '_')
    if value.find('_') == -1:
        return value[0].upper() + value[1:]
    return ''.join([v.capitalize() for v in value.split('_')])


def _to_kebab_case(value: str) -> str:
    """Converts a snake_case string into a kebab-case one."""
    return value.replace('_', '-').lower()

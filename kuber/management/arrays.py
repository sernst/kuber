import typing
import fnmatch

from kuber import management
from kuber.management import creation


def _matcher(value: typing.Optional[str], pattern: str) -> bool:
    """Returns the case insensitive matching parameter."""
    return fnmatch.fnmatch((value or "").lower(), (pattern or "*").lower())


def _matches_filter(
    resource: "creation.ResourceSubclass",
    resource_filter: str,
) -> bool:
    """Returns whether or not the resource matches the filter."""
    parts = resource_filter.split("/")

    name_filter = parts[-1]
    if not _matcher(resource.metadata.name, name_filter):
        return False

    kind_filter = parts[-2] if len(parts) > 1 else "*"
    if not _matcher(resource.kind, kind_filter):
        return False

    namespace_filter = parts[-3] if len(parts) > 2 else "*"
    if not _matcher(resource.metadata.namespace, namespace_filter):
        return False

    return True


def _is_matching_resource(
    resource: "creation.ResourceSubclass", filters: typing.List[str] = None
) -> bool:
    """
    Determines whether or not a given resource matches the specified
    filters. If filters is None or an empty list, all resources will
    match.
    """
    return not filters or any((_matches_filter(resource, f) for f in filters))


class ResourceKindArray:
    """
    A flexible accessor class for interacting with Kubernetes resources
    within a bundle that have been filtered by kind from a parent
    ResourceArray.
    """

    def __init__(
        self,
        array: "ResourceArray",
        kind: str,
        filters: typing.List[str] = None,
    ):
        """
        Creates a ResourceKindArray instance that filters on the specified
        Kubernetes resource kind.
        """
        self._kind = _to_pascal_case(kind)
        self._array = array
        self._filters = filters

    @property
    def _resources(self) -> typing.Tuple["creation.ResourceSubclass", ...]:
        """Internal dynamic resource filtering based on the source array."""
        return tuple(
            [
                r
                for r in getattr(self._array, "_resources")
                if r.kind == self._kind and _is_matching_resource(r, self._filters)
            ]
        )

    def to_list(self) -> typing.List["creation.ResourceSubclass"]:
        """Returns the resources in this object as a standard Python list."""
        return list(self._resources)

    def _get_resources(
        self,
        name: str,
    ) -> typing.List["creation.ResourceSubclass"]:
        """Internal filtering function to retrieve matching resources."""
        value = _to_kebab_case(name)
        matches = [r for r in self._resources if r.metadata.name == value]
        if len(matches) == 0:
            raise ValueError(f"Not found {self._kind}/{value}")

        return matches

    def __len__(self) -> int:
        """Number of matching resources."""
        return len(self._resources)

    def __getitem__(
        self, item: typing.Union[str, int]
    ) -> typing.Union[
        "creation.ResourceSubclass", typing.Tuple["creation.ResourceSubclass", ...]
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

    def __getattr__(
        self, item: str
    ) -> typing.Union[
        "creation.ResourceSubclass", typing.Tuple["creation.ResourceSubclass", ...]
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
        bundle: "management.ResourceBundle",
        namespace: str = None,
        filters: typing.List[str] = None,
    ):
        """
        Creates a ResourceArray for the given bundle and with an optional
        namespace filter.
        """
        self._bundle = bundle
        self._namespace = namespace
        self._filters = filters

    @property
    def _resources(self) -> typing.Tuple["creation.ResourceSubclass", ...]:
        """Internal dynamic resource filtering based on the source bundle."""
        namespace = self._namespace
        resources = getattr(self._bundle, "_resources")
        return tuple(
            [
                r
                for r in resources
                if (not namespace or r.metadata.namespace == namespace)
                and _is_matching_resource(r, self._filters)
            ]
        )

    def to_list(self) -> typing.List["creation.ResourceSubclass"]:
        """Returns the resources in this object as a standard Python list."""
        return list(self._resources)

    def within(self, namespace: str) -> "ResourceArray":
        """
        Filters this array down to only include resources of the specified
        kind.
        """
        return ResourceArray(self._bundle, namespace, self._filters)

    def matching(self, *args: str) -> "ResourceArray":
        """
        Filters this array down to only include resources that match at
        least one of the specified filter args. Filters are of the form

        - ``<NAMESPACE>/<KIND>/<NAME>``
        - ``<KIND>/<NAME>``
        - ``<NAME>``

        and can include shell-style wildcard characters. The filters are
        also case-insensitive. For example, the filter ``deployment/foo-*``
        would match all Deployments in the array that begin with the name
        ``foo-`` but could be ``foo-bar`` or ``foo-spam`` or so on.

        :param args:
            One or more filters to specify that will be used to return a
            ResourceArray containing only the resources that match at least
            one of the specified filters.
        :return:
            A ResourceArray that contains the subset of resources
            that match the specified filters from this source ResourceArray.
        """
        return ResourceArray(
            bundle=self._bundle,
            namespace=self._namespace,
            filters=list(self._filters or []) + (list(args) or []),
        )

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

        return ResourceKindArray(self, item, self._filters)

    def __getattr__(self, item: str):
        """A filtered array of resources of the matching kind."""
        return ResourceKindArray(self, item, self._filters)

    def __iter__(self):
        """Iterable form of the available resources."""
        return (r for r in self._resources)


def _to_pascal_case(value: str) -> str:
    """Converts a snake_case string into a PascalCase one."""
    value = value.replace("-", "_")
    if value.find("_") == -1:
        return value[0].upper() + value[1:]
    return "".join([v.capitalize() for v in value.split("_")])


def _to_kebab_case(value: str) -> str:
    """Converts a snake_case string into a kebab-case one."""
    return value.replace("_", "-").lower()

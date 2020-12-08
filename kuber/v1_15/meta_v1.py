import typing
import datetime as _datetime

from kubernetes import client

from kuber import definitions as _kuber_definitions
from kuber.v1_15.apimachinery_runtime import RawExtension


class APIGroup(_kuber_definitions.Definition):
    """
    APIGroup contains the name, the supported versions, and the
    preferred version of a group.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        preferred_version: "GroupVersionForDiscovery" = None,
        server_address_by_client_cidrs: typing.List["ServerAddressByClientCIDR"] = None,
        versions: typing.List["GroupVersionForDiscovery"] = None,
    ):
        """Create APIGroup instance."""
        super(APIGroup, self).__init__(api_version="meta/v1", kind="APIGroup")
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "preferredVersion": preferred_version
            if preferred_version is not None
            else GroupVersionForDiscovery(),
            "serverAddressByClientCIDRs": server_address_by_client_cidrs
            if server_address_by_client_cidrs is not None
            else [],
            "versions": versions if versions is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "preferredVersion": (GroupVersionForDiscovery, None),
            "serverAddressByClientCIDRs": (list, ServerAddressByClientCIDR),
            "versions": (list, GroupVersionForDiscovery),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        name is the name of the group.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the group.
        """
        self._properties["name"] = value

    @property
    def preferred_version(self) -> "GroupVersionForDiscovery":
        """
        preferredVersion is the version preferred by the API server,
        which probably is the storage version.
        """
        return typing.cast(
            "GroupVersionForDiscovery",
            self._properties.get("preferredVersion"),
        )

    @preferred_version.setter
    def preferred_version(self, value: typing.Union["GroupVersionForDiscovery", dict]):
        """
        preferredVersion is the version preferred by the API server,
        which probably is the storage version.
        """
        if isinstance(value, dict):
            value = typing.cast(
                GroupVersionForDiscovery,
                GroupVersionForDiscovery().from_dict(value),
            )
        self._properties["preferredVersion"] = value

    @property
    def server_address_by_client_cidrs(
        self,
    ) -> typing.List["ServerAddressByClientCIDR"]:
        """
        a map of client CIDR to server address that is serving this
        group. This is to help clients reach servers in the most
        network-efficient way possible. Clients can use the
        appropriate server address as per the CIDR that they match.
        In case of multiple matches, clients should use the longest
        matching CIDR. The server returns only those CIDRs that it
        thinks that the client can match. For example: the master
        will return an internal IP CIDR only, if the client reaches
        the server using an internal IP. Server looks at
        X-Forwarded-For header or X-Real-Ip header or
        request.RemoteAddr (in that order) to get the client IP.
        """
        return typing.cast(
            typing.List["ServerAddressByClientCIDR"],
            self._properties.get("serverAddressByClientCIDRs"),
        )

    @server_address_by_client_cidrs.setter
    def server_address_by_client_cidrs(
        self,
        value: typing.Union[
            typing.List["ServerAddressByClientCIDR"], typing.List[dict]
        ],
    ):
        """
        a map of client CIDR to server address that is serving this
        group. This is to help clients reach servers in the most
        network-efficient way possible. Clients can use the
        appropriate server address as per the CIDR that they match.
        In case of multiple matches, clients should use the longest
        matching CIDR. The server returns only those CIDRs that it
        thinks that the client can match. For example: the master
        will return an internal IP CIDR only, if the client reaches
        the server using an internal IP. Server looks at
        X-Forwarded-For header or X-Real-Ip header or
        request.RemoteAddr (in that order) to get the client IP.
        """
        cleaned: typing.List[ServerAddressByClientCIDR] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ServerAddressByClientCIDR,
                    ServerAddressByClientCIDR().from_dict(item),
                )
            cleaned.append(typing.cast(ServerAddressByClientCIDR, item))
        self._properties["serverAddressByClientCIDRs"] = cleaned

    @property
    def versions(self) -> typing.List["GroupVersionForDiscovery"]:
        """
        versions are the versions supported in this group.
        """
        return typing.cast(
            typing.List["GroupVersionForDiscovery"],
            self._properties.get("versions"),
        )

    @versions.setter
    def versions(
        self,
        value: typing.Union[typing.List["GroupVersionForDiscovery"], typing.List[dict]],
    ):
        """
        versions are the versions supported in this group.
        """
        cleaned: typing.List[GroupVersionForDiscovery] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    GroupVersionForDiscovery,
                    GroupVersionForDiscovery().from_dict(item),
                )
            cleaned.append(typing.cast(GroupVersionForDiscovery, item))
        self._properties["versions"] = cleaned

    def __enter__(self) -> "APIGroup":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIGroupList(_kuber_definitions.Definition):
    """
    APIGroupList is a list of APIGroup, to allow clients to
    discover the API at /apis.
    """

    def __init__(
        self,
        api_version: str = None,
        groups: typing.List["APIGroup"] = None,
        kind: str = None,
    ):
        """Create APIGroupList instance."""
        super(APIGroupList, self).__init__(api_version="meta/v1", kind="APIGroupList")
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "groups": groups if groups is not None else [],
            "kind": kind if kind is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "groups": (list, APIGroup),
            "kind": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def groups(self) -> typing.List["APIGroup"]:
        """
        groups is a list of APIGroup.
        """
        return typing.cast(
            typing.List["APIGroup"],
            self._properties.get("groups"),
        )

    @groups.setter
    def groups(self, value: typing.Union[typing.List["APIGroup"], typing.List[dict]]):
        """
        groups is a list of APIGroup.
        """
        cleaned: typing.List[APIGroup] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    APIGroup,
                    APIGroup().from_dict(item),
                )
            cleaned.append(typing.cast(APIGroup, item))
        self._properties["groups"] = cleaned

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    def __enter__(self) -> "APIGroupList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIResource(_kuber_definitions.Definition):
    """
    APIResource specifies the name of a resource and whether it
    is namespaced.
    """

    def __init__(
        self,
        categories: typing.List[str] = None,
        group: str = None,
        kind: str = None,
        name: str = None,
        namespaced: bool = None,
        short_names: typing.List[str] = None,
        singular_name: str = None,
        storage_version_hash: str = None,
        verbs: typing.List[str] = None,
        version: str = None,
    ):
        """Create APIResource instance."""
        super(APIResource, self).__init__(api_version="meta/v1", kind="APIResource")
        self._properties = {
            "categories": categories if categories is not None else [],
            "group": group if group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "namespaced": namespaced if namespaced is not None else None,
            "shortNames": short_names if short_names is not None else [],
            "singularName": singular_name if singular_name is not None else "",
            "storageVersionHash": storage_version_hash
            if storage_version_hash is not None
            else "",
            "verbs": verbs if verbs is not None else [],
            "version": version if version is not None else "",
        }
        self._types = {
            "categories": (list, str),
            "group": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "namespaced": (bool, None),
            "shortNames": (list, str),
            "singularName": (str, None),
            "storageVersionHash": (str, None),
            "verbs": (list, str),
            "version": (str, None),
        }

    @property
    def categories(self) -> typing.List[str]:
        """
        categories is a list of the grouped resources this resource
        belongs to (e.g. 'all')
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("categories"),
        )

    @categories.setter
    def categories(self, value: typing.List[str]):
        """
        categories is a list of the grouped resources this resource
        belongs to (e.g. 'all')
        """
        self._properties["categories"] = value

    @property
    def group(self) -> str:
        """
        group is the preferred group of the resource.  Empty implies
        the group of the containing resource list. For subresources,
        this may have a different value, for example: Scale".
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        group is the preferred group of the resource.  Empty implies
        the group of the containing resource list. For subresources,
        this may have a different value, for example: Scale".
        """
        self._properties["group"] = value

    @property
    def kind(self) -> str:
        """
        kind is the kind for the resource (e.g. 'Foo' is the kind
        for a resource 'foo')
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        kind is the kind for the resource (e.g. 'Foo' is the kind
        for a resource 'foo')
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        name is the plural name of the resource.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the plural name of the resource.
        """
        self._properties["name"] = value

    @property
    def namespaced(self) -> bool:
        """
        namespaced indicates if a resource is namespaced or not.
        """
        return typing.cast(
            bool,
            self._properties.get("namespaced"),
        )

    @namespaced.setter
    def namespaced(self, value: bool):
        """
        namespaced indicates if a resource is namespaced or not.
        """
        self._properties["namespaced"] = value

    @property
    def short_names(self) -> typing.List[str]:
        """
        shortNames is a list of suggested short names of the
        resource.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("shortNames"),
        )

    @short_names.setter
    def short_names(self, value: typing.List[str]):
        """
        shortNames is a list of suggested short names of the
        resource.
        """
        self._properties["shortNames"] = value

    @property
    def singular_name(self) -> str:
        """
        singularName is the singular name of the resource.  This
        allows clients to handle plural and singular opaquely. The
        singularName is more correct for reporting status on a
        single item and both singular and plural are allowed from
        the kubectl CLI interface.
        """
        return typing.cast(
            str,
            self._properties.get("singularName"),
        )

    @singular_name.setter
    def singular_name(self, value: str):
        """
        singularName is the singular name of the resource.  This
        allows clients to handle plural and singular opaquely. The
        singularName is more correct for reporting status on a
        single item and both singular and plural are allowed from
        the kubectl CLI interface.
        """
        self._properties["singularName"] = value

    @property
    def storage_version_hash(self) -> str:
        """
        The hash value of the storage version, the version this
        resource is converted to when written to the data store.
        Value must be treated as opaque by clients. Only equality
        comparison on the value is valid. This is an alpha feature
        and may change or be removed in the future. The field is
        populated by the apiserver only if the StorageVersionHash
        feature gate is enabled. This field will remain optional
        even if it graduates.
        """
        return typing.cast(
            str,
            self._properties.get("storageVersionHash"),
        )

    @storage_version_hash.setter
    def storage_version_hash(self, value: str):
        """
        The hash value of the storage version, the version this
        resource is converted to when written to the data store.
        Value must be treated as opaque by clients. Only equality
        comparison on the value is valid. This is an alpha feature
        and may change or be removed in the future. The field is
        populated by the apiserver only if the StorageVersionHash
        feature gate is enabled. This field will remain optional
        even if it graduates.
        """
        self._properties["storageVersionHash"] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        verbs is a list of supported kube verbs (this includes get,
        list, watch, create, update, patch, delete,
        deletecollection, and proxy)
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("verbs"),
        )

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        verbs is a list of supported kube verbs (this includes get,
        list, watch, create, update, patch, delete,
        deletecollection, and proxy)
        """
        self._properties["verbs"] = value

    @property
    def version(self) -> str:
        """
        version is the preferred version of the resource.  Empty
        implies the version of the containing resource list For
        subresources, this may have a different value, for example:
        v1 (while inside a v1beta1 version of the core resource's
        group)".
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        version is the preferred version of the resource.  Empty
        implies the version of the containing resource list For
        subresources, this may have a different value, for example:
        v1 (while inside a v1beta1 version of the core resource's
        group)".
        """
        self._properties["version"] = value

    def __enter__(self) -> "APIResource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIResourceList(_kuber_definitions.Definition):
    """
    APIResourceList is a list of APIResource, it is used to
    expose the name of the resources supported in a specific
    group and version, and if the resource is namespaced.
    """

    def __init__(
        self,
        api_version: str = None,
        group_version: str = None,
        kind: str = None,
        resources: typing.List["APIResource"] = None,
    ):
        """Create APIResourceList instance."""
        super(APIResourceList, self).__init__(
            api_version="meta/v1", kind="APIResourceList"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "groupVersion": group_version if group_version is not None else "",
            "kind": kind if kind is not None else "",
            "resources": resources if resources is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "groupVersion": (str, None),
            "kind": (str, None),
            "resources": (list, APIResource),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def group_version(self) -> str:
        """
        groupVersion is the group and version this APIResourceList
        is for.
        """
        return typing.cast(
            str,
            self._properties.get("groupVersion"),
        )

    @group_version.setter
    def group_version(self, value: str):
        """
        groupVersion is the group and version this APIResourceList
        is for.
        """
        self._properties["groupVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def resources(self) -> typing.List["APIResource"]:
        """
        resources contains the name of the resources and if they are
        namespaced.
        """
        return typing.cast(
            typing.List["APIResource"],
            self._properties.get("resources"),
        )

    @resources.setter
    def resources(
        self, value: typing.Union[typing.List["APIResource"], typing.List[dict]]
    ):
        """
        resources contains the name of the resources and if they are
        namespaced.
        """
        cleaned: typing.List[APIResource] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    APIResource,
                    APIResource().from_dict(item),
                )
            cleaned.append(typing.cast(APIResource, item))
        self._properties["resources"] = cleaned

    def __enter__(self) -> "APIResourceList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIVersions(_kuber_definitions.Definition):
    """
    APIVersions lists the versions that are available, to allow
    clients to discover the API at /api, which is the root path
    of the legacy v1 API.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        server_address_by_client_cidrs: typing.List["ServerAddressByClientCIDR"] = None,
        versions: typing.List[str] = None,
    ):
        """Create APIVersions instance."""
        super(APIVersions, self).__init__(api_version="meta/v1", kind="APIVersions")
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
            "serverAddressByClientCIDRs": server_address_by_client_cidrs
            if server_address_by_client_cidrs is not None
            else [],
            "versions": versions if versions is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "serverAddressByClientCIDRs": (list, ServerAddressByClientCIDR),
            "versions": (list, str),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def server_address_by_client_cidrs(
        self,
    ) -> typing.List["ServerAddressByClientCIDR"]:
        """
        a map of client CIDR to server address that is serving this
        group. This is to help clients reach servers in the most
        network-efficient way possible. Clients can use the
        appropriate server address as per the CIDR that they match.
        In case of multiple matches, clients should use the longest
        matching CIDR. The server returns only those CIDRs that it
        thinks that the client can match. For example: the master
        will return an internal IP CIDR only, if the client reaches
        the server using an internal IP. Server looks at
        X-Forwarded-For header or X-Real-Ip header or
        request.RemoteAddr (in that order) to get the client IP.
        """
        return typing.cast(
            typing.List["ServerAddressByClientCIDR"],
            self._properties.get("serverAddressByClientCIDRs"),
        )

    @server_address_by_client_cidrs.setter
    def server_address_by_client_cidrs(
        self,
        value: typing.Union[
            typing.List["ServerAddressByClientCIDR"], typing.List[dict]
        ],
    ):
        """
        a map of client CIDR to server address that is serving this
        group. This is to help clients reach servers in the most
        network-efficient way possible. Clients can use the
        appropriate server address as per the CIDR that they match.
        In case of multiple matches, clients should use the longest
        matching CIDR. The server returns only those CIDRs that it
        thinks that the client can match. For example: the master
        will return an internal IP CIDR only, if the client reaches
        the server using an internal IP. Server looks at
        X-Forwarded-For header or X-Real-Ip header or
        request.RemoteAddr (in that order) to get the client IP.
        """
        cleaned: typing.List[ServerAddressByClientCIDR] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ServerAddressByClientCIDR,
                    ServerAddressByClientCIDR().from_dict(item),
                )
            cleaned.append(typing.cast(ServerAddressByClientCIDR, item))
        self._properties["serverAddressByClientCIDRs"] = cleaned

    @property
    def versions(self) -> typing.List[str]:
        """
        versions are the api versions that are available.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("versions"),
        )

    @versions.setter
    def versions(self, value: typing.List[str]):
        """
        versions are the api versions that are available.
        """
        self._properties["versions"] = value

    def __enter__(self) -> "APIVersions":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeleteOptions(_kuber_definitions.Definition):
    """
    DeleteOptions may be provided when deleting an API object.
    """

    def __init__(
        self,
        api_version: str = None,
        dry_run: typing.List[str] = None,
        grace_period_seconds: int = None,
        kind: str = None,
        orphan_dependents: bool = None,
        preconditions: "Preconditions" = None,
        propagation_policy: str = None,
    ):
        """Create DeleteOptions instance."""
        super(DeleteOptions, self).__init__(api_version="meta/v1", kind="DeleteOptions")
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "dryRun": dry_run if dry_run is not None else [],
            "gracePeriodSeconds": grace_period_seconds
            if grace_period_seconds is not None
            else None,
            "kind": kind if kind is not None else "",
            "orphanDependents": orphan_dependents
            if orphan_dependents is not None
            else None,
            "preconditions": preconditions
            if preconditions is not None
            else Preconditions(),
            "propagationPolicy": propagation_policy
            if propagation_policy is not None
            else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "dryRun": (list, str),
            "gracePeriodSeconds": (int, None),
            "kind": (str, None),
            "orphanDependents": (bool, None),
            "preconditions": (Preconditions, None),
            "propagationPolicy": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def dry_run(self) -> typing.List[str]:
        """
        When present, indicates that modifications should not be
        persisted. An invalid or unrecognized dryRun directive will
        result in an error response and no further processing of the
        request. Valid values are: - All: all dry run stages will be
        processed
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("dryRun"),
        )

    @dry_run.setter
    def dry_run(self, value: typing.List[str]):
        """
        When present, indicates that modifications should not be
        persisted. An invalid or unrecognized dryRun directive will
        result in an error response and no further processing of the
        request. Valid values are: - All: all dry run stages will be
        processed
        """
        self._properties["dryRun"] = value

    @property
    def grace_period_seconds(self) -> int:
        """
        The duration in seconds before the object should be deleted.
        Value must be non-negative integer. The value zero indicates
        delete immediately. If this value is nil, the default grace
        period for the specified type will be used. Defaults to a
        per object value if not specified. zero means delete
        immediately.
        """
        return typing.cast(
            int,
            self._properties.get("gracePeriodSeconds"),
        )

    @grace_period_seconds.setter
    def grace_period_seconds(self, value: int):
        """
        The duration in seconds before the object should be deleted.
        Value must be non-negative integer. The value zero indicates
        delete immediately. If this value is nil, the default grace
        period for the specified type will be used. Defaults to a
        per object value if not specified. zero means delete
        immediately.
        """
        self._properties["gracePeriodSeconds"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def orphan_dependents(self) -> bool:
        """
        Deprecated: please use the PropagationPolicy, this field
        will be deprecated in 1.7. Should the dependent objects be
        orphaned. If true/false, the "orphan" finalizer will be
        added to/removed from the object's finalizers list. Either
        this field or PropagationPolicy may be set, but not both.
        """
        return typing.cast(
            bool,
            self._properties.get("orphanDependents"),
        )

    @orphan_dependents.setter
    def orphan_dependents(self, value: bool):
        """
        Deprecated: please use the PropagationPolicy, this field
        will be deprecated in 1.7. Should the dependent objects be
        orphaned. If true/false, the "orphan" finalizer will be
        added to/removed from the object's finalizers list. Either
        this field or PropagationPolicy may be set, but not both.
        """
        self._properties["orphanDependents"] = value

    @property
    def preconditions(self) -> "Preconditions":
        """
        Must be fulfilled before a deletion is carried out. If not
        possible, a 409 Conflict status will be returned.
        """
        return typing.cast(
            "Preconditions",
            self._properties.get("preconditions"),
        )

    @preconditions.setter
    def preconditions(self, value: typing.Union["Preconditions", dict]):
        """
        Must be fulfilled before a deletion is carried out. If not
        possible, a 409 Conflict status will be returned.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Preconditions,
                Preconditions().from_dict(value),
            )
        self._properties["preconditions"] = value

    @property
    def propagation_policy(self) -> str:
        """
        Whether and how garbage collection will be performed. Either
        this field or OrphanDependents may be set, but not both. The
        default policy is decided by the existing finalizer set in
        the metadata.finalizers and the resource-specific default
        policy. Acceptable values are: 'Orphan' - orphan the
        dependents; 'Background' - allow the garbage collector to
        delete the dependents in the background; 'Foreground' - a
        cascading policy that deletes all dependents in the
        foreground.
        """
        return typing.cast(
            str,
            self._properties.get("propagationPolicy"),
        )

    @propagation_policy.setter
    def propagation_policy(self, value: str):
        """
        Whether and how garbage collection will be performed. Either
        this field or OrphanDependents may be set, but not both. The
        default policy is decided by the existing finalizer set in
        the metadata.finalizers and the resource-specific default
        policy. Acceptable values are: 'Orphan' - orphan the
        dependents; 'Background' - allow the garbage collector to
        delete the dependents in the background; 'Foreground' - a
        cascading policy that deletes all dependents in the
        foreground.
        """
        self._properties["propagationPolicy"] = value

    def __enter__(self) -> "DeleteOptions":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Fields(_kuber_definitions.Definition):
    """
    Fields stores a set of fields in a data structure like a
    Trie. To understand how this is used, see:
    https://github.com/kubernetes-sigs/structured-merge-diff
    """

    def __init__(
        self,
    ):
        """Create Fields instance."""
        super(Fields, self).__init__(api_version="meta/v1", kind="Fields")
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "Fields":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GroupVersionForDiscovery(_kuber_definitions.Definition):
    """
    GroupVersion contains the "group/version" and "version"
    string of a version. It is made a struct to keep
    extensibility.
    """

    def __init__(
        self,
        group_version: str = None,
        version: str = None,
    ):
        """Create GroupVersionForDiscovery instance."""
        super(GroupVersionForDiscovery, self).__init__(
            api_version="meta/v1", kind="GroupVersionForDiscovery"
        )
        self._properties = {
            "groupVersion": group_version if group_version is not None else "",
            "version": version if version is not None else "",
        }
        self._types = {
            "groupVersion": (str, None),
            "version": (str, None),
        }

    @property
    def group_version(self) -> str:
        """
        groupVersion specifies the API group and version in the form
        "group/version"
        """
        return typing.cast(
            str,
            self._properties.get("groupVersion"),
        )

    @group_version.setter
    def group_version(self, value: str):
        """
        groupVersion specifies the API group and version in the form
        "group/version"
        """
        self._properties["groupVersion"] = value

    @property
    def version(self) -> str:
        """
        version specifies the version in the form of "version". This
        is to save the clients the trouble of splitting the
        GroupVersion.
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        version specifies the version in the form of "version". This
        is to save the clients the trouble of splitting the
        GroupVersion.
        """
        self._properties["version"] = value

    def __enter__(self) -> "GroupVersionForDiscovery":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Initializer(_kuber_definitions.Definition):
    """
    Initializer is information about an initializer that has not
    yet completed.
    """

    def __init__(
        self,
        name: str = None,
    ):
        """Create Initializer instance."""
        super(Initializer, self).__init__(api_version="meta/v1", kind="Initializer")
        self._properties = {
            "name": name if name is not None else "",
        }
        self._types = {
            "name": (str, None),
        }

    @property
    def name(self) -> str:
        """
        name of the process that is responsible for initializing
        this object.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name of the process that is responsible for initializing
        this object.
        """
        self._properties["name"] = value

    def __enter__(self) -> "Initializer":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Initializers(_kuber_definitions.Definition):
    """
    Initializers tracks the progress of initialization.
    """

    def __init__(
        self,
        pending: typing.List["Initializer"] = None,
        result: "Status" = None,
    ):
        """Create Initializers instance."""
        super(Initializers, self).__init__(api_version="meta/v1", kind="Initializers")
        self._properties = {
            "pending": pending if pending is not None else [],
            "result": result if result is not None else Status(),
        }
        self._types = {
            "pending": (list, Initializer),
            "result": (Status, None),
        }

    @property
    def pending(self) -> typing.List["Initializer"]:
        """
        Pending is a list of initializers that must execute in order
        before this object is visible. When the last pending
        initializer is removed, and no failing result is set, the
        initializers struct will be set to nil and the object is
        considered as initialized and visible to all clients.
        """
        return typing.cast(
            typing.List["Initializer"],
            self._properties.get("pending"),
        )

    @pending.setter
    def pending(
        self, value: typing.Union[typing.List["Initializer"], typing.List[dict]]
    ):
        """
        Pending is a list of initializers that must execute in order
        before this object is visible. When the last pending
        initializer is removed, and no failing result is set, the
        initializers struct will be set to nil and the object is
        considered as initialized and visible to all clients.
        """
        cleaned: typing.List[Initializer] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Initializer,
                    Initializer().from_dict(item),
                )
            cleaned.append(typing.cast(Initializer, item))
        self._properties["pending"] = cleaned

    @property
    def result(self) -> "Status":
        """
        If result is set with the Failure field, the object will be
        persisted to storage and then deleted, ensuring that other
        clients can observe the deletion.
        """
        return typing.cast(
            "Status",
            self._properties.get("result"),
        )

    @result.setter
    def result(self, value: typing.Union["Status", dict]):
        """
        If result is set with the Failure field, the object will be
        persisted to storage and then deleted, ensuring that other
        clients can observe the deletion.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Status,
                Status().from_dict(value),
            )
        self._properties["result"] = value

    def __enter__(self) -> "Initializers":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LabelSelector(_kuber_definitions.Definition):
    """
    A label selector is a label query over a set of resources.
    The result of matchLabels and matchExpressions are ANDed. An
    empty label selector matches all objects. A null label
    selector matches no objects.
    """

    def __init__(
        self,
        match_expressions: typing.List["LabelSelectorRequirement"] = None,
        match_labels: dict = None,
    ):
        """Create LabelSelector instance."""
        super(LabelSelector, self).__init__(api_version="meta/v1", kind="LabelSelector")
        self._properties = {
            "matchExpressions": match_expressions
            if match_expressions is not None
            else [],
            "matchLabels": match_labels if match_labels is not None else {},
        }
        self._types = {
            "matchExpressions": (list, LabelSelectorRequirement),
            "matchLabels": (dict, None),
        }

    @property
    def match_expressions(self) -> typing.List["LabelSelectorRequirement"]:
        """
        matchExpressions is a list of label selector requirements.
        The requirements are ANDed.
        """
        return typing.cast(
            typing.List["LabelSelectorRequirement"],
            self._properties.get("matchExpressions"),
        )

    @match_expressions.setter
    def match_expressions(
        self,
        value: typing.Union[typing.List["LabelSelectorRequirement"], typing.List[dict]],
    ):
        """
        matchExpressions is a list of label selector requirements.
        The requirements are ANDed.
        """
        cleaned: typing.List[LabelSelectorRequirement] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    LabelSelectorRequirement,
                    LabelSelectorRequirement().from_dict(item),
                )
            cleaned.append(typing.cast(LabelSelectorRequirement, item))
        self._properties["matchExpressions"] = cleaned

    @property
    def match_labels(self) -> dict:
        """
        matchLabels is a map of {key,value} pairs. A single
        {key,value} in the matchLabels map is equivalent to an
        element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only
        "value". The requirements are ANDed.
        """
        return typing.cast(
            dict,
            self._properties.get("matchLabels"),
        )

    @match_labels.setter
    def match_labels(self, value: dict):
        """
        matchLabels is a map of {key,value} pairs. A single
        {key,value} in the matchLabels map is equivalent to an
        element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only
        "value". The requirements are ANDed.
        """
        self._properties["matchLabels"] = value

    def __enter__(self) -> "LabelSelector":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LabelSelectorRequirement(_kuber_definitions.Definition):
    """
    A label selector requirement is a selector that contains
    values, a key, and an operator that relates the key and
    values.
    """

    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: typing.List[str] = None,
    ):
        """Create LabelSelectorRequirement instance."""
        super(LabelSelectorRequirement, self).__init__(
            api_version="meta/v1", kind="LabelSelectorRequirement"
        )
        self._properties = {
            "key": key if key is not None else "",
            "operator": operator if operator is not None else "",
            "values": values if values is not None else [],
        }
        self._types = {
            "key": (str, None),
            "operator": (str, None),
            "values": (list, str),
        }

    @property
    def key(self) -> str:
        """
        key is the label key that the selector applies to.
        """
        return typing.cast(
            str,
            self._properties.get("key"),
        )

    @key.setter
    def key(self, value: str):
        """
        key is the label key that the selector applies to.
        """
        self._properties["key"] = value

    @property
    def operator(self) -> str:
        """
        operator represents a key's relationship to a set of values.
        Valid operators are In, NotIn, Exists and DoesNotExist.
        """
        return typing.cast(
            str,
            self._properties.get("operator"),
        )

    @operator.setter
    def operator(self, value: str):
        """
        operator represents a key's relationship to a set of values.
        Valid operators are In, NotIn, Exists and DoesNotExist.
        """
        self._properties["operator"] = value

    @property
    def values(self) -> typing.List[str]:
        """
        values is an array of string values. If the operator is In
        or NotIn, the values array must be non-empty. If the
        operator is Exists or DoesNotExist, the values array must be
        empty. This array is replaced during a strategic merge
        patch.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("values"),
        )

    @values.setter
    def values(self, value: typing.List[str]):
        """
        values is an array of string values. If the operator is In
        or NotIn, the values array must be non-empty. If the
        operator is Exists or DoesNotExist, the values array must be
        empty. This array is replaced during a strategic merge
        patch.
        """
        self._properties["values"] = value

    def __enter__(self) -> "LabelSelectorRequirement":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ListMeta(_kuber_definitions.Definition):
    """
    ListMeta describes metadata that synthetic resources must
    have, including lists and various status objects. A resource
    may have only one of {ObjectMeta, ListMeta}.
    """

    def __init__(
        self,
        continue_: str = None,
        remaining_item_count: int = None,
        resource_version: str = None,
        self_link: str = None,
    ):
        """Create ListMeta instance."""
        super(ListMeta, self).__init__(api_version="meta/v1", kind="ListMeta")
        self._properties = {
            "continue": continue_ if continue_ is not None else "",
            "remainingItemCount": remaining_item_count
            if remaining_item_count is not None
            else None,
            "resourceVersion": resource_version if resource_version is not None else "",
            "selfLink": self_link if self_link is not None else "",
        }
        self._types = {
            "continue": (str, None),
            "remainingItemCount": (int, None),
            "resourceVersion": (str, None),
            "selfLink": (str, None),
        }

    @property
    def continue_(self) -> str:
        """
        continue may be set if the user set a limit on the number of
        items returned, and indicates that the server has more data
        available. The value is opaque and may be used to issue
        another request to the endpoint that served this list to
        retrieve the next set of available objects. Continuing a
        consistent list may not be possible if the server
        configuration has changed or more than a few minutes have
        passed. The resourceVersion field returned when using this
        continue value will be identical to the value in the first
        response, unless you have received this token from an error
        message.
        """
        return typing.cast(
            str,
            self._properties.get("continue"),
        )

    @continue_.setter
    def continue_(self, value: str):
        """
        continue may be set if the user set a limit on the number of
        items returned, and indicates that the server has more data
        available. The value is opaque and may be used to issue
        another request to the endpoint that served this list to
        retrieve the next set of available objects. Continuing a
        consistent list may not be possible if the server
        configuration has changed or more than a few minutes have
        passed. The resourceVersion field returned when using this
        continue value will be identical to the value in the first
        response, unless you have received this token from an error
        message.
        """
        self._properties["continue"] = value

    @property
    def remaining_item_count(self) -> int:
        """
        remainingItemCount is the number of subsequent items in the
        list which are not included in this list response. If the
        list request contained label or field selectors, then the
        number of remaining items is unknown and the field will be
        left unset and omitted during serialization. If the list is
        complete (either because it is not chunking or because this
        is the last chunk), then there are no more remaining items
        and this field will be left unset and omitted during
        serialization. Servers older than v1.15 do not set this
        field. The intended use of the remainingItemCount is
        *estimating* the size of a collection. Clients should not
        rely on the remainingItemCount to be set or to be exact.

        This field is alpha and can be changed or removed without
        notice.
        """
        return typing.cast(
            int,
            self._properties.get("remainingItemCount"),
        )

    @remaining_item_count.setter
    def remaining_item_count(self, value: int):
        """
        remainingItemCount is the number of subsequent items in the
        list which are not included in this list response. If the
        list request contained label or field selectors, then the
        number of remaining items is unknown and the field will be
        left unset and omitted during serialization. If the list is
        complete (either because it is not chunking or because this
        is the last chunk), then there are no more remaining items
        and this field will be left unset and omitted during
        serialization. Servers older than v1.15 do not set this
        field. The intended use of the remainingItemCount is
        *estimating* the size of a collection. Clients should not
        rely on the remainingItemCount to be set or to be exact.

        This field is alpha and can be changed or removed without
        notice.
        """
        self._properties["remainingItemCount"] = value

    @property
    def resource_version(self) -> str:
        """
        String that identifies the server's internal version of this
        object that can be used by clients to determine when objects
        have changed. Value must be treated as opaque by clients and
        passed unmodified back to the server. Populated by the
        system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        return typing.cast(
            str,
            self._properties.get("resourceVersion"),
        )

    @resource_version.setter
    def resource_version(self, value: str):
        """
        String that identifies the server's internal version of this
        object that can be used by clients to determine when objects
        have changed. Value must be treated as opaque by clients and
        passed unmodified back to the server. Populated by the
        system. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        self._properties["resourceVersion"] = value

    @property
    def self_link(self) -> str:
        """
        selfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        return typing.cast(
            str,
            self._properties.get("selfLink"),
        )

    @self_link.setter
    def self_link(self, value: str):
        """
        selfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        self._properties["selfLink"] = value

    def __enter__(self) -> "ListMeta":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ManagedFieldsEntry(_kuber_definitions.Definition):
    """
    ManagedFieldsEntry is a workflow-id, a FieldSet and the
    group version of the resource that the fieldset applies to.
    """

    def __init__(
        self,
        api_version: str = None,
        fields: "Fields" = None,
        manager: str = None,
        operation: str = None,
        time: str = None,
    ):
        """Create ManagedFieldsEntry instance."""
        super(ManagedFieldsEntry, self).__init__(
            api_version="meta/v1", kind="ManagedFieldsEntry"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "fields": fields if fields is not None else Fields(),
            "manager": manager if manager is not None else "",
            "operation": operation if operation is not None else "",
            "time": time if time is not None else None,
        }
        self._types = {
            "apiVersion": (str, None),
            "fields": (Fields, None),
            "manager": (str, None),
            "operation": (str, None),
            "time": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the version of this resource that this
        field set applies to. The format is "group/version" just
        like the top-level APIVersion field. It is necessary to
        track the version of a field set because it cannot be
        automatically converted.
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the version of this resource that this
        field set applies to. The format is "group/version" just
        like the top-level APIVersion field. It is necessary to
        track the version of a field set because it cannot be
        automatically converted.
        """
        self._properties["apiVersion"] = value

    @property
    def fields(self) -> "Fields":
        """
        Fields identifies a set of fields.
        """
        return typing.cast(
            "Fields",
            self._properties.get("fields"),
        )

    @fields.setter
    def fields(self, value: typing.Union["Fields", dict]):
        """
        Fields identifies a set of fields.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Fields,
                Fields().from_dict(value),
            )
        self._properties["fields"] = value

    @property
    def manager(self) -> str:
        """
        Manager is an identifier of the workflow managing these
        fields.
        """
        return typing.cast(
            str,
            self._properties.get("manager"),
        )

    @manager.setter
    def manager(self, value: str):
        """
        Manager is an identifier of the workflow managing these
        fields.
        """
        self._properties["manager"] = value

    @property
    def operation(self) -> str:
        """
        Operation is the type of operation which lead to this
        ManagedFieldsEntry being created. The only valid values for
        this field are 'Apply' and 'Update'.
        """
        return typing.cast(
            str,
            self._properties.get("operation"),
        )

    @operation.setter
    def operation(self, value: str):
        """
        Operation is the type of operation which lead to this
        ManagedFieldsEntry being created. The only valid values for
        this field are 'Apply' and 'Update'.
        """
        self._properties["operation"] = value

    @property
    def time(self) -> str:
        """
        Time is timestamp of when these fields were set. It should
        always be empty if Operation is 'Apply'
        """
        return typing.cast(
            str,
            self._properties.get("time"),
        )

    @time.setter
    def time(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        Time is timestamp of when these fields were set. It should
        always be empty if Operation is 'Apply'
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["time"] = value

    def __enter__(self) -> "ManagedFieldsEntry":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MicroTime(_kuber_definitions.Definition):
    """
    MicroTime is version of Time with microsecond level
    precision.
    """

    def __init__(
        self,
    ):
        """Create MicroTime instance."""
        super(MicroTime, self).__init__(api_version="meta/v1", kind="MicroTime")
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "MicroTime":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ObjectMeta(_kuber_definitions.Definition):
    """
    ObjectMeta is metadata that all persisted resources must
    have, which includes all objects users must create.
    """

    def __init__(
        self,
        annotations: dict = None,
        cluster_name: str = None,
        creation_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        deletion_timestamp: str = None,
        finalizers: typing.List[str] = None,
        generate_name: str = None,
        generation: int = None,
        initializers: "Initializers" = None,
        labels: dict = None,
        managed_fields: typing.List["ManagedFieldsEntry"] = None,
        name: str = None,
        namespace: str = None,
        owner_references: typing.List["OwnerReference"] = None,
        resource_version: str = None,
        self_link: str = None,
        uid: str = None,
    ):
        """Create ObjectMeta instance."""
        super(ObjectMeta, self).__init__(api_version="meta/v1", kind="ObjectMeta")
        self._properties = {
            "annotations": annotations if annotations is not None else {},
            "clusterName": cluster_name if cluster_name is not None else "",
            "creationTimestamp": creation_timestamp
            if creation_timestamp is not None
            else None,
            "deletionGracePeriodSeconds": deletion_grace_period_seconds
            if deletion_grace_period_seconds is not None
            else None,
            "deletionTimestamp": deletion_timestamp
            if deletion_timestamp is not None
            else None,
            "finalizers": finalizers if finalizers is not None else [],
            "generateName": generate_name if generate_name is not None else "",
            "generation": generation if generation is not None else None,
            "initializers": initializers
            if initializers is not None
            else Initializers(),
            "labels": labels if labels is not None else {},
            "managedFields": managed_fields if managed_fields is not None else [],
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "ownerReferences": owner_references if owner_references is not None else [],
            "resourceVersion": resource_version if resource_version is not None else "",
            "selfLink": self_link if self_link is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "annotations": (dict, None),
            "clusterName": (str, None),
            "creationTimestamp": (str, None),
            "deletionGracePeriodSeconds": (int, None),
            "deletionTimestamp": (str, None),
            "finalizers": (list, str),
            "generateName": (str, None),
            "generation": (int, None),
            "initializers": (Initializers, None),
            "labels": (dict, None),
            "managedFields": (list, ManagedFieldsEntry),
            "name": (str, None),
            "namespace": (str, None),
            "ownerReferences": (list, OwnerReference),
            "resourceVersion": (str, None),
            "selfLink": (str, None),
            "uid": (str, None),
        }

    @property
    def annotations(self) -> dict:
        """
        Annotations is an unstructured key value map stored with a
        resource that may be set by external tools to store and
        retrieve arbitrary metadata. They are not queryable and
        should be preserved when modifying objects. More info:
        http://kubernetes.io/docs/user-guide/annotations
        """
        return typing.cast(
            dict,
            self._properties.get("annotations"),
        )

    @annotations.setter
    def annotations(self, value: dict):
        """
        Annotations is an unstructured key value map stored with a
        resource that may be set by external tools to store and
        retrieve arbitrary metadata. They are not queryable and
        should be preserved when modifying objects. More info:
        http://kubernetes.io/docs/user-guide/annotations
        """
        self._properties["annotations"] = value

    @property
    def cluster_name(self) -> str:
        """
        The name of the cluster which the object belongs to. This is
        used to distinguish resources with same name and namespace
        in different clusters. This field is not set anywhere right
        now and apiserver is going to ignore it if set in create or
        update request.
        """
        return typing.cast(
            str,
            self._properties.get("clusterName"),
        )

    @cluster_name.setter
    def cluster_name(self, value: str):
        """
        The name of the cluster which the object belongs to. This is
        used to distinguish resources with same name and namespace
        in different clusters. This field is not set anywhere right
        now and apiserver is going to ignore it if set in create or
        update request.
        """
        self._properties["clusterName"] = value

    @property
    def creation_timestamp(self) -> str:
        """
        CreationTimestamp is a timestamp representing the server
        time when this object was created. It is not guaranteed to
        be set in happens-before order across separate operations.
        Clients may not set this value. It is represented in RFC3339
        form and is in UTC.

        Populated by the system. Read-only. Null for lists. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            str,
            self._properties.get("creationTimestamp"),
        )

    @creation_timestamp.setter
    def creation_timestamp(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        CreationTimestamp is a timestamp representing the server
        time when this object was created. It is not guaranteed to
        be set in happens-before order across separate operations.
        Clients may not set this value. It is represented in RFC3339
        form and is in UTC.

        Populated by the system. Read-only. Null for lists. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["creationTimestamp"] = value

    @property
    def deletion_grace_period_seconds(self) -> int:
        """
        Number of seconds allowed for this object to gracefully
        terminate before it will be removed from the system. Only
        set when deletionTimestamp is also set. May only be
        shortened. Read-only.
        """
        return typing.cast(
            int,
            self._properties.get("deletionGracePeriodSeconds"),
        )

    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, value: int):
        """
        Number of seconds allowed for this object to gracefully
        terminate before it will be removed from the system. Only
        set when deletionTimestamp is also set. May only be
        shortened. Read-only.
        """
        self._properties["deletionGracePeriodSeconds"] = value

    @property
    def deletion_timestamp(self) -> str:
        """
        DeletionTimestamp is RFC 3339 date and time at which this
        resource will be deleted. This field is set by the server
        when a graceful deletion is requested by the user, and is
        not directly settable by a client. The resource is expected
        to be deleted (no longer visible from resource lists, and
        not reachable by name) after the time in this field, once
        the finalizers list is empty. As long as the finalizers list
        contains items, deletion is blocked. Once the
        deletionTimestamp is set, this value may not be unset or be
        set further into the future, although it may be shortened or
        the resource may be deleted prior to this time. For example,
        a user may request that a pod is deleted in 30 seconds. The
        Kubelet will react by sending a graceful termination signal
        to the containers in the pod. After that 30 seconds, the
        Kubelet will send a hard termination signal (SIGKILL) to the
        container and after cleanup, remove the pod from the API. In
        the presence of network partitions, this object may still
        exist after this timestamp, until an administrator or
        automated process can determine the resource is fully
        terminated. If not set, graceful deletion of the object has
        not been requested.

        Populated by the system when a graceful deletion is
        requested. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return typing.cast(
            str,
            self._properties.get("deletionTimestamp"),
        )

    @deletion_timestamp.setter
    def deletion_timestamp(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        DeletionTimestamp is RFC 3339 date and time at which this
        resource will be deleted. This field is set by the server
        when a graceful deletion is requested by the user, and is
        not directly settable by a client. The resource is expected
        to be deleted (no longer visible from resource lists, and
        not reachable by name) after the time in this field, once
        the finalizers list is empty. As long as the finalizers list
        contains items, deletion is blocked. Once the
        deletionTimestamp is set, this value may not be unset or be
        set further into the future, although it may be shortened or
        the resource may be deleted prior to this time. For example,
        a user may request that a pod is deleted in 30 seconds. The
        Kubelet will react by sending a graceful termination signal
        to the containers in the pod. After that 30 seconds, the
        Kubelet will send a hard termination signal (SIGKILL) to the
        container and after cleanup, remove the pod from the API. In
        the presence of network partitions, this object may still
        exist after this timestamp, until an administrator or
        automated process can determine the resource is fully
        terminated. If not set, graceful deletion of the object has
        not been requested.

        Populated by the system when a graceful deletion is
        requested. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["deletionTimestamp"] = value

    @property
    def finalizers(self) -> typing.List[str]:
        """
        Must be empty before the object is deleted from the
        registry. Each entry is an identifier for the responsible
        component that will remove the entry from the list. If the
        deletionTimestamp of the object is non-nil, entries in this
        list can only be removed.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("finalizers"),
        )

    @finalizers.setter
    def finalizers(self, value: typing.List[str]):
        """
        Must be empty before the object is deleted from the
        registry. Each entry is an identifier for the responsible
        component that will remove the entry from the list. If the
        deletionTimestamp of the object is non-nil, entries in this
        list can only be removed.
        """
        self._properties["finalizers"] = value

    @property
    def generate_name(self) -> str:
        """
        GenerateName is an optional prefix, used by the server, to
        generate a unique name ONLY IF the Name field has not been
        provided. If this field is used, the name returned to the
        client will be different than the name passed. This value
        will also be combined with a unique suffix. The provided
        value has the same validation rules as the Name field, and
        may be truncated by the length of the suffix required to
        make the value unique on the server.

        If this field is specified and the generated name exists,
        the server will NOT return a 409 - instead, it will either
        return 201 Created or 500 with Reason ServerTimeout
        indicating a unique name could not be found in the time
        allotted, and the client should retry (optionally after the
        time indicated in the Retry-After header).

        Applied only if Name is not specified. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#idempotency
        """
        return typing.cast(
            str,
            self._properties.get("generateName"),
        )

    @generate_name.setter
    def generate_name(self, value: str):
        """
        GenerateName is an optional prefix, used by the server, to
        generate a unique name ONLY IF the Name field has not been
        provided. If this field is used, the name returned to the
        client will be different than the name passed. This value
        will also be combined with a unique suffix. The provided
        value has the same validation rules as the Name field, and
        may be truncated by the length of the suffix required to
        make the value unique on the server.

        If this field is specified and the generated name exists,
        the server will NOT return a 409 - instead, it will either
        return 201 Created or 500 with Reason ServerTimeout
        indicating a unique name could not be found in the time
        allotted, and the client should retry (optionally after the
        time indicated in the Retry-After header).

        Applied only if Name is not specified. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#idempotency
        """
        self._properties["generateName"] = value

    @property
    def generation(self) -> int:
        """
        A sequence number representing a specific generation of the
        desired state. Populated by the system. Read-only.
        """
        return typing.cast(
            int,
            self._properties.get("generation"),
        )

    @generation.setter
    def generation(self, value: int):
        """
        A sequence number representing a specific generation of the
        desired state. Populated by the system. Read-only.
        """
        self._properties["generation"] = value

    @property
    def initializers(self) -> "Initializers":
        """
        An initializer is a controller which enforces some system
        invariant at object creation time. This field is a list of
        initializers that have not yet acted on this object. If nil
        or empty, this object has been completely initialized.
        Otherwise, the object is considered uninitialized and is
        hidden (in list/watch and get calls) from clients that
        haven't explicitly asked to observe uninitialized objects.

        When an object is created, the system will populate this
        list with the current set of initializers. Only privileged
        users may set or modify this list. Once it is empty, it may
        not be modified further by any user.

        DEPRECATED - initializers are an alpha field and will be
        removed in v1.15.
        """
        return typing.cast(
            "Initializers",
            self._properties.get("initializers"),
        )

    @initializers.setter
    def initializers(self, value: typing.Union["Initializers", dict]):
        """
        An initializer is a controller which enforces some system
        invariant at object creation time. This field is a list of
        initializers that have not yet acted on this object. If nil
        or empty, this object has been completely initialized.
        Otherwise, the object is considered uninitialized and is
        hidden (in list/watch and get calls) from clients that
        haven't explicitly asked to observe uninitialized objects.

        When an object is created, the system will populate this
        list with the current set of initializers. Only privileged
        users may set or modify this list. Once it is empty, it may
        not be modified further by any user.

        DEPRECATED - initializers are an alpha field and will be
        removed in v1.15.
        """
        if isinstance(value, dict):
            value = typing.cast(
                Initializers,
                Initializers().from_dict(value),
            )
        self._properties["initializers"] = value

    @property
    def labels(self) -> dict:
        """
        Map of string keys and values that can be used to organize
        and categorize (scope and select) objects. May match
        selectors of replication controllers and services. More
        info: http://kubernetes.io/docs/user-guide/labels
        """
        return typing.cast(
            dict,
            self._properties.get("labels"),
        )

    @labels.setter
    def labels(self, value: dict):
        """
        Map of string keys and values that can be used to organize
        and categorize (scope and select) objects. May match
        selectors of replication controllers and services. More
        info: http://kubernetes.io/docs/user-guide/labels
        """
        self._properties["labels"] = value

    @property
    def managed_fields(self) -> typing.List["ManagedFieldsEntry"]:
        """
        ManagedFields maps workflow-id and version to the set of
        fields that are managed by that workflow. This is mostly for
        internal housekeeping, and users typically shouldn't need to
        set or understand this field. A workflow can be the user's
        name, a controller's name, or the name of a specific apply
        path like "ci-cd". The set of fields is always in the
        version that the workflow used when modifying the object.

        This field is alpha and can be changed or removed without
        notice.
        """
        return typing.cast(
            typing.List["ManagedFieldsEntry"],
            self._properties.get("managedFields"),
        )

    @managed_fields.setter
    def managed_fields(
        self, value: typing.Union[typing.List["ManagedFieldsEntry"], typing.List[dict]]
    ):
        """
        ManagedFields maps workflow-id and version to the set of
        fields that are managed by that workflow. This is mostly for
        internal housekeeping, and users typically shouldn't need to
        set or understand this field. A workflow can be the user's
        name, a controller's name, or the name of a specific apply
        path like "ci-cd". The set of fields is always in the
        version that the workflow used when modifying the object.

        This field is alpha and can be changed or removed without
        notice.
        """
        cleaned: typing.List[ManagedFieldsEntry] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ManagedFieldsEntry,
                    ManagedFieldsEntry().from_dict(item),
                )
            cleaned.append(typing.cast(ManagedFieldsEntry, item))
        self._properties["managedFields"] = cleaned

    @property
    def name(self) -> str:
        """
        Name must be unique within a namespace. Is required when
        creating resources, although some resources may allow a
        client to request the generation of an appropriate name
        automatically. Name is primarily intended for creation
        idempotence and configuration definition. Cannot be updated.
        More info: http://kubernetes.io/docs/user-
        guide/identifiers#names
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name must be unique within a namespace. Is required when
        creating resources, although some resources may allow a
        client to request the generation of an appropriate name
        automatically. Name is primarily intended for creation
        idempotence and configuration definition. Cannot be updated.
        More info: http://kubernetes.io/docs/user-
        guide/identifiers#names
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace defines the space within each name must be unique.
        An empty namespace is equivalent to the "default" namespace,
        but "default" is the canonical representation. Not all
        objects are required to be scoped to a namespace - the value
        of this field for those objects will be empty.

        Must be a DNS_LABEL. Cannot be updated. More info:
        http://kubernetes.io/docs/user-guide/namespaces
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace defines the space within each name must be unique.
        An empty namespace is equivalent to the "default" namespace,
        but "default" is the canonical representation. Not all
        objects are required to be scoped to a namespace - the value
        of this field for those objects will be empty.

        Must be a DNS_LABEL. Cannot be updated. More info:
        http://kubernetes.io/docs/user-guide/namespaces
        """
        self._properties["namespace"] = value

    @property
    def owner_references(self) -> typing.List["OwnerReference"]:
        """
        List of objects depended by this object. If ALL objects in
        the list have been deleted, this object will be garbage
        collected. If this object is managed by a controller, then
        an entry in this list will point to this controller, with
        the controller field set to true. There cannot be more than
        one managing controller.
        """
        return typing.cast(
            typing.List["OwnerReference"],
            self._properties.get("ownerReferences"),
        )

    @owner_references.setter
    def owner_references(
        self, value: typing.Union[typing.List["OwnerReference"], typing.List[dict]]
    ):
        """
        List of objects depended by this object. If ALL objects in
        the list have been deleted, this object will be garbage
        collected. If this object is managed by a controller, then
        an entry in this list will point to this controller, with
        the controller field set to true. There cannot be more than
        one managing controller.
        """
        cleaned: typing.List[OwnerReference] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    OwnerReference,
                    OwnerReference().from_dict(item),
                )
            cleaned.append(typing.cast(OwnerReference, item))
        self._properties["ownerReferences"] = cleaned

    @property
    def resource_version(self) -> str:
        """
        An opaque value that represents the internal version of this
        object that can be used by clients to determine when objects
        have changed. May be used for optimistic concurrency, change
        detection, and the watch operation on a resource or set of
        resources. Clients must treat these values as opaque and
        passed unmodified back to the server. They may only be valid
        for a particular resource or set of resources.

        Populated by the system. Read-only. Value must be treated as
        opaque by clients and . More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        return typing.cast(
            str,
            self._properties.get("resourceVersion"),
        )

    @resource_version.setter
    def resource_version(self, value: str):
        """
        An opaque value that represents the internal version of this
        object that can be used by clients to determine when objects
        have changed. May be used for optimistic concurrency, change
        detection, and the watch operation on a resource or set of
        resources. Clients must treat these values as opaque and
        passed unmodified back to the server. They may only be valid
        for a particular resource or set of resources.

        Populated by the system. Read-only. Value must be treated as
        opaque by clients and . More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        self._properties["resourceVersion"] = value

    @property
    def self_link(self) -> str:
        """
        SelfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        return typing.cast(
            str,
            self._properties.get("selfLink"),
        )

    @self_link.setter
    def self_link(self, value: str):
        """
        SelfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        self._properties["selfLink"] = value

    @property
    def uid(self) -> str:
        """
        UID is the unique in time and space value for this object.
        It is typically generated by the server on successful
        creation of a resource and is not allowed to change on PUT
        operations.

        Populated by the system. Read-only. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID is the unique in time and space value for this object.
        It is typically generated by the server on successful
        creation of a resource and is not allowed to change on PUT
        operations.

        Populated by the system. Read-only. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        self._properties["uid"] = value

    def __enter__(self) -> "ObjectMeta":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class OwnerReference(_kuber_definitions.Definition):
    """
    OwnerReference contains enough information to let you
    identify an owning object. An owning object must be in the
    same namespace as the dependent, or be cluster-scoped, so
    there is no namespace field.
    """

    def __init__(
        self,
        api_version: str = None,
        block_owner_deletion: bool = None,
        controller: bool = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
    ):
        """Create OwnerReference instance."""
        super(OwnerReference, self).__init__(
            api_version="meta/v1", kind="OwnerReference"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "blockOwnerDeletion": block_owner_deletion
            if block_owner_deletion is not None
            else None,
            "controller": controller if controller is not None else None,
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "blockOwnerDeletion": (bool, None),
            "controller": (bool, None),
            "kind": (str, None),
            "name": (str, None),
            "uid": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent.
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent.
        """
        self._properties["apiVersion"] = value

    @property
    def block_owner_deletion(self) -> bool:
        """
        If true, AND if the owner has the "foregroundDeletion"
        finalizer, then the owner cannot be deleted from the key-
        value store until this reference is removed. Defaults to
        false. To set this field, a user needs "delete" permission
        of the owner, otherwise 422 (Unprocessable Entity) will be
        returned.
        """
        return typing.cast(
            bool,
            self._properties.get("blockOwnerDeletion"),
        )

    @block_owner_deletion.setter
    def block_owner_deletion(self, value: bool):
        """
        If true, AND if the owner has the "foregroundDeletion"
        finalizer, then the owner cannot be deleted from the key-
        value store until this reference is removed. Defaults to
        false. To set this field, a user needs "delete" permission
        of the owner, otherwise 422 (Unprocessable Entity) will be
        returned.
        """
        self._properties["blockOwnerDeletion"] = value

    @property
    def controller(self) -> bool:
        """
        If true, this reference points to the managing controller.
        """
        return typing.cast(
            bool,
            self._properties.get("controller"),
        )

    @controller.setter
    def controller(self, value: bool):
        """
        If true, this reference points to the managing controller.
        """
        self._properties["controller"] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        self._properties["name"] = value

    @property
    def uid(self) -> str:
        """
        UID of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        self._properties["uid"] = value

    def __enter__(self) -> "OwnerReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Patch(_kuber_definitions.Definition):
    """
    Patch is provided to give a concrete name and type to the
    Kubernetes PATCH request body.
    """

    def __init__(
        self,
    ):
        """Create Patch instance."""
        super(Patch, self).__init__(api_version="meta/v1", kind="Patch")
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "Patch":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Preconditions(_kuber_definitions.Definition):
    """
    Preconditions must be fulfilled before an operation (update,
    delete, etc.) is carried out.
    """

    def __init__(
        self,
        resource_version: str = None,
        uid: str = None,
    ):
        """Create Preconditions instance."""
        super(Preconditions, self).__init__(api_version="meta/v1", kind="Preconditions")
        self._properties = {
            "resourceVersion": resource_version if resource_version is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "resourceVersion": (str, None),
            "uid": (str, None),
        }

    @property
    def resource_version(self) -> str:
        """
        Specifies the target ResourceVersion
        """
        return typing.cast(
            str,
            self._properties.get("resourceVersion"),
        )

    @resource_version.setter
    def resource_version(self, value: str):
        """
        Specifies the target ResourceVersion
        """
        self._properties["resourceVersion"] = value

    @property
    def uid(self) -> str:
        """
        Specifies the target UID.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        Specifies the target UID.
        """
        self._properties["uid"] = value

    def __enter__(self) -> "Preconditions":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServerAddressByClientCIDR(_kuber_definitions.Definition):
    """
    ServerAddressByClientCIDR helps the client to determine the
    server address that they should use, depending on the
    clientCIDR that they match.
    """

    def __init__(
        self,
        client_cidr: str = None,
        server_address: str = None,
    ):
        """Create ServerAddressByClientCIDR instance."""
        super(ServerAddressByClientCIDR, self).__init__(
            api_version="meta/v1", kind="ServerAddressByClientCIDR"
        )
        self._properties = {
            "clientCIDR": client_cidr if client_cidr is not None else "",
            "serverAddress": server_address if server_address is not None else "",
        }
        self._types = {
            "clientCIDR": (str, None),
            "serverAddress": (str, None),
        }

    @property
    def client_cidr(self) -> str:
        """
        The CIDR with which clients can match their IP to figure out
        the server address that they should use.
        """
        return typing.cast(
            str,
            self._properties.get("clientCIDR"),
        )

    @client_cidr.setter
    def client_cidr(self, value: str):
        """
        The CIDR with which clients can match their IP to figure out
        the server address that they should use.
        """
        self._properties["clientCIDR"] = value

    @property
    def server_address(self) -> str:
        """
        Address of this server, suitable for a client that matches
        the above CIDR. This can be a hostname, hostname:port, IP or
        IP:port.
        """
        return typing.cast(
            str,
            self._properties.get("serverAddress"),
        )

    @server_address.setter
    def server_address(self, value: str):
        """
        Address of this server, suitable for a client that matches
        the above CIDR. This can be a hostname, hostname:port, IP or
        IP:port.
        """
        self._properties["serverAddress"] = value

    def __enter__(self) -> "ServerAddressByClientCIDR":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Status(_kuber_definitions.Definition):
    """
    Status is a return value for calls that don't return other
    objects.
    """

    def __init__(
        self,
        api_version: str = None,
        code: int = None,
        details: "StatusDetails" = None,
        kind: str = None,
        message: str = None,
        metadata: "ListMeta" = None,
        reason: str = None,
        status: str = None,
    ):
        """Create Status instance."""
        super(Status, self).__init__(api_version="meta/v1", kind="Status")
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "code": code if code is not None else None,
            "details": details if details is not None else StatusDetails(),
            "kind": kind if kind is not None else "",
            "message": message if message is not None else "",
            "metadata": metadata if metadata is not None else ListMeta(),
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "code": (int, None),
            "details": (StatusDetails, None),
            "kind": (str, None),
            "message": (str, None),
            "metadata": (ListMeta, None),
            "reason": (str, None),
            "status": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion defines the versioned schema of this
        representation of an object. Servers should convert
        recognized schemas to the latest internal value, and may
        reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#resources
        """
        self._properties["apiVersion"] = value

    @property
    def code(self) -> int:
        """
        Suggested HTTP return code for this status, 0 if not set.
        """
        return typing.cast(
            int,
            self._properties.get("code"),
        )

    @code.setter
    def code(self, value: int):
        """
        Suggested HTTP return code for this status, 0 if not set.
        """
        self._properties["code"] = value

    @property
    def details(self) -> "StatusDetails":
        """
        Extended data associated with the reason.  Each reason may
        define its own extended details. This field is optional and
        the data returned is not guaranteed to conform to any schema
        except that defined by the reason type.
        """
        return typing.cast(
            "StatusDetails",
            self._properties.get("details"),
        )

    @details.setter
    def details(self, value: typing.Union["StatusDetails", dict]):
        """
        Extended data associated with the reason.  Each reason may
        define its own extended details. This field is optional and
        the data returned is not guaranteed to conform to any schema
        except that defined by the reason type.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StatusDetails,
                StatusDetails().from_dict(value),
            )
        self._properties["details"] = value

    @property
    def kind(self) -> str:
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is a string value representing the REST resource this
        object represents. Servers may infer this from the endpoint
        the client submits requests to. Cannot be updated. In
        CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def message(self) -> str:
        """
        A human-readable description of the status of this
        operation.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human-readable description of the status of this
        operation.
        """
        self._properties["message"] = value

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def reason(self) -> str:
        """
        A machine-readable description of why this operation is in
        the "Failure" status. If this value is empty there is no
        information available. A Reason clarifies an HTTP status
        code but does not override it.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        A machine-readable description of why this operation is in
        the "Failure" status. If this value is empty there is no
        information available. A Reason clarifies an HTTP status
        code but does not override it.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the operation. One of: "Success" or "Failure".
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the operation. One of: "Success" or "Failure".
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        self._properties["status"] = value

    def __enter__(self) -> "Status":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatusCause(_kuber_definitions.Definition):
    """
    StatusCause provides more information about an api.Status
    failure, including cases when multiple errors are
    encountered.
    """

    def __init__(
        self,
        field: str = None,
        message: str = None,
        reason: str = None,
    ):
        """Create StatusCause instance."""
        super(StatusCause, self).__init__(api_version="meta/v1", kind="StatusCause")
        self._properties = {
            "field": field if field is not None else "",
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
        }
        self._types = {
            "field": (str, None),
            "message": (str, None),
            "reason": (str, None),
        }

    @property
    def field(self) -> str:
        """
        The field of the resource that has caused this error, as
        named by its JSON serialization. May include dot and postfix
        notation for nested attributes. Arrays are zero-indexed.
        Fields may appear more than once in an array of causes due
        to fields having multiple errors. Optional.

        Examples:
          "name" - the field "name" on the current resource
          "items[0].name" - the field "name" on the first array
        entry in "items"
        """
        return typing.cast(
            str,
            self._properties.get("field"),
        )

    @field.setter
    def field(self, value: str):
        """
        The field of the resource that has caused this error, as
        named by its JSON serialization. May include dot and postfix
        notation for nested attributes. Arrays are zero-indexed.
        Fields may appear more than once in an array of causes due
        to fields having multiple errors. Optional.

        Examples:
          "name" - the field "name" on the current resource
          "items[0].name" - the field "name" on the first array
        entry in "items"
        """
        self._properties["field"] = value

    @property
    def message(self) -> str:
        """
        A human-readable description of the cause of the error.
        This field may be presented as-is to a reader.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        A human-readable description of the cause of the error.
        This field may be presented as-is to a reader.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        A machine-readable description of the cause of the error. If
        this value is empty there is no information available.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        A machine-readable description of the cause of the error. If
        this value is empty there is no information available.
        """
        self._properties["reason"] = value

    def __enter__(self) -> "StatusCause":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatusDetails(_kuber_definitions.Definition):
    """
    StatusDetails is a set of additional properties that MAY be
    set by the server to provide additional information about a
    response. The Reason field of a Status object defines what
    attributes will be set. Clients must ignore fields that do
    not match the defined type of each attribute, and should
    assume that any attribute may be empty, invalid, or under
    defined.
    """

    def __init__(
        self,
        causes: typing.List["StatusCause"] = None,
        group: str = None,
        kind: str = None,
        name: str = None,
        retry_after_seconds: int = None,
        uid: str = None,
    ):
        """Create StatusDetails instance."""
        super(StatusDetails, self).__init__(api_version="meta/v1", kind="StatusDetails")
        self._properties = {
            "causes": causes if causes is not None else [],
            "group": group if group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "retryAfterSeconds": retry_after_seconds
            if retry_after_seconds is not None
            else None,
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "causes": (list, StatusCause),
            "group": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "retryAfterSeconds": (int, None),
            "uid": (str, None),
        }

    @property
    def causes(self) -> typing.List["StatusCause"]:
        """
        The Causes array includes more details associated with the
        StatusReason failure. Not all StatusReasons may provide
        detailed causes.
        """
        return typing.cast(
            typing.List["StatusCause"],
            self._properties.get("causes"),
        )

    @causes.setter
    def causes(
        self, value: typing.Union[typing.List["StatusCause"], typing.List[dict]]
    ):
        """
        The Causes array includes more details associated with the
        StatusReason failure. Not all StatusReasons may provide
        detailed causes.
        """
        cleaned: typing.List[StatusCause] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StatusCause,
                    StatusCause().from_dict(item),
                )
            cleaned.append(typing.cast(StatusCause, item))
        self._properties["causes"] = cleaned

    @property
    def group(self) -> str:
        """
        The group attribute of the resource associated with the
        status StatusReason.
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        The group attribute of the resource associated with the
        status StatusReason.
        """
        self._properties["group"] = value

    @property
    def kind(self) -> str:
        """
        The kind attribute of the resource associated with the
        status StatusReason. On some operations may differ from the
        requested resource Kind. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        The kind attribute of the resource associated with the
        status StatusReason. On some operations may differ from the
        requested resource Kind. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        The name attribute of the resource associated with the
        status StatusReason (when there is a single name which can
        be described).
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        The name attribute of the resource associated with the
        status StatusReason (when there is a single name which can
        be described).
        """
        self._properties["name"] = value

    @property
    def retry_after_seconds(self) -> int:
        """
        If specified, the time in seconds before the operation
        should be retried. Some errors may indicate the client must
        take an alternate action - for those errors this field may
        indicate how long to wait before taking the alternate
        action.
        """
        return typing.cast(
            int,
            self._properties.get("retryAfterSeconds"),
        )

    @retry_after_seconds.setter
    def retry_after_seconds(self, value: int):
        """
        If specified, the time in seconds before the operation
        should be retried. Some errors may indicate the client must
        take an alternate action - for those errors this field may
        indicate how long to wait before taking the alternate
        action.
        """
        self._properties["retryAfterSeconds"] = value

    @property
    def uid(self) -> str:
        """
        UID of the resource. (when there is a single resource which
        can be described). More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID of the resource. (when there is a single resource which
        can be described). More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        self._properties["uid"] = value

    def __enter__(self) -> "StatusDetails":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Time(_kuber_definitions.Definition):
    """
    Time is a wrapper around time.Time which supports correct
    marshaling to YAML and JSON.  Wrappers are provided for many
    of the factory methods that the time package offers.
    """

    def __init__(
        self,
    ):
        """Create Time instance."""
        super(Time, self).__init__(api_version="meta/v1", kind="Time")
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "Time":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WatchEvent(_kuber_definitions.Definition):
    """
    Event represents a single event to a watched resource.
    """

    def __init__(
        self,
        object_: "RawExtension" = None,
        type_: str = None,
    ):
        """Create WatchEvent instance."""
        super(WatchEvent, self).__init__(api_version="meta/v1", kind="WatchEvent")
        self._properties = {
            "object": object_ if object_ is not None else RawExtension(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "object": (RawExtension, None),
            "type": (str, None),
        }

    @property
    def object_(self) -> "RawExtension":
        """
        Object is:
         * If Type is Added or Modified: the new state of the
        object.
         * If Type is Deleted: the state of the object immediately
        before deletion.
         * If Type is Error: *Status is recommended; other types may
        make sense
           depending on context.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("object"),
        )

    @object_.setter
    def object_(self, value: typing.Union["RawExtension", dict]):
        """
        Object is:
         * If Type is Added or Modified: the new state of the
        object.
         * If Type is Deleted: the state of the object immediately
        before deletion.
         * If Type is Error: *Status is recommended; other types may
        make sense
           depending on context.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["object"] = value

    @property
    def type_(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """"""
        self._properties["type"] = value

    def __enter__(self) -> "WatchEvent":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

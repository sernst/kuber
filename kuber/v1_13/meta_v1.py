import typing
import datetime as _datetime

from kubernetes import client

from kuber import definitions as _kuber_definitions
from kuber.v1_13.apimachinery_runtime import RawExtension


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
            preferred_version: 'GroupVersionForDiscovery' = None,
            server_address_by_client_cidrs: typing.List['ServerAddressByClientCIDR'] = None,
            versions: typing.List['GroupVersionForDiscovery'] = None,
    ):
        """Create APIGroup instance."""
        super(APIGroup, self).__init__(
            api_version='meta/v1',
            kind='APIGroup'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'kind': kind or '',
            'name': name or '',
            'preferredVersion': preferred_version or GroupVersionForDiscovery(),
            'serverAddressByClientCIDRs': server_address_by_client_cidrs or [],
            'versions': versions or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'name': (str, None),
            'preferredVersion': (GroupVersionForDiscovery, None),
            'serverAddressByClientCIDRs': (list, ServerAddressByClientCIDR),
            'versions': (list, GroupVersionForDiscovery),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        name is the name of the group.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name is the name of the group.
        """
        self._properties['name'] = value

    @property
    def preferred_version(self) -> 'GroupVersionForDiscovery':
        """
        preferredVersion is the version preferred by the API server,
        which probably is the storage version.
        """
        return self._properties.get('preferredVersion')

    @preferred_version.setter
    def preferred_version(self, value: typing.Union['GroupVersionForDiscovery', dict]):
        """
        preferredVersion is the version preferred by the API server,
        which probably is the storage version.
        """
        if isinstance(value, dict):
            value = GroupVersionForDiscovery().from_dict(value)
        self._properties['preferredVersion'] = value

    @property
    def server_address_by_client_cidrs(self) -> typing.List['ServerAddressByClientCIDR']:
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
        return self._properties.get('serverAddressByClientCIDRs')

    @server_address_by_client_cidrs.setter
    def server_address_by_client_cidrs(
            self,
            value: typing.Union[typing.List['ServerAddressByClientCIDR'], typing.List[dict]]
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
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ServerAddressByClientCIDR().from_dict(item)
            cleaned.append(item)
        self._properties['serverAddressByClientCIDRs'] = cleaned

    @property
    def versions(self) -> typing.List['GroupVersionForDiscovery']:
        """
        versions are the versions supported in this group.
        """
        return self._properties.get('versions')

    @versions.setter
    def versions(
            self,
            value: typing.Union[typing.List['GroupVersionForDiscovery'], typing.List[dict]]
    ):
        """
        versions are the versions supported in this group.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = GroupVersionForDiscovery().from_dict(item)
            cleaned.append(item)
        self._properties['versions'] = cleaned

    def __enter__(self) -> 'APIGroup':
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
            groups: typing.List['APIGroup'] = None,
            kind: str = None,
    ):
        """Create APIGroupList instance."""
        super(APIGroupList, self).__init__(
            api_version='meta/v1',
            kind='APIGroupList'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'groups': groups or [],
            'kind': kind or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'groups': (list, APIGroup),
            'kind': (str, None),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

    @property
    def groups(self) -> typing.List['APIGroup']:
        """
        groups is a list of APIGroup.
        """
        return self._properties.get('groups')

    @groups.setter
    def groups(
            self,
            value: typing.Union[typing.List['APIGroup'], typing.List[dict]]
    ):
        """
        groups is a list of APIGroup.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = APIGroup().from_dict(item)
            cleaned.append(item)
        self._properties['groups'] = cleaned

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    def __enter__(self) -> 'APIGroupList':
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
            verbs: typing.List[str] = None,
            version: str = None,
    ):
        """Create APIResource instance."""
        super(APIResource, self).__init__(
            api_version='meta/v1',
            kind='APIResource'
        )
        self._properties = {
            'categories': categories or [],
            'group': group or '',
            'kind': kind or '',
            'name': name or '',
            'namespaced': namespaced or None,
            'shortNames': short_names or [],
            'singularName': singular_name or '',
            'verbs': verbs or [],
            'version': version or '',

        }
        self._types = {
            'categories': (list, str),
            'group': (str, None),
            'kind': (str, None),
            'name': (str, None),
            'namespaced': (bool, None),
            'shortNames': (list, str),
            'singularName': (str, None),
            'verbs': (list, str),
            'version': (str, None),

        }

    @property
    def categories(self) -> typing.List[str]:
        """
        categories is a list of the grouped resources this resource
        belongs to (e.g. 'all')
        """
        return self._properties.get('categories')

    @categories.setter
    def categories(self, value: typing.List[str]):
        """
        categories is a list of the grouped resources this resource
        belongs to (e.g. 'all')
        """
        self._properties['categories'] = value

    @property
    def group(self) -> str:
        """
        group is the preferred group of the resource.  Empty implies
        the group of the containing resource list. For subresources,
        this may have a different value, for example: Scale".
        """
        return self._properties.get('group')

    @group.setter
    def group(self, value: str):
        """
        group is the preferred group of the resource.  Empty implies
        the group of the containing resource list. For subresources,
        this may have a different value, for example: Scale".
        """
        self._properties['group'] = value

    @property
    def kind(self) -> str:
        """
        kind is the kind for the resource (e.g. 'Foo' is the kind
        for a resource 'foo')
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        kind is the kind for the resource (e.g. 'Foo' is the kind
        for a resource 'foo')
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        name is the plural name of the resource.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name is the plural name of the resource.
        """
        self._properties['name'] = value

    @property
    def namespaced(self) -> bool:
        """
        namespaced indicates if a resource is namespaced or not.
        """
        return self._properties.get('namespaced')

    @namespaced.setter
    def namespaced(self, value: bool):
        """
        namespaced indicates if a resource is namespaced or not.
        """
        self._properties['namespaced'] = value

    @property
    def short_names(self) -> typing.List[str]:
        """
        shortNames is a list of suggested short names of the
        resource.
        """
        return self._properties.get('shortNames')

    @short_names.setter
    def short_names(self, value: typing.List[str]):
        """
        shortNames is a list of suggested short names of the
        resource.
        """
        self._properties['shortNames'] = value

    @property
    def singular_name(self) -> str:
        """
        singularName is the singular name of the resource.  This
        allows clients to handle plural and singular opaquely. The
        singularName is more correct for reporting status on a
        single item and both singular and plural are allowed from
        the kubectl CLI interface.
        """
        return self._properties.get('singularName')

    @singular_name.setter
    def singular_name(self, value: str):
        """
        singularName is the singular name of the resource.  This
        allows clients to handle plural and singular opaquely. The
        singularName is more correct for reporting status on a
        single item and both singular and plural are allowed from
        the kubectl CLI interface.
        """
        self._properties['singularName'] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        verbs is a list of supported kube verbs (this includes get,
        list, watch, create, update, patch, delete,
        deletecollection, and proxy)
        """
        return self._properties.get('verbs')

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        verbs is a list of supported kube verbs (this includes get,
        list, watch, create, update, patch, delete,
        deletecollection, and proxy)
        """
        self._properties['verbs'] = value

    @property
    def version(self) -> str:
        """
        version is the preferred version of the resource.  Empty
        implies the version of the containing resource list For
        subresources, this may have a different value, for example:
        v1 (while inside a v1beta1 version of the core resource's
        group)".
        """
        return self._properties.get('version')

    @version.setter
    def version(self, value: str):
        """
        version is the preferred version of the resource.  Empty
        implies the version of the containing resource list For
        subresources, this may have a different value, for example:
        v1 (while inside a v1beta1 version of the core resource's
        group)".
        """
        self._properties['version'] = value

    def __enter__(self) -> 'APIResource':
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
            resources: typing.List['APIResource'] = None,
    ):
        """Create APIResourceList instance."""
        super(APIResourceList, self).__init__(
            api_version='meta/v1',
            kind='APIResourceList'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'groupVersion': group_version or '',
            'kind': kind or '',
            'resources': resources or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'groupVersion': (str, None),
            'kind': (str, None),
            'resources': (list, APIResource),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

    @property
    def group_version(self) -> str:
        """
        groupVersion is the group and version this APIResourceList
        is for.
        """
        return self._properties.get('groupVersion')

    @group_version.setter
    def group_version(self, value: str):
        """
        groupVersion is the group and version this APIResourceList
        is for.
        """
        self._properties['groupVersion'] = value

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    @property
    def resources(self) -> typing.List['APIResource']:
        """
        resources contains the name of the resources and if they are
        namespaced.
        """
        return self._properties.get('resources')

    @resources.setter
    def resources(
            self,
            value: typing.Union[typing.List['APIResource'], typing.List[dict]]
    ):
        """
        resources contains the name of the resources and if they are
        namespaced.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = APIResource().from_dict(item)
            cleaned.append(item)
        self._properties['resources'] = cleaned

    def __enter__(self) -> 'APIResourceList':
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
            server_address_by_client_cidrs: typing.List['ServerAddressByClientCIDR'] = None,
            versions: typing.List[str] = None,
    ):
        """Create APIVersions instance."""
        super(APIVersions, self).__init__(
            api_version='meta/v1',
            kind='APIVersions'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'kind': kind or '',
            'serverAddressByClientCIDRs': server_address_by_client_cidrs or [],
            'versions': versions or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'serverAddressByClientCIDRs': (list, ServerAddressByClientCIDR),
            'versions': (list, str),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    @property
    def server_address_by_client_cidrs(self) -> typing.List['ServerAddressByClientCIDR']:
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
        return self._properties.get('serverAddressByClientCIDRs')

    @server_address_by_client_cidrs.setter
    def server_address_by_client_cidrs(
            self,
            value: typing.Union[typing.List['ServerAddressByClientCIDR'], typing.List[dict]]
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
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ServerAddressByClientCIDR().from_dict(item)
            cleaned.append(item)
        self._properties['serverAddressByClientCIDRs'] = cleaned

    @property
    def versions(self) -> typing.List[str]:
        """
        versions are the api versions that are available.
        """
        return self._properties.get('versions')

    @versions.setter
    def versions(self, value: typing.List[str]):
        """
        versions are the api versions that are available.
        """
        self._properties['versions'] = value

    def __enter__(self) -> 'APIVersions':
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
            preconditions: 'Preconditions' = None,
            propagation_policy: str = None,
    ):
        """Create DeleteOptions instance."""
        super(DeleteOptions, self).__init__(
            api_version='meta/v1',
            kind='DeleteOptions'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'dryRun': dry_run or [],
            'gracePeriodSeconds': grace_period_seconds or None,
            'kind': kind or '',
            'orphanDependents': orphan_dependents or None,
            'preconditions': preconditions or Preconditions(),
            'propagationPolicy': propagation_policy or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'dryRun': (list, str),
            'gracePeriodSeconds': (int, None),
            'kind': (str, None),
            'orphanDependents': (bool, None),
            'preconditions': (Preconditions, None),
            'propagationPolicy': (str, None),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

    @property
    def dry_run(self) -> typing.List[str]:
        """
        When present, indicates that modifications should not be
        persisted. An invalid or unrecognized dryRun directive will
        result in an error response and no further processing of the
        request. Valid values are: - All: all dry run stages will be
        processed
        """
        return self._properties.get('dryRun')

    @dry_run.setter
    def dry_run(self, value: typing.List[str]):
        """
        When present, indicates that modifications should not be
        persisted. An invalid or unrecognized dryRun directive will
        result in an error response and no further processing of the
        request. Valid values are: - All: all dry run stages will be
        processed
        """
        self._properties['dryRun'] = value

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
        return self._properties.get('gracePeriodSeconds')

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
        self._properties['gracePeriodSeconds'] = value

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    @property
    def orphan_dependents(self) -> bool:
        """
        Deprecated: please use the PropagationPolicy, this field
        will be deprecated in 1.7. Should the dependent objects be
        orphaned. If true/false, the "orphan" finalizer will be
        added to/removed from the object's finalizers list. Either
        this field or PropagationPolicy may be set, but not both.
        """
        return self._properties.get('orphanDependents')

    @orphan_dependents.setter
    def orphan_dependents(self, value: bool):
        """
        Deprecated: please use the PropagationPolicy, this field
        will be deprecated in 1.7. Should the dependent objects be
        orphaned. If true/false, the "orphan" finalizer will be
        added to/removed from the object's finalizers list. Either
        this field or PropagationPolicy may be set, but not both.
        """
        self._properties['orphanDependents'] = value

    @property
    def preconditions(self) -> 'Preconditions':
        """
        Must be fulfilled before a deletion is carried out. If not
        possible, a 409 Conflict status will be returned.
        """
        return self._properties.get('preconditions')

    @preconditions.setter
    def preconditions(self, value: typing.Union['Preconditions', dict]):
        """
        Must be fulfilled before a deletion is carried out. If not
        possible, a 409 Conflict status will be returned.
        """
        if isinstance(value, dict):
            value = Preconditions().from_dict(value)
        self._properties['preconditions'] = value

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
        return self._properties.get('propagationPolicy')

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
        self._properties['propagationPolicy'] = value

    def __enter__(self) -> 'DeleteOptions':
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
            api_version='meta/v1',
            kind='GroupVersionForDiscovery'
        )
        self._properties = {
            'groupVersion': group_version or '',
            'version': version or '',

        }
        self._types = {
            'groupVersion': (str, None),
            'version': (str, None),

        }

    @property
    def group_version(self) -> str:
        """
        groupVersion specifies the API group and version in the form
        "group/version"
        """
        return self._properties.get('groupVersion')

    @group_version.setter
    def group_version(self, value: str):
        """
        groupVersion specifies the API group and version in the form
        "group/version"
        """
        self._properties['groupVersion'] = value

    @property
    def version(self) -> str:
        """
        version specifies the version in the form of "version". This
        is to save the clients the trouble of splitting the
        GroupVersion.
        """
        return self._properties.get('version')

    @version.setter
    def version(self, value: str):
        """
        version specifies the version in the form of "version". This
        is to save the clients the trouble of splitting the
        GroupVersion.
        """
        self._properties['version'] = value

    def __enter__(self) -> 'GroupVersionForDiscovery':
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
        super(Initializer, self).__init__(
            api_version='meta/v1',
            kind='Initializer'
        )
        self._properties = {
            'name': name or '',

        }
        self._types = {
            'name': (str, None),

        }

    @property
    def name(self) -> str:
        """
        name of the process that is responsible for initializing
        this object.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        name of the process that is responsible for initializing
        this object.
        """
        self._properties['name'] = value

    def __enter__(self) -> 'Initializer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Initializers(_kuber_definitions.Definition):
    """
    Initializers tracks the progress of initialization.
    """

    def __init__(
            self,
            pending: typing.List['Initializer'] = None,
            result: 'Status' = None,
    ):
        """Create Initializers instance."""
        super(Initializers, self).__init__(
            api_version='meta/v1',
            kind='Initializers'
        )
        self._properties = {
            'pending': pending or [],
            'result': result or Status(),

        }
        self._types = {
            'pending': (list, Initializer),
            'result': (Status, None),

        }

    @property
    def pending(self) -> typing.List['Initializer']:
        """
        Pending is a list of initializers that must execute in order
        before this object is visible. When the last pending
        initializer is removed, and no failing result is set, the
        initializers struct will be set to nil and the object is
        considered as initialized and visible to all clients.
        """
        return self._properties.get('pending')

    @pending.setter
    def pending(
            self,
            value: typing.Union[typing.List['Initializer'], typing.List[dict]]
    ):
        """
        Pending is a list of initializers that must execute in order
        before this object is visible. When the last pending
        initializer is removed, and no failing result is set, the
        initializers struct will be set to nil and the object is
        considered as initialized and visible to all clients.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Initializer().from_dict(item)
            cleaned.append(item)
        self._properties['pending'] = cleaned

    @property
    def result(self) -> 'Status':
        """
        If result is set with the Failure field, the object will be
        persisted to storage and then deleted, ensuring that other
        clients can observe the deletion.
        """
        return self._properties.get('result')

    @result.setter
    def result(self, value: typing.Union['Status', dict]):
        """
        If result is set with the Failure field, the object will be
        persisted to storage and then deleted, ensuring that other
        clients can observe the deletion.
        """
        if isinstance(value, dict):
            value = Status().from_dict(value)
        self._properties['result'] = value

    def __enter__(self) -> 'Initializers':
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
            match_expressions: typing.List['LabelSelectorRequirement'] = None,
            match_labels: dict = None,
    ):
        """Create LabelSelector instance."""
        super(LabelSelector, self).__init__(
            api_version='meta/v1',
            kind='LabelSelector'
        )
        self._properties = {
            'matchExpressions': match_expressions or [],
            'matchLabels': match_labels or {},

        }
        self._types = {
            'matchExpressions': (list, LabelSelectorRequirement),
            'matchLabels': (dict, None),

        }

    @property
    def match_expressions(self) -> typing.List['LabelSelectorRequirement']:
        """
        matchExpressions is a list of label selector requirements.
        The requirements are ANDed.
        """
        return self._properties.get('matchExpressions')

    @match_expressions.setter
    def match_expressions(
            self,
            value: typing.Union[typing.List['LabelSelectorRequirement'], typing.List[dict]]
    ):
        """
        matchExpressions is a list of label selector requirements.
        The requirements are ANDed.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = LabelSelectorRequirement().from_dict(item)
            cleaned.append(item)
        self._properties['matchExpressions'] = cleaned

    @property
    def match_labels(self) -> dict:
        """
        matchLabels is a map of {key,value} pairs. A single
        {key,value} in the matchLabels map is equivalent to an
        element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only
        "value". The requirements are ANDed.
        """
        return self._properties.get('matchLabels')

    @match_labels.setter
    def match_labels(self, value: dict):
        """
        matchLabels is a map of {key,value} pairs. A single
        {key,value} in the matchLabels map is equivalent to an
        element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only
        "value". The requirements are ANDed.
        """
        self._properties['matchLabels'] = value

    def __enter__(self) -> 'LabelSelector':
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
            api_version='meta/v1',
            kind='LabelSelectorRequirement'
        )
        self._properties = {
            'key': key or '',
            'operator': operator or '',
            'values': values or [],

        }
        self._types = {
            'key': (str, None),
            'operator': (str, None),
            'values': (list, str),

        }

    @property
    def key(self) -> str:
        """
        key is the label key that the selector applies to.
        """
        return self._properties.get('key')

    @key.setter
    def key(self, value: str):
        """
        key is the label key that the selector applies to.
        """
        self._properties['key'] = value

    @property
    def operator(self) -> str:
        """
        operator represents a key's relationship to a set of values.
        Valid operators are In, NotIn, Exists and DoesNotExist.
        """
        return self._properties.get('operator')

    @operator.setter
    def operator(self, value: str):
        """
        operator represents a key's relationship to a set of values.
        Valid operators are In, NotIn, Exists and DoesNotExist.
        """
        self._properties['operator'] = value

    @property
    def values(self) -> typing.List[str]:
        """
        values is an array of string values. If the operator is In
        or NotIn, the values array must be non-empty. If the
        operator is Exists or DoesNotExist, the values array must be
        empty. This array is replaced during a strategic merge
        patch.
        """
        return self._properties.get('values')

    @values.setter
    def values(self, value: typing.List[str]):
        """
        values is an array of string values. If the operator is In
        or NotIn, the values array must be non-empty. If the
        operator is Exists or DoesNotExist, the values array must be
        empty. This array is replaced during a strategic merge
        patch.
        """
        self._properties['values'] = value

    def __enter__(self) -> 'LabelSelectorRequirement':
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
            resource_version: str = None,
            self_link: str = None,
    ):
        """Create ListMeta instance."""
        super(ListMeta, self).__init__(
            api_version='meta/v1',
            kind='ListMeta'
        )
        self._properties = {
            'continue': continue_ or '',
            'resourceVersion': resource_version or '',
            'selfLink': self_link or '',

        }
        self._types = {
            'continue': (str, None),
            'resourceVersion': (str, None),
            'selfLink': (str, None),

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
        return self._properties.get('continue')

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
        self._properties['continue'] = value

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
        return self._properties.get('resourceVersion')

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
        self._properties['resourceVersion'] = value

    @property
    def self_link(self) -> str:
        """
        selfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        return self._properties.get('selfLink')

    @self_link.setter
    def self_link(self, value: str):
        """
        selfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        self._properties['selfLink'] = value

    def __enter__(self) -> 'ListMeta':
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
        super(MicroTime, self).__init__(
            api_version='meta/v1',
            kind='MicroTime'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'MicroTime':
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
            initializers: 'Initializers' = None,
            labels: dict = None,
            name: str = None,
            namespace: str = None,
            owner_references: typing.List['OwnerReference'] = None,
            resource_version: str = None,
            self_link: str = None,
            uid: str = None,
    ):
        """Create ObjectMeta instance."""
        super(ObjectMeta, self).__init__(
            api_version='meta/v1',
            kind='ObjectMeta'
        )
        self._properties = {
            'annotations': annotations or {},
            'clusterName': cluster_name or '',
            'creationTimestamp': creation_timestamp or None,
            'deletionGracePeriodSeconds': deletion_grace_period_seconds or None,
            'deletionTimestamp': deletion_timestamp or None,
            'finalizers': finalizers or [],
            'generateName': generate_name or '',
            'generation': generation or None,
            'initializers': initializers or Initializers(),
            'labels': labels or {},
            'name': name or '',
            'namespace': namespace or '',
            'ownerReferences': owner_references or [],
            'resourceVersion': resource_version or '',
            'selfLink': self_link or '',
            'uid': uid or '',

        }
        self._types = {
            'annotations': (dict, None),
            'clusterName': (str, None),
            'creationTimestamp': (str, None),
            'deletionGracePeriodSeconds': (int, None),
            'deletionTimestamp': (str, None),
            'finalizers': (list, str),
            'generateName': (str, None),
            'generation': (int, None),
            'initializers': (Initializers, None),
            'labels': (dict, None),
            'name': (str, None),
            'namespace': (str, None),
            'ownerReferences': (list, OwnerReference),
            'resourceVersion': (str, None),
            'selfLink': (str, None),
            'uid': (str, None),

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
        return self._properties.get('annotations')

    @annotations.setter
    def annotations(self, value: dict):
        """
        Annotations is an unstructured key value map stored with a
        resource that may be set by external tools to store and
        retrieve arbitrary metadata. They are not queryable and
        should be preserved when modifying objects. More info:
        http://kubernetes.io/docs/user-guide/annotations
        """
        self._properties['annotations'] = value

    @property
    def cluster_name(self) -> str:
        """
        The name of the cluster which the object belongs to. This is
        used to distinguish resources with same name and namespace
        in different clusters. This field is not set anywhere right
        now and apiserver is going to ignore it if set in create or
        update request.
        """
        return self._properties.get('clusterName')

    @cluster_name.setter
    def cluster_name(self, value: str):
        """
        The name of the cluster which the object belongs to. This is
        used to distinguish resources with same name and namespace
        in different clusters. This field is not set anywhere right
        now and apiserver is going to ignore it if set in create or
        update request.
        """
        self._properties['clusterName'] = value

    @property
    def creation_timestamp(self) -> str:
        """
        CreationTimestamp is a timestamp representing the server
        time when this object was created. It is not guaranteed to
        be set in happens-before order across separate operations.
        Clients may not set this value. It is represented in RFC3339
        form and is in UTC.

        Populated by the system. Read-only.
        Null for lists. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('creationTimestamp')

    @creation_timestamp.setter
    def creation_timestamp(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        CreationTimestamp is a timestamp representing the server
        time when this object was created. It is not guaranteed to
        be set in happens-before order across separate operations.
        Clients may not set this value. It is represented in RFC3339
        form and is in UTC.

        Populated by the system. Read-only.
        Null for lists. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['creationTimestamp'] = value

    @property
    def deletion_grace_period_seconds(self) -> int:
        """
        Number of seconds allowed for this object to gracefully
        terminate before it will be removed from the system. Only
        set when deletionTimestamp is also set. May only be
        shortened. Read-only.
        """
        return self._properties.get('deletionGracePeriodSeconds')

    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, value: int):
        """
        Number of seconds allowed for this object to gracefully
        terminate before it will be removed from the system. Only
        set when deletionTimestamp is also set. May only be
        shortened. Read-only.
        """
        self._properties['deletionGracePeriodSeconds'] = value

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

        Populated by the system when a graceful
        deletion is requested. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('deletionTimestamp')

    @deletion_timestamp.setter
    def deletion_timestamp(
            self,
            value: typing.Union[str, _datetime.datetime, _datetime.date]
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

        Populated by the system when a graceful
        deletion is requested. Read-only. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(value, _datetime.date):
            value = value.strftime('%Y-%m-%dT00:00:00Z')
        self._properties['deletionTimestamp'] = value

    @property
    def finalizers(self) -> typing.List[str]:
        """
        Must be empty before the object is deleted from the
        registry. Each entry is an identifier for the responsible
        component that will remove the entry from the list. If the
        deletionTimestamp of the object is non-nil, entries in this
        list can only be removed.
        """
        return self._properties.get('finalizers')

    @finalizers.setter
    def finalizers(self, value: typing.List[str]):
        """
        Must be empty before the object is deleted from the
        registry. Each entry is an identifier for the responsible
        component that will remove the entry from the list. If the
        deletionTimestamp of the object is non-nil, entries in this
        list can only be removed.
        """
        self._properties['finalizers'] = value

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

        If this field is
        specified and the generated name exists, the server will NOT
        return a 409 - instead, it will either return 201 Created or
        500 with Reason ServerTimeout indicating a unique name could
        not be found in the time allotted, and the client should
        retry (optionally after the time indicated in the Retry-
        After header).

        Applied only if Name is not specified. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#idempotency
        """
        return self._properties.get('generateName')

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

        If this field is
        specified and the generated name exists, the server will NOT
        return a 409 - instead, it will either return 201 Created or
        500 with Reason ServerTimeout indicating a unique name could
        not be found in the time allotted, and the client should
        retry (optionally after the time indicated in the Retry-
        After header).

        Applied only if Name is not specified. More
        info: https://git.k8s.io/community/contributors/devel/api-
        conventions.md#idempotency
        """
        self._properties['generateName'] = value

    @property
    def generation(self) -> int:
        """
        A sequence number representing a specific generation of the
        desired state. Populated by the system. Read-only.
        """
        return self._properties.get('generation')

    @generation.setter
    def generation(self, value: int):
        """
        A sequence number representing a specific generation of the
        desired state. Populated by the system. Read-only.
        """
        self._properties['generation'] = value

    @property
    def initializers(self) -> 'Initializers':
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
        """
        return self._properties.get('initializers')

    @initializers.setter
    def initializers(self, value: typing.Union['Initializers', dict]):
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
        """
        if isinstance(value, dict):
            value = Initializers().from_dict(value)
        self._properties['initializers'] = value

    @property
    def labels(self) -> dict:
        """
        Map of string keys and values that can be used to organize
        and categorize (scope and select) objects. May match
        selectors of replication controllers and services. More
        info: http://kubernetes.io/docs/user-guide/labels
        """
        return self._properties.get('labels')

    @labels.setter
    def labels(self, value: dict):
        """
        Map of string keys and values that can be used to organize
        and categorize (scope and select) objects. May match
        selectors of replication controllers and services. More
        info: http://kubernetes.io/docs/user-guide/labels
        """
        self._properties['labels'] = value

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
        return self._properties.get('name')

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
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        Namespace defines the space within each name must be unique.
        An empty namespace is equivalent to the "default" namespace,
        but "default" is the canonical representation. Not all
        objects are required to be scoped to a namespace - the value
        of this field for those objects will be empty.

        Must be a
        DNS_LABEL. Cannot be updated. More info:
        http://kubernetes.io/docs/user-guide/namespaces
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace defines the space within each name must be unique.
        An empty namespace is equivalent to the "default" namespace,
        but "default" is the canonical representation. Not all
        objects are required to be scoped to a namespace - the value
        of this field for those objects will be empty.

        Must be a
        DNS_LABEL. Cannot be updated. More info:
        http://kubernetes.io/docs/user-guide/namespaces
        """
        self._properties['namespace'] = value

    @property
    def owner_references(self) -> typing.List['OwnerReference']:
        """
        List of objects depended by this object. If ALL objects in
        the list have been deleted, this object will be garbage
        collected. If this object is managed by a controller, then
        an entry in this list will point to this controller, with
        the controller field set to true. There cannot be more than
        one managing controller.
        """
        return self._properties.get('ownerReferences')

    @owner_references.setter
    def owner_references(
            self,
            value: typing.Union[typing.List['OwnerReference'], typing.List[dict]]
    ):
        """
        List of objects depended by this object. If ALL objects in
        the list have been deleted, this object will be garbage
        collected. If this object is managed by a controller, then
        an entry in this list will point to this controller, with
        the controller field set to true. There cannot be more than
        one managing controller.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = OwnerReference().from_dict(item)
            cleaned.append(item)
        self._properties['ownerReferences'] = cleaned

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

        Populated by
        the system. Read-only. Value must be treated as opaque by
        clients and . More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        return self._properties.get('resourceVersion')

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

        Populated by
        the system. Read-only. Value must be treated as opaque by
        clients and . More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#concurrency-control-and-consistency
        """
        self._properties['resourceVersion'] = value

    @property
    def self_link(self) -> str:
        """
        SelfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        return self._properties.get('selfLink')

    @self_link.setter
    def self_link(self, value: str):
        """
        SelfLink is a URL representing this object. Populated by the
        system. Read-only.
        """
        self._properties['selfLink'] = value

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
        return self._properties.get('uid')

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
        self._properties['uid'] = value

    def __enter__(self) -> 'ObjectMeta':
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
            api_version='meta/v1',
            kind='OwnerReference'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'blockOwnerDeletion': block_owner_deletion or None,
            'controller': controller or None,
            'kind': kind or '',
            'name': name or '',
            'uid': uid or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'blockOwnerDeletion': (bool, None),
            'controller': (bool, None),
            'kind': (str, None),
            'name': (str, None),
            'uid': (str, None),

        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent.
        """
        return self._properties.get('apiVersion')

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent.
        """
        self._properties['apiVersion'] = value

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
        return self._properties.get('blockOwnerDeletion')

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
        self._properties['blockOwnerDeletion'] = value

    @property
    def controller(self) -> bool:
        """
        If true, this reference points to the managing controller.
        """
        return self._properties.get('controller')

    @controller.setter
    def controller(self, value: bool):
        """
        If true, this reference points to the managing controller.
        """
        self._properties['controller'] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        Name of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#names
        """
        self._properties['name'] = value

    @property
    def uid(self) -> str:
        """
        UID of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        UID of the referent. More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        self._properties['uid'] = value

    def __enter__(self) -> 'OwnerReference':
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
        super(Patch, self).__init__(
            api_version='meta/v1',
            kind='Patch'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Patch':
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
            uid: str = None,
    ):
        """Create Preconditions instance."""
        super(Preconditions, self).__init__(
            api_version='meta/v1',
            kind='Preconditions'
        )
        self._properties = {
            'uid': uid or '',

        }
        self._types = {
            'uid': (str, None),

        }

    @property
    def uid(self) -> str:
        """
        Specifies the target UID.
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        Specifies the target UID.
        """
        self._properties['uid'] = value

    def __enter__(self) -> 'Preconditions':
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
            api_version='meta/v1',
            kind='ServerAddressByClientCIDR'
        )
        self._properties = {
            'clientCIDR': client_cidr or '',
            'serverAddress': server_address or '',

        }
        self._types = {
            'clientCIDR': (str, None),
            'serverAddress': (str, None),

        }

    @property
    def client_cidr(self) -> str:
        """
        The CIDR with which clients can match their IP to figure out
        the server address that they should use.
        """
        return self._properties.get('clientCIDR')

    @client_cidr.setter
    def client_cidr(self, value: str):
        """
        The CIDR with which clients can match their IP to figure out
        the server address that they should use.
        """
        self._properties['clientCIDR'] = value

    @property
    def server_address(self) -> str:
        """
        Address of this server, suitable for a client that matches
        the above CIDR. This can be a hostname, hostname:port, IP or
        IP:port.
        """
        return self._properties.get('serverAddress')

    @server_address.setter
    def server_address(self, value: str):
        """
        Address of this server, suitable for a client that matches
        the above CIDR. This can be a hostname, hostname:port, IP or
        IP:port.
        """
        self._properties['serverAddress'] = value

    def __enter__(self) -> 'ServerAddressByClientCIDR':
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
            details: 'StatusDetails' = None,
            kind: str = None,
            message: str = None,
            metadata: 'ListMeta' = None,
            reason: str = None,
            status: str = None,
    ):
        """Create Status instance."""
        super(Status, self).__init__(
            api_version='meta/v1',
            kind='Status'
        )
        self._properties = {
            'apiVersion': api_version or '',
            'code': code or None,
            'details': details or StatusDetails(),
            'kind': kind or '',
            'message': message or '',
            'metadata': metadata or ListMeta(),
            'reason': reason or '',
            'status': status or '',

        }
        self._types = {
            'apiVersion': (str, None),
            'code': (int, None),
            'details': (StatusDetails, None),
            'kind': (str, None),
            'message': (str, None),
            'metadata': (ListMeta, None),
            'reason': (str, None),
            'status': (str, None),

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
        return self._properties.get('apiVersion')

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
        self._properties['apiVersion'] = value

    @property
    def code(self) -> int:
        """
        Suggested HTTP return code for this status, 0 if not set.
        """
        return self._properties.get('code')

    @code.setter
    def code(self, value: int):
        """
        Suggested HTTP return code for this status, 0 if not set.
        """
        self._properties['code'] = value

    @property
    def details(self) -> 'StatusDetails':
        """
        Extended data associated with the reason.  Each reason may
        define its own extended details. This field is optional and
        the data returned is not guaranteed to conform to any schema
        except that defined by the reason type.
        """
        return self._properties.get('details')

    @details.setter
    def details(self, value: typing.Union['StatusDetails', dict]):
        """
        Extended data associated with the reason.  Each reason may
        define its own extended details. This field is optional and
        the data returned is not guaranteed to conform to any schema
        except that defined by the reason type.
        """
        if isinstance(value, dict):
            value = StatusDetails().from_dict(value)
        self._properties['details'] = value

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
        return self._properties.get('kind')

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
        self._properties['kind'] = value

    @property
    def message(self) -> str:
        """
        A human-readable description of the status of this
        operation.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human-readable description of the status of this
        operation.
        """
        self._properties['message'] = value

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def reason(self) -> str:
        """
        A machine-readable description of why this operation is in
        the "Failure" status. If this value is empty there is no
        information available. A Reason clarifies an HTTP status
        code but does not override it.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        A machine-readable description of why this operation is in
        the "Failure" status. If this value is empty there is no
        information available. A Reason clarifies an HTTP status
        code but does not override it.
        """
        self._properties['reason'] = value

    @property
    def status(self) -> str:
        """
        Status of the operation. One of: "Success" or "Failure".
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: str):
        """
        Status of the operation. One of: "Success" or "Failure".
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        self._properties['status'] = value

    def __enter__(self) -> 'Status':
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
        super(StatusCause, self).__init__(
            api_version='meta/v1',
            kind='StatusCause'
        )
        self._properties = {
            'field': field or '',
            'message': message or '',
            'reason': reason or '',

        }
        self._types = {
            'field': (str, None),
            'message': (str, None),
            'reason': (str, None),

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
        "items[0].name" - the field "name" on the first array entry
        in "items"
        """
        return self._properties.get('field')

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
        "items[0].name" - the field "name" on the first array entry
        in "items"
        """
        self._properties['field'] = value

    @property
    def message(self) -> str:
        """
        A human-readable description of the cause of the error.
        This field may be presented as-is to a reader.
        """
        return self._properties.get('message')

    @message.setter
    def message(self, value: str):
        """
        A human-readable description of the cause of the error.
        This field may be presented as-is to a reader.
        """
        self._properties['message'] = value

    @property
    def reason(self) -> str:
        """
        A machine-readable description of the cause of the error. If
        this value is empty there is no information available.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        A machine-readable description of the cause of the error. If
        this value is empty there is no information available.
        """
        self._properties['reason'] = value

    def __enter__(self) -> 'StatusCause':
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
            causes: typing.List['StatusCause'] = None,
            group: str = None,
            kind: str = None,
            name: str = None,
            retry_after_seconds: int = None,
            uid: str = None,
    ):
        """Create StatusDetails instance."""
        super(StatusDetails, self).__init__(
            api_version='meta/v1',
            kind='StatusDetails'
        )
        self._properties = {
            'causes': causes or [],
            'group': group or '',
            'kind': kind or '',
            'name': name or '',
            'retryAfterSeconds': retry_after_seconds or None,
            'uid': uid or '',

        }
        self._types = {
            'causes': (list, StatusCause),
            'group': (str, None),
            'kind': (str, None),
            'name': (str, None),
            'retryAfterSeconds': (int, None),
            'uid': (str, None),

        }

    @property
    def causes(self) -> typing.List['StatusCause']:
        """
        The Causes array includes more details associated with the
        StatusReason failure. Not all StatusReasons may provide
        detailed causes.
        """
        return self._properties.get('causes')

    @causes.setter
    def causes(
            self,
            value: typing.Union[typing.List['StatusCause'], typing.List[dict]]
    ):
        """
        The Causes array includes more details associated with the
        StatusReason failure. Not all StatusReasons may provide
        detailed causes.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = StatusCause().from_dict(item)
            cleaned.append(item)
        self._properties['causes'] = cleaned

    @property
    def group(self) -> str:
        """
        The group attribute of the resource associated with the
        status StatusReason.
        """
        return self._properties.get('group')

    @group.setter
    def group(self, value: str):
        """
        The group attribute of the resource associated with the
        status StatusReason.
        """
        self._properties['group'] = value

    @property
    def kind(self) -> str:
        """
        The kind attribute of the resource associated with the
        status StatusReason. On some operations may differ from the
        requested resource Kind. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        return self._properties.get('kind')

    @kind.setter
    def kind(self, value: str):
        """
        The kind attribute of the resource associated with the
        status StatusReason. On some operations may differ from the
        requested resource Kind. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#types-kinds
        """
        self._properties['kind'] = value

    @property
    def name(self) -> str:
        """
        The name attribute of the resource associated with the
        status StatusReason (when there is a single name which can
        be described).
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        The name attribute of the resource associated with the
        status StatusReason (when there is a single name which can
        be described).
        """
        self._properties['name'] = value

    @property
    def retry_after_seconds(self) -> int:
        """
        If specified, the time in seconds before the operation
        should be retried. Some errors may indicate the client must
        take an alternate action - for those errors this field may
        indicate how long to wait before taking the alternate
        action.
        """
        return self._properties.get('retryAfterSeconds')

    @retry_after_seconds.setter
    def retry_after_seconds(self, value: int):
        """
        If specified, the time in seconds before the operation
        should be retried. Some errors may indicate the client must
        take an alternate action - for those errors this field may
        indicate how long to wait before taking the alternate
        action.
        """
        self._properties['retryAfterSeconds'] = value

    @property
    def uid(self) -> str:
        """
        UID of the resource. (when there is a single resource which
        can be described). More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        UID of the resource. (when there is a single resource which
        can be described). More info:
        http://kubernetes.io/docs/user-guide/identifiers#uids
        """
        self._properties['uid'] = value

    def __enter__(self) -> 'StatusDetails':
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
        super(Time, self).__init__(
            api_version='meta/v1',
            kind='Time'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Time':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WatchEvent(_kuber_definitions.Definition):
    """
    Event represents a single event to a watched resource.
    """

    def __init__(
            self,
            object_: 'RawExtension' = None,
            type_: str = None,
    ):
        """Create WatchEvent instance."""
        super(WatchEvent, self).__init__(
            api_version='meta/v1',
            kind='WatchEvent'
        )
        self._properties = {
            'object': object_ or RawExtension(),
            'type': type_ or '',

        }
        self._types = {
            'object': (RawExtension, None),
            'type': (str, None),

        }

    @property
    def object_(self) -> 'RawExtension':
        """
        Object is:
         * If Type is Added or Modified: the new state of
        the object.
         * If Type is Deleted: the state of the object
        immediately before deletion.
         * If Type is Error: *Status is
        recommended; other types may make sense
           depending on
        context.
        """
        return self._properties.get('object')

    @object_.setter
    def object_(self, value: typing.Union['RawExtension', dict]):
        """
        Object is:
         * If Type is Added or Modified: the new state of
        the object.
         * If Type is Deleted: the state of the object
        immediately before deletion.
         * If Type is Error: *Status is
        recommended; other types may make sense
           depending on
        context.
        """
        if isinstance(value, dict):
            value = RawExtension().from_dict(value)
        self._properties['object'] = value

    @property
    def type_(self) -> str:
        """

        """
        return self._properties.get('type')

    @type_.setter
    def type_(self, value: str):
        """

        """
        self._properties['type'] = value

    def __enter__(self) -> 'WatchEvent':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

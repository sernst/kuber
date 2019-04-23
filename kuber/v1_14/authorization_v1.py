import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_14.meta_v1 import ListMeta
from kuber.v1_14.meta_v1 import ObjectMeta
from kuber.v1_14.meta_v1 import Status
from kuber.v1_14.meta_v1 import StatusDetails


class LocalSubjectAccessReview(_kuber_definitions.Resource):
    """
    LocalSubjectAccessReview checks whether or not a user or
    group can perform an action in a given namespace. Having a
    namespace scoped resource makes it much easier to grant
    namespace scoped policy that includes permissions checking.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'SubjectAccessReviewSpec' = None,
    ):
        """Create LocalSubjectAccessReview instance."""
        super(LocalSubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='LocalSubjectAccessReview'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or SubjectAccessReviewSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (SubjectAccessReviewSpec, None),
            'status': (SubjectAccessReviewStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'SubjectAccessReviewSpec':
        """
        Spec holds information about the request being evaluated.
        spec.namespace must be equal to the namespace you made the
        request against.  If empty, it is defaulted.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['SubjectAccessReviewSpec', dict]):
        """
        Spec holds information about the request being evaluated.
        spec.namespace must be equal to the namespace you made the
        request against.  If empty, it is defaulted.
        """
        if isinstance(value, dict):
            value = SubjectAccessReviewSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'LocalSubjectAccessReviewStatus':
        """
        Creates the LocalSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_local_subject_access_review',
            'create_local_subject_access_review'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            LocalSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'LocalSubjectAccessReviewStatus':
        """
        Replaces the LocalSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_local_subject_access_review',
            'replace_local_subject_access_review'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            LocalSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'LocalSubjectAccessReviewStatus':
        """
        Patches the LocalSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_local_subject_access_review',
            'patch_local_subject_access_review'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            LocalSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'LocalSubjectAccessReviewStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_local_subject_access_review',
            'read_local_subject_access_review'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            LocalSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the LocalSubjectAccessReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_local_subject_access_review',
            'read_local_subject_access_review'
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
        Deletes the LocalSubjectAccessReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_local_subject_access_review',
            'delete_local_subject_access_review'
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
    ) -> 'client.AuthorizationV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuthorizationV1Api(**kwargs)

    def __enter__(self) -> 'LocalSubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NonResourceAttributes(_kuber_definitions.Definition):
    """
    NonResourceAttributes includes the authorization attributes
    available for non-resource requests to the Authorizer
    interface
    """

    def __init__(
            self,
            path: str = None,
            verb: str = None,
    ):
        """Create NonResourceAttributes instance."""
        super(NonResourceAttributes, self).__init__(
            api_version='authorization/v1',
            kind='NonResourceAttributes'
        )
        self._properties = {
            'path': path or '',
            'verb': verb or '',

        }
        self._types = {
            'path': (str, None),
            'verb': (str, None),

        }

    @property
    def path(self) -> str:
        """
        Path is the URL path of the request
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is the URL path of the request
        """
        self._properties['path'] = value

    @property
    def verb(self) -> str:
        """
        Verb is the standard HTTP verb
        """
        return self._properties.get('verb')

    @verb.setter
    def verb(self, value: str):
        """
        Verb is the standard HTTP verb
        """
        self._properties['verb'] = value

    def __enter__(self) -> 'NonResourceAttributes':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NonResourceRule(_kuber_definitions.Definition):
    """
    NonResourceRule holds information that describes a rule for
    the non-resource
    """

    def __init__(
            self,
            non_resource_urls: typing.List[str] = None,
            verbs: typing.List[str] = None,
    ):
        """Create NonResourceRule instance."""
        super(NonResourceRule, self).__init__(
            api_version='authorization/v1',
            kind='NonResourceRule'
        )
        self._properties = {
            'nonResourceURLs': non_resource_urls or [],
            'verbs': verbs or [],

        }
        self._types = {
            'nonResourceURLs': (list, str),
            'verbs': (list, str),

        }

    @property
    def non_resource_urls(self) -> typing.List[str]:
        """
        NonResourceURLs is a set of partial urls that a user should
        have access to.  *s are allowed, but only as the full, final
        step in the path.  "*" means all.
        """
        return self._properties.get('nonResourceURLs')

    @non_resource_urls.setter
    def non_resource_urls(self, value: typing.List[str]):
        """
        NonResourceURLs is a set of partial urls that a user should
        have access to.  *s are allowed, but only as the full, final
        step in the path.  "*" means all.
        """
        self._properties['nonResourceURLs'] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        Verb is a list of kubernetes non-resource API verbs, like:
        get, post, put, delete, patch, head, options.  "*" means
        all.
        """
        return self._properties.get('verbs')

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        Verb is a list of kubernetes non-resource API verbs, like:
        get, post, put, delete, patch, head, options.  "*" means
        all.
        """
        self._properties['verbs'] = value

    def __enter__(self) -> 'NonResourceRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceAttributes(_kuber_definitions.Definition):
    """
    ResourceAttributes includes the authorization attributes
    available for resource requests to the Authorizer interface
    """

    def __init__(
            self,
            group: str = None,
            name: str = None,
            namespace: str = None,
            resource: str = None,
            subresource: str = None,
            verb: str = None,
            version: str = None,
    ):
        """Create ResourceAttributes instance."""
        super(ResourceAttributes, self).__init__(
            api_version='authorization/v1',
            kind='ResourceAttributes'
        )
        self._properties = {
            'group': group or '',
            'name': name or '',
            'namespace': namespace or '',
            'resource': resource or '',
            'subresource': subresource or '',
            'verb': verb or '',
            'version': version or '',

        }
        self._types = {
            'group': (str, None),
            'name': (str, None),
            'namespace': (str, None),
            'resource': (str, None),
            'subresource': (str, None),
            'verb': (str, None),
            'version': (str, None),

        }

    @property
    def group(self) -> str:
        """
        Group is the API Group of the Resource.  "*" means all.
        """
        return self._properties.get('group')

    @group.setter
    def group(self, value: str):
        """
        Group is the API Group of the Resource.  "*" means all.
        """
        self._properties['group'] = value

    @property
    def name(self) -> str:
        """
        Name is the name of the resource being requested for a "get"
        or deleted for a "delete". "" (empty) means all.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the resource being requested for a "get"
        or deleted for a "delete". "" (empty) means all.
        """
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        Namespace is the namespace of the action being requested.
        Currently, there is no distinction between no namespace and
        all namespaces "" (empty) is defaulted for
        LocalSubjectAccessReviews "" (empty) is empty for cluster-
        scoped resources "" (empty) means "all" for namespace scoped
        resources from a SubjectAccessReview or
        SelfSubjectAccessReview
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace is the namespace of the action being requested.
        Currently, there is no distinction between no namespace and
        all namespaces "" (empty) is defaulted for
        LocalSubjectAccessReviews "" (empty) is empty for cluster-
        scoped resources "" (empty) means "all" for namespace scoped
        resources from a SubjectAccessReview or
        SelfSubjectAccessReview
        """
        self._properties['namespace'] = value

    @property
    def resource(self) -> str:
        """
        Resource is one of the existing resource types.  "*" means
        all.
        """
        return self._properties.get('resource')

    @resource.setter
    def resource(self, value: str):
        """
        Resource is one of the existing resource types.  "*" means
        all.
        """
        self._properties['resource'] = value

    @property
    def subresource(self) -> str:
        """
        Subresource is one of the existing resource types.  "" means
        none.
        """
        return self._properties.get('subresource')

    @subresource.setter
    def subresource(self, value: str):
        """
        Subresource is one of the existing resource types.  "" means
        none.
        """
        self._properties['subresource'] = value

    @property
    def verb(self) -> str:
        """
        Verb is a kubernetes resource API verb, like: get, list,
        watch, create, update, delete, proxy.  "*" means all.
        """
        return self._properties.get('verb')

    @verb.setter
    def verb(self, value: str):
        """
        Verb is a kubernetes resource API verb, like: get, list,
        watch, create, update, delete, proxy.  "*" means all.
        """
        self._properties['verb'] = value

    @property
    def version(self) -> str:
        """
        Version is the API Version of the Resource.  "*" means all.
        """
        return self._properties.get('version')

    @version.setter
    def version(self, value: str):
        """
        Version is the API Version of the Resource.  "*" means all.
        """
        self._properties['version'] = value

    def __enter__(self) -> 'ResourceAttributes':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceRule(_kuber_definitions.Definition):
    """
    ResourceRule is the list of actions the subject is allowed
    to perform on resources. The list ordering isn't
    significant, may contain duplicates, and possibly be
    incomplete.
    """

    def __init__(
            self,
            api_groups: typing.List[str] = None,
            resource_names: typing.List[str] = None,
            resources: typing.List[str] = None,
            verbs: typing.List[str] = None,
    ):
        """Create ResourceRule instance."""
        super(ResourceRule, self).__init__(
            api_version='authorization/v1',
            kind='ResourceRule'
        )
        self._properties = {
            'apiGroups': api_groups or [],
            'resourceNames': resource_names or [],
            'resources': resources or [],
            'verbs': verbs or [],

        }
        self._types = {
            'apiGroups': (list, str),
            'resourceNames': (list, str),
            'resources': (list, str),
            'verbs': (list, str),

        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        APIGroups is the name of the APIGroup that contains the
        resources.  If multiple API groups are specified, any action
        requested against one of the enumerated resources in any API
        group will be allowed.  "*" means all.
        """
        return self._properties.get('apiGroups')

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        APIGroups is the name of the APIGroup that contains the
        resources.  If multiple API groups are specified, any action
        requested against one of the enumerated resources in any API
        group will be allowed.  "*" means all.
        """
        self._properties['apiGroups'] = value

    @property
    def resource_names(self) -> typing.List[str]:
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.  "*" means all.
        """
        return self._properties.get('resourceNames')

    @resource_names.setter
    def resource_names(self, value: typing.List[str]):
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.  "*" means all.
        """
        self._properties['resourceNames'] = value

    @property
    def resources(self) -> typing.List[str]:
        """
        Resources is a list of resources this rule applies to.  "*"
        means all in the specified apiGroups.
         "*/foo" represents
        the subresource 'foo' for all resources in the specified
        apiGroups.
        """
        return self._properties.get('resources')

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        Resources is a list of resources this rule applies to.  "*"
        means all in the specified apiGroups.
         "*/foo" represents
        the subresource 'foo' for all resources in the specified
        apiGroups.
        """
        self._properties['resources'] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        Verb is a list of kubernetes resource API verbs, like: get,
        list, watch, create, update, delete, proxy.  "*" means all.
        """
        return self._properties.get('verbs')

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        Verb is a list of kubernetes resource API verbs, like: get,
        list, watch, create, update, delete, proxy.  "*" means all.
        """
        self._properties['verbs'] = value

    def __enter__(self) -> 'ResourceRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectAccessReview(_kuber_definitions.Resource):
    """
    SelfSubjectAccessReview checks whether or the current user
    can perform an action.  Not filling in a spec.namespace
    means "in all namespaces".  Self is a special case, because
    users should always be able to check whether they can
    perform an action
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'SelfSubjectAccessReviewSpec' = None,
    ):
        """Create SelfSubjectAccessReview instance."""
        super(SelfSubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectAccessReview'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or SelfSubjectAccessReviewSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (SelfSubjectAccessReviewSpec, None),
            'status': (SubjectAccessReviewStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'SelfSubjectAccessReviewSpec':
        """
        Spec holds information about the request being evaluated.
        user and groups must be empty
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['SelfSubjectAccessReviewSpec', dict]):
        """
        Spec holds information about the request being evaluated.
        user and groups must be empty
        """
        if isinstance(value, dict):
            value = SelfSubjectAccessReviewSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectAccessReviewStatus':
        """
        Creates the SelfSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_self_subject_access_review',
            'create_self_subject_access_review'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            SelfSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectAccessReviewStatus':
        """
        Replaces the SelfSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_self_subject_access_review',
            'replace_self_subject_access_review'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SelfSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectAccessReviewStatus':
        """
        Patches the SelfSubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_self_subject_access_review',
            'patch_self_subject_access_review'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SelfSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectAccessReviewStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_self_subject_access_review',
            'read_self_subject_access_review'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            SelfSubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the SelfSubjectAccessReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_self_subject_access_review',
            'read_self_subject_access_review'
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
        Deletes the SelfSubjectAccessReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_self_subject_access_review',
            'delete_self_subject_access_review'
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
    ) -> 'client.AuthorizationV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuthorizationV1Api(**kwargs)

    def __enter__(self) -> 'SelfSubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectAccessReviewSpec(_kuber_definitions.Definition):
    """
    SelfSubjectAccessReviewSpec is a description of the access
    request.  Exactly one of ResourceAuthorizationAttributes and
    NonResourceAuthorizationAttributes must be set
    """

    def __init__(
            self,
            non_resource_attributes: 'NonResourceAttributes' = None,
            resource_attributes: 'ResourceAttributes' = None,
    ):
        """Create SelfSubjectAccessReviewSpec instance."""
        super(SelfSubjectAccessReviewSpec, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectAccessReviewSpec'
        )
        self._properties = {
            'nonResourceAttributes': non_resource_attributes or NonResourceAttributes(),
            'resourceAttributes': resource_attributes or ResourceAttributes(),

        }
        self._types = {
            'nonResourceAttributes': (NonResourceAttributes, None),
            'resourceAttributes': (ResourceAttributes, None),

        }

    @property
    def non_resource_attributes(self) -> 'NonResourceAttributes':
        """
        NonResourceAttributes describes information for a non-
        resource access request
        """
        return self._properties.get('nonResourceAttributes')

    @non_resource_attributes.setter
    def non_resource_attributes(self, value: typing.Union['NonResourceAttributes', dict]):
        """
        NonResourceAttributes describes information for a non-
        resource access request
        """
        if isinstance(value, dict):
            value = NonResourceAttributes().from_dict(value)
        self._properties['nonResourceAttributes'] = value

    @property
    def resource_attributes(self) -> 'ResourceAttributes':
        """
        ResourceAuthorizationAttributes describes information for a
        resource access request
        """
        return self._properties.get('resourceAttributes')

    @resource_attributes.setter
    def resource_attributes(self, value: typing.Union['ResourceAttributes', dict]):
        """
        ResourceAuthorizationAttributes describes information for a
        resource access request
        """
        if isinstance(value, dict):
            value = ResourceAttributes().from_dict(value)
        self._properties['resourceAttributes'] = value

    def __enter__(self) -> 'SelfSubjectAccessReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectRulesReview(_kuber_definitions.Resource):
    """
    SelfSubjectRulesReview enumerates the set of actions the
    current user can perform within a namespace. The returned
    list of actions may be incomplete depending on the server's
    authorization mode, and any errors experienced during the
    evaluation. SelfSubjectRulesReview should be used by UIs to
    show/hide actions, or to quickly let an end user reason
    about their permissions. It should NOT Be used by external
    systems to drive authorization decisions as this raises
    confused deputy, cache lifetime/revocation, and correctness
    concerns. SubjectAccessReview, and LocalAccessReview are the
    correct way to defer authorization decisions to the API
    server.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'SelfSubjectRulesReviewSpec' = None,
    ):
        """Create SelfSubjectRulesReview instance."""
        super(SelfSubjectRulesReview, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectRulesReview'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or SelfSubjectRulesReviewSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (SelfSubjectRulesReviewSpec, None),
            'status': (SubjectRulesReviewStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'SelfSubjectRulesReviewSpec':
        """
        Spec holds information about the request being evaluated.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['SelfSubjectRulesReviewSpec', dict]):
        """
        Spec holds information about the request being evaluated.
        """
        if isinstance(value, dict):
            value = SelfSubjectRulesReviewSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectRulesReviewStatus':
        """
        Creates the SelfSubjectRulesReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_self_subject_rules_review',
            'create_self_subject_rules_review'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            SelfSubjectRulesReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectRulesReviewStatus':
        """
        Replaces the SelfSubjectRulesReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_self_subject_rules_review',
            'replace_self_subject_rules_review'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SelfSubjectRulesReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectRulesReviewStatus':
        """
        Patches the SelfSubjectRulesReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_self_subject_rules_review',
            'patch_self_subject_rules_review'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SelfSubjectRulesReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'SelfSubjectRulesReviewStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_self_subject_rules_review',
            'read_self_subject_rules_review'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            SelfSubjectRulesReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the SelfSubjectRulesReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_self_subject_rules_review',
            'read_self_subject_rules_review'
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
        Deletes the SelfSubjectRulesReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_self_subject_rules_review',
            'delete_self_subject_rules_review'
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
    ) -> 'client.AuthorizationV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuthorizationV1Api(**kwargs)

    def __enter__(self) -> 'SelfSubjectRulesReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectRulesReviewSpec(_kuber_definitions.Definition):
    """

    """

    def __init__(
            self,
            namespace: str = None,
    ):
        """Create SelfSubjectRulesReviewSpec instance."""
        super(SelfSubjectRulesReviewSpec, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectRulesReviewSpec'
        )
        self._properties = {
            'namespace': namespace or '',

        }
        self._types = {
            'namespace': (str, None),

        }

    @property
    def namespace(self) -> str:
        """
        Namespace to evaluate rules for. Required.
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace to evaluate rules for. Required.
        """
        self._properties['namespace'] = value

    def __enter__(self) -> 'SelfSubjectRulesReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReview(_kuber_definitions.Resource):
    """
    SubjectAccessReview checks whether or not a user or group
    can perform an action.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'SubjectAccessReviewSpec' = None,
    ):
        """Create SubjectAccessReview instance."""
        super(SubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReview'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or SubjectAccessReviewSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (SubjectAccessReviewSpec, None),
            'status': (SubjectAccessReviewStatus, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'SubjectAccessReviewSpec':
        """
        Spec holds information about the request being evaluated
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['SubjectAccessReviewSpec', dict]):
        """
        Spec holds information about the request being evaluated
        """
        if isinstance(value, dict):
            value = SubjectAccessReviewSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'SubjectAccessReviewStatus':
        """
        Creates the SubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_subject_access_review',
            'create_subject_access_review'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            SubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'SubjectAccessReviewStatus':
        """
        Replaces the SubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_subject_access_review',
            'replace_subject_access_review'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'SubjectAccessReviewStatus':
        """
        Patches the SubjectAccessReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_subject_access_review',
            'patch_subject_access_review'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            SubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'SubjectAccessReviewStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_subject_access_review',
            'read_subject_access_review'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            SubjectAccessReviewStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the SubjectAccessReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_subject_access_review',
            'read_subject_access_review'
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
        Deletes the SubjectAccessReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_subject_access_review',
            'delete_subject_access_review'
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
    ) -> 'client.AuthorizationV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuthorizationV1Api(**kwargs)

    def __enter__(self) -> 'SubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReviewSpec(_kuber_definitions.Definition):
    """
    SubjectAccessReviewSpec is a description of the access
    request.  Exactly one of ResourceAuthorizationAttributes and
    NonResourceAuthorizationAttributes must be set
    """

    def __init__(
            self,
            extra: dict = None,
            groups: typing.List[str] = None,
            non_resource_attributes: 'NonResourceAttributes' = None,
            resource_attributes: 'ResourceAttributes' = None,
            uid: str = None,
            user: str = None,
    ):
        """Create SubjectAccessReviewSpec instance."""
        super(SubjectAccessReviewSpec, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReviewSpec'
        )
        self._properties = {
            'extra': extra or {},
            'groups': groups or [],
            'nonResourceAttributes': non_resource_attributes or NonResourceAttributes(),
            'resourceAttributes': resource_attributes or ResourceAttributes(),
            'uid': uid or '',
            'user': user or '',

        }
        self._types = {
            'extra': (dict, None),
            'groups': (list, str),
            'nonResourceAttributes': (NonResourceAttributes, None),
            'resourceAttributes': (ResourceAttributes, None),
            'uid': (str, None),
            'user': (str, None),

        }

    @property
    def extra(self) -> dict:
        """
        Extra corresponds to the user.Info.GetExtra() method from
        the authenticator.  Since that is input to the authorizer it
        needs a reflection here.
        """
        return self._properties.get('extra')

    @extra.setter
    def extra(self, value: dict):
        """
        Extra corresponds to the user.Info.GetExtra() method from
        the authenticator.  Since that is input to the authorizer it
        needs a reflection here.
        """
        self._properties['extra'] = value

    @property
    def groups(self) -> typing.List[str]:
        """
        Groups is the groups you're testing for.
        """
        return self._properties.get('groups')

    @groups.setter
    def groups(self, value: typing.List[str]):
        """
        Groups is the groups you're testing for.
        """
        self._properties['groups'] = value

    @property
    def non_resource_attributes(self) -> 'NonResourceAttributes':
        """
        NonResourceAttributes describes information for a non-
        resource access request
        """
        return self._properties.get('nonResourceAttributes')

    @non_resource_attributes.setter
    def non_resource_attributes(self, value: typing.Union['NonResourceAttributes', dict]):
        """
        NonResourceAttributes describes information for a non-
        resource access request
        """
        if isinstance(value, dict):
            value = NonResourceAttributes().from_dict(value)
        self._properties['nonResourceAttributes'] = value

    @property
    def resource_attributes(self) -> 'ResourceAttributes':
        """
        ResourceAuthorizationAttributes describes information for a
        resource access request
        """
        return self._properties.get('resourceAttributes')

    @resource_attributes.setter
    def resource_attributes(self, value: typing.Union['ResourceAttributes', dict]):
        """
        ResourceAuthorizationAttributes describes information for a
        resource access request
        """
        if isinstance(value, dict):
            value = ResourceAttributes().from_dict(value)
        self._properties['resourceAttributes'] = value

    @property
    def uid(self) -> str:
        """
        UID information about the requesting user.
        """
        return self._properties.get('uid')

    @uid.setter
    def uid(self, value: str):
        """
        UID information about the requesting user.
        """
        self._properties['uid'] = value

    @property
    def user(self) -> str:
        """
        User is the user you're testing for. If you specify "User"
        but not "Groups", then is it interpreted as "What if User
        were not a member of any groups
        """
        return self._properties.get('user')

    @user.setter
    def user(self, value: str):
        """
        User is the user you're testing for. If you specify "User"
        but not "Groups", then is it interpreted as "What if User
        were not a member of any groups
        """
        self._properties['user'] = value

    def __enter__(self) -> 'SubjectAccessReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReviewStatus(_kuber_definitions.Definition):
    """
    SubjectAccessReviewStatus
    """

    def __init__(
            self,
            allowed: bool = None,
            denied: bool = None,
            evaluation_error: str = None,
            reason: str = None,
    ):
        """Create SubjectAccessReviewStatus instance."""
        super(SubjectAccessReviewStatus, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReviewStatus'
        )
        self._properties = {
            'allowed': allowed or None,
            'denied': denied or None,
            'evaluationError': evaluation_error or '',
            'reason': reason or '',

        }
        self._types = {
            'allowed': (bool, None),
            'denied': (bool, None),
            'evaluationError': (str, None),
            'reason': (str, None),

        }

    @property
    def allowed(self) -> bool:
        """
        Allowed is required. True if the action would be allowed,
        false otherwise.
        """
        return self._properties.get('allowed')

    @allowed.setter
    def allowed(self, value: bool):
        """
        Allowed is required. True if the action would be allowed,
        false otherwise.
        """
        self._properties['allowed'] = value

    @property
    def denied(self) -> bool:
        """
        Denied is optional. True if the action would be denied,
        otherwise false. If both allowed is false and denied is
        false, then the authorizer has no opinion on whether to
        authorize the action. Denied may not be true if Allowed is
        true.
        """
        return self._properties.get('denied')

    @denied.setter
    def denied(self, value: bool):
        """
        Denied is optional. True if the action would be denied,
        otherwise false. If both allowed is false and denied is
        false, then the authorizer has no opinion on whether to
        authorize the action. Denied may not be true if Allowed is
        true.
        """
        self._properties['denied'] = value

    @property
    def evaluation_error(self) -> str:
        """
        EvaluationError is an indication that some error occurred
        during the authorization check. It is entirely possible to
        get an error and be able to continue determine authorization
        status in spite of it. For instance, RBAC can be missing a
        role, but enough roles are still present and bound to reason
        about the request.
        """
        return self._properties.get('evaluationError')

    @evaluation_error.setter
    def evaluation_error(self, value: str):
        """
        EvaluationError is an indication that some error occurred
        during the authorization check. It is entirely possible to
        get an error and be able to continue determine authorization
        status in spite of it. For instance, RBAC can be missing a
        role, but enough roles are still present and bound to reason
        about the request.
        """
        self._properties['evaluationError'] = value

    @property
    def reason(self) -> str:
        """
        Reason is optional.  It indicates why a request was allowed
        or denied.
        """
        return self._properties.get('reason')

    @reason.setter
    def reason(self, value: str):
        """
        Reason is optional.  It indicates why a request was allowed
        or denied.
        """
        self._properties['reason'] = value

    def __enter__(self) -> 'SubjectAccessReviewStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectRulesReviewStatus(_kuber_definitions.Definition):
    """
    SubjectRulesReviewStatus contains the result of a rules
    check. This check can be incomplete depending on the set of
    authorizers the server is configured with and any errors
    experienced during evaluation. Because authorization rules
    are additive, if a rule appears in a list it's safe to
    assume the subject has that permission, even if that list is
    incomplete.
    """

    def __init__(
            self,
            evaluation_error: str = None,
            incomplete: bool = None,
            non_resource_rules: typing.List['NonResourceRule'] = None,
            resource_rules: typing.List['ResourceRule'] = None,
    ):
        """Create SubjectRulesReviewStatus instance."""
        super(SubjectRulesReviewStatus, self).__init__(
            api_version='authorization/v1',
            kind='SubjectRulesReviewStatus'
        )
        self._properties = {
            'evaluationError': evaluation_error or '',
            'incomplete': incomplete or None,
            'nonResourceRules': non_resource_rules or [],
            'resourceRules': resource_rules or [],

        }
        self._types = {
            'evaluationError': (str, None),
            'incomplete': (bool, None),
            'nonResourceRules': (list, NonResourceRule),
            'resourceRules': (list, ResourceRule),

        }

    @property
    def evaluation_error(self) -> str:
        """
        EvaluationError can appear in combination with Rules. It
        indicates an error occurred during rule evaluation, such as
        an authorizer that doesn't support rule evaluation, and that
        ResourceRules and/or NonResourceRules may be incomplete.
        """
        return self._properties.get('evaluationError')

    @evaluation_error.setter
    def evaluation_error(self, value: str):
        """
        EvaluationError can appear in combination with Rules. It
        indicates an error occurred during rule evaluation, such as
        an authorizer that doesn't support rule evaluation, and that
        ResourceRules and/or NonResourceRules may be incomplete.
        """
        self._properties['evaluationError'] = value

    @property
    def incomplete(self) -> bool:
        """
        Incomplete is true when the rules returned by this call are
        incomplete. This is most commonly encountered when an
        authorizer, such as an external authorizer, doesn't support
        rules evaluation.
        """
        return self._properties.get('incomplete')

    @incomplete.setter
    def incomplete(self, value: bool):
        """
        Incomplete is true when the rules returned by this call are
        incomplete. This is most commonly encountered when an
        authorizer, such as an external authorizer, doesn't support
        rules evaluation.
        """
        self._properties['incomplete'] = value

    @property
    def non_resource_rules(self) -> typing.List['NonResourceRule']:
        """
        NonResourceRules is the list of actions the subject is
        allowed to perform on non-resources. The list ordering isn't
        significant, may contain duplicates, and possibly be
        incomplete.
        """
        return self._properties.get('nonResourceRules')

    @non_resource_rules.setter
    def non_resource_rules(
            self,
            value: typing.Union[typing.List['NonResourceRule'], typing.List[dict]]
    ):
        """
        NonResourceRules is the list of actions the subject is
        allowed to perform on non-resources. The list ordering isn't
        significant, may contain duplicates, and possibly be
        incomplete.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NonResourceRule().from_dict(item)
            cleaned.append(item)
        self._properties['nonResourceRules'] = cleaned

    @property
    def resource_rules(self) -> typing.List['ResourceRule']:
        """
        ResourceRules is the list of actions the subject is allowed
        to perform on resources. The list ordering isn't
        significant, may contain duplicates, and possibly be
        incomplete.
        """
        return self._properties.get('resourceRules')

    @resource_rules.setter
    def resource_rules(
            self,
            value: typing.Union[typing.List['ResourceRule'], typing.List[dict]]
    ):
        """
        ResourceRules is the list of actions the subject is allowed
        to perform on resources. The list ordering isn't
        significant, may contain duplicates, and possibly be
        incomplete.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ResourceRule().from_dict(item)
            cleaned.append(item)
        self._properties['resourceRules'] = cleaned

    def __enter__(self) -> 'SubjectRulesReviewStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

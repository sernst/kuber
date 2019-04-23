import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_12.meta_v1 import ListMeta
from kuber.v1_12.meta_v1 import ObjectMeta


class Initializer(_kuber_definitions.Definition):
    """
    Initializer describes the name and the failure policy of an
    initializer, and what resources it applies to.
    """

    def __init__(
            self,
            name: str = None,
            rules: typing.List['Rule'] = None,
    ):
        """Create Initializer instance."""
        super(Initializer, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='Initializer'
        )
        self._properties = {
            'name': name or '',
            'rules': rules or [],

        }
        self._types = {
            'name': (str, None),
            'rules': (list, Rule),

        }

    @property
    def name(self) -> str:
        """
        Name is the identifier of the initializer. It will be added
        to the object that needs to be initialized. Name should be
        fully qualified, e.g., alwayspullimages.kubernetes.io, where
        "alwayspullimages" is the name of the webhook, and
        kubernetes.io is the name of the organization. Required
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        Name is the identifier of the initializer. It will be added
        to the object that needs to be initialized. Name should be
        fully qualified, e.g., alwayspullimages.kubernetes.io, where
        "alwayspullimages" is the name of the webhook, and
        kubernetes.io is the name of the organization. Required
        """
        self._properties['name'] = value

    @property
    def rules(self) -> typing.List['Rule']:
        """
        Rules describes what resources/subresources the initializer
        cares about. The initializer cares about an operation if it
        matches _any_ Rule. Rule.Resources must not include
        subresources.
        """
        return self._properties.get('rules')

    @rules.setter
    def rules(
            self,
            value: typing.Union[typing.List['Rule'], typing.List[dict]]
    ):
        """
        Rules describes what resources/subresources the initializer
        cares about. The initializer cares about an operation if it
        matches _any_ Rule. Rule.Resources must not include
        subresources.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Rule().from_dict(item)
            cleaned.append(item)
        self._properties['rules'] = cleaned

    def __enter__(self) -> 'Initializer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class InitializerConfiguration(_kuber_definitions.Resource):
    """
    InitializerConfiguration describes the configuration of
    initializers.
    """

    def __init__(
            self,
            initializers: typing.List['Initializer'] = None,
            metadata: 'ObjectMeta' = None,
    ):
        """Create InitializerConfiguration instance."""
        super(InitializerConfiguration, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='InitializerConfiguration'
        )
        self._properties = {
            'initializers': initializers or [],
            'metadata': metadata or ObjectMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'initializers': (list, Initializer),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),

        }

    @property
    def initializers(self) -> typing.List['Initializer']:
        """
        Initializers is a list of resources and their default
        initializers Order-sensitive. When merging multiple
        InitializerConfigurations, we sort the initializers from
        different InitializerConfigurations by the name of the
        InitializerConfigurations; the order of the initializers
        from the same InitializerConfiguration is preserved.
        """
        return self._properties.get('initializers')

    @initializers.setter
    def initializers(
            self,
            value: typing.Union[typing.List['Initializer'], typing.List[dict]]
    ):
        """
        Initializers is a list of resources and their default
        initializers Order-sensitive. When merging multiple
        InitializerConfigurations, we sort the initializers from
        different InitializerConfigurations by the name of the
        InitializerConfigurations; the order of the initializers
        from the same InitializerConfiguration is preserved.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Initializer().from_dict(item)
            cleaned.append(item)
        self._properties['initializers'] = cleaned

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata.
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the InitializerConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_initializer_configuration',
            'create_initializer_configuration'
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
        Replaces the InitializerConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_initializer_configuration',
            'replace_initializer_configuration'
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
        Patches the InitializerConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_initializer_configuration',
            'patch_initializer_configuration'
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
        Reads the InitializerConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_initializer_configuration',
            'read_initializer_configuration'
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
        Deletes the InitializerConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_initializer_configuration',
            'delete_initializer_configuration'
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
    ) -> 'client.AdmissionregistrationV1alpha1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> 'InitializerConfiguration':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class InitializerConfigurationList(_kuber_definitions.Collection):
    """
    InitializerConfigurationList is a list of
    InitializerConfiguration.
    """

    def __init__(
            self,
            items: typing.List['InitializerConfiguration'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create InitializerConfigurationList instance."""
        super(InitializerConfigurationList, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='InitializerConfigurationList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, InitializerConfiguration),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['InitializerConfiguration']:
        """
        List of InitializerConfiguration.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['InitializerConfiguration'], typing.List[dict]]
    ):
        """
        List of InitializerConfiguration.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = InitializerConfiguration().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

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

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.AdmissionregistrationV1alpha1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> 'InitializerConfigurationList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Rule(_kuber_definitions.Definition):
    """
    Rule is a tuple of APIGroups, APIVersion, and Resources.It
    is recommended to make sure that all the tuple expansions
    are valid.
    """

    def __init__(
            self,
            api_groups: typing.List[str] = None,
            api_versions: typing.List[str] = None,
            resources: typing.List[str] = None,
    ):
        """Create Rule instance."""
        super(Rule, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='Rule'
        )
        self._properties = {
            'apiGroups': api_groups or [],
            'apiVersions': api_versions or [],
            'resources': resources or [],

        }
        self._types = {
            'apiGroups': (list, str),
            'apiVersions': (list, str),
            'resources': (list, str),

        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        return self._properties.get('apiGroups')

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        self._properties['apiGroups'] = value

    @property
    def api_versions(self) -> typing.List[str]:
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        return self._properties.get('apiVersions')

    @api_versions.setter
    def api_versions(self, value: typing.List[str]):
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        self._properties['apiVersions'] = value

    @property
    def resources(self) -> typing.List[str]:
        """
        Resources is a list of resources this rule applies to.

        For
        example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present,
        the validation rule will ensure resources do not overlap
        with each other.

        Depending on the enclosing object,
        subresources might not be allowed. Required.
        """
        return self._properties.get('resources')

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        Resources is a list of resources this rule applies to.

        For
        example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present,
        the validation rule will ensure resources do not overlap
        with each other.

        Depending on the enclosing object,
        subresources might not be allowed. Required.
        """
        self._properties['resources'] = value

    def __enter__(self) -> 'Rule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

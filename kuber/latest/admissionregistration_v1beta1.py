import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.latest.meta_v1 import LabelSelector
from kuber.latest.meta_v1 import ListMeta
from kuber.latest.meta_v1 import ObjectMeta


class MutatingWebhookConfiguration(_kuber_definitions.Resource):
    """
    MutatingWebhookConfiguration describes the configuration of
    and admission webhook that accept or reject and may change
    the object.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            webhooks: typing.List['Webhook'] = None,
    ):
        """Create MutatingWebhookConfiguration instance."""
        super(MutatingWebhookConfiguration, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='MutatingWebhookConfiguration'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'webhooks': webhooks or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'webhooks': (list, Webhook),

        }

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

    @property
    def webhooks(self) -> typing.List['Webhook']:
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        return self._properties.get('webhooks')

    @webhooks.setter
    def webhooks(
            self,
            value: typing.Union[typing.List['Webhook'], typing.List[dict]]
    ):
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Webhook().from_dict(item)
            cleaned.append(item)
        self._properties['webhooks'] = cleaned

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_mutating_webhook_configuration',
            'create_mutating_webhook_configuration'
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
        Replaces the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_mutating_webhook_configuration',
            'replace_mutating_webhook_configuration'
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
        Patches the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_mutating_webhook_configuration',
            'patch_mutating_webhook_configuration'
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
        Reads the MutatingWebhookConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_mutating_webhook_configuration',
            'read_mutating_webhook_configuration'
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
        Deletes the MutatingWebhookConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_mutating_webhook_configuration',
            'delete_mutating_webhook_configuration'
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
    ) -> 'client.AdmissionregistrationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> 'MutatingWebhookConfiguration':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingWebhookConfigurationList(_kuber_definitions.Collection):
    """
    MutatingWebhookConfigurationList is a list of
    MutatingWebhookConfiguration.
    """

    def __init__(
            self,
            items: typing.List['MutatingWebhookConfiguration'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create MutatingWebhookConfigurationList instance."""
        super(MutatingWebhookConfigurationList, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='MutatingWebhookConfigurationList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, MutatingWebhookConfiguration),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['MutatingWebhookConfiguration']:
        """
        List of MutatingWebhookConfiguration.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['MutatingWebhookConfiguration'], typing.List[dict]]
    ):
        """
        List of MutatingWebhookConfiguration.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = MutatingWebhookConfiguration().from_dict(item)
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
    ) -> 'client.AdmissionregistrationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> 'MutatingWebhookConfigurationList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuleWithOperations(_kuber_definitions.Definition):
    """
    RuleWithOperations is a tuple of Operations and Resources.
    It is recommended to make sure that all the tuple expansions
    are valid.
    """

    def __init__(
            self,
            api_groups: typing.List[str] = None,
            api_versions: typing.List[str] = None,
            operations: typing.List[str] = None,
            resources: typing.List[str] = None,
            scope: str = None,
    ):
        """Create RuleWithOperations instance."""
        super(RuleWithOperations, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='RuleWithOperations'
        )
        self._properties = {
            'apiGroups': api_groups or [],
            'apiVersions': api_versions or [],
            'operations': operations or [],
            'resources': resources or [],
            'scope': scope or '',

        }
        self._types = {
            'apiGroups': (list, str),
            'apiVersions': (list, str),
            'operations': (list, str),
            'resources': (list, str),
            'scope': (str, None),

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
    def operations(self) -> typing.List[str]:
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, or * for all operations. If '*' is
        present, the length of the slice must be one. Required.
        """
        return self._properties.get('operations')

    @operations.setter
    def operations(self, value: typing.List[str]):
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, or * for all operations. If '*' is
        present, the length of the slice must be one. Required.
        """
        self._properties['operations'] = value

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

    @property
    def scope(self) -> str:
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        return self._properties.get('scope')

    @scope.setter
    def scope(self, value: str):
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        self._properties['scope'] = value

    def __enter__(self) -> 'RuleWithOperations':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceReference(_kuber_definitions.Definition):
    """
    ServiceReference holds a reference to Service.legacy.k8s.io
    """

    def __init__(
            self,
            name: str = None,
            namespace: str = None,
            path: str = None,
    ):
        """Create ServiceReference instance."""
        super(ServiceReference, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='ServiceReference'
        )
        self._properties = {
            'name': name or '',
            'namespace': namespace or '',
            'path': path or '',

        }
        self._types = {
            'name': (str, None),
            'namespace': (str, None),
            'path': (str, None),

        }

    @property
    def name(self) -> str:
        """
        `name` is the name of the service. Required
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of the service. Required
        """
        self._properties['name'] = value

    @property
    def namespace(self) -> str:
        """
        `namespace` is the namespace of the service. Required
        """
        return self._properties.get('namespace')

    @namespace.setter
    def namespace(self, value: str):
        """
        `namespace` is the namespace of the service. Required
        """
        self._properties['namespace'] = value

    @property
    def path(self) -> str:
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        self._properties['path'] = value

    def __enter__(self) -> 'ServiceReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingWebhookConfiguration(_kuber_definitions.Resource):
    """
    ValidatingWebhookConfiguration describes the configuration
    of and admission webhook that accept or reject and object
    without changing it.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            webhooks: typing.List['Webhook'] = None,
    ):
        """Create ValidatingWebhookConfiguration instance."""
        super(ValidatingWebhookConfiguration, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='ValidatingWebhookConfiguration'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'webhooks': webhooks or [],

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'webhooks': (list, Webhook),

        }

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

    @property
    def webhooks(self) -> typing.List['Webhook']:
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        return self._properties.get('webhooks')

    @webhooks.setter
    def webhooks(
            self,
            value: typing.Union[typing.List['Webhook'], typing.List[dict]]
    ):
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Webhook().from_dict(item)
            cleaned.append(item)
        self._properties['webhooks'] = cleaned

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_validating_webhook_configuration',
            'create_validating_webhook_configuration'
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
        Replaces the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_validating_webhook_configuration',
            'replace_validating_webhook_configuration'
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
        Patches the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_validating_webhook_configuration',
            'patch_validating_webhook_configuration'
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
        Reads the ValidatingWebhookConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_validating_webhook_configuration',
            'read_validating_webhook_configuration'
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
        Deletes the ValidatingWebhookConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_validating_webhook_configuration',
            'delete_validating_webhook_configuration'
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
    ) -> 'client.AdmissionregistrationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> 'ValidatingWebhookConfiguration':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingWebhookConfigurationList(_kuber_definitions.Collection):
    """
    ValidatingWebhookConfigurationList is a list of
    ValidatingWebhookConfiguration.
    """

    def __init__(
            self,
            items: typing.List['ValidatingWebhookConfiguration'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create ValidatingWebhookConfigurationList instance."""
        super(ValidatingWebhookConfigurationList, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='ValidatingWebhookConfigurationList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, ValidatingWebhookConfiguration),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['ValidatingWebhookConfiguration']:
        """
        List of ValidatingWebhookConfiguration.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['ValidatingWebhookConfiguration'], typing.List[dict]]
    ):
        """
        List of ValidatingWebhookConfiguration.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = ValidatingWebhookConfiguration().from_dict(item)
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
    ) -> 'client.AdmissionregistrationV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> 'ValidatingWebhookConfigurationList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Webhook(_kuber_definitions.Definition):
    """
    Webhook describes an admission webhook and the resources and
    operations it applies to.
    """

    def __init__(
            self,
            admission_review_versions: typing.List[str] = None,
            client_config: 'WebhookClientConfig' = None,
            failure_policy: str = None,
            name: str = None,
            namespace_selector: 'LabelSelector' = None,
            rules: typing.List['RuleWithOperations'] = None,
            side_effects: str = None,
            timeout_seconds: int = None,
    ):
        """Create Webhook instance."""
        super(Webhook, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='Webhook'
        )
        self._properties = {
            'admissionReviewVersions': admission_review_versions or [],
            'clientConfig': client_config or WebhookClientConfig(),
            'failurePolicy': failure_policy or '',
            'name': name or '',
            'namespaceSelector': namespace_selector or LabelSelector(),
            'rules': rules or [],
            'sideEffects': side_effects or '',
            'timeoutSeconds': timeout_seconds or None,

        }
        self._types = {
            'admissionReviewVersions': (list, str),
            'clientConfig': (WebhookClientConfig, None),
            'failurePolicy': (str, None),
            'name': (str, None),
            'namespaceSelector': (LabelSelector, None),
            'rules': (list, RuleWithOperations),
            'sideEffects': (str, None),
            'timeoutSeconds': (int, None),

        }

    @property
    def admission_review_versions(self) -> typing.List[str]:
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy. Default to `['v1beta1']`.
        """
        return self._properties.get('admissionReviewVersions')

    @admission_review_versions.setter
    def admission_review_versions(self, value: typing.List[str]):
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy. Default to `['v1beta1']`.
        """
        self._properties['admissionReviewVersions'] = value

    @property
    def client_config(self) -> 'WebhookClientConfig':
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        return self._properties.get('clientConfig')

    @client_config.setter
    def client_config(self, value: typing.Union['WebhookClientConfig', dict]):
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        if isinstance(value, dict):
            value = WebhookClientConfig().from_dict(value)
        self._properties['clientConfig'] = value

    @property
    def failure_policy(self) -> str:
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Ignore.
        """
        return self._properties.get('failurePolicy')

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Ignore.
        """
        self._properties['failurePolicy'] = value

    @property
    def name(self) -> str:
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        return self._properties.get('name')

    @name.setter
    def name(self, value: str):
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        self._properties['name'] = value

    @property
    def namespace_selector(self) -> 'LabelSelector':
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects
        whose namespace is not associated with "runlevel" of "0" or
        "1";  you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
        "key": "runlevel",
              "operator": "NotIn",
        "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If
        instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
        "key": "environment",
              "operator": "In",
        "values": [
                "prod",
                "staging"
              ]
            }
        ]
        }

        See
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/ for more examples of label selectors.
        Default to the empty LabelSelector, which matches
        everything.
        """
        return self._properties.get('namespaceSelector')

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects
        whose namespace is not associated with "runlevel" of "0" or
        "1";  you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
        "key": "runlevel",
              "operator": "NotIn",
        "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If
        instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
        "key": "environment",
              "operator": "In",
        "values": [
                "prod",
                "staging"
              ]
            }
        ]
        }

        See
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/ for more examples of label selectors.
        Default to the empty LabelSelector, which matches
        everything.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['namespaceSelector'] = value

    @property
    def rules(self) -> typing.List['RuleWithOperations']:
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        return self._properties.get('rules')

    @rules.setter
    def rules(
            self,
            value: typing.Union[typing.List['RuleWithOperations'], typing.List[dict]]
    ):
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = RuleWithOperations().from_dict(item)
            cleaned.append(item)
        self._properties['rules'] = cleaned

    @property
    def side_effects(self) -> str:
        """
        SideEffects states whether this webhookk has side effects.
        Acceptable values are: Unknown, None, Some, NoneOnDryRun
        Webhooks with side effects MUST implement a reconciliation
        system, since a request may be rejected by a future step in
        the admission change and the side effects therefore need to
        be undone. Requests with the dryRun attribute will be auto-
        rejected if they match a webhook with sideEffects == Unknown
        or Some. Defaults to Unknown.
        """
        return self._properties.get('sideEffects')

    @side_effects.setter
    def side_effects(self, value: str):
        """
        SideEffects states whether this webhookk has side effects.
        Acceptable values are: Unknown, None, Some, NoneOnDryRun
        Webhooks with side effects MUST implement a reconciliation
        system, since a request may be rejected by a future step in
        the admission change and the side effects therefore need to
        be undone. Requests with the dryRun attribute will be auto-
        rejected if they match a webhook with sideEffects == Unknown
        or Some. Defaults to Unknown.
        """
        self._properties['sideEffects'] = value

    @property
    def timeout_seconds(self) -> int:
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 30
        seconds.
        """
        return self._properties.get('timeoutSeconds')

    @timeout_seconds.setter
    def timeout_seconds(self, value: int):
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 30
        seconds.
        """
        self._properties['timeoutSeconds'] = value

    def __enter__(self) -> 'Webhook':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WebhookClientConfig(_kuber_definitions.Definition):
    """
    WebhookClientConfig contains the information to make a TLS
    connection with the webhook
    """

    def __init__(
            self,
            ca_bundle: str = None,
            service: 'ServiceReference' = None,
            url: str = None,
    ):
        """Create WebhookClientConfig instance."""
        super(WebhookClientConfig, self).__init__(
            api_version='admissionregistration/v1beta1',
            kind='WebhookClientConfig'
        )
        self._properties = {
            'caBundle': ca_bundle or '',
            'service': service or ServiceReference(),
            'url': url or '',

        }
        self._types = {
            'caBundle': (str, None),
            'service': (ServiceReference, None),
            'url': (str, None),

        }

    @property
    def ca_bundle(self) -> str:
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        return self._properties.get('caBundle')

    @ca_bundle.setter
    def ca_bundle(self, value: str):
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        self._properties['caBundle'] = value

    @property
    def service(self) -> 'ServiceReference':
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook
        is running within the cluster, then you should use
        `service`.

        Port 443 will be used if it is open, otherwise
        it is an error.
        """
        return self._properties.get('service')

    @service.setter
    def service(self, value: typing.Union['ServiceReference', dict]):
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook
        is running within the cluster, then you should use
        `service`.

        Port 443 will be used if it is open, otherwise
        it is an error.
        """
        if isinstance(value, dict):
            value = ServiceReference().from_dict(value)
        self._properties['service'] = value

    @property
    def url(self) -> str:
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to
        a service running in the cluster; use the `service` field
        instead. The host might be resolved via external DNS in some
        apiservers (e.g., `kube-apiserver` cannot resolve in-cluster
        DNS as that would be a layering violation). `host` may also
        be an IP address.

        Please note that using `localhost` or
        `127.0.0.1` as a `host` is risky unless you take great care
        to run this webhook on all hosts which run an apiserver
        which might need to make calls to this webhook. Such
        installs are likely to be non-portable, i.e., not easy to
        turn up in a new cluster.

        The scheme must be "https"; the
        URL must begin with "https://".

        A path is optional, and if
        present may be any string permissible in a URL. You may use
        the path to pass an arbitrary string to the webhook, for
        example, a cluster identifier.

        Attempting to use a user or
        basic auth e.g. "user:password@" is not allowed. Fragments
        ("#...") and query parameters ("?...") are not allowed,
        either.
        """
        return self._properties.get('url')

    @url.setter
    def url(self, value: str):
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to
        a service running in the cluster; use the `service` field
        instead. The host might be resolved via external DNS in some
        apiservers (e.g., `kube-apiserver` cannot resolve in-cluster
        DNS as that would be a layering violation). `host` may also
        be an IP address.

        Please note that using `localhost` or
        `127.0.0.1` as a `host` is risky unless you take great care
        to run this webhook on all hosts which run an apiserver
        which might need to make calls to this webhook. Such
        installs are likely to be non-portable, i.e., not easy to
        turn up in a new cluster.

        The scheme must be "https"; the
        URL must begin with "https://".

        A path is optional, and if
        present may be any string permissible in a URL. You may use
        the path to pass an arbitrary string to the webhook, for
        example, a cluster identifier.

        Attempting to use a user or
        basic auth e.g. "user:password@" is not allowed. Fragments
        ("#...") and query parameters ("?...") are not allowed,
        either.
        """
        self._properties['url'] = value

    def __enter__(self) -> 'WebhookClientConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

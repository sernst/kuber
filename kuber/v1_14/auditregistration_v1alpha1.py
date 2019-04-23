import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_14.meta_v1 import ListMeta
from kuber.v1_14.meta_v1 import ObjectMeta


class AuditSink(_kuber_definitions.Resource):
    """
    AuditSink represents a cluster level audit sink
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'AuditSinkSpec' = None,
    ):
        """Create AuditSink instance."""
        super(AuditSink, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='AuditSink'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or AuditSinkSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (AuditSinkSpec, None),

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
    def spec(self) -> 'AuditSinkSpec':
        """
        Spec defines the audit configuration spec
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['AuditSinkSpec', dict]):
        """
        Spec defines the audit configuration spec
        """
        if isinstance(value, dict):
            value = AuditSinkSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the AuditSink in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_audit_sink',
            'create_audit_sink'
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
        Replaces the AuditSink in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_audit_sink',
            'replace_audit_sink'
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
        Patches the AuditSink in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_audit_sink',
            'patch_audit_sink'
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
        Reads the AuditSink from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_audit_sink',
            'read_audit_sink'
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
        Deletes the AuditSink from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_audit_sink',
            'delete_audit_sink'
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
    ) -> 'client.AuditregistrationV1alpha1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuditregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> 'AuditSink':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AuditSinkList(_kuber_definitions.Collection):
    """
    AuditSinkList is a list of AuditSink items.
    """

    def __init__(
            self,
            items: typing.List['AuditSink'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create AuditSinkList instance."""
        super(AuditSinkList, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='AuditSinkList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, AuditSink),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['AuditSink']:
        """
        List of audit configurations.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['AuditSink'], typing.List[dict]]
    ):
        """
        List of audit configurations.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = AuditSink().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """

        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """

        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.AuditregistrationV1alpha1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.AuditregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> 'AuditSinkList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AuditSinkSpec(_kuber_definitions.Definition):
    """
    AuditSinkSpec holds the spec for the audit sink
    """

    def __init__(
            self,
            policy: 'Policy' = None,
            webhook: 'Webhook' = None,
    ):
        """Create AuditSinkSpec instance."""
        super(AuditSinkSpec, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='AuditSinkSpec'
        )
        self._properties = {
            'policy': policy or Policy(),
            'webhook': webhook or Webhook(),

        }
        self._types = {
            'policy': (Policy, None),
            'webhook': (Webhook, None),

        }

    @property
    def policy(self) -> 'Policy':
        """
        Policy defines the policy for selecting which events should
        be sent to the webhook required
        """
        return self._properties.get('policy')

    @policy.setter
    def policy(self, value: typing.Union['Policy', dict]):
        """
        Policy defines the policy for selecting which events should
        be sent to the webhook required
        """
        if isinstance(value, dict):
            value = Policy().from_dict(value)
        self._properties['policy'] = value

    @property
    def webhook(self) -> 'Webhook':
        """
        Webhook to send events required
        """
        return self._properties.get('webhook')

    @webhook.setter
    def webhook(self, value: typing.Union['Webhook', dict]):
        """
        Webhook to send events required
        """
        if isinstance(value, dict):
            value = Webhook().from_dict(value)
        self._properties['webhook'] = value

    def __enter__(self) -> 'AuditSinkSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Policy(_kuber_definitions.Definition):
    """
    Policy defines the configuration of how audit events are
    logged
    """

    def __init__(
            self,
            level: str = None,
            stages: typing.List[str] = None,
    ):
        """Create Policy instance."""
        super(Policy, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='Policy'
        )
        self._properties = {
            'level': level or '',
            'stages': stages or [],

        }
        self._types = {
            'level': (str, None),
            'stages': (list, str),

        }

    @property
    def level(self) -> str:
        """
        The Level that all requests are recorded at. available
        options: None, Metadata, Request, RequestResponse required
        """
        return self._properties.get('level')

    @level.setter
    def level(self, value: str):
        """
        The Level that all requests are recorded at. available
        options: None, Metadata, Request, RequestResponse required
        """
        self._properties['level'] = value

    @property
    def stages(self) -> typing.List[str]:
        """
        Stages is a list of stages for which events are created.
        """
        return self._properties.get('stages')

    @stages.setter
    def stages(self, value: typing.List[str]):
        """
        Stages is a list of stages for which events are created.
        """
        self._properties['stages'] = value

    def __enter__(self) -> 'Policy':
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
            api_version='auditregistration/v1alpha1',
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


class Webhook(_kuber_definitions.Definition):
    """
    Webhook holds the configuration of the webhook
    """

    def __init__(
            self,
            client_config: 'WebhookClientConfig' = None,
            throttle: 'WebhookThrottleConfig' = None,
    ):
        """Create Webhook instance."""
        super(Webhook, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='Webhook'
        )
        self._properties = {
            'clientConfig': client_config or WebhookClientConfig(),
            'throttle': throttle or WebhookThrottleConfig(),

        }
        self._types = {
            'clientConfig': (WebhookClientConfig, None),
            'throttle': (WebhookThrottleConfig, None),

        }

    @property
    def client_config(self) -> 'WebhookClientConfig':
        """
        ClientConfig holds the connection parameters for the webhook
        required
        """
        return self._properties.get('clientConfig')

    @client_config.setter
    def client_config(self, value: typing.Union['WebhookClientConfig', dict]):
        """
        ClientConfig holds the connection parameters for the webhook
        required
        """
        if isinstance(value, dict):
            value = WebhookClientConfig().from_dict(value)
        self._properties['clientConfig'] = value

    @property
    def throttle(self) -> 'WebhookThrottleConfig':
        """
        Throttle holds the options for throttling the webhook
        """
        return self._properties.get('throttle')

    @throttle.setter
    def throttle(self, value: typing.Union['WebhookThrottleConfig', dict]):
        """
        Throttle holds the options for throttling the webhook
        """
        if isinstance(value, dict):
            value = WebhookThrottleConfig().from_dict(value)
        self._properties['throttle'] = value

    def __enter__(self) -> 'Webhook':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WebhookClientConfig(_kuber_definitions.Definition):
    """
    WebhookClientConfig contains the information to make a
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
            api_version='auditregistration/v1alpha1',
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


class WebhookThrottleConfig(_kuber_definitions.Definition):
    """
    WebhookThrottleConfig holds the configuration for throttling
    events
    """

    def __init__(
            self,
            burst: int = None,
            qps: int = None,
    ):
        """Create WebhookThrottleConfig instance."""
        super(WebhookThrottleConfig, self).__init__(
            api_version='auditregistration/v1alpha1',
            kind='WebhookThrottleConfig'
        )
        self._properties = {
            'burst': burst or None,
            'qps': qps or None,

        }
        self._types = {
            'burst': (int, None),
            'qps': (int, None),

        }

    @property
    def burst(self) -> int:
        """
        ThrottleBurst is the maximum number of events sent at the
        same moment default 15 QPS
        """
        return self._properties.get('burst')

    @burst.setter
    def burst(self, value: int):
        """
        ThrottleBurst is the maximum number of events sent at the
        same moment default 15 QPS
        """
        self._properties['burst'] = value

    @property
    def qps(self) -> int:
        """
        ThrottleQPS maximum number of batches per second default 10
        QPS
        """
        return self._properties.get('qps')

    @qps.setter
    def qps(self, value: int):
        """
        ThrottleQPS maximum number of batches per second default 10
        QPS
        """
        self._properties['qps'] = value

    def __enter__(self) -> 'WebhookThrottleConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

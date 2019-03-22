import typing

from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ListMeta
from kuber.v1_13.apimachinery.pkg.apis.meta.v1 import ObjectMeta


class RuntimeClass(_kuber_definitions.Resource):
    """
    RuntimeClass defines a class of container runtime supported
    in the cluster. The RuntimeClass is used to determine which
    container runtime is used to run all containers in a pod.
    RuntimeClasses are (currently) manually defined by a user or
    cluster provisioner, and referenced in the PodSpec. The
    Kubelet is responsible for resolving the RuntimeClassName
    reference before running the pod.  For more details, see
    https://git.k8s.io/enhancements/keps/sig-node/runtime-
    class.md
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'RuntimeClassSpec' = None,
    ):
        """Create RuntimeClass instance."""
        super(RuntimeClass, self).__init__(
            api_version='node/v1alpha1',
            kind='RuntimeClass'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or RuntimeClassSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (RuntimeClassSpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'RuntimeClassSpec':
        """
        Specification of the RuntimeClass More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['RuntimeClassSpec', dict]):
        """
        Specification of the RuntimeClass More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = RuntimeClassSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None) -> bool:
        """
        Creates the RuntimeClass in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the RuntimeClass was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the RuntimeClass in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the RuntimeClass was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the RuntimeClass from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'RuntimeClass':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuntimeClassList(_kuber_definitions.Resource):
    """
    RuntimeClassList is a list of RuntimeClass objects.
    """

    def __init__(
            self,
            items: typing.List['RuntimeClass'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create RuntimeClassList instance."""
        super(RuntimeClassList, self).__init__(
            api_version='node/v1alpha1',
            kind='RuntimeClassList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, RuntimeClass),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['RuntimeClass']:
        """
        Items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['RuntimeClass'], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = RuntimeClass().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    def create_resource(self, namespace: 'str' = None) -> bool:
        """
        Creates the RuntimeClassList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the RuntimeClassList was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the RuntimeClassList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the RuntimeClassList was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the RuntimeClassList from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'RuntimeClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuntimeClassSpec(_kuber_definitions.Definition):
    """
    RuntimeClassSpec is a specification of a RuntimeClass. It
    contains parameters that are required to describe the
    RuntimeClass to the Container Runtime Interface (CRI)
    implementation, as well as any other components that need to
    understand how the pod will be run. The RuntimeClassSpec is
    immutable.
    """

    def __init__(
            self,
            runtime_handler: str = None,
    ):
        """Create RuntimeClassSpec instance."""
        super(RuntimeClassSpec, self).__init__(
            api_version='node/v1alpha1',
            kind='RuntimeClassSpec'
        )
        self._properties = {
            'runtimeHandler': runtime_handler or '',

        }
        self._types = {
            'runtimeHandler': (str, None),

        }

    @property
    def runtime_handler(self) -> str:
        """
        RuntimeHandler specifies the underlying runtime and
        configuration that the CRI implementation will use to handle
        pods of this class. The possible values are specific to the
        node & CRI configuration.  It is assumed that all handlers
        are available on every node, and handlers of the same name
        are equivalent on every node. For example, a handler called
        "runc" might specify that the runc OCI runtime (using native
        Linux containers) will be used to run the containers in a
        pod. The RuntimeHandler must conform to the DNS Label (RFC
        1123) requirements and is immutable.
        """
        return self._properties.get('runtimeHandler')

    @runtime_handler.setter
    def runtime_handler(self, value: str):
        """
        RuntimeHandler specifies the underlying runtime and
        configuration that the CRI implementation will use to handle
        pods of this class. The possible values are specific to the
        node & CRI configuration.  It is assumed that all handlers
        are available on every node, and handlers of the same name
        are equivalent on every node. For example, a handler called
        "runc" might specify that the runc OCI runtime (using native
        Linux containers) will be used to run the containers in a
        pod. The RuntimeHandler must conform to the DNS Label (RFC
        1123) requirements and is immutable.
        """
        self._properties['runtimeHandler'] = value

    def __enter__(self) -> 'RuntimeClassSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

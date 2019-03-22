import typing

from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_12.core.v1 import EnvFromSource
from kuber.v1_12.core.v1 import EnvVar
from kuber.v1_12.apimachinery.pkg.apis.meta.v1 import LabelSelector
from kuber.v1_12.apimachinery.pkg.apis.meta.v1 import ListMeta
from kuber.v1_12.apimachinery.pkg.apis.meta.v1 import ObjectMeta
from kuber.v1_12.core.v1 import Volume
from kuber.v1_12.core.v1 import VolumeMount


class PodPreset(_kuber_definitions.Resource):
    """
    PodPreset is a policy resource that defines additional
    runtime requirements for a Pod.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'PodPresetSpec' = None,
    ):
        """Create PodPreset instance."""
        super(PodPreset, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPreset'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or PodPresetSpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (PodPresetSpec, None),

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
    def spec(self) -> 'PodPresetSpec':
        """

        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['PodPresetSpec', dict]):
        """

        """
        if isinstance(value, dict):
            value = PodPresetSpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None) -> bool:
        """
        Creates the PodPreset in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PodPreset was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the PodPreset in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PodPreset was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the PodPreset from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'PodPreset':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetList(_kuber_definitions.Resource):
    """
    PodPresetList is a list of PodPreset objects.
    """

    def __init__(
            self,
            items: typing.List['PodPreset'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create PodPresetList instance."""
        super(PodPresetList, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPresetList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, PodPreset),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['PodPreset']:
        """
        Items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['PodPreset'], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = PodPreset().from_dict(item)
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
        Creates the PodPresetList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PodPresetList was actually created.
        """
        try:
            _kube_api.create_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def replace_resource(self, namespace: 'str' = None) -> bool:
        """
        Replaces the PodPresetList in the currently
        configured Kubernetes cluster and returns a boolean indicating whether
        or not the PodPresetList was actually replaced.
        """
        try:
            _kube_api.replace_resource(self, namespace=namespace)
            return True
        except _kube_api.KubectlError:
            return False

    def delete_resource(self, namespace: 'str' = None) -> bool:
        """
        Deletes the PodPresetList from the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API in response to the delete action.
        """
        try:
            response = _kube_api.delete_resource(self, namespace=namespace)
            return response.success
        except _kube_api.KubectlError:
            return False

    def __enter__(self) -> 'PodPresetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetSpec(_kuber_definitions.Definition):
    """
    PodPresetSpec is a description of a pod preset.
    """

    def __init__(
            self,
            env: typing.List['EnvVar'] = None,
            env_from: typing.List['EnvFromSource'] = None,
            selector: 'LabelSelector' = None,
            volume_mounts: typing.List['VolumeMount'] = None,
            volumes: typing.List['Volume'] = None,
    ):
        """Create PodPresetSpec instance."""
        super(PodPresetSpec, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPresetSpec'
        )
        self._properties = {
            'env': env or [],
            'envFrom': env_from or [],
            'selector': selector or LabelSelector(),
            'volumeMounts': volume_mounts or [],
            'volumes': volumes or [],

        }
        self._types = {
            'env': (list, EnvVar),
            'envFrom': (list, EnvFromSource),
            'selector': (LabelSelector, None),
            'volumeMounts': (list, VolumeMount),
            'volumes': (list, Volume),

        }

    @property
    def env(self) -> typing.List['EnvVar']:
        """
        Env defines the collection of EnvVar to inject into
        containers.
        """
        return self._properties.get('env')

    @env.setter
    def env(
            self,
            value: typing.Union[typing.List['EnvVar'], typing.List[dict]]
    ):
        """
        Env defines the collection of EnvVar to inject into
        containers.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EnvVar().from_dict(item)
            cleaned.append(item)
        self._properties['env'] = cleaned

    @property
    def env_from(self) -> typing.List['EnvFromSource']:
        """
        EnvFrom defines the collection of EnvFromSource to inject
        into containers.
        """
        return self._properties.get('envFrom')

    @env_from.setter
    def env_from(
            self,
            value: typing.Union[typing.List['EnvFromSource'], typing.List[dict]]
    ):
        """
        EnvFrom defines the collection of EnvFromSource to inject
        into containers.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = EnvFromSource().from_dict(item)
            cleaned.append(item)
        self._properties['envFrom'] = cleaned

    @property
    def selector(self) -> 'LabelSelector':
        """
        Selector is a label query over a set of resources, in this
        case pods. Required.
        """
        return self._properties.get('selector')

    @selector.setter
    def selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selector is a label query over a set of resources, in this
        case pods. Required.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['selector'] = value

    @property
    def volume_mounts(self) -> typing.List['VolumeMount']:
        """
        VolumeMounts defines the collection of VolumeMount to inject
        into containers.
        """
        return self._properties.get('volumeMounts')

    @volume_mounts.setter
    def volume_mounts(
            self,
            value: typing.Union[typing.List['VolumeMount'], typing.List[dict]]
    ):
        """
        VolumeMounts defines the collection of VolumeMount to inject
        into containers.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = VolumeMount().from_dict(item)
            cleaned.append(item)
        self._properties['volumeMounts'] = cleaned

    @property
    def volumes(self) -> typing.List['Volume']:
        """
        Volumes defines the collection of Volume to inject into the
        pod.
        """
        return self._properties.get('volumes')

    @volumes.setter
    def volumes(
            self,
            value: typing.Union[typing.List['Volume'], typing.List[dict]]
    ):
        """
        Volumes defines the collection of Volume to inject into the
        pod.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Volume().from_dict(item)
            cleaned.append(item)
        self._properties['volumes'] = cleaned

    def __enter__(self) -> 'PodPresetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

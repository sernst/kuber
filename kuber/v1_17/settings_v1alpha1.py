import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_17.core_v1 import EnvFromSource  # noqa: F401
from kuber.v1_17.core_v1 import EnvVar  # noqa: F401
from kuber.v1_17.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_17.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_17.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_17.core_v1 import Volume  # noqa: F401
from kuber.v1_17.core_v1 import VolumeMount  # noqa: F401


class PodPreset(_kuber_definitions.Resource):
    """
    PodPreset is a policy resource that defines additional
    runtime requirements for a Pod.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "PodPresetSpec" = None,
    ):
        """Create PodPreset instance."""
        super(PodPreset, self).__init__(
            api_version="settings/v1alpha1", kind="PodPreset"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else PodPresetSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (PodPresetSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """"""
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "PodPresetSpec":
        """"""
        return typing.cast(
            "PodPresetSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["PodPresetSpec", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                PodPresetSpec,
                PodPresetSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: "str" = None):
        """
        Creates the PodPreset in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_pod_preset", "create_pod_preset"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: "str" = None):
        """
        Replaces the PodPreset in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_pod_preset", "replace_pod_preset"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: "str" = None):
        """
        Patches the PodPreset in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_pod_preset", "patch_pod_preset"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: "str" = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: str = None):
        """
        Reads the PodPreset from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_pod_preset",
            "read_pod_preset",
        ]
        return _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

    def delete_resource(
        self,
        namespace: str = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the PodPreset from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_pod_preset",
            "delete_pod_preset",
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds,
        )

        _kube_api.execute(
            action="delete",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name, "body": body},
        )

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.SettingsV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.SettingsV1alpha1Api(**kwargs)

    def __enter__(self) -> "PodPreset":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetList(_kuber_definitions.Collection):
    """
    PodPresetList is a list of PodPreset objects.
    """

    def __init__(
        self,
        items: typing.List["PodPreset"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create PodPresetList instance."""
        super(PodPresetList, self).__init__(
            api_version="settings/v1alpha1", kind="PodPresetList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PodPreset),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PodPreset"]:
        """
        Items is a list of schema objects.
        """
        return typing.cast(
            typing.List["PodPreset"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["PodPreset"], typing.List[dict]]):
        """
        Items is a list of schema objects.
        """
        cleaned: typing.List[PodPreset] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodPreset,
                    PodPreset().from_dict(item),
                )
            cleaned.append(typing.cast(PodPreset, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.SettingsV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.SettingsV1alpha1Api(**kwargs)

    def __enter__(self) -> "PodPresetList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetSpec(_kuber_definitions.Definition):
    """
    PodPresetSpec is a description of a pod preset.
    """

    def __init__(
        self,
        env: typing.List["EnvVar"] = None,
        env_from: typing.List["EnvFromSource"] = None,
        selector: "LabelSelector" = None,
        volume_mounts: typing.List["VolumeMount"] = None,
        volumes: typing.List["Volume"] = None,
    ):
        """Create PodPresetSpec instance."""
        super(PodPresetSpec, self).__init__(
            api_version="settings/v1alpha1", kind="PodPresetSpec"
        )
        self._properties = {
            "env": env if env is not None else [],
            "envFrom": env_from if env_from is not None else [],
            "selector": selector if selector is not None else LabelSelector(),
            "volumeMounts": volume_mounts if volume_mounts is not None else [],
            "volumes": volumes if volumes is not None else [],
        }
        self._types = {
            "env": (list, EnvVar),
            "envFrom": (list, EnvFromSource),
            "selector": (LabelSelector, None),
            "volumeMounts": (list, VolumeMount),
            "volumes": (list, Volume),
        }

    @property
    def env(self) -> typing.List["EnvVar"]:
        """
        Env defines the collection of EnvVar to inject into
        containers.
        """
        return typing.cast(
            typing.List["EnvVar"],
            self._properties.get("env"),
        )

    @env.setter
    def env(self, value: typing.Union[typing.List["EnvVar"], typing.List[dict]]):
        """
        Env defines the collection of EnvVar to inject into
        containers.
        """
        cleaned: typing.List[EnvVar] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    EnvVar,
                    EnvVar().from_dict(item),
                )
            cleaned.append(typing.cast(EnvVar, item))
        self._properties["env"] = cleaned

    @property
    def env_from(self) -> typing.List["EnvFromSource"]:
        """
        EnvFrom defines the collection of EnvFromSource to inject
        into containers.
        """
        return typing.cast(
            typing.List["EnvFromSource"],
            self._properties.get("envFrom"),
        )

    @env_from.setter
    def env_from(
        self, value: typing.Union[typing.List["EnvFromSource"], typing.List[dict]]
    ):
        """
        EnvFrom defines the collection of EnvFromSource to inject
        into containers.
        """
        cleaned: typing.List[EnvFromSource] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    EnvFromSource,
                    EnvFromSource().from_dict(item),
                )
            cleaned.append(typing.cast(EnvFromSource, item))
        self._properties["envFrom"] = cleaned

    @property
    def selector(self) -> "LabelSelector":
        """
        Selector is a label query over a set of resources, in this
        case pods. Required.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        Selector is a label query over a set of resources, in this
        case pods. Required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def volume_mounts(self) -> typing.List["VolumeMount"]:
        """
        VolumeMounts defines the collection of VolumeMount to inject
        into containers.
        """
        return typing.cast(
            typing.List["VolumeMount"],
            self._properties.get("volumeMounts"),
        )

    @volume_mounts.setter
    def volume_mounts(
        self, value: typing.Union[typing.List["VolumeMount"], typing.List[dict]]
    ):
        """
        VolumeMounts defines the collection of VolumeMount to inject
        into containers.
        """
        cleaned: typing.List[VolumeMount] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    VolumeMount,
                    VolumeMount().from_dict(item),
                )
            cleaned.append(typing.cast(VolumeMount, item))
        self._properties["volumeMounts"] = cleaned

    @property
    def volumes(self) -> typing.List["Volume"]:
        """
        Volumes defines the collection of Volume to inject into the
        pod.
        """
        return typing.cast(
            typing.List["Volume"],
            self._properties.get("volumes"),
        )

    @volumes.setter
    def volumes(self, value: typing.Union[typing.List["Volume"], typing.List[dict]]):
        """
        Volumes defines the collection of Volume to inject into the
        pod.
        """
        cleaned: typing.List[Volume] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Volume,
                    Volume().from_dict(item),
                )
            cleaned.append(typing.cast(Volume, item))
        self._properties["volumes"] = cleaned

    def __enter__(self) -> "PodPresetSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

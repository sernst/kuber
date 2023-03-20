import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_27.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_27.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_27.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_27.core_v1 import PersistentVolumeSpec  # noqa: F401
from kuber.v1_27.meta_v1 import Status  # noqa: F401
from kuber.v1_27.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_27.core_v1 import TopologySelectorTerm  # noqa: F401


class CSIDriver(_kuber_definitions.Resource):
    """
    CSIDriver captures information about a Container Storage
    Interface (CSI) volume driver deployed on the cluster.
    Kubernetes attach detach controller uses this object to
    determine whether attach is required. Kubelet uses this
    object to determine whether pod information needs to be
    passed on mount. CSIDriver objects are non-namespaced.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["CSIDriverSpec"] = None,
    ):
        """Create CSIDriver instance."""
        super(CSIDriver, self).__init__(api_version="storage/v1", kind="CSIDriver")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else CSIDriverSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (CSIDriverSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata. metadata.Name indicates the name
        of the CSI driver that this object refers to; it MUST be the
        same name returned by the CSI GetPluginName() call for that
        driver. The driver name must be 63 characters or less,
        beginning and ending with an alphanumeric character
        ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics
        between. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata. metadata.Name indicates the name
        of the CSI driver that this object refers to; it MUST be the
        same name returned by the CSI GetPluginName() call for that
        driver. The driver name must be 63 characters or less,
        beginning and ending with an alphanumeric character
        ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics
        between. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "CSIDriverSpec":
        """
        spec represents the specification of the CSI Driver.
        """
        return typing.cast(
            "CSIDriverSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["CSIDriverSpec", dict]):
        """
        spec represents the specification of the CSI Driver.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CSIDriverSpec,
                CSIDriverSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_csidriver", "create_csidriver"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: typing.Optional["str"] = None):
        """
        Replaces the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_csidriver", "replace_csidriver"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: typing.Optional["str"] = None):
        """
        Patches the CSIDriver in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_csidriver", "patch_csidriver"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the CSIDriver from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_csidriver",
            "read_csidriver",
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
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the CSIDriver from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_csidriver",
            "delete_csidriver",
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSIDriver":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIDriverList(_kuber_definitions.Collection):
    """
    CSIDriverList is a collection of CSIDriver objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["CSIDriver"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create CSIDriverList instance."""
        super(CSIDriverList, self).__init__(
            api_version="storage/v1", kind="CSIDriverList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CSIDriver),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CSIDriver"]:
        """
        items is the list of CSIDriver
        """
        return typing.cast(
            typing.List["CSIDriver"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["CSIDriver"], typing.List[dict]]):
        """
        items is the list of CSIDriver
        """
        cleaned: typing.List[CSIDriver] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CSIDriver,
                    CSIDriver().from_dict(item),
                )
            cleaned.append(typing.cast(CSIDriver, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSIDriverList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIDriverSpec(_kuber_definitions.Definition):
    """
    CSIDriverSpec is the specification of a CSIDriver.
    """

    def __init__(
        self,
        attach_required: typing.Optional[bool] = None,
        fs_group_policy: typing.Optional[str] = None,
        pod_info_on_mount: typing.Optional[bool] = None,
        requires_republish: typing.Optional[bool] = None,
        se_linux_mount: typing.Optional[bool] = None,
        storage_capacity: typing.Optional[bool] = None,
        token_requests: typing.Optional[typing.List["TokenRequest"]] = None,
        volume_lifecycle_modes: typing.Optional[typing.List[str]] = None,
    ):
        """Create CSIDriverSpec instance."""
        super(CSIDriverSpec, self).__init__(
            api_version="storage/v1", kind="CSIDriverSpec"
        )
        self._properties = {
            "attachRequired": attach_required if attach_required is not None else None,
            "fsGroupPolicy": fs_group_policy if fs_group_policy is not None else "",
            "podInfoOnMount": pod_info_on_mount
            if pod_info_on_mount is not None
            else None,
            "requiresRepublish": requires_republish
            if requires_republish is not None
            else None,
            "seLinuxMount": se_linux_mount if se_linux_mount is not None else None,
            "storageCapacity": storage_capacity
            if storage_capacity is not None
            else None,
            "tokenRequests": token_requests if token_requests is not None else [],
            "volumeLifecycleModes": volume_lifecycle_modes
            if volume_lifecycle_modes is not None
            else [],
        }
        self._types = {
            "attachRequired": (bool, None),
            "fsGroupPolicy": (str, None),
            "podInfoOnMount": (bool, None),
            "requiresRepublish": (bool, None),
            "seLinuxMount": (bool, None),
            "storageCapacity": (bool, None),
            "tokenRequests": (list, TokenRequest),
            "volumeLifecycleModes": (list, str),
        }

    @property
    def attach_required(self) -> bool:
        """
        attachRequired indicates this CSI volume driver requires an
        attach operation (because it implements the CSI
        ControllerPublishVolume() method), and that the Kubernetes
        attach detach controller should call the attach volume
        interface which checks the volumeattachment status and waits
        until the volume is attached before proceeding to mounting.
        The CSI external-attacher coordinates with CSI volume driver
        and updates the volumeattachment status when the attach
        operation is complete. If the CSIDriverRegistry feature gate
        is enabled and the value is specified to false, the attach
        operation will be skipped. Otherwise the attach operation
        will be called.

        This field is immutable.
        """
        return typing.cast(
            bool,
            self._properties.get("attachRequired"),
        )

    @attach_required.setter
    def attach_required(self, value: bool):
        """
        attachRequired indicates this CSI volume driver requires an
        attach operation (because it implements the CSI
        ControllerPublishVolume() method), and that the Kubernetes
        attach detach controller should call the attach volume
        interface which checks the volumeattachment status and waits
        until the volume is attached before proceeding to mounting.
        The CSI external-attacher coordinates with CSI volume driver
        and updates the volumeattachment status when the attach
        operation is complete. If the CSIDriverRegistry feature gate
        is enabled and the value is specified to false, the attach
        operation will be skipped. Otherwise the attach operation
        will be called.

        This field is immutable.
        """
        self._properties["attachRequired"] = value

    @property
    def fs_group_policy(self) -> str:
        """
        fsGroupPolicy defines if the underlying volume supports
        changing ownership and permission of the volume before being
        mounted. Refer to the specific FSGroupPolicy values for
        additional details.

        This field is immutable.

        Defaults to ReadWriteOnceWithFSType, which will examine each
        volume to determine if Kubernetes should modify ownership
        and permissions of the volume. With the default policy the
        defined fsGroup will only be applied if a fstype is defined
        and the volume's access mode contains ReadWriteOnce.
        """
        return typing.cast(
            str,
            self._properties.get("fsGroupPolicy"),
        )

    @fs_group_policy.setter
    def fs_group_policy(self, value: str):
        """
        fsGroupPolicy defines if the underlying volume supports
        changing ownership and permission of the volume before being
        mounted. Refer to the specific FSGroupPolicy values for
        additional details.

        This field is immutable.

        Defaults to ReadWriteOnceWithFSType, which will examine each
        volume to determine if Kubernetes should modify ownership
        and permissions of the volume. With the default policy the
        defined fsGroup will only be applied if a fstype is defined
        and the volume's access mode contains ReadWriteOnce.
        """
        self._properties["fsGroupPolicy"] = value

    @property
    def pod_info_on_mount(self) -> bool:
        """
        podInfoOnMount indicates this CSI volume driver requires
        additional pod information (like podName, podUID, etc.)
        during mount operations, if set to true. If set to false,
        pod information will not be passed on mount. Default is
        false.

        The CSI driver specifies podInfoOnMount as part of driver
        deployment. If true, Kubelet will pass pod information as
        VolumeContext in the CSI NodePublishVolume() calls. The CSI
        driver is responsible for parsing and validating the
        information passed in as VolumeContext.

        The following VolumeConext will be passed if podInfoOnMount
        is set to true. This list might grow, but the prefix will be
        used. "csi.storage.k8s.io/pod.name": pod.Name
        "csi.storage.k8s.io/pod.namespace": pod.Namespace
        "csi.storage.k8s.io/pod.uid": string(pod.UID)
        "csi.storage.k8s.io/ephemeral": "true" if the volume is an
        ephemeral inline volume
                                        defined by a
        CSIVolumeSource, otherwise "false"

        "csi.storage.k8s.io/ephemeral" is a new feature in
        Kubernetes 1.16. It is only required for drivers which
        support both the "Persistent" and "Ephemeral"
        VolumeLifecycleMode. Other drivers can leave pod info
        disabled and/or ignore this field. As Kubernetes 1.15
        doesn't support this field, drivers can only support one
        mode when deployed on such a cluster and the deployment
        determines which mode that is, for example via a command
        line parameter of the driver.

        This field is immutable.
        """
        return typing.cast(
            bool,
            self._properties.get("podInfoOnMount"),
        )

    @pod_info_on_mount.setter
    def pod_info_on_mount(self, value: bool):
        """
        podInfoOnMount indicates this CSI volume driver requires
        additional pod information (like podName, podUID, etc.)
        during mount operations, if set to true. If set to false,
        pod information will not be passed on mount. Default is
        false.

        The CSI driver specifies podInfoOnMount as part of driver
        deployment. If true, Kubelet will pass pod information as
        VolumeContext in the CSI NodePublishVolume() calls. The CSI
        driver is responsible for parsing and validating the
        information passed in as VolumeContext.

        The following VolumeConext will be passed if podInfoOnMount
        is set to true. This list might grow, but the prefix will be
        used. "csi.storage.k8s.io/pod.name": pod.Name
        "csi.storage.k8s.io/pod.namespace": pod.Namespace
        "csi.storage.k8s.io/pod.uid": string(pod.UID)
        "csi.storage.k8s.io/ephemeral": "true" if the volume is an
        ephemeral inline volume
                                        defined by a
        CSIVolumeSource, otherwise "false"

        "csi.storage.k8s.io/ephemeral" is a new feature in
        Kubernetes 1.16. It is only required for drivers which
        support both the "Persistent" and "Ephemeral"
        VolumeLifecycleMode. Other drivers can leave pod info
        disabled and/or ignore this field. As Kubernetes 1.15
        doesn't support this field, drivers can only support one
        mode when deployed on such a cluster and the deployment
        determines which mode that is, for example via a command
        line parameter of the driver.

        This field is immutable.
        """
        self._properties["podInfoOnMount"] = value

    @property
    def requires_republish(self) -> bool:
        """
        requiresRepublish indicates the CSI driver wants
        `NodePublishVolume` being periodically called to reflect any
        possible change in the mounted volume. This field defaults
        to false.

        Note: After a successful initial NodePublishVolume call,
        subsequent calls to NodePublishVolume should only update the
        contents of the volume. New mount points will not be seen by
        a running container.
        """
        return typing.cast(
            bool,
            self._properties.get("requiresRepublish"),
        )

    @requires_republish.setter
    def requires_republish(self, value: bool):
        """
        requiresRepublish indicates the CSI driver wants
        `NodePublishVolume` being periodically called to reflect any
        possible change in the mounted volume. This field defaults
        to false.

        Note: After a successful initial NodePublishVolume call,
        subsequent calls to NodePublishVolume should only update the
        contents of the volume. New mount points will not be seen by
        a running container.
        """
        self._properties["requiresRepublish"] = value

    @property
    def se_linux_mount(self) -> bool:
        """
        seLinuxMount specifies if the CSI driver supports "-o
        context" mount option.

        When "true", the CSI driver must ensure that all volumes
        provided by this CSI driver can be mounted separately with
        different `-o context` options. This is typical for storage
        backends that provide volumes as filesystems on block
        devices or as independent shared volumes. Kubernetes will
        call NodeStage / NodePublish with "-o context=xyz" mount
        option when mounting a ReadWriteOncePod volume used in Pod
        that has explicitly set SELinux context. In the future, it
        may be expanded to other volume AccessModes. In any case,
        Kubernetes will ensure that the volume is mounted only with
        a single SELinux context.

        When "false", Kubernetes won't pass any special SELinux
        mount options to the driver. This is typical for volumes
        that represent subdirectories of a bigger shared filesystem.

        Default is "false".
        """
        return typing.cast(
            bool,
            self._properties.get("seLinuxMount"),
        )

    @se_linux_mount.setter
    def se_linux_mount(self, value: bool):
        """
        seLinuxMount specifies if the CSI driver supports "-o
        context" mount option.

        When "true", the CSI driver must ensure that all volumes
        provided by this CSI driver can be mounted separately with
        different `-o context` options. This is typical for storage
        backends that provide volumes as filesystems on block
        devices or as independent shared volumes. Kubernetes will
        call NodeStage / NodePublish with "-o context=xyz" mount
        option when mounting a ReadWriteOncePod volume used in Pod
        that has explicitly set SELinux context. In the future, it
        may be expanded to other volume AccessModes. In any case,
        Kubernetes will ensure that the volume is mounted only with
        a single SELinux context.

        When "false", Kubernetes won't pass any special SELinux
        mount options to the driver. This is typical for volumes
        that represent subdirectories of a bigger shared filesystem.

        Default is "false".
        """
        self._properties["seLinuxMount"] = value

    @property
    def storage_capacity(self) -> bool:
        """
        storageCapacity indicates that the CSI volume driver wants
        pod scheduling to consider the storage capacity that the
        driver deployment will report by creating CSIStorageCapacity
        objects with capacity information, if set to true.

        The check can be enabled immediately when deploying a
        driver. In that case, provisioning new volumes with late
        binding will pause until the driver deployment has published
        some suitable CSIStorageCapacity object.

        Alternatively, the driver can be deployed with the field
        unset or false and it can be flipped later when storage
        capacity information has been published.

        This field was immutable in Kubernetes <= 1.22 and now is
        mutable.
        """
        return typing.cast(
            bool,
            self._properties.get("storageCapacity"),
        )

    @storage_capacity.setter
    def storage_capacity(self, value: bool):
        """
        storageCapacity indicates that the CSI volume driver wants
        pod scheduling to consider the storage capacity that the
        driver deployment will report by creating CSIStorageCapacity
        objects with capacity information, if set to true.

        The check can be enabled immediately when deploying a
        driver. In that case, provisioning new volumes with late
        binding will pause until the driver deployment has published
        some suitable CSIStorageCapacity object.

        Alternatively, the driver can be deployed with the field
        unset or false and it can be flipped later when storage
        capacity information has been published.

        This field was immutable in Kubernetes <= 1.22 and now is
        mutable.
        """
        self._properties["storageCapacity"] = value

    @property
    def token_requests(self) -> typing.List["TokenRequest"]:
        """
        tokenRequests indicates the CSI driver needs pods' service
        account tokens it is mounting volume for to do necessary
        authentication. Kubelet will pass the tokens in
        VolumeContext in the CSI NodePublishVolume calls. The CSI
        driver should parse and validate the following
        VolumeContext: "csi.storage.k8s.io/serviceAccount.tokens": {
          "<audience>": {
            "token": <token>,
            "expirationTimestamp": <expiration timestamp in
        RFC3339>,
          },
          ...
        }

        Note: Audience in each TokenRequest should be different and
        at most one token is empty string. To receive a new token
        after expiry, RequiresRepublish can be used to trigger
        NodePublishVolume periodically.
        """
        return typing.cast(
            typing.List["TokenRequest"],
            self._properties.get("tokenRequests"),
        )

    @token_requests.setter
    def token_requests(
        self, value: typing.Union[typing.List["TokenRequest"], typing.List[dict]]
    ):
        """
        tokenRequests indicates the CSI driver needs pods' service
        account tokens it is mounting volume for to do necessary
        authentication. Kubelet will pass the tokens in
        VolumeContext in the CSI NodePublishVolume calls. The CSI
        driver should parse and validate the following
        VolumeContext: "csi.storage.k8s.io/serviceAccount.tokens": {
          "<audience>": {
            "token": <token>,
            "expirationTimestamp": <expiration timestamp in
        RFC3339>,
          },
          ...
        }

        Note: Audience in each TokenRequest should be different and
        at most one token is empty string. To receive a new token
        after expiry, RequiresRepublish can be used to trigger
        NodePublishVolume periodically.
        """
        cleaned: typing.List[TokenRequest] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    TokenRequest,
                    TokenRequest().from_dict(item),
                )
            cleaned.append(typing.cast(TokenRequest, item))
        self._properties["tokenRequests"] = cleaned

    @property
    def volume_lifecycle_modes(self) -> typing.List[str]:
        """
        volumeLifecycleModes defines what kind of volumes this CSI
        volume driver supports. The default if the list is empty is
        "Persistent", which is the usage defined by the CSI
        specification and implemented in Kubernetes via the usual
        PV/PVC mechanism.

        The other mode is "Ephemeral". In this mode, volumes are
        defined inline inside the pod spec with CSIVolumeSource and
        their lifecycle is tied to the lifecycle of that pod. A
        driver has to be aware of this because it is only going to
        get a NodePublishVolume call for such a volume.

        For more information about implementing this mode, see
        https://kubernetes-csi.github.io/docs/ephemeral-local-
        volumes.html A driver can support one or more of these modes
        and more modes may be added in the future.

        This field is beta. This field is immutable.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("volumeLifecycleModes"),
        )

    @volume_lifecycle_modes.setter
    def volume_lifecycle_modes(self, value: typing.List[str]):
        """
        volumeLifecycleModes defines what kind of volumes this CSI
        volume driver supports. The default if the list is empty is
        "Persistent", which is the usage defined by the CSI
        specification and implemented in Kubernetes via the usual
        PV/PVC mechanism.

        The other mode is "Ephemeral". In this mode, volumes are
        defined inline inside the pod spec with CSIVolumeSource and
        their lifecycle is tied to the lifecycle of that pod. A
        driver has to be aware of this because it is only going to
        get a NodePublishVolume call for such a volume.

        For more information about implementing this mode, see
        https://kubernetes-csi.github.io/docs/ephemeral-local-
        volumes.html A driver can support one or more of these modes
        and more modes may be added in the future.

        This field is beta. This field is immutable.
        """
        self._properties["volumeLifecycleModes"] = value

    def __enter__(self) -> "CSIDriverSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINode(_kuber_definitions.Resource):
    """
    CSINode holds information about all CSI drivers installed on
    a node. CSI drivers do not need to create the CSINode object
    directly. As long as they use the node-driver-registrar
    sidecar container, the kubelet will automatically populate
    the CSINode object for the CSI driver as part of kubelet
    plugin registration. CSINode has the same name as a node. If
    the object is missing, it means either there are no CSI
    Drivers available on the node, or the Kubelet version is low
    enough that it doesn't create this object. CSINode has an
    OwnerReference that points to the corresponding node object.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["CSINodeSpec"] = None,
    ):
        """Create CSINode instance."""
        super(CSINode, self).__init__(api_version="storage/v1", kind="CSINode")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else CSINodeSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (CSINodeSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. metadata.name must be the
        Kubernetes node name.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. metadata.name must be the
        Kubernetes node name.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "CSINodeSpec":
        """
        spec is the specification of CSINode
        """
        return typing.cast(
            "CSINodeSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["CSINodeSpec", dict]):
        """
        spec is the specification of CSINode
        """
        if isinstance(value, dict):
            value = typing.cast(
                CSINodeSpec,
                CSINodeSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_csinode", "create_csinode"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: typing.Optional["str"] = None):
        """
        Replaces the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_csinode", "replace_csinode"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: typing.Optional["str"] = None):
        """
        Patches the CSINode in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_csinode", "patch_csinode"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the CSINode from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_csinode",
            "read_csinode",
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
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the CSINode from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_csinode",
            "delete_csinode",
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSINode":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeDriver(_kuber_definitions.Definition):
    """
    CSINodeDriver holds information about the specification of
    one CSI driver installed on a node
    """

    def __init__(
        self,
        allocatable: typing.Optional["VolumeNodeResources"] = None,
        name: typing.Optional[str] = None,
        node_id: typing.Optional[str] = None,
        topology_keys: typing.Optional[typing.List[str]] = None,
    ):
        """Create CSINodeDriver instance."""
        super(CSINodeDriver, self).__init__(
            api_version="storage/v1", kind="CSINodeDriver"
        )
        self._properties = {
            "allocatable": allocatable
            if allocatable is not None
            else VolumeNodeResources(),
            "name": name if name is not None else "",
            "nodeID": node_id if node_id is not None else "",
            "topologyKeys": topology_keys if topology_keys is not None else [],
        }
        self._types = {
            "allocatable": (VolumeNodeResources, None),
            "name": (str, None),
            "nodeID": (str, None),
            "topologyKeys": (list, str),
        }

    @property
    def allocatable(self) -> "VolumeNodeResources":
        """
        allocatable represents the volume resources of a node that
        are available for scheduling. This field is beta.
        """
        return typing.cast(
            "VolumeNodeResources",
            self._properties.get("allocatable"),
        )

    @allocatable.setter
    def allocatable(self, value: typing.Union["VolumeNodeResources", dict]):
        """
        allocatable represents the volume resources of a node that
        are available for scheduling. This field is beta.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeNodeResources,
                VolumeNodeResources().from_dict(value),
            )
        self._properties["allocatable"] = value

    @property
    def name(self) -> str:
        """
        name represents the name of the CSI driver that this object
        refers to. This MUST be the same name returned by the CSI
        GetPluginName() call for that driver.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name represents the name of the CSI driver that this object
        refers to. This MUST be the same name returned by the CSI
        GetPluginName() call for that driver.
        """
        self._properties["name"] = value

    @property
    def node_id(self) -> str:
        """
        nodeID of the node from the driver point of view. This field
        enables Kubernetes to communicate with storage systems that
        do not share the same nomenclature for nodes. For example,
        Kubernetes may refer to a given node as "node1", but the
        storage system may refer to the same node as "nodeA". When
        Kubernetes issues a command to the storage system to attach
        a volume to a specific node, it can use this field to refer
        to the node name using the ID that the storage system will
        understand, e.g. "nodeA" instead of "node1". This field is
        required.
        """
        return typing.cast(
            str,
            self._properties.get("nodeID"),
        )

    @node_id.setter
    def node_id(self, value: str):
        """
        nodeID of the node from the driver point of view. This field
        enables Kubernetes to communicate with storage systems that
        do not share the same nomenclature for nodes. For example,
        Kubernetes may refer to a given node as "node1", but the
        storage system may refer to the same node as "nodeA". When
        Kubernetes issues a command to the storage system to attach
        a volume to a specific node, it can use this field to refer
        to the node name using the ID that the storage system will
        understand, e.g. "nodeA" instead of "node1". This field is
        required.
        """
        self._properties["nodeID"] = value

    @property
    def topology_keys(self) -> typing.List[str]:
        """
        topologyKeys is the list of keys supported by the driver.
        When a driver is initialized on a cluster, it provides a set
        of topology keys that it understands (e.g.
        "company.com/zone", "company.com/region"). When a driver is
        initialized on a node, it provides the same topology keys
        along with values. Kubelet will expose these topology keys
        as labels on its own node object. When Kubernetes does
        topology aware provisioning, it can use this list to
        determine which labels it should retrieve from the node
        object and pass back to the driver. It is possible for
        different nodes to use different topology keys. This can be
        empty if driver does not support topology.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("topologyKeys"),
        )

    @topology_keys.setter
    def topology_keys(self, value: typing.List[str]):
        """
        topologyKeys is the list of keys supported by the driver.
        When a driver is initialized on a cluster, it provides a set
        of topology keys that it understands (e.g.
        "company.com/zone", "company.com/region"). When a driver is
        initialized on a node, it provides the same topology keys
        along with values. Kubelet will expose these topology keys
        as labels on its own node object. When Kubernetes does
        topology aware provisioning, it can use this list to
        determine which labels it should retrieve from the node
        object and pass back to the driver. It is possible for
        different nodes to use different topology keys. This can be
        empty if driver does not support topology.
        """
        self._properties["topologyKeys"] = value

    def __enter__(self) -> "CSINodeDriver":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeList(_kuber_definitions.Collection):
    """
    CSINodeList is a collection of CSINode objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["CSINode"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create CSINodeList instance."""
        super(CSINodeList, self).__init__(api_version="storage/v1", kind="CSINodeList")
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CSINode),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CSINode"]:
        """
        items is the list of CSINode
        """
        return typing.cast(
            typing.List["CSINode"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["CSINode"], typing.List[dict]]):
        """
        items is the list of CSINode
        """
        cleaned: typing.List[CSINode] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CSINode,
                    CSINode().from_dict(item),
                )
            cleaned.append(typing.cast(CSINode, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSINodeList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSINodeSpec(_kuber_definitions.Definition):
    """
    CSINodeSpec holds information about the specification of all
    CSI drivers installed on a node
    """

    def __init__(
        self,
        drivers: typing.Optional[typing.List["CSINodeDriver"]] = None,
    ):
        """Create CSINodeSpec instance."""
        super(CSINodeSpec, self).__init__(api_version="storage/v1", kind="CSINodeSpec")
        self._properties = {
            "drivers": drivers if drivers is not None else [],
        }
        self._types = {
            "drivers": (list, CSINodeDriver),
        }

    @property
    def drivers(self) -> typing.List["CSINodeDriver"]:
        """
        drivers is a list of information of all CSI Drivers existing
        on a node. If all drivers in the list are uninstalled, this
        can become empty.
        """
        return typing.cast(
            typing.List["CSINodeDriver"],
            self._properties.get("drivers"),
        )

    @drivers.setter
    def drivers(
        self, value: typing.Union[typing.List["CSINodeDriver"], typing.List[dict]]
    ):
        """
        drivers is a list of information of all CSI Drivers existing
        on a node. If all drivers in the list are uninstalled, this
        can become empty.
        """
        cleaned: typing.List[CSINodeDriver] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CSINodeDriver,
                    CSINodeDriver().from_dict(item),
                )
            cleaned.append(typing.cast(CSINodeDriver, item))
        self._properties["drivers"] = cleaned

    def __enter__(self) -> "CSINodeSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIStorageCapacity(_kuber_definitions.Resource):
    """
    CSIStorageCapacity stores the result of one CSI GetCapacity
    call. For a given StorageClass, this describes the available
    capacity in a particular topology segment.  This can be used
    when considering where to instantiate new PersistentVolumes.

    For example this can express things like: - StorageClass
    "standard" has "1234 GiB" available in
    "topology.kubernetes.io/zone=us-east1" - StorageClass
    "localssd" has "10 GiB" available in
    "kubernetes.io/hostname=knode-abc123"

    The following three cases all imply that no capacity is
    available for a certain combination: - no object exists with
    suitable topology and storage class name - such an object
    exists, but the capacity is unset - such an object exists,
    but the capacity is zero

    The producer of these objects can decide which approach is
    more suitable.

    They are consumed by the kube-scheduler when a CSI driver
    opts into capacity-aware scheduling with
    CSIDriverSpec.StorageCapacity. The scheduler compares the
    MaximumVolumeSize against the requested size of pending
    volumes to filter out unsuitable nodes. If MaximumVolumeSize
    is unset, it falls back to a comparison against the less
    precise Capacity. If that is also unset, the scheduler
    assumes that capacity is insufficient and tries some other
    node.
    """

    def __init__(
        self,
        capacity: typing.Optional[typing.Union[str, int, None]] = None,
        maximum_volume_size: typing.Optional[typing.Union[str, int, None]] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        node_topology: typing.Optional["LabelSelector"] = None,
        storage_class_name: typing.Optional[str] = None,
    ):
        """Create CSIStorageCapacity instance."""
        super(CSIStorageCapacity, self).__init__(
            api_version="storage/v1", kind="CSIStorageCapacity"
        )
        self._properties = {
            "capacity": capacity if capacity is not None else None,
            "maximumVolumeSize": maximum_volume_size
            if maximum_volume_size is not None
            else None,
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "nodeTopology": node_topology
            if node_topology is not None
            else LabelSelector(),
            "storageClassName": storage_class_name
            if storage_class_name is not None
            else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "capacity": (_types.integer_or_string, None),
            "kind": (str, None),
            "maximumVolumeSize": (_types.integer_or_string, None),
            "metadata": (ObjectMeta, None),
            "nodeTopology": (LabelSelector, None),
            "storageClassName": (str, None),
        }

    @property
    def capacity(self) -> typing.Optional[str]:
        """
        capacity is the value reported by the CSI driver in its
        GetCapacityResponse for a GetCapacityRequest with topology
        and parameters that match the previous fields.

        The semantic is currently (CSI spec 1.2) defined as: The
        available capacity, in bytes, of the storage that can be
        used to provision volumes. If not set, that information is
        currently unavailable.
        """
        value = self._properties.get("capacity")
        return f"{value}" if value is not None else None

    @capacity.setter
    def capacity(self, value: typing.Union[str, int, None]):
        """
        capacity is the value reported by the CSI driver in its
        GetCapacityResponse for a GetCapacityRequest with topology
        and parameters that match the previous fields.

        The semantic is currently (CSI spec 1.2) defined as: The
        available capacity, in bytes, of the storage that can be
        used to provision volumes. If not set, that information is
        currently unavailable.
        """
        self._properties["capacity"] = _types.integer_or_string(value)

    @property
    def maximum_volume_size(self) -> typing.Optional[str]:
        """
        maximumVolumeSize is the value reported by the CSI driver in
        its GetCapacityResponse for a GetCapacityRequest with
        topology and parameters that match the previous fields.

        This is defined since CSI spec 1.4.0 as the largest size
        that may be used in a
        CreateVolumeRequest.capacity_range.required_bytes field to
        create a volume with the same parameters as those in
        GetCapacityRequest. The corresponding value in the
        Kubernetes API is ResourceRequirements.Requests in a volume
        claim.
        """
        value = self._properties.get("maximumVolumeSize")
        return f"{value}" if value is not None else None

    @maximum_volume_size.setter
    def maximum_volume_size(self, value: typing.Union[str, int, None]):
        """
        maximumVolumeSize is the value reported by the CSI driver in
        its GetCapacityResponse for a GetCapacityRequest with
        topology and parameters that match the previous fields.

        This is defined since CSI spec 1.4.0 as the largest size
        that may be used in a
        CreateVolumeRequest.capacity_range.required_bytes field to
        create a volume with the same parameters as those in
        GetCapacityRequest. The corresponding value in the
        Kubernetes API is ResourceRequirements.Requests in a volume
        claim.
        """
        self._properties["maximumVolumeSize"] = _types.integer_or_string(value)

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. The name has no particular
        meaning. It must be a DNS subdomain (dots allowed, 253
        characters). To ensure that there are no conflicts with
        other CSI drivers on the cluster, the recommendation is to
        use csisc-<uuid>, a generated name, or a reverse-domain name
        which ends with the unique CSI driver name.

        Objects are namespaced.

        More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. The name has no particular
        meaning. It must be a DNS subdomain (dots allowed, 253
        characters). To ensure that there are no conflicts with
        other CSI drivers on the cluster, the recommendation is to
        use csisc-<uuid>, a generated name, or a reverse-domain name
        which ends with the unique CSI driver name.

        Objects are namespaced.

        More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def node_topology(self) -> "LabelSelector":
        """
        nodeTopology defines which nodes have access to the storage
        for which capacity was reported. If not set, the storage is
        not accessible from any node in the cluster. If empty, the
        storage is accessible from all nodes. This field is
        immutable.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("nodeTopology"),
        )

    @node_topology.setter
    def node_topology(self, value: typing.Union["LabelSelector", dict]):
        """
        nodeTopology defines which nodes have access to the storage
        for which capacity was reported. If not set, the storage is
        not accessible from any node in the cluster. If empty, the
        storage is accessible from all nodes. This field is
        immutable.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["nodeTopology"] = value

    @property
    def storage_class_name(self) -> str:
        """
        storageClassName represents the name of the StorageClass
        that the reported capacity applies to. It must meet the same
        requirements as the name of a StorageClass object (non-
        empty, DNS subdomain). If that object no longer exists, the
        CSIStorageCapacity object is obsolete and should be removed
        by its creator. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("storageClassName"),
        )

    @storage_class_name.setter
    def storage_class_name(self, value: str):
        """
        storageClassName represents the name of the StorageClass
        that the reported capacity applies to. It must meet the same
        requirements as the name of a StorageClass object (non-
        empty, DNS subdomain). If that object no longer exists, the
        CSIStorageCapacity object is obsolete and should be removed
        by its creator. This field is immutable.
        """
        self._properties["storageClassName"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_csistorage_capacity", "create_csistorage_capacity"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: typing.Optional["str"] = None):
        """
        Replaces the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_csistorage_capacity",
            "replace_csistorage_capacity",
        ]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: typing.Optional["str"] = None):
        """
        Patches the CSIStorageCapacity in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_csistorage_capacity", "patch_csistorage_capacity"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the CSIStorageCapacity from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_csistorage_capacity",
            "read_csistorage_capacity",
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
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the CSIStorageCapacity from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_csistorage_capacity",
            "delete_csistorage_capacity",
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSIStorageCapacity":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CSIStorageCapacityList(_kuber_definitions.Collection):
    """
    CSIStorageCapacityList is a collection of CSIStorageCapacity
    objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["CSIStorageCapacity"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create CSIStorageCapacityList instance."""
        super(CSIStorageCapacityList, self).__init__(
            api_version="storage/v1", kind="CSIStorageCapacityList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CSIStorageCapacity),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CSIStorageCapacity"]:
        """
        items is the list of CSIStorageCapacity objects.
        """
        return typing.cast(
            typing.List["CSIStorageCapacity"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["CSIStorageCapacity"], typing.List[dict]]
    ):
        """
        items is the list of CSIStorageCapacity objects.
        """
        cleaned: typing.List[CSIStorageCapacity] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CSIStorageCapacity,
                    CSIStorageCapacity().from_dict(item),
                )
            cleaned.append(typing.cast(CSIStorageCapacity, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "CSIStorageCapacityList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageClass(_kuber_definitions.Resource):
    """
    StorageClass describes the parameters for a class of storage
    for which PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-namespaced; the name of the storage
    class according to etcd is in ObjectMeta.Name.
    """

    def __init__(
        self,
        allow_volume_expansion: typing.Optional[bool] = None,
        allowed_topologies: typing.Optional[typing.List["TopologySelectorTerm"]] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        mount_options: typing.Optional[typing.List[str]] = None,
        parameters: typing.Optional[dict] = None,
        provisioner: typing.Optional[str] = None,
        reclaim_policy: typing.Optional[str] = None,
        volume_binding_mode: typing.Optional[str] = None,
    ):
        """Create StorageClass instance."""
        super(StorageClass, self).__init__(
            api_version="storage/v1", kind="StorageClass"
        )
        self._properties = {
            "allowVolumeExpansion": allow_volume_expansion
            if allow_volume_expansion is not None
            else None,
            "allowedTopologies": allowed_topologies
            if allowed_topologies is not None
            else [],
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "mountOptions": mount_options if mount_options is not None else [],
            "parameters": parameters if parameters is not None else {},
            "provisioner": provisioner if provisioner is not None else "",
            "reclaimPolicy": reclaim_policy if reclaim_policy is not None else "",
            "volumeBindingMode": volume_binding_mode
            if volume_binding_mode is not None
            else "",
        }
        self._types = {
            "allowVolumeExpansion": (bool, None),
            "allowedTopologies": (list, TopologySelectorTerm),
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "mountOptions": (list, str),
            "parameters": (dict, None),
            "provisioner": (str, None),
            "reclaimPolicy": (str, None),
            "volumeBindingMode": (str, None),
        }

    @property
    def allow_volume_expansion(self) -> bool:
        """
        allowVolumeExpansion shows whether the storage class allow
        volume expand.
        """
        return typing.cast(
            bool,
            self._properties.get("allowVolumeExpansion"),
        )

    @allow_volume_expansion.setter
    def allow_volume_expansion(self, value: bool):
        """
        allowVolumeExpansion shows whether the storage class allow
        volume expand.
        """
        self._properties["allowVolumeExpansion"] = value

    @property
    def allowed_topologies(self) -> typing.List["TopologySelectorTerm"]:
        """
        allowedTopologies restrict the node topologies where volumes
        can be dynamically provisioned. Each volume plugin defines
        its own supported topology specifications. An empty
        TopologySelectorTerm list means there is no topology
        restriction. This field is only honored by servers that
        enable the VolumeScheduling feature.
        """
        return typing.cast(
            typing.List["TopologySelectorTerm"],
            self._properties.get("allowedTopologies"),
        )

    @allowed_topologies.setter
    def allowed_topologies(
        self,
        value: typing.Union[typing.List["TopologySelectorTerm"], typing.List[dict]],
    ):
        """
        allowedTopologies restrict the node topologies where volumes
        can be dynamically provisioned. Each volume plugin defines
        its own supported topology specifications. An empty
        TopologySelectorTerm list means there is no topology
        restriction. This field is only honored by servers that
        enable the VolumeScheduling feature.
        """
        cleaned: typing.List[TopologySelectorTerm] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    TopologySelectorTerm,
                    TopologySelectorTerm().from_dict(item),
                )
            cleaned.append(typing.cast(TopologySelectorTerm, item))
        self._properties["allowedTopologies"] = cleaned

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def mount_options(self) -> typing.List[str]:
        """
        mountOptions controls the mountOptions for dynamically
        provisioned PersistentVolumes of this storage class. e.g.
        ["ro", "soft"]. Not validated - mount of the PVs will simply
        fail if one is invalid.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("mountOptions"),
        )

    @mount_options.setter
    def mount_options(self, value: typing.List[str]):
        """
        mountOptions controls the mountOptions for dynamically
        provisioned PersistentVolumes of this storage class. e.g.
        ["ro", "soft"]. Not validated - mount of the PVs will simply
        fail if one is invalid.
        """
        self._properties["mountOptions"] = value

    @property
    def parameters(self) -> dict:
        """
        parameters holds the parameters for the provisioner that
        should create volumes of this storage class.
        """
        return typing.cast(
            dict,
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: dict):
        """
        parameters holds the parameters for the provisioner that
        should create volumes of this storage class.
        """
        self._properties["parameters"] = value

    @property
    def provisioner(self) -> str:
        """
        provisioner indicates the type of the provisioner.
        """
        return typing.cast(
            str,
            self._properties.get("provisioner"),
        )

    @provisioner.setter
    def provisioner(self, value: str):
        """
        provisioner indicates the type of the provisioner.
        """
        self._properties["provisioner"] = value

    @property
    def reclaim_policy(self) -> str:
        """
        reclaimPolicy controls the reclaimPolicy for dynamically
        provisioned PersistentVolumes of this storage class.
        Defaults to Delete.
        """
        return typing.cast(
            str,
            self._properties.get("reclaimPolicy"),
        )

    @reclaim_policy.setter
    def reclaim_policy(self, value: str):
        """
        reclaimPolicy controls the reclaimPolicy for dynamically
        provisioned PersistentVolumes of this storage class.
        Defaults to Delete.
        """
        self._properties["reclaimPolicy"] = value

    @property
    def volume_binding_mode(self) -> str:
        """
        volumeBindingMode indicates how PersistentVolumeClaims
        should be provisioned and bound.  When unset,
        VolumeBindingImmediate is used. This field is only honored
        by servers that enable the VolumeScheduling feature.
        """
        return typing.cast(
            str,
            self._properties.get("volumeBindingMode"),
        )

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: str):
        """
        volumeBindingMode indicates how PersistentVolumeClaims
        should be provisioned and bound.  When unset,
        VolumeBindingImmediate is used. This field is only honored
        by servers that enable the VolumeScheduling feature.
        """
        self._properties["volumeBindingMode"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_storage_class", "create_storage_class"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: typing.Optional["str"] = None):
        """
        Replaces the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_storage_class", "replace_storage_class"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: typing.Optional["str"] = None):
        """
        Patches the StorageClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_storage_class", "patch_storage_class"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the StorageClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_storage_class",
            "read_storage_class",
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
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the StorageClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_storage_class",
            "delete_storage_class",
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "StorageClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageClassList(_kuber_definitions.Collection):
    """
    StorageClassList is a collection of storage classes.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["StorageClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create StorageClassList instance."""
        super(StorageClassList, self).__init__(
            api_version="storage/v1", kind="StorageClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, StorageClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["StorageClass"]:
        """
        items is the list of StorageClasses
        """
        return typing.cast(
            typing.List["StorageClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["StorageClass"], typing.List[dict]]
    ):
        """
        items is the list of StorageClasses
        """
        cleaned: typing.List[StorageClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    StorageClass,
                    StorageClass().from_dict(item),
                )
            cleaned.append(typing.cast(StorageClass, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "StorageClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenRequest(_kuber_definitions.Definition):
    """
    TokenRequest contains parameters of a service account token.
    """

    def __init__(
        self,
        audience: typing.Optional[str] = None,
        expiration_seconds: typing.Optional[int] = None,
    ):
        """Create TokenRequest instance."""
        super(TokenRequest, self).__init__(
            api_version="storage/v1", kind="TokenRequest"
        )
        self._properties = {
            "audience": audience if audience is not None else "",
            "expirationSeconds": expiration_seconds
            if expiration_seconds is not None
            else None,
        }
        self._types = {
            "audience": (str, None),
            "expirationSeconds": (int, None),
        }

    @property
    def audience(self) -> str:
        """
        audience is the intended audience of the token in
        "TokenRequestSpec". It will default to the audiences of kube
        apiserver.
        """
        return typing.cast(
            str,
            self._properties.get("audience"),
        )

    @audience.setter
    def audience(self, value: str):
        """
        audience is the intended audience of the token in
        "TokenRequestSpec". It will default to the audiences of kube
        apiserver.
        """
        self._properties["audience"] = value

    @property
    def expiration_seconds(self) -> int:
        """
        expirationSeconds is the duration of validity of the token
        in "TokenRequestSpec". It has the same default value of
        "ExpirationSeconds" in "TokenRequestSpec".
        """
        return typing.cast(
            int,
            self._properties.get("expirationSeconds"),
        )

    @expiration_seconds.setter
    def expiration_seconds(self, value: int):
        """
        expirationSeconds is the duration of validity of the token
        in "TokenRequestSpec". It has the same default value of
        "ExpirationSeconds" in "TokenRequestSpec".
        """
        self._properties["expirationSeconds"] = value

    def __enter__(self) -> "TokenRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachment(_kuber_definitions.Resource):
    """
    VolumeAttachment captures the intent to attach or detach the
    specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["VolumeAttachmentSpec"] = None,
        status: typing.Optional["VolumeAttachmentStatus"] = None,
    ):
        """Create VolumeAttachment instance."""
        super(VolumeAttachment, self).__init__(
            api_version="storage/v1", kind="VolumeAttachment"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else VolumeAttachmentSpec(),
            "status": status if status is not None else VolumeAttachmentStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (VolumeAttachmentSpec, None),
            "status": (VolumeAttachmentStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "VolumeAttachmentSpec":
        """
        spec represents specification of the desired attach/detach
        volume behavior. Populated by the Kubernetes system.
        """
        return typing.cast(
            "VolumeAttachmentSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["VolumeAttachmentSpec", dict]):
        """
        spec represents specification of the desired attach/detach
        volume behavior. Populated by the Kubernetes system.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentSpec,
                VolumeAttachmentSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "VolumeAttachmentStatus":
        """
        status represents status of the VolumeAttachment request.
        Populated by the entity completing the attach or detach
        operation, i.e. the external-attacher.
        """
        return typing.cast(
            "VolumeAttachmentStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["VolumeAttachmentStatus", dict]):
        """
        status represents status of the VolumeAttachment request.
        Populated by the entity completing the attach or detach
        operation, i.e. the external-attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentStatus,
                VolumeAttachmentStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "VolumeAttachmentStatus":
        """
        Creates the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_volume_attachment", "create_volume_attachment"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "VolumeAttachmentStatus":
        """
        Replaces the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_volume_attachment", "replace_volume_attachment"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "VolumeAttachmentStatus":
        """
        Patches the VolumeAttachment in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_volume_attachment", "patch_volume_attachment"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "VolumeAttachmentStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_volume_attachment",
            "read_volume_attachment",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = VolumeAttachmentStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the VolumeAttachment from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_volume_attachment",
            "read_volume_attachment",
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
        namespace: typing.Optional[str] = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the VolumeAttachment from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_volume_attachment",
            "delete_volume_attachment",
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "VolumeAttachment":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentList(_kuber_definitions.Collection):
    """
    VolumeAttachmentList is a collection of VolumeAttachment
    objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["VolumeAttachment"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create VolumeAttachmentList instance."""
        super(VolumeAttachmentList, self).__init__(
            api_version="storage/v1", kind="VolumeAttachmentList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, VolumeAttachment),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["VolumeAttachment"]:
        """
        items is the list of VolumeAttachments
        """
        return typing.cast(
            typing.List["VolumeAttachment"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["VolumeAttachment"], typing.List[dict]]
    ):
        """
        items is the list of VolumeAttachments
        """
        cleaned: typing.List[VolumeAttachment] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    VolumeAttachment,
                    VolumeAttachment().from_dict(item),
                )
            cleaned.append(typing.cast(VolumeAttachment, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata More info:
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
        Standard list metadata More info:
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.StorageV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.StorageV1Api(**kwargs)

    def __enter__(self) -> "VolumeAttachmentList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSource(_kuber_definitions.Definition):
    """
    VolumeAttachmentSource represents a volume that should be
    attached. Right now only PersistenVolumes can be attached
    via external attacher, in future we may allow also inline
    volumes in pods. Exactly one member can be set.
    """

    def __init__(
        self,
        inline_volume_spec: typing.Optional["PersistentVolumeSpec"] = None,
        persistent_volume_name: typing.Optional[str] = None,
    ):
        """Create VolumeAttachmentSource instance."""
        super(VolumeAttachmentSource, self).__init__(
            api_version="storage/v1", kind="VolumeAttachmentSource"
        )
        self._properties = {
            "inlineVolumeSpec": inline_volume_spec
            if inline_volume_spec is not None
            else PersistentVolumeSpec(),
            "persistentVolumeName": persistent_volume_name
            if persistent_volume_name is not None
            else "",
        }
        self._types = {
            "inlineVolumeSpec": (PersistentVolumeSpec, None),
            "persistentVolumeName": (str, None),
        }

    @property
    def inline_volume_spec(self) -> "PersistentVolumeSpec":
        """
        inlineVolumeSpec contains all the information necessary to
        attach a persistent volume defined by a pod's inline
        VolumeSource. This field is populated only for the
        CSIMigration feature. It contains translated fields from a
        pod's inline VolumeSource to a PersistentVolumeSpec. This
        field is beta-level and is only honored by servers that
        enabled the CSIMigration feature.
        """
        return typing.cast(
            "PersistentVolumeSpec",
            self._properties.get("inlineVolumeSpec"),
        )

    @inline_volume_spec.setter
    def inline_volume_spec(self, value: typing.Union["PersistentVolumeSpec", dict]):
        """
        inlineVolumeSpec contains all the information necessary to
        attach a persistent volume defined by a pod's inline
        VolumeSource. This field is populated only for the
        CSIMigration feature. It contains translated fields from a
        pod's inline VolumeSource to a PersistentVolumeSpec. This
        field is beta-level and is only honored by servers that
        enabled the CSIMigration feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PersistentVolumeSpec,
                PersistentVolumeSpec().from_dict(value),
            )
        self._properties["inlineVolumeSpec"] = value

    @property
    def persistent_volume_name(self) -> str:
        """
        persistentVolumeName represents the name of the persistent
        volume to attach.
        """
        return typing.cast(
            str,
            self._properties.get("persistentVolumeName"),
        )

    @persistent_volume_name.setter
    def persistent_volume_name(self, value: str):
        """
        persistentVolumeName represents the name of the persistent
        volume to attach.
        """
        self._properties["persistentVolumeName"] = value

    def __enter__(self) -> "VolumeAttachmentSource":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentSpec(_kuber_definitions.Definition):
    """
    VolumeAttachmentSpec is the specification of a
    VolumeAttachment request.
    """

    def __init__(
        self,
        attacher: typing.Optional[str] = None,
        node_name: typing.Optional[str] = None,
        source: typing.Optional["VolumeAttachmentSource"] = None,
    ):
        """Create VolumeAttachmentSpec instance."""
        super(VolumeAttachmentSpec, self).__init__(
            api_version="storage/v1", kind="VolumeAttachmentSpec"
        )
        self._properties = {
            "attacher": attacher if attacher is not None else "",
            "nodeName": node_name if node_name is not None else "",
            "source": source if source is not None else VolumeAttachmentSource(),
        }
        self._types = {
            "attacher": (str, None),
            "nodeName": (str, None),
            "source": (VolumeAttachmentSource, None),
        }

    @property
    def attacher(self) -> str:
        """
        attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        return typing.cast(
            str,
            self._properties.get("attacher"),
        )

    @attacher.setter
    def attacher(self, value: str):
        """
        attacher indicates the name of the volume driver that MUST
        handle this request. This is the name returned by
        GetPluginName().
        """
        self._properties["attacher"] = value

    @property
    def node_name(self) -> str:
        """
        nodeName represents the node that the volume should be
        attached to.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        nodeName represents the node that the volume should be
        attached to.
        """
        self._properties["nodeName"] = value

    @property
    def source(self) -> "VolumeAttachmentSource":
        """
        source represents the volume that should be attached.
        """
        return typing.cast(
            "VolumeAttachmentSource",
            self._properties.get("source"),
        )

    @source.setter
    def source(self, value: typing.Union["VolumeAttachmentSource", dict]):
        """
        source represents the volume that should be attached.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeAttachmentSource,
                VolumeAttachmentSource().from_dict(value),
            )
        self._properties["source"] = value

    def __enter__(self) -> "VolumeAttachmentSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeAttachmentStatus(_kuber_definitions.Definition):
    """
    VolumeAttachmentStatus is the status of a VolumeAttachment
    request.
    """

    def __init__(
        self,
        attach_error: typing.Optional["VolumeError"] = None,
        attached: typing.Optional[bool] = None,
        attachment_metadata: typing.Optional[dict] = None,
        detach_error: typing.Optional["VolumeError"] = None,
    ):
        """Create VolumeAttachmentStatus instance."""
        super(VolumeAttachmentStatus, self).__init__(
            api_version="storage/v1", kind="VolumeAttachmentStatus"
        )
        self._properties = {
            "attachError": attach_error if attach_error is not None else VolumeError(),
            "attached": attached if attached is not None else None,
            "attachmentMetadata": attachment_metadata
            if attachment_metadata is not None
            else {},
            "detachError": detach_error if detach_error is not None else VolumeError(),
        }
        self._types = {
            "attachError": (VolumeError, None),
            "attached": (bool, None),
            "attachmentMetadata": (dict, None),
            "detachError": (VolumeError, None),
        }

    @property
    def attach_error(self) -> "VolumeError":
        """
        attachError represents the last error encountered during
        attach operation, if any. This field must only be set by the
        entity completing the attach operation, i.e. the external-
        attacher.
        """
        return typing.cast(
            "VolumeError",
            self._properties.get("attachError"),
        )

    @attach_error.setter
    def attach_error(self, value: typing.Union["VolumeError", dict]):
        """
        attachError represents the last error encountered during
        attach operation, if any. This field must only be set by the
        entity completing the attach operation, i.e. the external-
        attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeError,
                VolumeError().from_dict(value),
            )
        self._properties["attachError"] = value

    @property
    def attached(self) -> bool:
        """
        attached indicates the volume is successfully attached. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        return typing.cast(
            bool,
            self._properties.get("attached"),
        )

    @attached.setter
    def attached(self, value: bool):
        """
        attached indicates the volume is successfully attached. This
        field must only be set by the entity completing the attach
        operation, i.e. the external-attacher.
        """
        self._properties["attached"] = value

    @property
    def attachment_metadata(self) -> dict:
        """
        attachmentMetadata is populated with any information
        returned by the attach operation, upon successful attach,
        that must be passed into subsequent WaitForAttach or Mount
        calls. This field must only be set by the entity completing
        the attach operation, i.e. the external-attacher.
        """
        return typing.cast(
            dict,
            self._properties.get("attachmentMetadata"),
        )

    @attachment_metadata.setter
    def attachment_metadata(self, value: dict):
        """
        attachmentMetadata is populated with any information
        returned by the attach operation, upon successful attach,
        that must be passed into subsequent WaitForAttach or Mount
        calls. This field must only be set by the entity completing
        the attach operation, i.e. the external-attacher.
        """
        self._properties["attachmentMetadata"] = value

    @property
    def detach_error(self) -> "VolumeError":
        """
        detachError represents the last error encountered during
        detach operation, if any. This field must only be set by the
        entity completing the detach operation, i.e. the external-
        attacher.
        """
        return typing.cast(
            "VolumeError",
            self._properties.get("detachError"),
        )

    @detach_error.setter
    def detach_error(self, value: typing.Union["VolumeError", dict]):
        """
        detachError represents the last error encountered during
        detach operation, if any. This field must only be set by the
        entity completing the detach operation, i.e. the external-
        attacher.
        """
        if isinstance(value, dict):
            value = typing.cast(
                VolumeError,
                VolumeError().from_dict(value),
            )
        self._properties["detachError"] = value

    def __enter__(self) -> "VolumeAttachmentStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeError(_kuber_definitions.Definition):
    """
    VolumeError captures an error encountered during a volume
    operation.
    """

    def __init__(
        self,
        message: typing.Optional[str] = None,
        time: typing.Optional[str] = None,
    ):
        """Create VolumeError instance."""
        super(VolumeError, self).__init__(api_version="storage/v1", kind="VolumeError")
        self._properties = {
            "message": message if message is not None else "",
            "time": time if time is not None else None,
        }
        self._types = {
            "message": (str, None),
            "time": (str, None),
        }

    @property
    def message(self) -> str:
        """
        message represents the error encountered during Attach or
        Detach operation. This string may be logged, so it should
        not contain sensitive information.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        message represents the error encountered during Attach or
        Detach operation. This string may be logged, so it should
        not contain sensitive information.
        """
        self._properties["message"] = value

    @property
    def time(self) -> str:
        """
        time represents the time the error was encountered.
        """
        return typing.cast(
            str,
            self._properties.get("time"),
        )

    @time.setter
    def time(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        time represents the time the error was encountered.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["time"] = value

    def __enter__(self) -> "VolumeError":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VolumeNodeResources(_kuber_definitions.Definition):
    """
    VolumeNodeResources is a set of resource limits for
    scheduling of volumes.
    """

    def __init__(
        self,
        count: typing.Optional[int] = None,
    ):
        """Create VolumeNodeResources instance."""
        super(VolumeNodeResources, self).__init__(
            api_version="storage/v1", kind="VolumeNodeResources"
        )
        self._properties = {
            "count": count if count is not None else None,
        }
        self._types = {
            "count": (int, None),
        }

    @property
    def count(self) -> int:
        """
        count indicates the maximum number of unique volumes managed
        by the CSI driver that can be used on a node. A volume that
        is both attached and mounted on a node is considered to be
        used once, not twice. The same rule applies for a unique
        volume that is shared among multiple pods on the same node.
        If this field is not specified, then the supported number of
        volumes on this node is unbounded.
        """
        return typing.cast(
            int,
            self._properties.get("count"),
        )

    @count.setter
    def count(self, value: int):
        """
        count indicates the maximum number of unique volumes managed
        by the CSI driver that can be used on a node. A volume that
        is both attached and mounted on a node is considered to be
        used once, not twice. The same rule applies for a unique
        volume that is shared among multiple pods on the same node.
        If this field is not specified, then the supported number of
        volumes on this node is unbounded.
        """
        self._properties["count"] = value

    def __enter__(self) -> "VolumeNodeResources":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

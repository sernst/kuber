import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401


class ClusterTrustBundle(_kuber_definitions.Resource):
    """
    ClusterTrustBundle is a cluster-scoped container for X.509
    trust anchors (root certificates).

    ClusterTrustBundle objects are considered to be readable by
    any authenticated user in the cluster, because they can be
    mounted by pods using the `clusterTrustBundle` projection.
    All service accounts have read access to ClusterTrustBundles
    by default.  Users who only have namespace-level access to a
    cluster can read ClusterTrustBundles by impersonating a
    serviceaccount that they have access to.

    It can be optionally associated with a particular assigner,
    in which case it contains one valid set of trust anchors for
    that signer. Signers may have multiple associated
    ClusterTrustBundles; each is an independent set of trust
    anchors for that signer. Admission control is used to
    enforce that only users with permissions on the signer can
    create or modify the corresponding bundle.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ClusterTrustBundleSpec"] = None,
    ):
        """Create ClusterTrustBundle instance."""
        super(ClusterTrustBundle, self).__init__(
            api_version="certificates/v1alpha1", kind="ClusterTrustBundle"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ClusterTrustBundleSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ClusterTrustBundleSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        metadata contains the object metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        metadata contains the object metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ClusterTrustBundleSpec":
        """
        spec contains the signer (if any) and trust anchors.
        """
        return typing.cast(
            "ClusterTrustBundleSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ClusterTrustBundleSpec", dict]):
        """
        spec contains the signer (if any) and trust anchors.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ClusterTrustBundleSpec,
                ClusterTrustBundleSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ClusterTrustBundle in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_cluster_trust_bundle",
            "create_cluster_trust_bundle",
        ]

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
        Replaces the ClusterTrustBundle in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_cluster_trust_bundle",
            "replace_cluster_trust_bundle",
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
        Patches the ClusterTrustBundle in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_cluster_trust_bundle", "patch_cluster_trust_bundle"]

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
        Reads the ClusterTrustBundle from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_cluster_trust_bundle",
            "read_cluster_trust_bundle",
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
        Deletes the ClusterTrustBundle from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_cluster_trust_bundle",
            "delete_cluster_trust_bundle",
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
    ) -> "client.CertificatesV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CertificatesV1alpha1Api(**kwargs)

    def __enter__(self) -> "ClusterTrustBundle":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterTrustBundleList(_kuber_definitions.Collection):
    """
    ClusterTrustBundleList is a collection of ClusterTrustBundle
    objects
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ClusterTrustBundle"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ClusterTrustBundleList instance."""
        super(ClusterTrustBundleList, self).__init__(
            api_version="certificates/v1alpha1", kind="ClusterTrustBundleList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ClusterTrustBundle),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ClusterTrustBundle"]:
        """
        items is a collection of ClusterTrustBundle objects
        """
        return typing.cast(
            typing.List["ClusterTrustBundle"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ClusterTrustBundle"], typing.List[dict]]
    ):
        """
        items is a collection of ClusterTrustBundle objects
        """
        cleaned: typing.List[ClusterTrustBundle] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ClusterTrustBundle,
                    ClusterTrustBundle().from_dict(item),
                )
            cleaned.append(typing.cast(ClusterTrustBundle, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        metadata contains the list metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        metadata contains the list metadata.
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
    ) -> "client.CertificatesV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CertificatesV1alpha1Api(**kwargs)

    def __enter__(self) -> "ClusterTrustBundleList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterTrustBundleSpec(_kuber_definitions.Definition):
    """
    ClusterTrustBundleSpec contains the signer and trust
    anchors.
    """

    def __init__(
        self,
        signer_name: typing.Optional[str] = None,
        trust_bundle: typing.Optional[str] = None,
    ):
        """Create ClusterTrustBundleSpec instance."""
        super(ClusterTrustBundleSpec, self).__init__(
            api_version="certificates/v1alpha1", kind="ClusterTrustBundleSpec"
        )
        self._properties = {
            "signerName": signer_name if signer_name is not None else "",
            "trustBundle": trust_bundle if trust_bundle is not None else "",
        }
        self._types = {
            "signerName": (str, None),
            "trustBundle": (str, None),
        }

    @property
    def signer_name(self) -> str:
        """
        signerName indicates the associated signer, if any.

        In order to create or update a ClusterTrustBundle that sets
        signerName, you must have the following cluster-scoped
        permission: group=certificates.k8s.io resource=signers
        resourceName=<the signer name> verb=attest.

        If signerName is not empty, then the ClusterTrustBundle
        object must be named with the signer name as a prefix
        (translating slashes to colons). For example, for the signer
        name `example.com/foo`, valid ClusterTrustBundle object
        names include `example.com:foo:abc` and
        `example.com:foo:v1`.

        If signerName is empty, then the ClusterTrustBundle object's
        name must not have such a prefix.

        List/watch requests for ClusterTrustBundles can filter on
        this field using a `spec.signerName=NAME` field selector.
        """
        return typing.cast(
            str,
            self._properties.get("signerName"),
        )

    @signer_name.setter
    def signer_name(self, value: str):
        """
        signerName indicates the associated signer, if any.

        In order to create or update a ClusterTrustBundle that sets
        signerName, you must have the following cluster-scoped
        permission: group=certificates.k8s.io resource=signers
        resourceName=<the signer name> verb=attest.

        If signerName is not empty, then the ClusterTrustBundle
        object must be named with the signer name as a prefix
        (translating slashes to colons). For example, for the signer
        name `example.com/foo`, valid ClusterTrustBundle object
        names include `example.com:foo:abc` and
        `example.com:foo:v1`.

        If signerName is empty, then the ClusterTrustBundle object's
        name must not have such a prefix.

        List/watch requests for ClusterTrustBundles can filter on
        this field using a `spec.signerName=NAME` field selector.
        """
        self._properties["signerName"] = value

    @property
    def trust_bundle(self) -> str:
        """
        trustBundle contains the individual X.509 trust anchors for
        this bundle, as PEM bundle of PEM-wrapped, DER-formatted
        X.509 certificates.

        The data must consist only of PEM certificate blocks that
        parse as valid X.509 certificates.  Each certificate must
        include a basic constraints extension with the CA bit set.
        The API server will reject objects that contain duplicate
        certificates, or that use PEM block headers.

        Users of ClusterTrustBundles, including Kubelet, are free to
        reorder and deduplicate certificate blocks in this file
        according to their own logic, as well as to drop PEM block
        headers and inter-block data.
        """
        return typing.cast(
            str,
            self._properties.get("trustBundle"),
        )

    @trust_bundle.setter
    def trust_bundle(self, value: str):
        """
        trustBundle contains the individual X.509 trust anchors for
        this bundle, as PEM bundle of PEM-wrapped, DER-formatted
        X.509 certificates.

        The data must consist only of PEM certificate blocks that
        parse as valid X.509 certificates.  Each certificate must
        include a basic constraints extension with the CA bit set.
        The API server will reject objects that contain duplicate
        certificates, or that use PEM block headers.

        Users of ClusterTrustBundles, including Kubelet, are free to
        reorder and deduplicate certificate blocks in this file
        according to their own logic, as well as to drop PEM block
        headers and inter-block data.
        """
        self._properties["trustBundle"] = value

    def __enter__(self) -> "ClusterTrustBundleSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

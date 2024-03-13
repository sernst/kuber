import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_29.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_29.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_29.meta_v1 import Status  # noqa: F401
from kuber.v1_29.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_29.authentication_v1 import UserInfo  # noqa: F401


class SelfSubjectReview(_kuber_definitions.Resource):
    """
    SelfSubjectReview contains the user information that the
    kube-apiserver has about the user making this request. When
    using impersonation, users will receive the user info of the
    user being impersonated.  If impersonation or request header
    authentication is used, any extra keys will have their case
    ignored and returned as lowercase.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        status: typing.Optional["SelfSubjectReviewStatus"] = None,
    ):
        """Create SelfSubjectReview instance."""
        super(SelfSubjectReview, self).__init__(
            api_version="authentication/v1beta1", kind="SelfSubjectReview"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "status": status if status is not None else SelfSubjectReviewStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "status": (SelfSubjectReviewStatus, None),
        }

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
    def status(self) -> "SelfSubjectReviewStatus":
        """
        Status is filled in by the server with the user attributes.
        """
        return typing.cast(
            "SelfSubjectReviewStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["SelfSubjectReviewStatus", dict]):
        """
        Status is filled in by the server with the user attributes.
        """
        if isinstance(value, dict):
            value = typing.cast(
                SelfSubjectReviewStatus,
                SelfSubjectReviewStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "SelfSubjectReviewStatus":
        """
        Creates the SelfSubjectReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_self_subject_review", "create_self_subject_review"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = SelfSubjectReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "SelfSubjectReviewStatus":
        """
        Replaces the SelfSubjectReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_self_subject_review",
            "replace_self_subject_review",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = SelfSubjectReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "SelfSubjectReviewStatus":
        """
        Patches the SelfSubjectReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_self_subject_review", "patch_self_subject_review"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = SelfSubjectReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "SelfSubjectReviewStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_self_subject_review",
            "read_self_subject_review",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = SelfSubjectReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the SelfSubjectReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_self_subject_review",
            "read_self_subject_review",
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
        Deletes the SelfSubjectReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_self_subject_review",
            "delete_self_subject_review",
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
    ) -> "client.AuthenticationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AuthenticationV1beta1Api(**kwargs)

    def __enter__(self) -> "SelfSubjectReview":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectReviewStatus(_kuber_definitions.Definition):
    """
    SelfSubjectReviewStatus is filled by the kube-apiserver and
    sent back to a user.
    """

    def __init__(
        self,
        user_info: typing.Optional["UserInfo"] = None,
    ):
        """Create SelfSubjectReviewStatus instance."""
        super(SelfSubjectReviewStatus, self).__init__(
            api_version="authentication/v1beta1", kind="SelfSubjectReviewStatus"
        )
        self._properties = {
            "userInfo": user_info if user_info is not None else UserInfo(),
        }
        self._types = {
            "userInfo": (UserInfo, None),
        }

    @property
    def user_info(self) -> "UserInfo":
        """
        User attributes of the user making this request.
        """
        return typing.cast(
            "UserInfo",
            self._properties.get("userInfo"),
        )

    @user_info.setter
    def user_info(self, value: typing.Union["UserInfo", dict]):
        """
        User attributes of the user making this request.
        """
        if isinstance(value, dict):
            value = typing.cast(
                UserInfo,
                UserInfo().from_dict(value),
            )
        self._properties["userInfo"] = value

    def __enter__(self) -> "SelfSubjectReviewStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

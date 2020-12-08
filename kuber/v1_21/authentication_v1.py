import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_21.meta_v1 import ListMeta
from kuber.v1_21.meta_v1 import ObjectMeta
from kuber.v1_21.meta_v1 import Status
from kuber.v1_21.meta_v1 import StatusDetails


class BoundObjectReference(_kuber_definitions.Definition):
    """
    BoundObjectReference is a reference to an object that a
    token is bound to.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
    ):
        """Create BoundObjectReference instance."""
        super(BoundObjectReference, self).__init__(
            api_version="authentication/v1", kind="BoundObjectReference"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "uid": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        API version of the referent.
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        API version of the referent.
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name of the referent.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name of the referent.
        """
        self._properties["name"] = value

    @property
    def uid(self) -> str:
        """
        UID of the referent.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID of the referent.
        """
        self._properties["uid"] = value

    def __enter__(self) -> "BoundObjectReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenRequest(_kuber_definitions.Resource):
    """
    TokenRequest requests a token for a given service account.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "TokenRequestSpec" = None,
        status: "TokenRequestStatus" = None,
    ):
        """Create TokenRequest instance."""
        super(TokenRequest, self).__init__(
            api_version="authentication/v1", kind="TokenRequest"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else TokenRequestSpec(),
            "status": status if status is not None else TokenRequestStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (TokenRequestSpec, None),
            "status": (TokenRequestStatus, None),
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
    def spec(self) -> "TokenRequestSpec":
        """"""
        return typing.cast(
            "TokenRequestSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["TokenRequestSpec", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                TokenRequestSpec,
                TokenRequestSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "TokenRequestStatus":
        """"""
        return typing.cast(
            "TokenRequestStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["TokenRequestStatus", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                TokenRequestStatus,
                TokenRequestStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "TokenRequestStatus":
        """
        Creates the TokenRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_token_request", "create_token_request"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = TokenRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "TokenRequestStatus":
        """
        Replaces the TokenRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_token_request", "replace_token_request"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = TokenRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "TokenRequestStatus":
        """
        Patches the TokenRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_token_request", "patch_token_request"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = TokenRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "TokenRequestStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_token_request", "read_token_request"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = TokenRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the TokenRequest from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_token_request",
            "read_token_request",
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
        Deletes the TokenRequest from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_token_request",
            "delete_token_request",
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
    ) -> "client.AuthenticationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AuthenticationV1Api(**kwargs)

    def __enter__(self) -> "TokenRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenRequestSpec(_kuber_definitions.Definition):
    """
    TokenRequestSpec contains client provided parameters of a
    token request.
    """

    def __init__(
        self,
        audiences: typing.List[str] = None,
        bound_object_ref: "BoundObjectReference" = None,
        expiration_seconds: int = None,
    ):
        """Create TokenRequestSpec instance."""
        super(TokenRequestSpec, self).__init__(
            api_version="authentication/v1", kind="TokenRequestSpec"
        )
        self._properties = {
            "audiences": audiences if audiences is not None else [],
            "boundObjectRef": bound_object_ref
            if bound_object_ref is not None
            else BoundObjectReference(),
            "expirationSeconds": expiration_seconds
            if expiration_seconds is not None
            else None,
        }
        self._types = {
            "audiences": (list, str),
            "boundObjectRef": (BoundObjectReference, None),
            "expirationSeconds": (int, None),
        }

    @property
    def audiences(self) -> typing.List[str]:
        """
        Audiences are the intendend audiences of the token. A
        recipient of a token must identitfy themself with an
        identifier in the list of audiences of the token, and
        otherwise should reject the token. A token issued for
        multiple audiences may be used to authenticate against any
        of the audiences listed but implies a high degree of trust
        between the target audiences.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("audiences"),
        )

    @audiences.setter
    def audiences(self, value: typing.List[str]):
        """
        Audiences are the intendend audiences of the token. A
        recipient of a token must identitfy themself with an
        identifier in the list of audiences of the token, and
        otherwise should reject the token. A token issued for
        multiple audiences may be used to authenticate against any
        of the audiences listed but implies a high degree of trust
        between the target audiences.
        """
        self._properties["audiences"] = value

    @property
    def bound_object_ref(self) -> "BoundObjectReference":
        """
        BoundObjectRef is a reference to an object that the token
        will be bound to. The token will only be valid for as long
        as the bound object exists. NOTE: The API server's
        TokenReview endpoint will validate the BoundObjectRef, but
        other audiences may not. Keep ExpirationSeconds small if you
        want prompt revocation.
        """
        return typing.cast(
            "BoundObjectReference",
            self._properties.get("boundObjectRef"),
        )

    @bound_object_ref.setter
    def bound_object_ref(self, value: typing.Union["BoundObjectReference", dict]):
        """
        BoundObjectRef is a reference to an object that the token
        will be bound to. The token will only be valid for as long
        as the bound object exists. NOTE: The API server's
        TokenReview endpoint will validate the BoundObjectRef, but
        other audiences may not. Keep ExpirationSeconds small if you
        want prompt revocation.
        """
        if isinstance(value, dict):
            value = typing.cast(
                BoundObjectReference,
                BoundObjectReference().from_dict(value),
            )
        self._properties["boundObjectRef"] = value

    @property
    def expiration_seconds(self) -> int:
        """
        ExpirationSeconds is the requested duration of validity of
        the request. The token issuer may return a token with a
        different validity duration so a client needs to check the
        'expiration' field in a response.
        """
        return typing.cast(
            int,
            self._properties.get("expirationSeconds"),
        )

    @expiration_seconds.setter
    def expiration_seconds(self, value: int):
        """
        ExpirationSeconds is the requested duration of validity of
        the request. The token issuer may return a token with a
        different validity duration so a client needs to check the
        'expiration' field in a response.
        """
        self._properties["expirationSeconds"] = value

    def __enter__(self) -> "TokenRequestSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenRequestStatus(_kuber_definitions.Definition):
    """
    TokenRequestStatus is the result of a token request.
    """

    def __init__(
        self,
        expiration_timestamp: str = None,
        token: str = None,
    ):
        """Create TokenRequestStatus instance."""
        super(TokenRequestStatus, self).__init__(
            api_version="authentication/v1", kind="TokenRequestStatus"
        )
        self._properties = {
            "expirationTimestamp": expiration_timestamp
            if expiration_timestamp is not None
            else None,
            "token": token if token is not None else "",
        }
        self._types = {
            "expirationTimestamp": (str, None),
            "token": (str, None),
        }

    @property
    def expiration_timestamp(self) -> str:
        """
        ExpirationTimestamp is the time of expiration of the
        returned token.
        """
        return typing.cast(
            str,
            self._properties.get("expirationTimestamp"),
        )

    @expiration_timestamp.setter
    def expiration_timestamp(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        ExpirationTimestamp is the time of expiration of the
        returned token.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["expirationTimestamp"] = value

    @property
    def token(self) -> str:
        """
        Token is the opaque bearer token.
        """
        return typing.cast(
            str,
            self._properties.get("token"),
        )

    @token.setter
    def token(self, value: str):
        """
        Token is the opaque bearer token.
        """
        self._properties["token"] = value

    def __enter__(self) -> "TokenRequestStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenReview(_kuber_definitions.Resource):
    """
    TokenReview attempts to authenticate a token to a known
    user. Note: TokenReview requests may be cached by the
    webhook token authenticator plugin in the kube-apiserver.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "TokenReviewSpec" = None,
        status: "TokenReviewStatus" = None,
    ):
        """Create TokenReview instance."""
        super(TokenReview, self).__init__(
            api_version="authentication/v1", kind="TokenReview"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else TokenReviewSpec(),
            "status": status if status is not None else TokenReviewStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (TokenReviewSpec, None),
            "status": (TokenReviewStatus, None),
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
    def spec(self) -> "TokenReviewSpec":
        """
        Spec holds information about the request being evaluated
        """
        return typing.cast(
            "TokenReviewSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["TokenReviewSpec", dict]):
        """
        Spec holds information about the request being evaluated
        """
        if isinstance(value, dict):
            value = typing.cast(
                TokenReviewSpec,
                TokenReviewSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "TokenReviewStatus":
        """
        Status is filled in by the server and indicates whether the
        request can be authenticated.
        """
        return typing.cast(
            "TokenReviewStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["TokenReviewStatus", dict]):
        """
        Status is filled in by the server and indicates whether the
        request can be authenticated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                TokenReviewStatus,
                TokenReviewStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "TokenReviewStatus":
        """
        Creates the TokenReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_token_review", "create_token_review"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = TokenReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "TokenReviewStatus":
        """
        Replaces the TokenReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_token_review", "replace_token_review"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = TokenReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "TokenReviewStatus":
        """
        Patches the TokenReview in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_token_review", "patch_token_review"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = TokenReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "TokenReviewStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_token_review", "read_token_review"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = TokenReviewStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the TokenReview from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_token_review",
            "read_token_review",
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
        Deletes the TokenReview from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_token_review",
            "delete_token_review",
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
    ) -> "client.AuthenticationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AuthenticationV1Api(**kwargs)

    def __enter__(self) -> "TokenReview":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenReviewSpec(_kuber_definitions.Definition):
    """
    TokenReviewSpec is a description of the token authentication
    request.
    """

    def __init__(
        self,
        audiences: typing.List[str] = None,
        token: str = None,
    ):
        """Create TokenReviewSpec instance."""
        super(TokenReviewSpec, self).__init__(
            api_version="authentication/v1", kind="TokenReviewSpec"
        )
        self._properties = {
            "audiences": audiences if audiences is not None else [],
            "token": token if token is not None else "",
        }
        self._types = {
            "audiences": (list, str),
            "token": (str, None),
        }

    @property
    def audiences(self) -> typing.List[str]:
        """
        Audiences is a list of the identifiers that the resource
        server presented with the token identifies as. Audience-
        aware token authenticators will verify that the token was
        intended for at least one of the audiences in this list. If
        no audiences are provided, the audience will default to the
        audience of the Kubernetes apiserver.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("audiences"),
        )

    @audiences.setter
    def audiences(self, value: typing.List[str]):
        """
        Audiences is a list of the identifiers that the resource
        server presented with the token identifies as. Audience-
        aware token authenticators will verify that the token was
        intended for at least one of the audiences in this list. If
        no audiences are provided, the audience will default to the
        audience of the Kubernetes apiserver.
        """
        self._properties["audiences"] = value

    @property
    def token(self) -> str:
        """
        Token is the opaque bearer token.
        """
        return typing.cast(
            str,
            self._properties.get("token"),
        )

    @token.setter
    def token(self, value: str):
        """
        Token is the opaque bearer token.
        """
        self._properties["token"] = value

    def __enter__(self) -> "TokenReviewSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenReviewStatus(_kuber_definitions.Definition):
    """
    TokenReviewStatus is the result of the token authentication
    request.
    """

    def __init__(
        self,
        audiences: typing.List[str] = None,
        authenticated: bool = None,
        error: str = None,
        user: "UserInfo" = None,
    ):
        """Create TokenReviewStatus instance."""
        super(TokenReviewStatus, self).__init__(
            api_version="authentication/v1", kind="TokenReviewStatus"
        )
        self._properties = {
            "audiences": audiences if audiences is not None else [],
            "authenticated": authenticated if authenticated is not None else None,
            "error": error if error is not None else "",
            "user": user if user is not None else UserInfo(),
        }
        self._types = {
            "audiences": (list, str),
            "authenticated": (bool, None),
            "error": (str, None),
            "user": (UserInfo, None),
        }

    @property
    def audiences(self) -> typing.List[str]:
        """
        Audiences are audience identifiers chosen by the
        authenticator that are compatible with both the TokenReview
        and token. An identifier is any identifier in the
        intersection of the TokenReviewSpec audiences and the
        token's audiences. A client of the TokenReview API that sets
        the spec.audiences field should validate that a compatible
        audience identifier is returned in the status.audiences
        field to ensure that the TokenReview server is audience
        aware. If a TokenReview returns an empty status.audience
        field where status.authenticated is "true", the token is
        valid against the audience of the Kubernetes API server.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("audiences"),
        )

    @audiences.setter
    def audiences(self, value: typing.List[str]):
        """
        Audiences are audience identifiers chosen by the
        authenticator that are compatible with both the TokenReview
        and token. An identifier is any identifier in the
        intersection of the TokenReviewSpec audiences and the
        token's audiences. A client of the TokenReview API that sets
        the spec.audiences field should validate that a compatible
        audience identifier is returned in the status.audiences
        field to ensure that the TokenReview server is audience
        aware. If a TokenReview returns an empty status.audience
        field where status.authenticated is "true", the token is
        valid against the audience of the Kubernetes API server.
        """
        self._properties["audiences"] = value

    @property
    def authenticated(self) -> bool:
        """
        Authenticated indicates that the token was associated with a
        known user.
        """
        return typing.cast(
            bool,
            self._properties.get("authenticated"),
        )

    @authenticated.setter
    def authenticated(self, value: bool):
        """
        Authenticated indicates that the token was associated with a
        known user.
        """
        self._properties["authenticated"] = value

    @property
    def error(self) -> str:
        """
        Error indicates that the token couldn't be checked
        """
        return typing.cast(
            str,
            self._properties.get("error"),
        )

    @error.setter
    def error(self, value: str):
        """
        Error indicates that the token couldn't be checked
        """
        self._properties["error"] = value

    @property
    def user(self) -> "UserInfo":
        """
        User is the UserInfo associated with the provided token.
        """
        return typing.cast(
            "UserInfo",
            self._properties.get("user"),
        )

    @user.setter
    def user(self, value: typing.Union["UserInfo", dict]):
        """
        User is the UserInfo associated with the provided token.
        """
        if isinstance(value, dict):
            value = typing.cast(
                UserInfo,
                UserInfo().from_dict(value),
            )
        self._properties["user"] = value

    def __enter__(self) -> "TokenReviewStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class UserInfo(_kuber_definitions.Definition):
    """
    UserInfo holds the information about the user needed to
    implement the user.Info interface.
    """

    def __init__(
        self,
        extra: dict = None,
        groups: typing.List[str] = None,
        uid: str = None,
        username: str = None,
    ):
        """Create UserInfo instance."""
        super(UserInfo, self).__init__(api_version="authentication/v1", kind="UserInfo")
        self._properties = {
            "extra": extra if extra is not None else {},
            "groups": groups if groups is not None else [],
            "uid": uid if uid is not None else "",
            "username": username if username is not None else "",
        }
        self._types = {
            "extra": (dict, None),
            "groups": (list, str),
            "uid": (str, None),
            "username": (str, None),
        }

    @property
    def extra(self) -> dict:
        """
        Any additional information provided by the authenticator.
        """
        return typing.cast(
            dict,
            self._properties.get("extra"),
        )

    @extra.setter
    def extra(self, value: dict):
        """
        Any additional information provided by the authenticator.
        """
        self._properties["extra"] = value

    @property
    def groups(self) -> typing.List[str]:
        """
        The names of groups this user is a part of.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("groups"),
        )

    @groups.setter
    def groups(self, value: typing.List[str]):
        """
        The names of groups this user is a part of.
        """
        self._properties["groups"] = value

    @property
    def uid(self) -> str:
        """
        A unique value that identifies this user across time. If
        this user is deleted and another user by the same name is
        added, they will have different UIDs.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        A unique value that identifies this user across time. If
        this user is deleted and another user by the same name is
        added, they will have different UIDs.
        """
        self._properties["uid"] = value

    @property
    def username(self) -> str:
        """
        The name that uniquely identifies this user among all active
        users.
        """
        return typing.cast(
            str,
            self._properties.get("username"),
        )

    @username.setter
    def username(self, value: str):
        """
        The name that uniquely identifies this user among all active
        users.
        """
        self._properties["username"] = value

    def __enter__(self) -> "UserInfo":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_19.meta_v1 import ListMeta
from kuber.v1_19.meta_v1 import ObjectMeta
from kuber.v1_19.meta_v1 import Status
from kuber.v1_19.meta_v1 import StatusDetails


class CertificateSigningRequest(_kuber_definitions.Resource):
    """
    Describes a certificate signing request
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "CertificateSigningRequestSpec" = None,
        status: "CertificateSigningRequestStatus" = None,
    ):
        """Create CertificateSigningRequest instance."""
        super(CertificateSigningRequest, self).__init__(
            api_version="certificates/v1beta1", kind="CertificateSigningRequest"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else CertificateSigningRequestSpec(),
            "status": status
            if status is not None
            else CertificateSigningRequestStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (CertificateSigningRequestSpec, None),
            "status": (CertificateSigningRequestStatus, None),
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
    def spec(self) -> "CertificateSigningRequestSpec":
        """
        The certificate request itself and any additional
        information.
        """
        return typing.cast(
            "CertificateSigningRequestSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["CertificateSigningRequestSpec", dict]):
        """
        The certificate request itself and any additional
        information.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CertificateSigningRequestSpec,
                CertificateSigningRequestSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "CertificateSigningRequestStatus":
        """
        Derived information about the request.
        """
        return typing.cast(
            "CertificateSigningRequestStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["CertificateSigningRequestStatus", dict]):
        """
        Derived information about the request.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CertificateSigningRequestStatus,
                CertificateSigningRequestStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: "str" = None
    ) -> "CertificateSigningRequestStatus":
        """
        Creates the CertificateSigningRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_certificate_signing_request",
            "create_certificate_signing_request",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = CertificateSigningRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: "str" = None
    ) -> "CertificateSigningRequestStatus":
        """
        Replaces the CertificateSigningRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_certificate_signing_request",
            "replace_certificate_signing_request",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CertificateSigningRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: "str" = None
    ) -> "CertificateSigningRequestStatus":
        """
        Patches the CertificateSigningRequest in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_certificate_signing_request",
            "patch_certificate_signing_request",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CertificateSigningRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: "str" = None
    ) -> "CertificateSigningRequestStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_certificate_signing_request",
            "read_certificate_signing_request",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = CertificateSigningRequestStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the CertificateSigningRequest from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_certificate_signing_request",
            "read_certificate_signing_request",
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
        Deletes the CertificateSigningRequest from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_certificate_signing_request",
            "delete_certificate_signing_request",
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
    ) -> "client.CertificatesV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CertificatesV1beta1Api(**kwargs)

    def __enter__(self) -> "CertificateSigningRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestCondition(_kuber_definitions.Definition):
    """"""

    def __init__(
        self,
        last_transition_time: str = None,
        last_update_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create CertificateSigningRequestCondition instance."""
        super(CertificateSigningRequestCondition, self).__init__(
            api_version="certificates/v1beta1",
            kind="CertificateSigningRequestCondition",
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "lastUpdateTime": last_update_time
            if last_update_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "lastUpdateTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        lastTransitionTime is the time the condition last
        transitioned from one status to another. If unset, when a
        new condition type is added or an existing condition's
        status is changed, the server defaults this to the current
        time.
        """
        return typing.cast(
            str,
            self._properties.get("lastTransitionTime"),
        )

    @last_transition_time.setter
    def last_transition_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        lastTransitionTime is the time the condition last
        transitioned from one status to another. If unset, when a
        new condition type is added or an existing condition's
        status is changed, the server defaults this to the current
        time.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def last_update_time(self) -> str:
        """
        timestamp for the last update to this condition
        """
        return typing.cast(
            str,
            self._properties.get("lastUpdateTime"),
        )

    @last_update_time.setter
    def last_update_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        timestamp for the last update to this condition
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastUpdateTime"] = value

    @property
    def message(self) -> str:
        """
        human readable message with details about the request state
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        human readable message with details about the request state
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        brief reason for the request state
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        brief reason for the request state
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        Approved, Denied, and Failed conditions may not be "False"
        or "Unknown". Defaults to "True". If unset, should be
        treated as "True".
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        Approved, Denied, and Failed conditions may not be "False"
        or "Unknown". Defaults to "True". If unset, should be
        treated as "True".
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        type of the condition. Known conditions include "Approved",
        "Denied", and "Failed".
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type of the condition. Known conditions include "Approved",
        "Denied", and "Failed".
        """
        self._properties["type"] = value

    def __enter__(self) -> "CertificateSigningRequestCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestList(_kuber_definitions.Collection):
    """"""

    def __init__(
        self,
        items: typing.List["CertificateSigningRequest"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create CertificateSigningRequestList instance."""
        super(CertificateSigningRequestList, self).__init__(
            api_version="certificates/v1beta1", kind="CertificateSigningRequestList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CertificateSigningRequest),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CertificateSigningRequest"]:
        """"""
        return typing.cast(
            typing.List["CertificateSigningRequest"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["CertificateSigningRequest"], typing.List[dict]
        ],
    ):
        """"""
        cleaned: typing.List[CertificateSigningRequest] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CertificateSigningRequest,
                    CertificateSigningRequest().from_dict(item),
                )
            cleaned.append(typing.cast(CertificateSigningRequest, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """"""
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.CertificatesV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.CertificatesV1beta1Api(**kwargs)

    def __enter__(self) -> "CertificateSigningRequestList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestSpec(_kuber_definitions.Definition):
    """
    This information is immutable after the request is created.
    Only the Request and Usages fields can be set on creation,
    other fields are derived by Kubernetes and cannot be
    modified by users.
    """

    def __init__(
        self,
        extra: dict = None,
        groups: typing.List[str] = None,
        request: str = None,
        signer_name: str = None,
        uid: str = None,
        usages: typing.List[str] = None,
        username: str = None,
    ):
        """Create CertificateSigningRequestSpec instance."""
        super(CertificateSigningRequestSpec, self).__init__(
            api_version="certificates/v1beta1", kind="CertificateSigningRequestSpec"
        )
        self._properties = {
            "extra": extra if extra is not None else {},
            "groups": groups if groups is not None else [],
            "request": request if request is not None else "",
            "signerName": signer_name if signer_name is not None else "",
            "uid": uid if uid is not None else "",
            "usages": usages if usages is not None else [],
            "username": username if username is not None else "",
        }
        self._types = {
            "extra": (dict, None),
            "groups": (list, str),
            "request": (str, None),
            "signerName": (str, None),
            "uid": (str, None),
            "usages": (list, str),
            "username": (str, None),
        }

    @property
    def extra(self) -> dict:
        """
        Extra information about the requesting user. See user.Info
        interface for details.
        """
        return typing.cast(
            dict,
            self._properties.get("extra"),
        )

    @extra.setter
    def extra(self, value: dict):
        """
        Extra information about the requesting user. See user.Info
        interface for details.
        """
        self._properties["extra"] = value

    @property
    def groups(self) -> typing.List[str]:
        """
        Group information about the requesting user. See user.Info
        interface for details.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("groups"),
        )

    @groups.setter
    def groups(self, value: typing.List[str]):
        """
        Group information about the requesting user. See user.Info
        interface for details.
        """
        self._properties["groups"] = value

    @property
    def request(self) -> str:
        """
        Base64-encoded PKCS#10 CSR data
        """
        return typing.cast(
            str,
            self._properties.get("request"),
        )

    @request.setter
    def request(self, value: str):
        """
        Base64-encoded PKCS#10 CSR data
        """
        self._properties["request"] = value

    @property
    def signer_name(self) -> str:
        """
        Requested signer for the request. It is a qualified name in
        the form: `scope-hostname.io/name`. If empty, it will be
        defaulted:
         1. If it's a kubelet client certificate, it is assigned
            "kubernetes.io/kube-apiserver-client-kubelet".
         2. If it's a kubelet serving certificate, it is assigned
            "kubernetes.io/kubelet-serving".
         3. Otherwise, it is assigned "kubernetes.io/legacy-
        unknown".
        Distribution of trust for signers happens out of band. You
        can select on this field using `spec.signerName`.
        """
        return typing.cast(
            str,
            self._properties.get("signerName"),
        )

    @signer_name.setter
    def signer_name(self, value: str):
        """
        Requested signer for the request. It is a qualified name in
        the form: `scope-hostname.io/name`. If empty, it will be
        defaulted:
         1. If it's a kubelet client certificate, it is assigned
            "kubernetes.io/kube-apiserver-client-kubelet".
         2. If it's a kubelet serving certificate, it is assigned
            "kubernetes.io/kubelet-serving".
         3. Otherwise, it is assigned "kubernetes.io/legacy-
        unknown".
        Distribution of trust for signers happens out of band. You
        can select on this field using `spec.signerName`.
        """
        self._properties["signerName"] = value

    @property
    def uid(self) -> str:
        """
        UID information about the requesting user. See user.Info
        interface for details.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID information about the requesting user. See user.Info
        interface for details.
        """
        self._properties["uid"] = value

    @property
    def usages(self) -> typing.List[str]:
        """
        allowedUsages specifies a set of usage contexts the key will
        be valid for. See:
        https://tools.ietf.org/html/rfc5280#section-4.2.1.3
             https://tools.ietf.org/html/rfc5280#section-4.2.1.12
        Valid values are:
         "signing",
         "digital signature",
         "content commitment",
         "key encipherment",
         "key agreement",
         "data encipherment",
         "cert sign",
         "crl sign",
         "encipher only",
         "decipher only",
         "any",
         "server auth",
         "client auth",
         "code signing",
         "email protection",
         "s/mime",
         "ipsec end system",
         "ipsec tunnel",
         "ipsec user",
         "timestamping",
         "ocsp signing",
         "microsoft sgc",
         "netscape sgc"
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("usages"),
        )

    @usages.setter
    def usages(self, value: typing.List[str]):
        """
        allowedUsages specifies a set of usage contexts the key will
        be valid for. See:
        https://tools.ietf.org/html/rfc5280#section-4.2.1.3
             https://tools.ietf.org/html/rfc5280#section-4.2.1.12
        Valid values are:
         "signing",
         "digital signature",
         "content commitment",
         "key encipherment",
         "key agreement",
         "data encipherment",
         "cert sign",
         "crl sign",
         "encipher only",
         "decipher only",
         "any",
         "server auth",
         "client auth",
         "code signing",
         "email protection",
         "s/mime",
         "ipsec end system",
         "ipsec tunnel",
         "ipsec user",
         "timestamping",
         "ocsp signing",
         "microsoft sgc",
         "netscape sgc"
        """
        self._properties["usages"] = value

    @property
    def username(self) -> str:
        """
        Information about the requesting user. See user.Info
        interface for details.
        """
        return typing.cast(
            str,
            self._properties.get("username"),
        )

    @username.setter
    def username(self, value: str):
        """
        Information about the requesting user. See user.Info
        interface for details.
        """
        self._properties["username"] = value

    def __enter__(self) -> "CertificateSigningRequestSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestStatus(_kuber_definitions.Definition):
    """"""

    def __init__(
        self,
        certificate: str = None,
        conditions: typing.List["CertificateSigningRequestCondition"] = None,
    ):
        """Create CertificateSigningRequestStatus instance."""
        super(CertificateSigningRequestStatus, self).__init__(
            api_version="certificates/v1beta1", kind="CertificateSigningRequestStatus"
        )
        self._properties = {
            "certificate": certificate if certificate is not None else "",
            "conditions": conditions if conditions is not None else [],
        }
        self._types = {
            "certificate": (str, None),
            "conditions": (list, CertificateSigningRequestCondition),
        }

    @property
    def certificate(self) -> str:
        """
        If request was approved, the controller will place the
        issued certificate here.
        """
        return typing.cast(
            str,
            self._properties.get("certificate"),
        )

    @certificate.setter
    def certificate(self, value: str):
        """
        If request was approved, the controller will place the
        issued certificate here.
        """
        self._properties["certificate"] = value

    @property
    def conditions(self) -> typing.List["CertificateSigningRequestCondition"]:
        """
        Conditions applied to the request, such as approval or
        denial.
        """
        return typing.cast(
            typing.List["CertificateSigningRequestCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[
            typing.List["CertificateSigningRequestCondition"], typing.List[dict]
        ],
    ):
        """
        Conditions applied to the request, such as approval or
        denial.
        """
        cleaned: typing.List[CertificateSigningRequestCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CertificateSigningRequestCondition,
                    CertificateSigningRequestCondition().from_dict(item),
                )
            cleaned.append(typing.cast(CertificateSigningRequestCondition, item))
        self._properties["conditions"] = cleaned

    def __enter__(self) -> "CertificateSigningRequestStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

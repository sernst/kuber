import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_15.meta_v1 import ListMeta
from kuber.v1_15.meta_v1 import ObjectMeta
from kuber.v1_15.meta_v1 import Status
from kuber.v1_15.meta_v1 import StatusDetails


class APIService(_kuber_definitions.Resource):
    """
    APIService represents a server for a particular
    GroupVersion. Name must be "version.group".
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "APIServiceSpec" = None,
        status: "APIServiceStatus" = None,
    ):
        """Create APIService instance."""
        super(APIService, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="APIService"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else APIServiceSpec(),
            "status": status if status is not None else APIServiceStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (APIServiceSpec, None),
            "status": (APIServiceStatus, None),
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
    def spec(self) -> "APIServiceSpec":
        """
        Spec contains information for locating and communicating
        with a server
        """
        return typing.cast(
            "APIServiceSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["APIServiceSpec", dict]):
        """
        Spec contains information for locating and communicating
        with a server
        """
        if isinstance(value, dict):
            value = typing.cast(
                APIServiceSpec,
                APIServiceSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "APIServiceStatus":
        """
        Status contains derived information about an API server
        """
        return typing.cast(
            "APIServiceStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["APIServiceStatus", dict]):
        """
        Status contains derived information about an API server
        """
        if isinstance(value, dict):
            value = typing.cast(
                APIServiceStatus,
                APIServiceStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "APIServiceStatus":
        """
        Creates the APIService in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_api_service", "create_api_service"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = APIServiceStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "APIServiceStatus":
        """
        Replaces the APIService in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_api_service", "replace_api_service"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = APIServiceStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "APIServiceStatus":
        """
        Patches the APIService in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_api_service", "patch_api_service"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = APIServiceStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "APIServiceStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_api_service", "read_api_service"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = APIServiceStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the APIService from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_api_service",
            "read_api_service",
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
        Deletes the APIService from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_api_service",
            "delete_api_service",
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
    ) -> "client.ApiregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "APIService":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIServiceCondition(_kuber_definitions.Definition):
    """
    APIServiceCondition describes the state of an APIService at
    a particular point
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create APIServiceCondition instance."""
        super(APIServiceCondition, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="APIServiceCondition"
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transitioned from one status to
        another.
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
        Last time the condition transitioned from one status to
        another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        Human-readable message indicating details about last
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        Human-readable message indicating details about last
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        Unique, one-word, CamelCase reason for the condition's last
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        Unique, one-word, CamelCase reason for the condition's last
        transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status is the status of the condition. Can be True, False,
        Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status is the status of the condition. Can be True, False,
        Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type is the type of the condition.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type is the type of the condition.
        """
        self._properties["type"] = value

    def __enter__(self) -> "APIServiceCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIServiceList(_kuber_definitions.Collection):
    """
    APIServiceList is a list of APIService objects.
    """

    def __init__(
        self,
        items: typing.List["APIService"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create APIServiceList instance."""
        super(APIServiceList, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="APIServiceList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, APIService),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["APIService"]:
        """"""
        return typing.cast(
            typing.List["APIService"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["APIService"], typing.List[dict]]):
        """"""
        cleaned: typing.List[APIService] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    APIService,
                    APIService().from_dict(item),
                )
            cleaned.append(typing.cast(APIService, item))
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
    ) -> "client.ApiregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "APIServiceList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIServiceSpec(_kuber_definitions.Definition):
    """
    APIServiceSpec contains information for locating and
    communicating with a server. Only https is supported, though
    you are able to disable certificate verification.
    """

    def __init__(
        self,
        ca_bundle: str = None,
        group: str = None,
        group_priority_minimum: int = None,
        insecure_skip_tlsverify: bool = None,
        service: "ServiceReference" = None,
        version: str = None,
        version_priority: int = None,
    ):
        """Create APIServiceSpec instance."""
        super(APIServiceSpec, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="APIServiceSpec"
        )
        self._properties = {
            "caBundle": ca_bundle if ca_bundle is not None else "",
            "group": group if group is not None else "",
            "groupPriorityMinimum": group_priority_minimum
            if group_priority_minimum is not None
            else None,
            "insecureSkipTLSVerify": insecure_skip_tlsverify
            if insecure_skip_tlsverify is not None
            else None,
            "service": service if service is not None else ServiceReference(),
            "version": version if version is not None else "",
            "versionPriority": version_priority
            if version_priority is not None
            else None,
        }
        self._types = {
            "caBundle": (str, None),
            "group": (str, None),
            "groupPriorityMinimum": (int, None),
            "insecureSkipTLSVerify": (bool, None),
            "service": (ServiceReference, None),
            "version": (str, None),
            "versionPriority": (int, None),
        }

    @property
    def ca_bundle(self) -> str:
        """
        CABundle is a PEM encoded CA bundle which will be used to
        validate an API server's serving certificate. If
        unspecified, system trust roots on the apiserver are used.
        """
        return typing.cast(
            str,
            self._properties.get("caBundle"),
        )

    @ca_bundle.setter
    def ca_bundle(self, value: str):
        """
        CABundle is a PEM encoded CA bundle which will be used to
        validate an API server's serving certificate. If
        unspecified, system trust roots on the apiserver are used.
        """
        self._properties["caBundle"] = value

    @property
    def group(self) -> str:
        """
        Group is the API group name this server hosts
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        Group is the API group name this server hosts
        """
        self._properties["group"] = value

    @property
    def group_priority_minimum(self) -> int:
        """
        GroupPriorityMininum is the priority this group should have
        at least. Higher priority means that the group is preferred
        by clients over lower priority ones. Note that other
        versions of this group might specify even higher
        GroupPriorityMininum values such that the whole group gets a
        higher priority. The primary sort is based on
        GroupPriorityMinimum, ordered highest number to lowest (20
        before 10). The secondary sort is based on the alphabetical
        comparison of the name of the object.  (v1.bar before
        v1.foo) We'd recommend something like: *.k8s.io (except
        extensions) at 18000 and PaaSes (OpenShift, Deis) are
        recommended to be in the 2000s
        """
        return typing.cast(
            int,
            self._properties.get("groupPriorityMinimum"),
        )

    @group_priority_minimum.setter
    def group_priority_minimum(self, value: int):
        """
        GroupPriorityMininum is the priority this group should have
        at least. Higher priority means that the group is preferred
        by clients over lower priority ones. Note that other
        versions of this group might specify even higher
        GroupPriorityMininum values such that the whole group gets a
        higher priority. The primary sort is based on
        GroupPriorityMinimum, ordered highest number to lowest (20
        before 10). The secondary sort is based on the alphabetical
        comparison of the name of the object.  (v1.bar before
        v1.foo) We'd recommend something like: *.k8s.io (except
        extensions) at 18000 and PaaSes (OpenShift, Deis) are
        recommended to be in the 2000s
        """
        self._properties["groupPriorityMinimum"] = value

    @property
    def insecure_skip_tlsverify(self) -> bool:
        """
        InsecureSkipTLSVerify disables TLS certificate verification
        when communicating with this server. This is strongly
        discouraged.  You should use the CABundle instead.
        """
        return typing.cast(
            bool,
            self._properties.get("insecureSkipTLSVerify"),
        )

    @insecure_skip_tlsverify.setter
    def insecure_skip_tlsverify(self, value: bool):
        """
        InsecureSkipTLSVerify disables TLS certificate verification
        when communicating with this server. This is strongly
        discouraged.  You should use the CABundle instead.
        """
        self._properties["insecureSkipTLSVerify"] = value

    @property
    def service(self) -> "ServiceReference":
        """
        Service is a reference to the service for this API server.
        It must communicate on port 443 If the Service is nil, that
        means the handling for the API groupversion is handled
        locally on this server. The call will simply delegate to the
        normal handler chain to be fulfilled.
        """
        return typing.cast(
            "ServiceReference",
            self._properties.get("service"),
        )

    @service.setter
    def service(self, value: typing.Union["ServiceReference", dict]):
        """
        Service is a reference to the service for this API server.
        It must communicate on port 443 If the Service is nil, that
        means the handling for the API groupversion is handled
        locally on this server. The call will simply delegate to the
        normal handler chain to be fulfilled.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceReference,
                ServiceReference().from_dict(value),
            )
        self._properties["service"] = value

    @property
    def version(self) -> str:
        """
        Version is the API version this server hosts.  For example,
        "v1"
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        Version is the API version this server hosts.  For example,
        "v1"
        """
        self._properties["version"] = value

    @property
    def version_priority(self) -> int:
        """
        VersionPriority controls the ordering of this API version
        inside of its group.  Must be greater than zero. The primary
        sort is based on VersionPriority, ordered highest to lowest
        (20 before 10). Since it's inside of a group, the number can
        be small, probably in the 10s. In case of equal version
        priorities, the version string will be used to compute the
        order inside a group. If the version string is "kube-like",
        it will sort above non "kube-like" version strings, which
        are ordered lexicographically. "Kube-like" versions start
        with a "v", then are followed by a number (the major
        version), then optionally the string "alpha" or "beta" and
        another number (the minor version). These are sorted first
        by GA > beta > alpha (where GA is a version with no suffix
        such as beta or alpha), and then by comparing major version,
        then minor version. An example sorted list of versions: v10,
        v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2,
        foo1, foo10.
        """
        return typing.cast(
            int,
            self._properties.get("versionPriority"),
        )

    @version_priority.setter
    def version_priority(self, value: int):
        """
        VersionPriority controls the ordering of this API version
        inside of its group.  Must be greater than zero. The primary
        sort is based on VersionPriority, ordered highest to lowest
        (20 before 10). Since it's inside of a group, the number can
        be small, probably in the 10s. In case of equal version
        priorities, the version string will be used to compute the
        order inside a group. If the version string is "kube-like",
        it will sort above non "kube-like" version strings, which
        are ordered lexicographically. "Kube-like" versions start
        with a "v", then are followed by a number (the major
        version), then optionally the string "alpha" or "beta" and
        another number (the minor version). These are sorted first
        by GA > beta > alpha (where GA is a version with no suffix
        such as beta or alpha), and then by comparing major version,
        then minor version. An example sorted list of versions: v10,
        v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2,
        foo1, foo10.
        """
        self._properties["versionPriority"] = value

    def __enter__(self) -> "APIServiceSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class APIServiceStatus(_kuber_definitions.Definition):
    """
    APIServiceStatus contains derived information about an API
    server
    """

    def __init__(
        self,
        conditions: typing.List["APIServiceCondition"] = None,
    ):
        """Create APIServiceStatus instance."""
        super(APIServiceStatus, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="APIServiceStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
        }
        self._types = {
            "conditions": (list, APIServiceCondition),
        }

    @property
    def conditions(self) -> typing.List["APIServiceCondition"]:
        """
        Current service state of apiService.
        """
        return typing.cast(
            typing.List["APIServiceCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["APIServiceCondition"], typing.List[dict]]
    ):
        """
        Current service state of apiService.
        """
        cleaned: typing.List[APIServiceCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    APIServiceCondition,
                    APIServiceCondition().from_dict(item),
                )
            cleaned.append(typing.cast(APIServiceCondition, item))
        self._properties["conditions"] = cleaned

    def __enter__(self) -> "APIServiceStatus":
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
        port: int = None,
    ):
        """Create ServiceReference instance."""
        super(ServiceReference, self).__init__(
            api_version="apiregistration.k8s.io/v1beta1", kind="ServiceReference"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "port": port if port is not None else None,
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
            "port": (int, None),
        }

    @property
    def name(self) -> str:
        """
        Name is the name of the service
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the service
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace is the namespace of the service
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace is the namespace of the service
        """
        self._properties["namespace"] = value

    @property
    def port(self) -> int:
        """
        If specified, the port on the service that hosting webhook.
        Default to 443 for backward compatibility. `port` should be
        a valid port number (1-65535, inclusive).
        """
        return typing.cast(
            int,
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: int):
        """
        If specified, the port on the service that hosting webhook.
        Default to 443 for backward compatibility. `port` should be
        a valid port number (1-65535, inclusive).
        """
        self._properties["port"] = value

    def __enter__(self) -> "ServiceReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

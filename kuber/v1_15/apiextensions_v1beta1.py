import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_15.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_15.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_15.meta_v1 import Status  # noqa: F401
from kuber.v1_15.meta_v1 import StatusDetails  # noqa: F401


class CustomResourceColumnDefinition(_kuber_definitions.Definition):
    """
    CustomResourceColumnDefinition specifies a column for server
    side printing.
    """

    def __init__(
        self,
        jsonpath: str = None,
        description: str = None,
        format_: str = None,
        name: str = None,
        priority: int = None,
        type_: str = None,
    ):
        """Create CustomResourceColumnDefinition instance."""
        super(CustomResourceColumnDefinition, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceColumnDefinition"
        )
        self._properties = {
            "JSONPath": jsonpath if jsonpath is not None else "",
            "description": description if description is not None else "",
            "format": format_ if format_ is not None else "",
            "name": name if name is not None else "",
            "priority": priority if priority is not None else None,
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "JSONPath": (str, None),
            "description": (str, None),
            "format": (str, None),
            "name": (str, None),
            "priority": (int, None),
            "type": (str, None),
        }

    @property
    def jsonpath(self) -> str:
        """
        JSONPath is a simple JSON path, i.e. with array notation.
        """
        return typing.cast(
            str,
            self._properties.get("JSONPath"),
        )

    @jsonpath.setter
    def jsonpath(self, value: str):
        """
        JSONPath is a simple JSON path, i.e. with array notation.
        """
        self._properties["JSONPath"] = value

    @property
    def description(self) -> str:
        """
        description is a human readable description of this column.
        """
        return typing.cast(
            str,
            self._properties.get("description"),
        )

    @description.setter
    def description(self, value: str):
        """
        description is a human readable description of this column.
        """
        self._properties["description"] = value

    @property
    def format_(self) -> str:
        """
        format is an optional OpenAPI type definition for this
        column. The 'name' format is applied to the primary
        identifier column to assist in clients identifying column is
        the resource name. See https://github.com/OAI/OpenAPI-
        Specification/blob/master/versions/2.0.md#data-types for
        more.
        """
        return typing.cast(
            str,
            self._properties.get("format"),
        )

    @format_.setter
    def format_(self, value: str):
        """
        format is an optional OpenAPI type definition for this
        column. The 'name' format is applied to the primary
        identifier column to assist in clients identifying column is
        the resource name. See https://github.com/OAI/OpenAPI-
        Specification/blob/master/versions/2.0.md#data-types for
        more.
        """
        self._properties["format"] = value

    @property
    def name(self) -> str:
        """
        name is a human readable name for the column.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is a human readable name for the column.
        """
        self._properties["name"] = value

    @property
    def priority(self) -> int:
        """
        priority is an integer defining the relative importance of
        this column compared to others. Lower numbers are considered
        higher priority. Columns that may be omitted in limited
        space scenarios should be given a higher priority.
        """
        return typing.cast(
            int,
            self._properties.get("priority"),
        )

    @priority.setter
    def priority(self, value: int):
        """
        priority is an integer defining the relative importance of
        this column compared to others. Lower numbers are considered
        higher priority. Columns that may be omitted in limited
        space scenarios should be given a higher priority.
        """
        self._properties["priority"] = value

    @property
    def type_(self) -> str:
        """
        type is an OpenAPI type definition for this column. See
        https://github.com/OAI/OpenAPI-
        Specification/blob/master/versions/2.0.md#data-types for
        more.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type is an OpenAPI type definition for this column. See
        https://github.com/OAI/OpenAPI-
        Specification/blob/master/versions/2.0.md#data-types for
        more.
        """
        self._properties["type"] = value

    def __enter__(self) -> "CustomResourceColumnDefinition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceConversion(_kuber_definitions.Definition):
    """
    CustomResourceConversion describes how to convert different
    versions of a CR.
    """

    def __init__(
        self,
        conversion_review_versions: typing.List[str] = None,
        strategy: str = None,
        webhook_client_config: "WebhookClientConfig" = None,
    ):
        """Create CustomResourceConversion instance."""
        super(CustomResourceConversion, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceConversion"
        )
        self._properties = {
            "conversionReviewVersions": conversion_review_versions
            if conversion_review_versions is not None
            else [],
            "strategy": strategy if strategy is not None else "",
            "webhookClientConfig": webhook_client_config
            if webhook_client_config is not None
            else WebhookClientConfig(),
        }
        self._types = {
            "conversionReviewVersions": (list, str),
            "strategy": (str, None),
            "webhookClientConfig": (WebhookClientConfig, None),
        }

    @property
    def conversion_review_versions(self) -> typing.List[str]:
        """
        ConversionReviewVersions is an ordered list of preferred
        `ConversionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, conversion will fail for this object. If a
        persisted Webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail. Default to `['v1beta1']`.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("conversionReviewVersions"),
        )

    @conversion_review_versions.setter
    def conversion_review_versions(self, value: typing.List[str]):
        """
        ConversionReviewVersions is an ordered list of preferred
        `ConversionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, conversion will fail for this object. If a
        persisted Webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail. Default to `['v1beta1']`.
        """
        self._properties["conversionReviewVersions"] = value

    @property
    def strategy(self) -> str:
        """
        `strategy` specifies the conversion strategy. Allowed values
        are: - `None`: The converter only change the apiVersion and
        would not touch any other field in the CR. - `Webhook`: API
        Server will call to an external webhook to do the
        conversion. Additional information
          is needed for this option. This requires
        spec.preserveUnknownFields to be false.
        """
        return typing.cast(
            str,
            self._properties.get("strategy"),
        )

    @strategy.setter
    def strategy(self, value: str):
        """
        `strategy` specifies the conversion strategy. Allowed values
        are: - `None`: The converter only change the apiVersion and
        would not touch any other field in the CR. - `Webhook`: API
        Server will call to an external webhook to do the
        conversion. Additional information
          is needed for this option. This requires
        spec.preserveUnknownFields to be false.
        """
        self._properties["strategy"] = value

    @property
    def webhook_client_config(self) -> "WebhookClientConfig":
        """
        `webhookClientConfig` is the instructions for how to call
        the webhook if strategy is `Webhook`. This field is alpha-
        level and is only honored by servers that enable the
        CustomResourceWebhookConversion feature.
        """
        return typing.cast(
            "WebhookClientConfig",
            self._properties.get("webhookClientConfig"),
        )

    @webhook_client_config.setter
    def webhook_client_config(self, value: typing.Union["WebhookClientConfig", dict]):
        """
        `webhookClientConfig` is the instructions for how to call
        the webhook if strategy is `Webhook`. This field is alpha-
        level and is only honored by servers that enable the
        CustomResourceWebhookConversion feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                WebhookClientConfig,
                WebhookClientConfig().from_dict(value),
            )
        self._properties["webhookClientConfig"] = value

    def __enter__(self) -> "CustomResourceConversion":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinition(_kuber_definitions.Resource):
    """
    CustomResourceDefinition represents a resource that should
    be exposed on the API server.  Its name MUST be in the
    format <.spec.name>.<.spec.group>.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "CustomResourceDefinitionSpec" = None,
        status: "CustomResourceDefinitionStatus" = None,
    ):
        """Create CustomResourceDefinition instance."""
        super(CustomResourceDefinition, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinition"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else CustomResourceDefinitionSpec(),
            "status": status
            if status is not None
            else CustomResourceDefinitionStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (CustomResourceDefinitionSpec, None),
            "status": (CustomResourceDefinitionStatus, None),
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
    def spec(self) -> "CustomResourceDefinitionSpec":
        """
        Spec describes how the user wants the resources to appear
        """
        return typing.cast(
            "CustomResourceDefinitionSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["CustomResourceDefinitionSpec", dict]):
        """
        Spec describes how the user wants the resources to appear
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceDefinitionSpec,
                CustomResourceDefinitionSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "CustomResourceDefinitionStatus":
        """
        Status indicates the actual state of the
        CustomResourceDefinition
        """
        return typing.cast(
            "CustomResourceDefinitionStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["CustomResourceDefinitionStatus", dict]):
        """
        Status indicates the actual state of the
        CustomResourceDefinition
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceDefinitionStatus,
                CustomResourceDefinitionStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: "str" = None
    ) -> "CustomResourceDefinitionStatus":
        """
        Creates the CustomResourceDefinition in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_custom_resource_definition",
            "create_custom_resource_definition",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = CustomResourceDefinitionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: "str" = None
    ) -> "CustomResourceDefinitionStatus":
        """
        Replaces the CustomResourceDefinition in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_custom_resource_definition",
            "replace_custom_resource_definition",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CustomResourceDefinitionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: "str" = None
    ) -> "CustomResourceDefinitionStatus":
        """
        Patches the CustomResourceDefinition in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_custom_resource_definition",
            "patch_custom_resource_definition",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CustomResourceDefinitionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: "str" = None
    ) -> "CustomResourceDefinitionStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_custom_resource_definition",
            "read_custom_resource_definition",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = CustomResourceDefinitionStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the CustomResourceDefinition from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_custom_resource_definition",
            "read_custom_resource_definition",
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
        Deletes the CustomResourceDefinition from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_custom_resource_definition",
            "delete_custom_resource_definition",
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
    ) -> "client.ApiextensionsV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiextensionsV1beta1Api(**kwargs)

    def __enter__(self) -> "CustomResourceDefinition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionCondition(_kuber_definitions.Definition):
    """
    CustomResourceDefinitionCondition contains details for the
    current condition of this pod.
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create CustomResourceDefinitionCondition instance."""
        super(CustomResourceDefinitionCondition, self).__init__(
            api_version="apiextensions/v1beta1",
            kind="CustomResourceDefinitionCondition",
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
        Type is the type of the condition. Types include
        Established, NamesAccepted and Terminating.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type is the type of the condition. Types include
        Established, NamesAccepted and Terminating.
        """
        self._properties["type"] = value

    def __enter__(self) -> "CustomResourceDefinitionCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionList(_kuber_definitions.Collection):
    """
    CustomResourceDefinitionList is a list of
    CustomResourceDefinition objects.
    """

    def __init__(
        self,
        items: typing.List["CustomResourceDefinition"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create CustomResourceDefinitionList instance."""
        super(CustomResourceDefinitionList, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinitionList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CustomResourceDefinition),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CustomResourceDefinition"]:
        """
        Items individual CustomResourceDefinitions
        """
        return typing.cast(
            typing.List["CustomResourceDefinition"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["CustomResourceDefinition"], typing.List[dict]],
    ):
        """
        Items individual CustomResourceDefinitions
        """
        cleaned: typing.List[CustomResourceDefinition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CustomResourceDefinition,
                    CustomResourceDefinition().from_dict(item),
                )
            cleaned.append(typing.cast(CustomResourceDefinition, item))
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
    ) -> "client.ApiextensionsV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ApiextensionsV1beta1Api(**kwargs)

    def __enter__(self) -> "CustomResourceDefinitionList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionNames(_kuber_definitions.Definition):
    """
    CustomResourceDefinitionNames indicates the names to serve
    this CustomResourceDefinition
    """

    def __init__(
        self,
        categories: typing.List[str] = None,
        kind: str = None,
        list_kind: str = None,
        plural: str = None,
        short_names: typing.List[str] = None,
        singular: str = None,
    ):
        """Create CustomResourceDefinitionNames instance."""
        super(CustomResourceDefinitionNames, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinitionNames"
        )
        self._properties = {
            "categories": categories if categories is not None else [],
            "kind": kind if kind is not None else "",
            "listKind": list_kind if list_kind is not None else "",
            "plural": plural if plural is not None else "",
            "shortNames": short_names if short_names is not None else [],
            "singular": singular if singular is not None else "",
        }
        self._types = {
            "categories": (list, str),
            "kind": (str, None),
            "listKind": (str, None),
            "plural": (str, None),
            "shortNames": (list, str),
            "singular": (str, None),
        }

    @property
    def categories(self) -> typing.List[str]:
        """
        Categories is a list of grouped resources custom resources
        belong to (e.g. 'all')
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("categories"),
        )

    @categories.setter
    def categories(self, value: typing.List[str]):
        """
        Categories is a list of grouped resources custom resources
        belong to (e.g. 'all')
        """
        self._properties["categories"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the serialized kind of the resource.  It is normally
        CamelCase and singular.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the serialized kind of the resource.  It is normally
        CamelCase and singular.
        """
        self._properties["kind"] = value

    @property
    def list_kind(self) -> str:
        """
        ListKind is the serialized kind of the list for this
        resource.  Defaults to <kind>List.
        """
        return typing.cast(
            str,
            self._properties.get("listKind"),
        )

    @list_kind.setter
    def list_kind(self, value: str):
        """
        ListKind is the serialized kind of the list for this
        resource.  Defaults to <kind>List.
        """
        self._properties["listKind"] = value

    @property
    def plural(self) -> str:
        """
        Plural is the plural name of the resource to serve.  It must
        match the name of the CustomResourceDefinition-registration
        too: plural.group and it must be all lowercase.
        """
        return typing.cast(
            str,
            self._properties.get("plural"),
        )

    @plural.setter
    def plural(self, value: str):
        """
        Plural is the plural name of the resource to serve.  It must
        match the name of the CustomResourceDefinition-registration
        too: plural.group and it must be all lowercase.
        """
        self._properties["plural"] = value

    @property
    def short_names(self) -> typing.List[str]:
        """
        ShortNames are short names for the resource.  It must be all
        lowercase.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("shortNames"),
        )

    @short_names.setter
    def short_names(self, value: typing.List[str]):
        """
        ShortNames are short names for the resource.  It must be all
        lowercase.
        """
        self._properties["shortNames"] = value

    @property
    def singular(self) -> str:
        """
        Singular is the singular name of the resource.  It must be
        all lowercase  Defaults to lowercased <kind>
        """
        return typing.cast(
            str,
            self._properties.get("singular"),
        )

    @singular.setter
    def singular(self, value: str):
        """
        Singular is the singular name of the resource.  It must be
        all lowercase  Defaults to lowercased <kind>
        """
        self._properties["singular"] = value

    def __enter__(self) -> "CustomResourceDefinitionNames":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionSpec(_kuber_definitions.Definition):
    """
    CustomResourceDefinitionSpec describes how a user wants
    their resource to appear
    """

    def __init__(
        self,
        additional_printer_columns: typing.List[
            "CustomResourceColumnDefinition"
        ] = None,
        conversion: "CustomResourceConversion" = None,
        group: str = None,
        names: "CustomResourceDefinitionNames" = None,
        preserve_unknown_fields: bool = None,
        scope: str = None,
        subresources: "CustomResourceSubresources" = None,
        validation: "CustomResourceValidation" = None,
        version: str = None,
        versions: typing.List["CustomResourceDefinitionVersion"] = None,
    ):
        """Create CustomResourceDefinitionSpec instance."""
        super(CustomResourceDefinitionSpec, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinitionSpec"
        )
        self._properties = {
            "additionalPrinterColumns": additional_printer_columns
            if additional_printer_columns is not None
            else [],
            "conversion": conversion
            if conversion is not None
            else CustomResourceConversion(),
            "group": group if group is not None else "",
            "names": names if names is not None else CustomResourceDefinitionNames(),
            "preserveUnknownFields": preserve_unknown_fields
            if preserve_unknown_fields is not None
            else None,
            "scope": scope if scope is not None else "",
            "subresources": subresources
            if subresources is not None
            else CustomResourceSubresources(),
            "validation": validation
            if validation is not None
            else CustomResourceValidation(),
            "version": version if version is not None else "",
            "versions": versions if versions is not None else [],
        }
        self._types = {
            "additionalPrinterColumns": (list, CustomResourceColumnDefinition),
            "conversion": (CustomResourceConversion, None),
            "group": (str, None),
            "names": (CustomResourceDefinitionNames, None),
            "preserveUnknownFields": (bool, None),
            "scope": (str, None),
            "subresources": (CustomResourceSubresources, None),
            "validation": (CustomResourceValidation, None),
            "version": (str, None),
            "versions": (list, CustomResourceDefinitionVersion),
        }

    @property
    def additional_printer_columns(
        self,
    ) -> typing.List["CustomResourceColumnDefinition"]:
        """
        AdditionalPrinterColumns are additional columns shown e.g.
        in kubectl next to the name. Defaults to a created-at
        column. Optional, the global columns for all versions. Top-
        level and per-version columns are mutually exclusive.
        """
        return typing.cast(
            typing.List["CustomResourceColumnDefinition"],
            self._properties.get("additionalPrinterColumns"),
        )

    @additional_printer_columns.setter
    def additional_printer_columns(
        self,
        value: typing.Union[
            typing.List["CustomResourceColumnDefinition"], typing.List[dict]
        ],
    ):
        """
        AdditionalPrinterColumns are additional columns shown e.g.
        in kubectl next to the name. Defaults to a created-at
        column. Optional, the global columns for all versions. Top-
        level and per-version columns are mutually exclusive.
        """
        cleaned: typing.List[CustomResourceColumnDefinition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CustomResourceColumnDefinition,
                    CustomResourceColumnDefinition().from_dict(item),
                )
            cleaned.append(typing.cast(CustomResourceColumnDefinition, item))
        self._properties["additionalPrinterColumns"] = cleaned

    @property
    def conversion(self) -> "CustomResourceConversion":
        """
        `conversion` defines conversion settings for the CRD.
        """
        return typing.cast(
            "CustomResourceConversion",
            self._properties.get("conversion"),
        )

    @conversion.setter
    def conversion(self, value: typing.Union["CustomResourceConversion", dict]):
        """
        `conversion` defines conversion settings for the CRD.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceConversion,
                CustomResourceConversion().from_dict(value),
            )
        self._properties["conversion"] = value

    @property
    def group(self) -> str:
        """
        Group is the group this resource belongs in
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        Group is the group this resource belongs in
        """
        self._properties["group"] = value

    @property
    def names(self) -> "CustomResourceDefinitionNames":
        """
        Names are the names used to describe this custom resource
        """
        return typing.cast(
            "CustomResourceDefinitionNames",
            self._properties.get("names"),
        )

    @names.setter
    def names(self, value: typing.Union["CustomResourceDefinitionNames", dict]):
        """
        Names are the names used to describe this custom resource
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceDefinitionNames,
                CustomResourceDefinitionNames().from_dict(value),
            )
        self._properties["names"] = value

    @property
    def preserve_unknown_fields(self) -> bool:
        """
        preserveUnknownFields disables pruning of object fields
        which are not specified in the OpenAPI schema. apiVersion,
        kind, metadata and known fields inside metadata are always
        preserved. Defaults to true in v1beta and will default to
        false in v1.
        """
        return typing.cast(
            bool,
            self._properties.get("preserveUnknownFields"),
        )

    @preserve_unknown_fields.setter
    def preserve_unknown_fields(self, value: bool):
        """
        preserveUnknownFields disables pruning of object fields
        which are not specified in the OpenAPI schema. apiVersion,
        kind, metadata and known fields inside metadata are always
        preserved. Defaults to true in v1beta and will default to
        false in v1.
        """
        self._properties["preserveUnknownFields"] = value

    @property
    def scope(self) -> str:
        """
        Scope indicates whether this resource is cluster or
        namespace scoped.  Default is namespaced
        """
        return typing.cast(
            str,
            self._properties.get("scope"),
        )

    @scope.setter
    def scope(self, value: str):
        """
        Scope indicates whether this resource is cluster or
        namespace scoped.  Default is namespaced
        """
        self._properties["scope"] = value

    @property
    def subresources(self) -> "CustomResourceSubresources":
        """
        Subresources describes the subresources for CustomResource
        Optional, the global subresources for all versions. Top-
        level and per-version subresources are mutually exclusive.
        """
        return typing.cast(
            "CustomResourceSubresources",
            self._properties.get("subresources"),
        )

    @subresources.setter
    def subresources(self, value: typing.Union["CustomResourceSubresources", dict]):
        """
        Subresources describes the subresources for CustomResource
        Optional, the global subresources for all versions. Top-
        level and per-version subresources are mutually exclusive.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceSubresources,
                CustomResourceSubresources().from_dict(value),
            )
        self._properties["subresources"] = value

    @property
    def validation(self) -> "CustomResourceValidation":
        """
        Validation describes the validation methods for
        CustomResources Optional, the global validation schema for
        all versions. Top-level and per-version schemas are mutually
        exclusive.
        """
        return typing.cast(
            "CustomResourceValidation",
            self._properties.get("validation"),
        )

    @validation.setter
    def validation(self, value: typing.Union["CustomResourceValidation", dict]):
        """
        Validation describes the validation methods for
        CustomResources Optional, the global validation schema for
        all versions. Top-level and per-version schemas are mutually
        exclusive.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceValidation,
                CustomResourceValidation().from_dict(value),
            )
        self._properties["validation"] = value

    @property
    def version(self) -> str:
        """
        Version is the version this resource belongs in Should be
        always first item in Versions field if provided. Optional,
        but at least one of Version or Versions must be set.
        Deprecated: Please use `Versions`.
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        Version is the version this resource belongs in Should be
        always first item in Versions field if provided. Optional,
        but at least one of Version or Versions must be set.
        Deprecated: Please use `Versions`.
        """
        self._properties["version"] = value

    @property
    def versions(self) -> typing.List["CustomResourceDefinitionVersion"]:
        """
        Versions is the list of all supported versions for this
        resource. If Version field is provided, this field is
        optional. Validation: All versions must use the same
        validation schema for now. i.e., top level Validation field
        is applied to all of these versions. Order: The version name
        will be used to compute the order. If the version string is
        "kube-like", it will sort above non "kube-like" version
        strings, which are ordered lexicographically. "Kube-like"
        versions start with a "v", then are followed by a number
        (the major version), then optionally the string "alpha" or
        "beta" and another number (the minor version). These are
        sorted first by GA > beta > alpha (where GA is a version
        with no suffix such as beta or alpha), and then by comparing
        major version, then minor version. An example sorted list of
        versions: v10, v2, v1, v11beta2, v10beta3, v3beta1,
        v12alpha1, v11alpha2, foo1, foo10.
        """
        return typing.cast(
            typing.List["CustomResourceDefinitionVersion"],
            self._properties.get("versions"),
        )

    @versions.setter
    def versions(
        self,
        value: typing.Union[
            typing.List["CustomResourceDefinitionVersion"], typing.List[dict]
        ],
    ):
        """
        Versions is the list of all supported versions for this
        resource. If Version field is provided, this field is
        optional. Validation: All versions must use the same
        validation schema for now. i.e., top level Validation field
        is applied to all of these versions. Order: The version name
        will be used to compute the order. If the version string is
        "kube-like", it will sort above non "kube-like" version
        strings, which are ordered lexicographically. "Kube-like"
        versions start with a "v", then are followed by a number
        (the major version), then optionally the string "alpha" or
        "beta" and another number (the minor version). These are
        sorted first by GA > beta > alpha (where GA is a version
        with no suffix such as beta or alpha), and then by comparing
        major version, then minor version. An example sorted list of
        versions: v10, v2, v1, v11beta2, v10beta3, v3beta1,
        v12alpha1, v11alpha2, foo1, foo10.
        """
        cleaned: typing.List[CustomResourceDefinitionVersion] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CustomResourceDefinitionVersion,
                    CustomResourceDefinitionVersion().from_dict(item),
                )
            cleaned.append(typing.cast(CustomResourceDefinitionVersion, item))
        self._properties["versions"] = cleaned

    def __enter__(self) -> "CustomResourceDefinitionSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionStatus(_kuber_definitions.Definition):
    """
    CustomResourceDefinitionStatus indicates the state of the
    CustomResourceDefinition
    """

    def __init__(
        self,
        accepted_names: "CustomResourceDefinitionNames" = None,
        conditions: typing.List["CustomResourceDefinitionCondition"] = None,
        stored_versions: typing.List[str] = None,
    ):
        """Create CustomResourceDefinitionStatus instance."""
        super(CustomResourceDefinitionStatus, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinitionStatus"
        )
        self._properties = {
            "acceptedNames": accepted_names
            if accepted_names is not None
            else CustomResourceDefinitionNames(),
            "conditions": conditions if conditions is not None else [],
            "storedVersions": stored_versions if stored_versions is not None else [],
        }
        self._types = {
            "acceptedNames": (CustomResourceDefinitionNames, None),
            "conditions": (list, CustomResourceDefinitionCondition),
            "storedVersions": (list, str),
        }

    @property
    def accepted_names(self) -> "CustomResourceDefinitionNames":
        """
        AcceptedNames are the names that are actually being used to
        serve discovery They may be different than the names in
        spec.
        """
        return typing.cast(
            "CustomResourceDefinitionNames",
            self._properties.get("acceptedNames"),
        )

    @accepted_names.setter
    def accepted_names(
        self, value: typing.Union["CustomResourceDefinitionNames", dict]
    ):
        """
        AcceptedNames are the names that are actually being used to
        serve discovery They may be different than the names in
        spec.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceDefinitionNames,
                CustomResourceDefinitionNames().from_dict(value),
            )
        self._properties["acceptedNames"] = value

    @property
    def conditions(self) -> typing.List["CustomResourceDefinitionCondition"]:
        """
        Conditions indicate state for particular aspects of a
        CustomResourceDefinition
        """
        return typing.cast(
            typing.List["CustomResourceDefinitionCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[
            typing.List["CustomResourceDefinitionCondition"], typing.List[dict]
        ],
    ):
        """
        Conditions indicate state for particular aspects of a
        CustomResourceDefinition
        """
        cleaned: typing.List[CustomResourceDefinitionCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CustomResourceDefinitionCondition,
                    CustomResourceDefinitionCondition().from_dict(item),
                )
            cleaned.append(typing.cast(CustomResourceDefinitionCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def stored_versions(self) -> typing.List[str]:
        """
        StoredVersions are all versions of CustomResources that were
        ever persisted. Tracking these versions allows a migration
        path for stored versions in etcd. The field is mutable so
        the migration controller can first finish a migration to
        another version (i.e. that no old objects are left in the
        storage), and then remove the rest of the versions from this
        list. None of the versions in this list can be removed from
        the spec.Versions field.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("storedVersions"),
        )

    @stored_versions.setter
    def stored_versions(self, value: typing.List[str]):
        """
        StoredVersions are all versions of CustomResources that were
        ever persisted. Tracking these versions allows a migration
        path for stored versions in etcd. The field is mutable so
        the migration controller can first finish a migration to
        another version (i.e. that no old objects are left in the
        storage), and then remove the rest of the versions from this
        list. None of the versions in this list can be removed from
        the spec.Versions field.
        """
        self._properties["storedVersions"] = value

    def __enter__(self) -> "CustomResourceDefinitionStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceDefinitionVersion(_kuber_definitions.Definition):
    """
    CustomResourceDefinitionVersion describes a version for CRD.
    """

    def __init__(
        self,
        additional_printer_columns: typing.List[
            "CustomResourceColumnDefinition"
        ] = None,
        name: str = None,
        schema: "CustomResourceValidation" = None,
        served: bool = None,
        storage: bool = None,
        subresources: "CustomResourceSubresources" = None,
    ):
        """Create CustomResourceDefinitionVersion instance."""
        super(CustomResourceDefinitionVersion, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceDefinitionVersion"
        )
        self._properties = {
            "additionalPrinterColumns": additional_printer_columns
            if additional_printer_columns is not None
            else [],
            "name": name if name is not None else "",
            "schema": schema if schema is not None else CustomResourceValidation(),
            "served": served if served is not None else None,
            "storage": storage if storage is not None else None,
            "subresources": subresources
            if subresources is not None
            else CustomResourceSubresources(),
        }
        self._types = {
            "additionalPrinterColumns": (list, CustomResourceColumnDefinition),
            "name": (str, None),
            "schema": (CustomResourceValidation, None),
            "served": (bool, None),
            "storage": (bool, None),
            "subresources": (CustomResourceSubresources, None),
        }

    @property
    def additional_printer_columns(
        self,
    ) -> typing.List["CustomResourceColumnDefinition"]:
        """
        AdditionalPrinterColumns are additional columns shown e.g.
        in kubectl next to the name. Defaults to a created-at
        column. Top-level and per-version columns are mutually
        exclusive. Per-version columns must not all be set to
        identical values (top-level columns should be used instead)
        This field is alpha-level and is only honored by servers
        that enable the CustomResourceWebhookConversion feature.
        NOTE: CRDs created prior to 1.13 populated the top-level
        additionalPrinterColumns field by default. To apply an
        update that changes to per-version additionalPrinterColumns,
        the top-level additionalPrinterColumns field must be
        explicitly set to null
        """
        return typing.cast(
            typing.List["CustomResourceColumnDefinition"],
            self._properties.get("additionalPrinterColumns"),
        )

    @additional_printer_columns.setter
    def additional_printer_columns(
        self,
        value: typing.Union[
            typing.List["CustomResourceColumnDefinition"], typing.List[dict]
        ],
    ):
        """
        AdditionalPrinterColumns are additional columns shown e.g.
        in kubectl next to the name. Defaults to a created-at
        column. Top-level and per-version columns are mutually
        exclusive. Per-version columns must not all be set to
        identical values (top-level columns should be used instead)
        This field is alpha-level and is only honored by servers
        that enable the CustomResourceWebhookConversion feature.
        NOTE: CRDs created prior to 1.13 populated the top-level
        additionalPrinterColumns field by default. To apply an
        update that changes to per-version additionalPrinterColumns,
        the top-level additionalPrinterColumns field must be
        explicitly set to null
        """
        cleaned: typing.List[CustomResourceColumnDefinition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CustomResourceColumnDefinition,
                    CustomResourceColumnDefinition().from_dict(item),
                )
            cleaned.append(typing.cast(CustomResourceColumnDefinition, item))
        self._properties["additionalPrinterColumns"] = cleaned

    @property
    def name(self) -> str:
        """
        Name is the version name, e.g. v1, v2beta1, etc.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the version name, e.g. v1, v2beta1, etc.
        """
        self._properties["name"] = value

    @property
    def schema(self) -> "CustomResourceValidation":
        """
        Schema describes the schema for CustomResource used in
        validation, pruning, and defaulting. Top-level and per-
        version schemas are mutually exclusive. Per-version schemas
        must not all be set to identical values (top-level
        validation schema should be used instead) This field is
        alpha-level and is only honored by servers that enable the
        CustomResourceWebhookConversion feature.
        """
        return typing.cast(
            "CustomResourceValidation",
            self._properties.get("schema"),
        )

    @schema.setter
    def schema(self, value: typing.Union["CustomResourceValidation", dict]):
        """
        Schema describes the schema for CustomResource used in
        validation, pruning, and defaulting. Top-level and per-
        version schemas are mutually exclusive. Per-version schemas
        must not all be set to identical values (top-level
        validation schema should be used instead) This field is
        alpha-level and is only honored by servers that enable the
        CustomResourceWebhookConversion feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceValidation,
                CustomResourceValidation().from_dict(value),
            )
        self._properties["schema"] = value

    @property
    def served(self) -> bool:
        """
        Served is a flag enabling/disabling this version from being
        served via REST APIs
        """
        return typing.cast(
            bool,
            self._properties.get("served"),
        )

    @served.setter
    def served(self, value: bool):
        """
        Served is a flag enabling/disabling this version from being
        served via REST APIs
        """
        self._properties["served"] = value

    @property
    def storage(self) -> bool:
        """
        Storage flags the version as storage version. There must be
        exactly one flagged as storage version.
        """
        return typing.cast(
            bool,
            self._properties.get("storage"),
        )

    @storage.setter
    def storage(self, value: bool):
        """
        Storage flags the version as storage version. There must be
        exactly one flagged as storage version.
        """
        self._properties["storage"] = value

    @property
    def subresources(self) -> "CustomResourceSubresources":
        """
        Subresources describes the subresources for CustomResource
        Top-level and per-version subresources are mutually
        exclusive. Per-version subresources must not all be set to
        identical values (top-level subresources should be used
        instead) This field is alpha-level and is only honored by
        servers that enable the CustomResourceWebhookConversion
        feature.
        """
        return typing.cast(
            "CustomResourceSubresources",
            self._properties.get("subresources"),
        )

    @subresources.setter
    def subresources(self, value: typing.Union["CustomResourceSubresources", dict]):
        """
        Subresources describes the subresources for CustomResource
        Top-level and per-version subresources are mutually
        exclusive. Per-version subresources must not all be set to
        identical values (top-level subresources should be used
        instead) This field is alpha-level and is only honored by
        servers that enable the CustomResourceWebhookConversion
        feature.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceSubresources,
                CustomResourceSubresources().from_dict(value),
            )
        self._properties["subresources"] = value

    def __enter__(self) -> "CustomResourceDefinitionVersion":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceSubresourceScale(_kuber_definitions.Definition):
    """
    CustomResourceSubresourceScale defines how to serve the
    scale subresource for CustomResources.
    """

    def __init__(
        self,
        label_selector_path: str = None,
        spec_replicas_path: str = None,
        status_replicas_path: str = None,
    ):
        """Create CustomResourceSubresourceScale instance."""
        super(CustomResourceSubresourceScale, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceSubresourceScale"
        )
        self._properties = {
            "labelSelectorPath": label_selector_path
            if label_selector_path is not None
            else "",
            "specReplicasPath": spec_replicas_path
            if spec_replicas_path is not None
            else "",
            "statusReplicasPath": status_replicas_path
            if status_replicas_path is not None
            else "",
        }
        self._types = {
            "labelSelectorPath": (str, None),
            "specReplicasPath": (str, None),
            "statusReplicasPath": (str, None),
        }

    @property
    def label_selector_path(self) -> str:
        """
        LabelSelectorPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Status.Selector.
        Only JSON paths without the array notation are allowed. Must
        be a JSON Path under .status or .spec. Must be set to work
        with HPA. The field pointed by this JSON path must be a
        string field (not a complex selector struct) which contains
        a serialized label selector in string form. More info:
        https://kubernetes.io/docs/tasks/access-kubernetes-
        api/custom-resources/custom-resource-definitions#scale-
        subresource If there is no value under the given path in the
        CustomResource, the status label selector value in the
        /scale subresource will default to the empty string.
        """
        return typing.cast(
            str,
            self._properties.get("labelSelectorPath"),
        )

    @label_selector_path.setter
    def label_selector_path(self, value: str):
        """
        LabelSelectorPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Status.Selector.
        Only JSON paths without the array notation are allowed. Must
        be a JSON Path under .status or .spec. Must be set to work
        with HPA. The field pointed by this JSON path must be a
        string field (not a complex selector struct) which contains
        a serialized label selector in string form. More info:
        https://kubernetes.io/docs/tasks/access-kubernetes-
        api/custom-resources/custom-resource-definitions#scale-
        subresource If there is no value under the given path in the
        CustomResource, the status label selector value in the
        /scale subresource will default to the empty string.
        """
        self._properties["labelSelectorPath"] = value

    @property
    def spec_replicas_path(self) -> str:
        """
        SpecReplicasPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Spec.Replicas. Only
        JSON paths without the array notation are allowed. Must be a
        JSON Path under .spec. If there is no value under the given
        path in the CustomResource, the /scale subresource will
        return an error on GET.
        """
        return typing.cast(
            str,
            self._properties.get("specReplicasPath"),
        )

    @spec_replicas_path.setter
    def spec_replicas_path(self, value: str):
        """
        SpecReplicasPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Spec.Replicas. Only
        JSON paths without the array notation are allowed. Must be a
        JSON Path under .spec. If there is no value under the given
        path in the CustomResource, the /scale subresource will
        return an error on GET.
        """
        self._properties["specReplicasPath"] = value

    @property
    def status_replicas_path(self) -> str:
        """
        StatusReplicasPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Status.Replicas.
        Only JSON paths without the array notation are allowed. Must
        be a JSON Path under .status. If there is no value under the
        given path in the CustomResource, the status replica value
        in the /scale subresource will default to 0.
        """
        return typing.cast(
            str,
            self._properties.get("statusReplicasPath"),
        )

    @status_replicas_path.setter
    def status_replicas_path(self, value: str):
        """
        StatusReplicasPath defines the JSON path inside of a
        CustomResource that corresponds to Scale.Status.Replicas.
        Only JSON paths without the array notation are allowed. Must
        be a JSON Path under .status. If there is no value under the
        given path in the CustomResource, the status replica value
        in the /scale subresource will default to 0.
        """
        self._properties["statusReplicasPath"] = value

    def __enter__(self) -> "CustomResourceSubresourceScale":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceSubresourceStatus(_kuber_definitions.Definition):
    """
    CustomResourceSubresourceStatus defines how to serve the
    status subresource for CustomResources. Status is
    represented by the `.status` JSON path inside of a
    CustomResource. When set, * exposes a /status subresource
    for the custom resource * PUT requests to the /status
    subresource take a custom resource object, and ignore
    changes to anything except the status stanza *
    PUT/POST/PATCH requests to the custom resource ignore
    changes to the status stanza
    """

    def __init__(
        self,
    ):
        """Create CustomResourceSubresourceStatus instance."""
        super(CustomResourceSubresourceStatus, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceSubresourceStatus"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "CustomResourceSubresourceStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceSubresources(_kuber_definitions.Definition):
    """
    CustomResourceSubresources defines the status and scale
    subresources for CustomResources.
    """

    def __init__(
        self,
        scale: "CustomResourceSubresourceScale" = None,
        status: "CustomResourceSubresourceStatus" = None,
    ):
        """Create CustomResourceSubresources instance."""
        super(CustomResourceSubresources, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceSubresources"
        )
        self._properties = {
            "scale": scale if scale is not None else CustomResourceSubresourceScale(),
            "status": status
            if status is not None
            else CustomResourceSubresourceStatus(),
        }
        self._types = {
            "scale": (CustomResourceSubresourceScale, None),
            "status": (CustomResourceSubresourceStatus, None),
        }

    @property
    def scale(self) -> "CustomResourceSubresourceScale":
        """
        Scale denotes the scale subresource for CustomResources
        """
        return typing.cast(
            "CustomResourceSubresourceScale",
            self._properties.get("scale"),
        )

    @scale.setter
    def scale(self, value: typing.Union["CustomResourceSubresourceScale", dict]):
        """
        Scale denotes the scale subresource for CustomResources
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceSubresourceScale,
                CustomResourceSubresourceScale().from_dict(value),
            )
        self._properties["scale"] = value

    @property
    def status(self) -> "CustomResourceSubresourceStatus":
        """
        Status denotes the status subresource for CustomResources
        """
        return typing.cast(
            "CustomResourceSubresourceStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["CustomResourceSubresourceStatus", dict]):
        """
        Status denotes the status subresource for CustomResources
        """
        if isinstance(value, dict):
            value = typing.cast(
                CustomResourceSubresourceStatus,
                CustomResourceSubresourceStatus().from_dict(value),
            )
        self._properties["status"] = value

    def __enter__(self) -> "CustomResourceSubresources":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CustomResourceValidation(_kuber_definitions.Definition):
    """
    CustomResourceValidation is a list of validation methods for
    CustomResources.
    """

    def __init__(
        self,
        open_apiv3_schema: "JSONSchemaProps" = None,
    ):
        """Create CustomResourceValidation instance."""
        super(CustomResourceValidation, self).__init__(
            api_version="apiextensions/v1beta1", kind="CustomResourceValidation"
        )
        self._properties = {
            "openAPIV3Schema": open_apiv3_schema
            if open_apiv3_schema is not None
            else JSONSchemaProps(),
        }
        self._types = {
            "openAPIV3Schema": (JSONSchemaProps, None),
        }

    @property
    def open_apiv3_schema(self) -> "JSONSchemaProps":
        """
        OpenAPIV3Schema is the OpenAPI v3 schema to be validated
        against.
        """
        return typing.cast(
            "JSONSchemaProps",
            self._properties.get("openAPIV3Schema"),
        )

    @open_apiv3_schema.setter
    def open_apiv3_schema(self, value: typing.Union["JSONSchemaProps", dict]):
        """
        OpenAPIV3Schema is the OpenAPI v3 schema to be validated
        against.
        """
        if isinstance(value, dict):
            value = typing.cast(
                JSONSchemaProps,
                JSONSchemaProps().from_dict(value),
            )
        self._properties["openAPIV3Schema"] = value

    def __enter__(self) -> "CustomResourceValidation":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ExternalDocumentation(_kuber_definitions.Definition):
    """
    ExternalDocumentation allows referencing an external
    resource for extended documentation.
    """

    def __init__(
        self,
        description: str = None,
        url: str = None,
    ):
        """Create ExternalDocumentation instance."""
        super(ExternalDocumentation, self).__init__(
            api_version="apiextensions/v1beta1", kind="ExternalDocumentation"
        )
        self._properties = {
            "description": description if description is not None else "",
            "url": url if url is not None else "",
        }
        self._types = {
            "description": (str, None),
            "url": (str, None),
        }

    @property
    def description(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("description"),
        )

    @description.setter
    def description(self, value: str):
        """"""
        self._properties["description"] = value

    @property
    def url(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("url"),
        )

    @url.setter
    def url(self, value: str):
        """"""
        self._properties["url"] = value

    def __enter__(self) -> "ExternalDocumentation":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSON(_kuber_definitions.Definition):
    """
    JSON represents any valid JSON value. These types are
    supported: bool, int64, float64, string, []interface{},
    map[string]interface{} and nil.
    """

    def __init__(
        self,
    ):
        """Create JSON instance."""
        super(JSON, self).__init__(api_version="apiextensions/v1beta1", kind="JSON")
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "JSON":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSONSchemaProps(_kuber_definitions.Definition):
    """
    JSONSchemaProps is a JSON-Schema following Specification
    Draft 4 (http://json-schema.org/).
    """

    def __init__(
        self,
        additional_items: "JSONSchemaPropsOrBool" = None,
        additional_properties: "JSONSchemaPropsOrBool" = None,
        all_of: typing.List["JSONSchemaProps"] = None,
        any_of: typing.List["JSONSchemaProps"] = None,
        default: "JSON" = None,
        definitions: dict = None,
        dependencies: dict = None,
        description: str = None,
        enum: typing.List["JSON"] = None,
        example: "JSON" = None,
        exclusive_maximum: bool = None,
        exclusive_minimum: bool = None,
        external_docs: "ExternalDocumentation" = None,
        format_: str = None,
        id_: str = None,
        items: "JSONSchemaPropsOrArray" = None,
        max_items: int = None,
        max_length: int = None,
        max_properties: int = None,
        maximum: float = None,
        min_items: int = None,
        min_length: int = None,
        min_properties: int = None,
        minimum: float = None,
        multiple_of: float = None,
        not_: typing.Optional["JSONSchemaProps"] = None,
        nullable: bool = None,
        one_of: typing.List["JSONSchemaProps"] = None,
        pattern: str = None,
        pattern_properties: dict = None,
        properties: dict = None,
        required: typing.List[str] = None,
        title: str = None,
        type_: str = None,
        unique_items: bool = None,
        x_kubernetes_embedded_resource: bool = None,
        x_kubernetes_int_or_string: bool = None,
        x_kubernetes_preserve_unknown_fields: bool = None,
    ):
        """Create JSONSchemaProps instance."""
        super(JSONSchemaProps, self).__init__(
            api_version="apiextensions/v1beta1", kind="JSONSchemaProps"
        )
        self._properties = {
            "additionalItems": additional_items
            if additional_items is not None
            else JSONSchemaPropsOrBool(),
            "additionalProperties": additional_properties
            if additional_properties is not None
            else JSONSchemaPropsOrBool(),
            "allOf": all_of if all_of is not None else [],
            "anyOf": any_of if any_of is not None else [],
            "default": default if default is not None else JSON(),
            "definitions": definitions if definitions is not None else {},
            "dependencies": dependencies if dependencies is not None else {},
            "description": description if description is not None else "",
            "enum": enum if enum is not None else [],
            "example": example if example is not None else JSON(),
            "exclusiveMaximum": exclusive_maximum
            if exclusive_maximum is not None
            else None,
            "exclusiveMinimum": exclusive_minimum
            if exclusive_minimum is not None
            else None,
            "externalDocs": external_docs
            if external_docs is not None
            else ExternalDocumentation(),
            "format": format_ if format_ is not None else "",
            "id": id_ if id_ is not None else "",
            "items": items if items is not None else JSONSchemaPropsOrArray(),
            "maxItems": max_items if max_items is not None else None,
            "maxLength": max_length if max_length is not None else None,
            "maxProperties": max_properties if max_properties is not None else None,
            "maximum": maximum if maximum is not None else None,
            "minItems": min_items if min_items is not None else None,
            "minLength": min_length if min_length is not None else None,
            "minProperties": min_properties if min_properties is not None else None,
            "minimum": minimum if minimum is not None else None,
            "multipleOf": multiple_of if multiple_of is not None else None,
            "not": not_ if not_ is not None else None,
            "nullable": nullable if nullable is not None else None,
            "oneOf": one_of if one_of is not None else [],
            "pattern": pattern if pattern is not None else "",
            "patternProperties": pattern_properties
            if pattern_properties is not None
            else {},
            "properties": properties if properties is not None else {},
            "required": required if required is not None else [],
            "title": title if title is not None else "",
            "type": type_ if type_ is not None else "",
            "uniqueItems": unique_items if unique_items is not None else None,
            "x-kubernetes-embedded-resource": x_kubernetes_embedded_resource
            if x_kubernetes_embedded_resource is not None
            else None,
            "x-kubernetes-int-or-string": x_kubernetes_int_or_string
            if x_kubernetes_int_or_string is not None
            else None,
            "x-kubernetes-preserve-unknown-fields": x_kubernetes_preserve_unknown_fields
            if x_kubernetes_preserve_unknown_fields is not None
            else None,
        }
        self._types = {
            "additionalItems": (JSONSchemaPropsOrBool, None),
            "additionalProperties": (JSONSchemaPropsOrBool, None),
            "allOf": (list, JSONSchemaProps),
            "anyOf": (list, JSONSchemaProps),
            "default": (JSON, None),
            "definitions": (dict, None),
            "dependencies": (dict, None),
            "description": (str, None),
            "enum": (list, JSON),
            "example": (JSON, None),
            "exclusiveMaximum": (bool, None),
            "exclusiveMinimum": (bool, None),
            "externalDocs": (ExternalDocumentation, None),
            "format": (str, None),
            "id": (str, None),
            "items": (JSONSchemaPropsOrArray, None),
            "maxItems": (int, None),
            "maxLength": (int, None),
            "maxProperties": (int, None),
            "maximum": (float, None),
            "minItems": (int, None),
            "minLength": (int, None),
            "minProperties": (int, None),
            "minimum": (float, None),
            "multipleOf": (float, None),
            "not": (JSONSchemaProps, None),
            "nullable": (bool, None),
            "oneOf": (list, JSONSchemaProps),
            "pattern": (str, None),
            "patternProperties": (dict, None),
            "properties": (dict, None),
            "required": (list, str),
            "title": (str, None),
            "type": (str, None),
            "uniqueItems": (bool, None),
            "x-kubernetes-embedded-resource": (bool, None),
            "x-kubernetes-int-or-string": (bool, None),
            "x-kubernetes-preserve-unknown-fields": (bool, None),
        }

    @property
    def additional_items(self) -> "JSONSchemaPropsOrBool":
        """"""
        return typing.cast(
            "JSONSchemaPropsOrBool",
            self._properties.get("additionalItems"),
        )

    @additional_items.setter
    def additional_items(self, value: typing.Union["JSONSchemaPropsOrBool", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                JSONSchemaPropsOrBool,
                JSONSchemaPropsOrBool().from_dict(value),
            )
        self._properties["additionalItems"] = value

    @property
    def additional_properties(self) -> "JSONSchemaPropsOrBool":
        """"""
        return typing.cast(
            "JSONSchemaPropsOrBool",
            self._properties.get("additionalProperties"),
        )

    @additional_properties.setter
    def additional_properties(self, value: typing.Union["JSONSchemaPropsOrBool", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                JSONSchemaPropsOrBool,
                JSONSchemaPropsOrBool().from_dict(value),
            )
        self._properties["additionalProperties"] = value

    @property
    def all_of(self) -> typing.List["JSONSchemaProps"]:
        """"""
        return typing.cast(
            typing.List["JSONSchemaProps"],
            self._properties.get("allOf"),
        )

    @all_of.setter
    def all_of(
        self, value: typing.Union[typing.List["JSONSchemaProps"], typing.List[dict]]
    ):
        """"""
        cleaned: typing.List[JSONSchemaProps] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    JSONSchemaProps,
                    JSONSchemaProps().from_dict(item),
                )
            cleaned.append(typing.cast(JSONSchemaProps, item))
        self._properties["allOf"] = cleaned

    @property
    def any_of(self) -> typing.List["JSONSchemaProps"]:
        """"""
        return typing.cast(
            typing.List["JSONSchemaProps"],
            self._properties.get("anyOf"),
        )

    @any_of.setter
    def any_of(
        self, value: typing.Union[typing.List["JSONSchemaProps"], typing.List[dict]]
    ):
        """"""
        cleaned: typing.List[JSONSchemaProps] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    JSONSchemaProps,
                    JSONSchemaProps().from_dict(item),
                )
            cleaned.append(typing.cast(JSONSchemaProps, item))
        self._properties["anyOf"] = cleaned

    @property
    def default(self) -> "JSON":
        """
        default is a default value for undefined object fields.
        Defaulting is an alpha feature under the
        CustomResourceDefaulting feature gate. Defaulting requires
        spec.preserveUnknownFields to be false.
        """
        return typing.cast(
            "JSON",
            self._properties.get("default"),
        )

    @default.setter
    def default(self, value: typing.Union["JSON", dict]):
        """
        default is a default value for undefined object fields.
        Defaulting is an alpha feature under the
        CustomResourceDefaulting feature gate. Defaulting requires
        spec.preserveUnknownFields to be false.
        """
        if isinstance(value, dict):
            value = typing.cast(
                JSON,
                JSON().from_dict(value),
            )
        self._properties["default"] = value

    @property
    def definitions(self) -> dict:
        """"""
        return typing.cast(
            dict,
            self._properties.get("definitions"),
        )

    @definitions.setter
    def definitions(self, value: dict):
        """"""
        self._properties["definitions"] = value

    @property
    def dependencies(self) -> dict:
        """"""
        return typing.cast(
            dict,
            self._properties.get("dependencies"),
        )

    @dependencies.setter
    def dependencies(self, value: dict):
        """"""
        self._properties["dependencies"] = value

    @property
    def description(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("description"),
        )

    @description.setter
    def description(self, value: str):
        """"""
        self._properties["description"] = value

    @property
    def enum(self) -> typing.List["JSON"]:
        """"""
        return typing.cast(
            typing.List["JSON"],
            self._properties.get("enum"),
        )

    @enum.setter
    def enum(self, value: typing.Union[typing.List["JSON"], typing.List[dict]]):
        """"""
        cleaned: typing.List[JSON] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    JSON,
                    JSON().from_dict(item),
                )
            cleaned.append(typing.cast(JSON, item))
        self._properties["enum"] = cleaned

    @property
    def example(self) -> "JSON":
        """"""
        return typing.cast(
            "JSON",
            self._properties.get("example"),
        )

    @example.setter
    def example(self, value: typing.Union["JSON", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                JSON,
                JSON().from_dict(value),
            )
        self._properties["example"] = value

    @property
    def exclusive_maximum(self) -> bool:
        """"""
        return typing.cast(
            bool,
            self._properties.get("exclusiveMaximum"),
        )

    @exclusive_maximum.setter
    def exclusive_maximum(self, value: bool):
        """"""
        self._properties["exclusiveMaximum"] = value

    @property
    def exclusive_minimum(self) -> bool:
        """"""
        return typing.cast(
            bool,
            self._properties.get("exclusiveMinimum"),
        )

    @exclusive_minimum.setter
    def exclusive_minimum(self, value: bool):
        """"""
        self._properties["exclusiveMinimum"] = value

    @property
    def external_docs(self) -> "ExternalDocumentation":
        """"""
        return typing.cast(
            "ExternalDocumentation",
            self._properties.get("externalDocs"),
        )

    @external_docs.setter
    def external_docs(self, value: typing.Union["ExternalDocumentation", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ExternalDocumentation,
                ExternalDocumentation().from_dict(value),
            )
        self._properties["externalDocs"] = value

    @property
    def format_(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("format"),
        )

    @format_.setter
    def format_(self, value: str):
        """"""
        self._properties["format"] = value

    @property
    def id_(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("id"),
        )

    @id_.setter
    def id_(self, value: str):
        """"""
        self._properties["id"] = value

    @property
    def items(self) -> "JSONSchemaPropsOrArray":
        """"""
        return typing.cast(
            "JSONSchemaPropsOrArray",
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union["JSONSchemaPropsOrArray", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                JSONSchemaPropsOrArray,
                JSONSchemaPropsOrArray().from_dict(value),
            )
        self._properties["items"] = value

    @property
    def max_items(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("maxItems"),
        )

    @max_items.setter
    def max_items(self, value: int):
        """"""
        self._properties["maxItems"] = value

    @property
    def max_length(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("maxLength"),
        )

    @max_length.setter
    def max_length(self, value: int):
        """"""
        self._properties["maxLength"] = value

    @property
    def max_properties(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("maxProperties"),
        )

    @max_properties.setter
    def max_properties(self, value: int):
        """"""
        self._properties["maxProperties"] = value

    @property
    def maximum(self) -> float:
        """"""
        return typing.cast(
            float,
            self._properties.get("maximum"),
        )

    @maximum.setter
    def maximum(self, value: float):
        """"""
        self._properties["maximum"] = value

    @property
    def min_items(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("minItems"),
        )

    @min_items.setter
    def min_items(self, value: int):
        """"""
        self._properties["minItems"] = value

    @property
    def min_length(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("minLength"),
        )

    @min_length.setter
    def min_length(self, value: int):
        """"""
        self._properties["minLength"] = value

    @property
    def min_properties(self) -> int:
        """"""
        return typing.cast(
            int,
            self._properties.get("minProperties"),
        )

    @min_properties.setter
    def min_properties(self, value: int):
        """"""
        self._properties["minProperties"] = value

    @property
    def minimum(self) -> float:
        """"""
        return typing.cast(
            float,
            self._properties.get("minimum"),
        )

    @minimum.setter
    def minimum(self, value: float):
        """"""
        self._properties["minimum"] = value

    @property
    def multiple_of(self) -> float:
        """"""
        return typing.cast(
            float,
            self._properties.get("multipleOf"),
        )

    @multiple_of.setter
    def multiple_of(self, value: float):
        """"""
        self._properties["multipleOf"] = value

    @property
    def not_(self) -> typing.Optional["JSONSchemaProps"]:
        """"""
        return typing.cast(
            typing.Optional["JSONSchemaProps"],
            self._properties.get("not"),
        )

    @not_.setter
    def not_(self, value: typing.Union["JSONSchemaProps", dict, None]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                JSONSchemaProps,
                JSONSchemaProps().from_dict(value),
            )
        self._properties["not"] = value

    @property
    def nullable(self) -> bool:
        """"""
        return typing.cast(
            bool,
            self._properties.get("nullable"),
        )

    @nullable.setter
    def nullable(self, value: bool):
        """"""
        self._properties["nullable"] = value

    @property
    def one_of(self) -> typing.List["JSONSchemaProps"]:
        """"""
        return typing.cast(
            typing.List["JSONSchemaProps"],
            self._properties.get("oneOf"),
        )

    @one_of.setter
    def one_of(
        self, value: typing.Union[typing.List["JSONSchemaProps"], typing.List[dict]]
    ):
        """"""
        cleaned: typing.List[JSONSchemaProps] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    JSONSchemaProps,
                    JSONSchemaProps().from_dict(item),
                )
            cleaned.append(typing.cast(JSONSchemaProps, item))
        self._properties["oneOf"] = cleaned

    @property
    def pattern(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("pattern"),
        )

    @pattern.setter
    def pattern(self, value: str):
        """"""
        self._properties["pattern"] = value

    @property
    def pattern_properties(self) -> dict:
        """"""
        return typing.cast(
            dict,
            self._properties.get("patternProperties"),
        )

    @pattern_properties.setter
    def pattern_properties(self, value: dict):
        """"""
        self._properties["patternProperties"] = value

    @property
    def properties(self) -> dict:
        """"""
        return typing.cast(
            dict,
            self._properties.get("properties"),
        )

    @properties.setter
    def properties(self, value: dict):
        """"""
        self._properties["properties"] = value

    @property
    def required(self) -> typing.List[str]:
        """"""
        return typing.cast(
            typing.List[str],
            self._properties.get("required"),
        )

    @required.setter
    def required(self, value: typing.List[str]):
        """"""
        self._properties["required"] = value

    @property
    def title(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("title"),
        )

    @title.setter
    def title(self, value: str):
        """"""
        self._properties["title"] = value

    @property
    def type_(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """"""
        self._properties["type"] = value

    @property
    def unique_items(self) -> bool:
        """"""
        return typing.cast(
            bool,
            self._properties.get("uniqueItems"),
        )

    @unique_items.setter
    def unique_items(self, value: bool):
        """"""
        self._properties["uniqueItems"] = value

    @property
    def x_kubernetes_embedded_resource(self) -> bool:
        """
        x-kubernetes-embedded-resource defines that the value is an
        embedded Kubernetes runtime.Object, with TypeMeta and
        ObjectMeta. The type must be object. It is allowed to
        further restrict the embedded object. kind, apiVersion and
        metadata are validated automatically. x-kubernetes-preserve-
        unknown-fields is allowed to be true, but does not have to
        be if the object is fully specified (up to kind, apiVersion,
        metadata).
        """
        return typing.cast(
            bool,
            self._properties.get("x-kubernetes-embedded-resource"),
        )

    @x_kubernetes_embedded_resource.setter
    def x_kubernetes_embedded_resource(self, value: bool):
        """
        x-kubernetes-embedded-resource defines that the value is an
        embedded Kubernetes runtime.Object, with TypeMeta and
        ObjectMeta. The type must be object. It is allowed to
        further restrict the embedded object. kind, apiVersion and
        metadata are validated automatically. x-kubernetes-preserve-
        unknown-fields is allowed to be true, but does not have to
        be if the object is fully specified (up to kind, apiVersion,
        metadata).
        """
        self._properties["x-kubernetes-embedded-resource"] = value

    @property
    def x_kubernetes_int_or_string(self) -> bool:
        """
        x-kubernetes-int-or-string specifies that this value is
        either an integer or a string. If this is true, an empty
        type is allowed and type as child of anyOf is permitted if
        following one of the following patterns:

        1) anyOf:
           - type: integer
           - type: string
        2) allOf:
           - anyOf:
             - type: integer
             - type: string
           - ... zero or more
        """
        return typing.cast(
            bool,
            self._properties.get("x-kubernetes-int-or-string"),
        )

    @x_kubernetes_int_or_string.setter
    def x_kubernetes_int_or_string(self, value: bool):
        """
        x-kubernetes-int-or-string specifies that this value is
        either an integer or a string. If this is true, an empty
        type is allowed and type as child of anyOf is permitted if
        following one of the following patterns:

        1) anyOf:
           - type: integer
           - type: string
        2) allOf:
           - anyOf:
             - type: integer
             - type: string
           - ... zero or more
        """
        self._properties["x-kubernetes-int-or-string"] = value

    @property
    def x_kubernetes_preserve_unknown_fields(self) -> bool:
        """
        x-kubernetes-preserve-unknown-fields stops the API server
        decoding step from pruning fields which are not specified in
        the validation schema. This affects fields recursively, but
        switches back to normal pruning behaviour if nested
        properties or additionalProperties are specified in the
        schema. This can either be true or undefined. False is
        forbidden.
        """
        return typing.cast(
            bool,
            self._properties.get("x-kubernetes-preserve-unknown-fields"),
        )

    @x_kubernetes_preserve_unknown_fields.setter
    def x_kubernetes_preserve_unknown_fields(self, value: bool):
        """
        x-kubernetes-preserve-unknown-fields stops the API server
        decoding step from pruning fields which are not specified in
        the validation schema. This affects fields recursively, but
        switches back to normal pruning behaviour if nested
        properties or additionalProperties are specified in the
        schema. This can either be true or undefined. False is
        forbidden.
        """
        self._properties["x-kubernetes-preserve-unknown-fields"] = value

    def __enter__(self) -> "JSONSchemaProps":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSONSchemaPropsOrArray(_kuber_definitions.Definition):
    """
    JSONSchemaPropsOrArray represents a value that can either be
    a JSONSchemaProps or an array of JSONSchemaProps. Mainly
    here for serialization purposes.
    """

    def __init__(
        self,
    ):
        """Create JSONSchemaPropsOrArray instance."""
        super(JSONSchemaPropsOrArray, self).__init__(
            api_version="apiextensions/v1beta1", kind="JSONSchemaPropsOrArray"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "JSONSchemaPropsOrArray":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSONSchemaPropsOrBool(_kuber_definitions.Definition):
    """
    JSONSchemaPropsOrBool represents JSONSchemaProps or a
    boolean value. Defaults to true for the boolean property.
    """

    def __init__(
        self,
    ):
        """Create JSONSchemaPropsOrBool instance."""
        super(JSONSchemaPropsOrBool, self).__init__(
            api_version="apiextensions/v1beta1", kind="JSONSchemaPropsOrBool"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "JSONSchemaPropsOrBool":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSONSchemaPropsOrStringArray(_kuber_definitions.Definition):
    """
    JSONSchemaPropsOrStringArray represents a JSONSchemaProps or
    a string array.
    """

    def __init__(
        self,
    ):
        """Create JSONSchemaPropsOrStringArray instance."""
        super(JSONSchemaPropsOrStringArray, self).__init__(
            api_version="apiextensions/v1beta1", kind="JSONSchemaPropsOrStringArray"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "JSONSchemaPropsOrStringArray":
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
        port: int = None,
    ):
        """Create ServiceReference instance."""
        super(ServiceReference, self).__init__(
            api_version="apiextensions/v1beta1", kind="ServiceReference"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "path": path if path is not None else "",
            "port": port if port is not None else None,
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
            "path": (str, None),
            "port": (int, None),
        }

    @property
    def name(self) -> str:
        """
        `name` is the name of the service. Required
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of the service. Required
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        `namespace` is the namespace of the service. Required
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        `namespace` is the namespace of the service. Required
        """
        self._properties["namespace"] = value

    @property
    def path(self) -> str:
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        return typing.cast(
            str,
            self._properties.get("path"),
        )

    @path.setter
    def path(self, value: str):
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        self._properties["path"] = value

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


class WebhookClientConfig(_kuber_definitions.Definition):
    """
    WebhookClientConfig contains the information to make a TLS
    connection with the webhook. It has the same field as
    admissionregistration.v1beta1.WebhookClientConfig.
    """

    def __init__(
        self,
        ca_bundle: str = None,
        service: "ServiceReference" = None,
        url: str = None,
    ):
        """Create WebhookClientConfig instance."""
        super(WebhookClientConfig, self).__init__(
            api_version="apiextensions/v1beta1", kind="WebhookClientConfig"
        )
        self._properties = {
            "caBundle": ca_bundle if ca_bundle is not None else "",
            "service": service if service is not None else ServiceReference(),
            "url": url if url is not None else "",
        }
        self._types = {
            "caBundle": (str, None),
            "service": (ServiceReference, None),
            "url": (str, None),
        }

    @property
    def ca_bundle(self) -> str:
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        return typing.cast(
            str,
            self._properties.get("caBundle"),
        )

    @ca_bundle.setter
    def ca_bundle(self, value: str):
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        self._properties["caBundle"] = value

    @property
    def service(self) -> "ServiceReference":
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook is running within the cluster, then you
        should use `service`.
        """
        return typing.cast(
            "ServiceReference",
            self._properties.get("service"),
        )

    @service.setter
    def service(self, value: typing.Union["ServiceReference", dict]):
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook is running within the cluster, then you
        should use `service`.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceReference,
                ServiceReference().from_dict(value),
            )
        self._properties["service"] = value

    @property
    def url(self) -> str:
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to a service running in the
        cluster; use the `service` field instead. The host might be
        resolved via external DNS in some apiservers (e.g., `kube-
        apiserver` cannot resolve in-cluster DNS as that would be a
        layering violation). `host` may also be an IP address.

        Please note that using `localhost` or `127.0.0.1` as a
        `host` is risky unless you take great care to run this
        webhook on all hosts which run an apiserver which might need
        to make calls to this webhook. Such installs are likely to
        be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with
        "https://".

        A path is optional, and if present may be any string
        permissible in a URL. You may use the path to pass an
        arbitrary string to the webhook, for example, a cluster
        identifier.

        Attempting to use a user or basic auth e.g. "user:password@"
        is not allowed. Fragments ("#...") and query parameters
        ("?...") are not allowed, either.
        """
        return typing.cast(
            str,
            self._properties.get("url"),
        )

    @url.setter
    def url(self, value: str):
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to a service running in the
        cluster; use the `service` field instead. The host might be
        resolved via external DNS in some apiservers (e.g., `kube-
        apiserver` cannot resolve in-cluster DNS as that would be a
        layering violation). `host` may also be an IP address.

        Please note that using `localhost` or `127.0.0.1` as a
        `host` is risky unless you take great care to run this
        webhook on all hosts which run an apiserver which might need
        to make calls to this webhook. Such installs are likely to
        be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with
        "https://".

        A path is optional, and if present may be any string
        permissible in a URL. You may use the path to pass an
        arbitrary string to the webhook, for example, a cluster
        identifier.

        Attempting to use a user or basic auth e.g. "user:password@"
        is not allowed. Fragments ("#...") and query parameters
        ("?...") are not allowed, either.
        """
        self._properties["url"] = value

    def __enter__(self) -> "WebhookClientConfig":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

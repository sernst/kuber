import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_26.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_26.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_26.meta_v1 import ObjectMeta  # noqa: F401


class MatchResources(_kuber_definitions.Definition):
    """
    MatchResources decides whether to run the admission control
    policy on an object based on whether it meets the match
    criteria. The exclude rules take precedence over include
    rules (if a resource matches both, it is excluded)
    """

    def __init__(
        self,
        exclude_resource_rules: typing.Optional[
            typing.List["NamedRuleWithOperations"]
        ] = None,
        match_policy: typing.Optional[str] = None,
        namespace_selector: typing.Optional["LabelSelector"] = None,
        object_selector: typing.Optional["LabelSelector"] = None,
        resource_rules: typing.Optional[typing.List["NamedRuleWithOperations"]] = None,
    ):
        """Create MatchResources instance."""
        super(MatchResources, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="MatchResources"
        )
        self._properties = {
            "excludeResourceRules": (
                exclude_resource_rules if exclude_resource_rules is not None else []
            ),
            "matchPolicy": match_policy if match_policy is not None else "",
            "namespaceSelector": (
                namespace_selector
                if namespace_selector is not None
                else LabelSelector()
            ),
            "objectSelector": (
                object_selector if object_selector is not None else LabelSelector()
            ),
            "resourceRules": resource_rules if resource_rules is not None else [],
        }
        self._types = {
            "excludeResourceRules": (list, NamedRuleWithOperations),
            "matchPolicy": (str, None),
            "namespaceSelector": (LabelSelector, None),
            "objectSelector": (LabelSelector, None),
            "resourceRules": (list, NamedRuleWithOperations),
        }

    @property
    def exclude_resource_rules(self) -> typing.List["NamedRuleWithOperations"]:
        """
        ExcludeResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy should
        not care about. The exclude rules take precedence over
        include rules (if a resource matches both, it is excluded)
        """
        return typing.cast(
            typing.List["NamedRuleWithOperations"],
            self._properties.get("excludeResourceRules"),
        )

    @exclude_resource_rules.setter
    def exclude_resource_rules(
        self,
        value: typing.Union[typing.List["NamedRuleWithOperations"], typing.List[dict]],
    ):
        """
        ExcludeResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy should
        not care about. The exclude rules take precedence over
        include rules (if a resource matches both, it is excluded)
        """
        cleaned: typing.List[NamedRuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedRuleWithOperations,
                    NamedRuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(NamedRuleWithOperations, item))
        self._properties["excludeResourceRules"] = cleaned

    @property
    def match_policy(self) -> str:
        """
        matchPolicy defines how the "MatchResources" list is used to
        match incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the ValidatingAdmissionPolicy.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the ValidatingAdmissionPolicy.

        Defaults to "Equivalent"
        """
        return typing.cast(
            str,
            self._properties.get("matchPolicy"),
        )

    @match_policy.setter
    def match_policy(self, value: str):
        """
        matchPolicy defines how the "MatchResources" list is used to
        match incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the ValidatingAdmissionPolicy.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the ValidatingAdmissionPolicy.

        Defaults to "Equivalent"
        """
        self._properties["matchPolicy"] = value

    @property
    def namespace_selector(self) -> "LabelSelector":
        """
        NamespaceSelector decides whether to run the admission
        control policy on an object based on whether the namespace
        for that object matches the selector. If the object itself
        is a namespace, the matching is performed on
        object.metadata.labels. If the object is another cluster
        scoped resource, it never skips the policy.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the policy on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/ for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("namespaceSelector"),
        )

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        NamespaceSelector decides whether to run the admission
        control policy on an object based on whether the namespace
        for that object matches the selector. If the object itself
        is a namespace, the matching is performed on
        object.metadata.labels. If the object is another cluster
        scoped resource, it never skips the policy.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the policy on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/ for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["namespaceSelector"] = value

    @property
    def object_selector(self) -> "LabelSelector":
        """
        ObjectSelector decides whether to run the validation based
        on if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the cel validation, and is considered to
        match if either object matches the selector. A null object
        (oldObject in the case of create, or newObject in the case
        of delete) or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("objectSelector"),
        )

    @object_selector.setter
    def object_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        ObjectSelector decides whether to run the validation based
        on if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the cel validation, and is considered to
        match if either object matches the selector. A null object
        (oldObject in the case of create, or newObject in the case
        of delete) or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["objectSelector"] = value

    @property
    def resource_rules(self) -> typing.List["NamedRuleWithOperations"]:
        """
        ResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy
        matches. The policy cares about an operation if it matches
        _any_ Rule.
        """
        return typing.cast(
            typing.List["NamedRuleWithOperations"],
            self._properties.get("resourceRules"),
        )

    @resource_rules.setter
    def resource_rules(
        self,
        value: typing.Union[typing.List["NamedRuleWithOperations"], typing.List[dict]],
    ):
        """
        ResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy
        matches. The policy cares about an operation if it matches
        _any_ Rule.
        """
        cleaned: typing.List[NamedRuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedRuleWithOperations,
                    NamedRuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(NamedRuleWithOperations, item))
        self._properties["resourceRules"] = cleaned

    def __enter__(self) -> "MatchResources":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedRuleWithOperations(_kuber_definitions.Definition):
    """
    NamedRuleWithOperations is a tuple of Operations and
    Resources with ResourceNames.
    """

    def __init__(
        self,
        api_groups: typing.Optional[typing.List[str]] = None,
        api_versions: typing.Optional[typing.List[str]] = None,
        operations: typing.Optional[typing.List[str]] = None,
        resource_names: typing.Optional[typing.List[str]] = None,
        resources: typing.Optional[typing.List[str]] = None,
        scope: typing.Optional[str] = None,
    ):
        """Create NamedRuleWithOperations instance."""
        super(NamedRuleWithOperations, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="NamedRuleWithOperations"
        )
        self._properties = {
            "apiGroups": api_groups if api_groups is not None else [],
            "apiVersions": api_versions if api_versions is not None else [],
            "operations": operations if operations is not None else [],
            "resourceNames": resource_names if resource_names is not None else [],
            "resources": resources if resources is not None else [],
            "scope": scope if scope is not None else "",
        }
        self._types = {
            "apiGroups": (list, str),
            "apiVersions": (list, str),
            "operations": (list, str),
            "resourceNames": (list, str),
            "resources": (list, str),
            "scope": (str, None),
        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiGroups"),
        )

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        self._properties["apiGroups"] = value

    @property
    def api_versions(self) -> typing.List[str]:
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiVersions"),
        )

    @api_versions.setter
    def api_versions(self, value: typing.List[str]):
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        self._properties["apiVersions"] = value

    @property
    def operations(self) -> typing.List[str]:
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, DELETE, CONNECT or * for all of those
        operations and any future admission operations that are
        added. If '*' is present, the length of the slice must be
        one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("operations"),
        )

    @operations.setter
    def operations(self, value: typing.List[str]):
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, DELETE, CONNECT or * for all of those
        operations and any future admission operations that are
        added. If '*' is present, the length of the slice must be
        one. Required.
        """
        self._properties["operations"] = value

    @property
    def resource_names(self) -> typing.List[str]:
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resourceNames"),
        )

    @resource_names.setter
    def resource_names(self, value: typing.List[str]):
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.
        """
        self._properties["resourceNames"] = value

    @property
    def resources(self) -> typing.List[str]:
        """
        Resources is a list of resources this rule applies to.

        For example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present, the validation rule will ensure
        resources do not overlap with each other.

        Depending on the enclosing object, subresources might not be
        allowed. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resources"),
        )

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        Resources is a list of resources this rule applies to.

        For example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present, the validation rule will ensure
        resources do not overlap with each other.

        Depending on the enclosing object, subresources might not be
        allowed. Required.
        """
        self._properties["resources"] = value

    @property
    def scope(self) -> str:
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        return typing.cast(
            str,
            self._properties.get("scope"),
        )

    @scope.setter
    def scope(self, value: str):
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        self._properties["scope"] = value

    def __enter__(self) -> "NamedRuleWithOperations":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ParamKind(_kuber_definitions.Definition):
    """
    ParamKind is a tuple of Group Kind and Version.
    """

    def __init__(
        self,
        api_version: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
    ):
        """Create ParamKind instance."""
        super(ParamKind, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="ParamKind"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion is the API group version the resources belong to.
        In format of "group/version". Required.
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion is the API group version the resources belong to.
        In format of "group/version". Required.
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the API kind the resources belong to. Required.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the API kind the resources belong to. Required.
        """
        self._properties["kind"] = value

    def __enter__(self) -> "ParamKind":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ParamRef(_kuber_definitions.Definition):
    """
    ParamRef references a parameter resource
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
    ):
        """Create ParamRef instance."""
        super(ParamRef, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="ParamRef"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
        }

    @property
    def name(self) -> str:
        """
        Name of the resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name of the resource being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace of the referenced resource. Should be empty for
        the cluster-scoped resources
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace of the referenced resource. Should be empty for
        the cluster-scoped resources
        """
        self._properties["namespace"] = value

    def __enter__(self) -> "ParamRef":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicy(_kuber_definitions.Resource):
    """
    ValidatingAdmissionPolicy describes the definition of an
    admission validation policy that accepts or rejects an
    object without changing it.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ValidatingAdmissionPolicySpec"] = None,
    ):
        """Create ValidatingAdmissionPolicy instance."""
        super(ValidatingAdmissionPolicy, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicy",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ValidatingAdmissionPolicySpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ValidatingAdmissionPolicySpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ValidatingAdmissionPolicySpec":
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicy.
        """
        return typing.cast(
            "ValidatingAdmissionPolicySpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ValidatingAdmissionPolicySpec", dict]):
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicy.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ValidatingAdmissionPolicySpec,
                ValidatingAdmissionPolicySpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_validating_admission_policy",
            "create_validating_admission_policy",
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
        Replaces the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_validating_admission_policy",
            "replace_validating_admission_policy",
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
        Patches the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_validating_admission_policy",
            "patch_validating_admission_policy",
        ]

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
        Reads the ValidatingAdmissionPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_validating_admission_policy",
            "read_validating_admission_policy",
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
        Deletes the ValidatingAdmissionPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_validating_admission_policy",
            "delete_validating_admission_policy",
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
    ) -> "client.AdmissionregistrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBinding(_kuber_definitions.Resource):
    """
    ValidatingAdmissionPolicyBinding binds the
    ValidatingAdmissionPolicy with paramerized resources.
    ValidatingAdmissionPolicyBinding and parameter CRDs together
    define how cluster administrators configure policies for
    clusters.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ValidatingAdmissionPolicyBindingSpec"] = None,
    ):
        """Create ValidatingAdmissionPolicyBinding instance."""
        super(ValidatingAdmissionPolicyBinding, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicyBinding",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": (
                spec if spec is not None else ValidatingAdmissionPolicyBindingSpec()
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ValidatingAdmissionPolicyBindingSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ValidatingAdmissionPolicyBindingSpec":
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicyBinding.
        """
        return typing.cast(
            "ValidatingAdmissionPolicyBindingSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ValidatingAdmissionPolicyBindingSpec", dict]):
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicyBinding.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ValidatingAdmissionPolicyBindingSpec,
                ValidatingAdmissionPolicyBindingSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_validating_admission_policy_binding",
            "create_validating_admission_policy_binding",
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
        Replaces the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_validating_admission_policy_binding",
            "replace_validating_admission_policy_binding",
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
        Patches the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_validating_admission_policy_binding",
            "patch_validating_admission_policy_binding",
        ]

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
        Reads the ValidatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_validating_admission_policy_binding",
            "read_validating_admission_policy_binding",
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
        Deletes the ValidatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_validating_admission_policy_binding",
            "delete_validating_admission_policy_binding",
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
    ) -> "client.AdmissionregistrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyBinding":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBindingList(_kuber_definitions.Collection):
    """
    ValidatingAdmissionPolicyBindingList is a list of
    ValidatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ValidatingAdmissionPolicyBinding"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ValidatingAdmissionPolicyBindingList instance."""
        super(ValidatingAdmissionPolicyBindingList, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicyBindingList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ValidatingAdmissionPolicyBinding),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ValidatingAdmissionPolicyBinding"]:
        """
        List of PolicyBinding.
        """
        return typing.cast(
            typing.List["ValidatingAdmissionPolicyBinding"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["ValidatingAdmissionPolicyBinding"], typing.List[dict]
        ],
    ):
        """
        List of PolicyBinding.
        """
        cleaned: typing.List[ValidatingAdmissionPolicyBinding] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingAdmissionPolicyBinding,
                    ValidatingAdmissionPolicyBinding().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingAdmissionPolicyBinding, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
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
        architecture/api-conventions.md#types-kinds
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
    ) -> "client.AdmissionregistrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyBindingList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBindingSpec(_kuber_definitions.Definition):
    """
    ValidatingAdmissionPolicyBindingSpec is the specification of
    the ValidatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        match_resources: typing.Optional["MatchResources"] = None,
        param_ref: typing.Optional["ParamRef"] = None,
        policy_name: typing.Optional[str] = None,
    ):
        """Create ValidatingAdmissionPolicyBindingSpec instance."""
        super(ValidatingAdmissionPolicyBindingSpec, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicyBindingSpec",
        )
        self._properties = {
            "matchResources": (
                match_resources if match_resources is not None else MatchResources()
            ),
            "paramRef": param_ref if param_ref is not None else ParamRef(),
            "policyName": policy_name if policy_name is not None else "",
        }
        self._types = {
            "matchResources": (MatchResources, None),
            "paramRef": (ParamRef, None),
            "policyName": (str, None),
        }

    @property
    def match_resources(self) -> "MatchResources":
        """
        MatchResources declares what resources match this binding
        and will be validated by it. Note that this is intersected
        with the policy's matchConstraints, so only requests that
        are matched by the policy can be selected by this. If this
        is unset, all resources matched by the policy are validated
        by this binding When resourceRules is unset, it does not
        constrain resource matching. If a resource is matched by the
        other fields of this object, it will be validated. Note that
        this is differs from ValidatingAdmissionPolicy
        matchConstraints, where resourceRules are required.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchResources"),
        )

    @match_resources.setter
    def match_resources(self, value: typing.Union["MatchResources", dict]):
        """
        MatchResources declares what resources match this binding
        and will be validated by it. Note that this is intersected
        with the policy's matchConstraints, so only requests that
        are matched by the policy can be selected by this. If this
        is unset, all resources matched by the policy are validated
        by this binding When resourceRules is unset, it does not
        constrain resource matching. If a resource is matched by the
        other fields of this object, it will be validated. Note that
        this is differs from ValidatingAdmissionPolicy
        matchConstraints, where resourceRules are required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MatchResources,
                MatchResources().from_dict(value),
            )
        self._properties["matchResources"] = value

    @property
    def param_ref(self) -> "ParamRef":
        """
        ParamRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in ParamKind of the bound
        ValidatingAdmissionPolicy. If the policy specifies a
        ParamKind and the resource referred to by ParamRef does not
        exist, this binding is considered mis-configured and the
        FailurePolicy of the ValidatingAdmissionPolicy applied.
        """
        return typing.cast(
            "ParamRef",
            self._properties.get("paramRef"),
        )

    @param_ref.setter
    def param_ref(self, value: typing.Union["ParamRef", dict]):
        """
        ParamRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in ParamKind of the bound
        ValidatingAdmissionPolicy. If the policy specifies a
        ParamKind and the resource referred to by ParamRef does not
        exist, this binding is considered mis-configured and the
        FailurePolicy of the ValidatingAdmissionPolicy applied.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParamRef,
                ParamRef().from_dict(value),
            )
        self._properties["paramRef"] = value

    @property
    def policy_name(self) -> str:
        """
        PolicyName references a ValidatingAdmissionPolicy name which
        the ValidatingAdmissionPolicyBinding binds to. If the
        referenced resource does not exist, this binding is
        considered invalid and will be ignored Required.
        """
        return typing.cast(
            str,
            self._properties.get("policyName"),
        )

    @policy_name.setter
    def policy_name(self, value: str):
        """
        PolicyName references a ValidatingAdmissionPolicy name which
        the ValidatingAdmissionPolicyBinding binds to. If the
        referenced resource does not exist, this binding is
        considered invalid and will be ignored Required.
        """
        self._properties["policyName"] = value

    def __enter__(self) -> "ValidatingAdmissionPolicyBindingSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyList(_kuber_definitions.Collection):
    """
    ValidatingAdmissionPolicyList is a list of
    ValidatingAdmissionPolicy.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ValidatingAdmissionPolicy"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ValidatingAdmissionPolicyList instance."""
        super(ValidatingAdmissionPolicyList, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicyList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ValidatingAdmissionPolicy),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ValidatingAdmissionPolicy"]:
        """
        List of ValidatingAdmissionPolicy.
        """
        return typing.cast(
            typing.List["ValidatingAdmissionPolicy"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["ValidatingAdmissionPolicy"], typing.List[dict]
        ],
    ):
        """
        List of ValidatingAdmissionPolicy.
        """
        cleaned: typing.List[ValidatingAdmissionPolicy] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingAdmissionPolicy,
                    ValidatingAdmissionPolicy().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingAdmissionPolicy, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
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
        architecture/api-conventions.md#types-kinds
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
    ) -> "client.AdmissionregistrationV1alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1alpha1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicySpec(_kuber_definitions.Definition):
    """
    ValidatingAdmissionPolicySpec is the specification of the
    desired behavior of the AdmissionPolicy.
    """

    def __init__(
        self,
        failure_policy: typing.Optional[str] = None,
        match_constraints: typing.Optional["MatchResources"] = None,
        param_kind: typing.Optional["ParamKind"] = None,
        validations: typing.Optional[typing.List["Validation"]] = None,
    ):
        """Create ValidatingAdmissionPolicySpec instance."""
        super(ValidatingAdmissionPolicySpec, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="ValidatingAdmissionPolicySpec",
        )
        self._properties = {
            "failurePolicy": failure_policy if failure_policy is not None else "",
            "matchConstraints": (
                match_constraints if match_constraints is not None else MatchResources()
            ),
            "paramKind": param_kind if param_kind is not None else ParamKind(),
            "validations": validations if validations is not None else [],
        }
        self._types = {
            "failurePolicy": (str, None),
            "matchConstraints": (MatchResources, None),
            "paramKind": (ParamKind, None),
            "validations": (list, Validation),
        }

    @property
    def failure_policy(self) -> str:
        """
        FailurePolicy defines how to handle failures for the
        admission policy. Failures can occur from invalid or mis-
        configured policy definitions or bindings. A policy is
        invalid if spec.paramKind refers to a non-existent Kind. A
        binding is invalid if spec.paramRef.name refers to a non-
        existent resource. Allowed values are Ignore or Fail.
        Defaults to Fail.
        """
        return typing.cast(
            str,
            self._properties.get("failurePolicy"),
        )

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        FailurePolicy defines how to handle failures for the
        admission policy. Failures can occur from invalid or mis-
        configured policy definitions or bindings. A policy is
        invalid if spec.paramKind refers to a non-existent Kind. A
        binding is invalid if spec.paramRef.name refers to a non-
        existent resource. Allowed values are Ignore or Fail.
        Defaults to Fail.
        """
        self._properties["failurePolicy"] = value

    @property
    def match_constraints(self) -> "MatchResources":
        """
        MatchConstraints specifies what resources this policy is
        designed to validate. The AdmissionPolicy cares about a
        request if it matches _all_ Constraints. However, in order
        to prevent clusters from being put into an unstable state
        that cannot be recovered from via the API
        ValidatingAdmissionPolicy cannot match
        ValidatingAdmissionPolicy and
        ValidatingAdmissionPolicyBinding. Required.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchConstraints"),
        )

    @match_constraints.setter
    def match_constraints(self, value: typing.Union["MatchResources", dict]):
        """
        MatchConstraints specifies what resources this policy is
        designed to validate. The AdmissionPolicy cares about a
        request if it matches _all_ Constraints. However, in order
        to prevent clusters from being put into an unstable state
        that cannot be recovered from via the API
        ValidatingAdmissionPolicy cannot match
        ValidatingAdmissionPolicy and
        ValidatingAdmissionPolicyBinding. Required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MatchResources,
                MatchResources().from_dict(value),
            )
        self._properties["matchConstraints"] = value

    @property
    def param_kind(self) -> "ParamKind":
        """
        ParamKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If ParamKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in ValidatingAdmissionPolicyBinding,
        the params variable will be null.
        """
        return typing.cast(
            "ParamKind",
            self._properties.get("paramKind"),
        )

    @param_kind.setter
    def param_kind(self, value: typing.Union["ParamKind", dict]):
        """
        ParamKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If ParamKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in ValidatingAdmissionPolicyBinding,
        the params variable will be null.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParamKind,
                ParamKind().from_dict(value),
            )
        self._properties["paramKind"] = value

    @property
    def validations(self) -> typing.List["Validation"]:
        """
        Validations contain CEL expressions which is used to apply
        the validation. A minimum of one validation is required for
        a policy definition. Required.
        """
        return typing.cast(
            typing.List["Validation"],
            self._properties.get("validations"),
        )

    @validations.setter
    def validations(
        self, value: typing.Union[typing.List["Validation"], typing.List[dict]]
    ):
        """
        Validations contain CEL expressions which is used to apply
        the validation. A minimum of one validation is required for
        a policy definition. Required.
        """
        cleaned: typing.List[Validation] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Validation,
                    Validation().from_dict(item),
                )
            cleaned.append(typing.cast(Validation, item))
        self._properties["validations"] = cleaned

    def __enter__(self) -> "ValidatingAdmissionPolicySpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Validation(_kuber_definitions.Definition):
    """
    Validation specifies the CEL expression which is used to
    apply the validation.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
    ):
        """Create Validation instance."""
        super(Validation, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="Validation"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "message": (str, None),
            "reason": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression represents the expression which will be evaluated
        by CEL. ref: https://github.com/google/cel-spec CEL
        expressions have access to the contents of the Admission
        request/response, organized into CEL variables as well as
        some other useful variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission request([ref](/pkg/apis/admissio
        n/types.go#AdmissionRequest)). 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property
        names are escaped according to the following rules when
        accessed in the expression: - '__' escapes to
        '__underscores__' - '.' escapes to '__dot__' - '-' escapes
        to '__dash__' - '/' escapes to '__slash__' - Property names
        that exactly match a CEL RESERVED keyword escape to
        '__{keyword}__'. The keywords are:
                  "true", "false", "null", "in", "as", "break", "const",
        "continue", "else", "for", "function", "if",
                  "import", "let", "loop", "package", "namespace",
        "return".
        Examples:
          - Expression accessing a property named "namespace":
        {"Expression": "object.__namespace__ > 0"}
          - Expression accessing a property named "x-prop":
        {"Expression": "object.x__dash__prop > 0"}
          - Expression accessing a property named "redact__d":
        {"Expression": "object.redact__underscores__d > 0"}

        Equality on arrays with list type of 'set' or 'map' ignores
        element order, i.e. [1, 2] == [2, 1]. Concatenation on
        arrays with x-kubernetes-list-type use the semantics of the
        list type:
          - 'set': `X + Y` performs a union where the array
        positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining
        their partial order.
          - 'map': `X + Y` performs a merge where the array
        positions of all keys in `X` are preserved but the values
            are overwritten by values in `Y` when the key sets of
        `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their
        partial order.
        Required.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression represents the expression which will be evaluated
        by CEL. ref: https://github.com/google/cel-spec CEL
        expressions have access to the contents of the Admission
        request/response, organized into CEL variables as well as
        some other useful variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission request([ref](/pkg/apis/admissio
        n/types.go#AdmissionRequest)). 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property
        names are escaped according to the following rules when
        accessed in the expression: - '__' escapes to
        '__underscores__' - '.' escapes to '__dot__' - '-' escapes
        to '__dash__' - '/' escapes to '__slash__' - Property names
        that exactly match a CEL RESERVED keyword escape to
        '__{keyword}__'. The keywords are:
                  "true", "false", "null", "in", "as", "break", "const",
        "continue", "else", "for", "function", "if",
                  "import", "let", "loop", "package", "namespace",
        "return".
        Examples:
          - Expression accessing a property named "namespace":
        {"Expression": "object.__namespace__ > 0"}
          - Expression accessing a property named "x-prop":
        {"Expression": "object.x__dash__prop > 0"}
          - Expression accessing a property named "redact__d":
        {"Expression": "object.redact__underscores__d > 0"}

        Equality on arrays with list type of 'set' or 'map' ignores
        element order, i.e. [1, 2] == [2, 1]. Concatenation on
        arrays with x-kubernetes-list-type use the semantics of the
        list type:
          - 'set': `X + Y` performs a union where the array
        positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining
        their partial order.
          - 'map': `X + Y` performs a merge where the array
        positions of all keys in `X` are preserved but the values
            are overwritten by values in `Y` when the key sets of
        `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their
        partial order.
        Required.
        """
        self._properties["expression"] = value

    @property
    def message(self) -> str:
        """
        Message represents the message displayed when validation
        fails. The message is required if the Expression contains
        line breaks. The message must not contain line breaks. If
        unset, the message is "failed rule: {Rule}". e.g. "must be a
        URL with the host matching spec.host" If the Expression
        contains line breaks. Message is required. The message must
        not contain line breaks. If unset, the message is "failed
        Expression: {Expression}".
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        Message represents the message displayed when validation
        fails. The message is required if the Expression contains
        line breaks. The message must not contain line breaks. If
        unset, the message is "failed rule: {Rule}". e.g. "must be a
        URL with the host matching spec.host" If the Expression
        contains line breaks. Message is required. The message must
        not contain line breaks. If unset, the message is "failed
        Expression: {Expression}".
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        Reason represents a machine-readable description of why this
        validation failed. If this is the first validation in the
        list to fail, this reason, as well as the corresponding HTTP
        response code, are used in the HTTP response to the client.
        The currently supported reasons are: "Unauthorized",
        "Forbidden", "Invalid", "RequestEntityTooLarge". If not set,
        StatusReasonInvalid is used in the response to the client.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        Reason represents a machine-readable description of why this
        validation failed. If this is the first validation in the
        list to fail, this reason, as well as the corresponding HTTP
        response code, are used in the HTTP response to the client.
        The currently supported reasons are: "Unauthorized",
        "Forbidden", "Invalid", "RequestEntityTooLarge". If not set,
        StatusReasonInvalid is used in the response to the client.
        """
        self._properties["reason"] = value

    def __enter__(self) -> "Validation":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

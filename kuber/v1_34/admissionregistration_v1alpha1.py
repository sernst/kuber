import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_34.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_34.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_34.meta_v1 import ObjectMeta  # noqa: F401


class ApplyConfiguration(_kuber_definitions.Definition):
    """
    ApplyConfiguration defines the desired configuration values
    of an object.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
    ):
        """Create ApplyConfiguration instance."""
        super(ApplyConfiguration, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="ApplyConfiguration"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
        }
        self._types = {
            "expression": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        expression will be evaluated by CEL to create an apply
        configuration. ref: https://github.com/google/cel-spec

        Apply configurations are declared in CEL using object
        initialization. For example, this CEL expression returns an
        apply configuration to set a single field:

                Object{
                  spec: Object.spec{
                    serviceAccountName: "example"
                  }
                }

        Apply configurations may not modify atomic structs, maps or
        arrays due to the risk of accidental deletion of values not
        included in the apply configuration.

        CEL expressions have access to the object types needed to
        create apply configurations:

        - 'Object' - CEL type of the resource object. -
        'Object.<fieldName>' - CEL type of object field (such as
        'Object.spec') -
        'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type
        of nested field (such as 'Object.spec.containers')

        CEL expressions have access to the contents of the API
        request, organized into CEL variables as well as some other
        useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        expression will be evaluated by CEL to create an apply
        configuration. ref: https://github.com/google/cel-spec

        Apply configurations are declared in CEL using object
        initialization. For example, this CEL expression returns an
        apply configuration to set a single field:

                Object{
                  spec: Object.spec{
                    serviceAccountName: "example"
                  }
                }

        Apply configurations may not modify atomic structs, maps or
        arrays due to the risk of accidental deletion of values not
        included in the apply configuration.

        CEL expressions have access to the object types needed to
        create apply configurations:

        - 'Object' - CEL type of the resource object. -
        'Object.<fieldName>' - CEL type of object field (such as
        'Object.spec') -
        'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type
        of nested field (such as 'Object.spec.containers')

        CEL expressions have access to the contents of the API
        request, organized into CEL variables as well as some other
        useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.
        """
        self._properties["expression"] = value

    def __enter__(self) -> "ApplyConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JSONPatch(_kuber_definitions.Definition):
    """
    JSONPatch defines a JSON Patch.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
    ):
        """Create JSONPatch instance."""
        super(JSONPatch, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="JSONPatch"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
        }
        self._types = {
            "expression": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        expression will be evaluated by CEL to create a [JSON
        patch](https://jsonpatch.com/). ref:
        https://github.com/google/cel-spec

        expression must return an array of JSONPatch values.

        For example, this CEL expression returns a JSON patch to
        conditionally modify a value:

                  [
                    JSONPatch{op: "test", path: "/spec/example", value:
        "Red"},
                    JSONPatch{op: "replace", path: "/spec/example", value:
        "Green"}
                  ]

        To define an object for the patch value, use Object types.
        For example:

                  [
                    JSONPatch{
                      op: "add",
                      path: "/spec/selector",
                      value: Object.spec.selector{matchLabels:
        {"environment": "test"}}
                    }
                  ]

        To use strings containing '/' and '~' as JSONPatch path
        keys, use "jsonpatch.escapeKey". For example:

                  [
                    JSONPatch{
                      op: "add",
                      path: "/metadata/labels/" +
        jsonpatch.escapeKey("example.com/environment"),
                      value: "test"
                    },
                  ]

        CEL expressions have access to the types needed to create
        JSON patches and objects:

        - 'JSONPatch' - CEL type of JSON Patch operations. JSONPatch
        has the fields 'op', 'from', 'path' and 'value'.
          See [JSON patch](https://jsonpatch.com/) for more details.
        The 'value' field may be set to any of: string,
          integer, array, map or object.  If set, the 'path' and
        'from' fields must be set to a
          [JSON
        pointer](https://datatracker.ietf.org/doc/html/rfc6901/)
        string, where the 'jsonpatch.escapeKey()' CEL
          function may be used to escape path keys containing '/'
        and '~'.
        - 'Object' - CEL type of the resource object. -
        'Object.<fieldName>' - CEL type of object field (such as
        'Object.spec') -
        'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type
        of nested field (such as 'Object.spec.containers')

        CEL expressions have access to the contents of the API
        request, organized into CEL variables as well as some other
        useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        CEL expressions have access to [Kubernetes CEL function
        libraries](https://kubernetes.io/docs/reference/using-
        api/cel/#cel-options-language-features-and-libraries) as
        well as:

        - 'jsonpatch.escapeKey' - Performs JSONPatch key escaping.
        '~' and  '/' are escaped as '~0' and `~1' respectively).

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        expression will be evaluated by CEL to create a [JSON
        patch](https://jsonpatch.com/). ref:
        https://github.com/google/cel-spec

        expression must return an array of JSONPatch values.

        For example, this CEL expression returns a JSON patch to
        conditionally modify a value:

                  [
                    JSONPatch{op: "test", path: "/spec/example", value:
        "Red"},
                    JSONPatch{op: "replace", path: "/spec/example", value:
        "Green"}
                  ]

        To define an object for the patch value, use Object types.
        For example:

                  [
                    JSONPatch{
                      op: "add",
                      path: "/spec/selector",
                      value: Object.spec.selector{matchLabels:
        {"environment": "test"}}
                    }
                  ]

        To use strings containing '/' and '~' as JSONPatch path
        keys, use "jsonpatch.escapeKey". For example:

                  [
                    JSONPatch{
                      op: "add",
                      path: "/metadata/labels/" +
        jsonpatch.escapeKey("example.com/environment"),
                      value: "test"
                    },
                  ]

        CEL expressions have access to the types needed to create
        JSON patches and objects:

        - 'JSONPatch' - CEL type of JSON Patch operations. JSONPatch
        has the fields 'op', 'from', 'path' and 'value'.
          See [JSON patch](https://jsonpatch.com/) for more details.
        The 'value' field may be set to any of: string,
          integer, array, map or object.  If set, the 'path' and
        'from' fields must be set to a
          [JSON
        pointer](https://datatracker.ietf.org/doc/html/rfc6901/)
        string, where the 'jsonpatch.escapeKey()' CEL
          function may be used to escape path keys containing '/'
        and '~'.
        - 'Object' - CEL type of the resource object. -
        'Object.<fieldName>' - CEL type of object field (such as
        'Object.spec') -
        'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type
        of nested field (such as 'Object.spec.containers')

        CEL expressions have access to the contents of the API
        request, organized into CEL variables as well as some other
        useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        CEL expressions have access to [Kubernetes CEL function
        libraries](https://kubernetes.io/docs/reference/using-
        api/cel/#cel-options-language-features-and-libraries) as
        well as:

        - 'jsonpatch.escapeKey' - Performs JSONPatch key escaping.
        '~' and  '/' are escaped as '~0' and `~1' respectively).

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.
        """
        self._properties["expression"] = value

    def __enter__(self) -> "JSONPatch":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MatchCondition(_kuber_definitions.Definition):
    """ """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create MatchCondition instance."""
        super(MatchCondition, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="MatchCondition"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "name": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression represents the expression which will be evaluated
        by CEL. Must evaluate to bool. CEL expressions have access
        to the contents of the AdmissionRequest and Authorizer,
        organized into CEL variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission
        request(/pkg/apis/admission/types.go#AdmissionRequest).
        'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.
        Documentation on CEL:
        https://kubernetes.io/docs/reference/using-api/cel/

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
        by CEL. Must evaluate to bool. CEL expressions have access
        to the contents of the AdmissionRequest and Authorizer,
        organized into CEL variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission
        request(/pkg/apis/admission/types.go#AdmissionRequest).
        'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.
        Documentation on CEL:
        https://kubernetes.io/docs/reference/using-api/cel/

        Required.
        """
        self._properties["expression"] = value

    @property
    def name(self) -> str:
        """
        Name is an identifier for this match condition, used for
        strategic merging of MatchConditions, as well as providing
        an identifier for logging purposes. A good name should be
        descriptive of the associated expression. Name must be a
        qualified name consisting of alphanumeric characters, '-',
        '_' or '.', and must start and end with an alphanumeric
        character (e.g. 'MyName',  or 'my.name',  or '123-abc',
        regex used for validation is
        '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional
        DNS subdomain prefix and '/' (e.g. 'example.com/MyName')

        Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is an identifier for this match condition, used for
        strategic merging of MatchConditions, as well as providing
        an identifier for logging purposes. A good name should be
        descriptive of the associated expression. Name must be a
        qualified name consisting of alphanumeric characters, '-',
        '_' or '.', and must start and end with an alphanumeric
        character (e.g. 'MyName',  or 'my.name',  or '123-abc',
        regex used for validation is
        '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional
        DNS subdomain prefix and '/' (e.g. 'example.com/MyName')

        Required.
        """
        self._properties["name"] = value

    def __enter__(self) -> "MatchCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


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
        resources/subresources the policy should not care about. The
        exclude rules take precedence over include rules (if a
        resource matches both, it is excluded)
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
        resources/subresources the policy should not care about. The
        exclude rules take precedence over include rules (if a
        resource matches both, it is excluded)
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
        apiVersions:["v1"], resources: ["deployments"]`, the
        admission policy does not consider requests to apps/v1beta1
        or extensions/v1beta1 API groups.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, the admission policy **does** consider
        requests made to apps/v1beta1 or extensions/v1beta1 API
        groups. The API server translates the request to a matched
        resource API if necessary.

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
        apiVersions:["v1"], resources: ["deployments"]`, the
        admission policy does not consider requests to apps/v1beta1
        or extensions/v1beta1 API groups.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, the admission policy **does** consider
        requests made to apps/v1beta1 or extensions/v1beta1 API
        groups. The API server translates the request to a matched
        resource API if necessary.

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
        ObjectSelector decides whether to run the policy based on if
        the object has matching labels. objectSelector is evaluated
        against both the oldObject and newObject that would be sent
        to the policy's expression (CEL), and is considered to match
        if either object matches the selector. A null object
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
        ObjectSelector decides whether to run the policy based on if
        the object has matching labels. objectSelector is evaluated
        against both the oldObject and newObject that would be sent
        to the policy's expression (CEL), and is considered to match
        if either object matches the selector. A null object
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
        resources/subresources the admission policy matches. The
        policy cares about an operation if it matches _any_ Rule.
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
        resources/subresources the admission policy matches. The
        policy cares about an operation if it matches _any_ Rule.
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


class MutatingAdmissionPolicy(_kuber_definitions.Resource):
    """
    MutatingAdmissionPolicy describes the definition of an
    admission mutation policy that mutates the object coming
    into admission chain.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["MutatingAdmissionPolicySpec"] = None,
    ):
        """Create MutatingAdmissionPolicy instance."""
        super(MutatingAdmissionPolicy, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="MutatingAdmissionPolicy"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else MutatingAdmissionPolicySpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (MutatingAdmissionPolicySpec, None),
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
    def spec(self) -> "MutatingAdmissionPolicySpec":
        """
        Specification of the desired behavior of the
        MutatingAdmissionPolicy.
        """
        return typing.cast(
            "MutatingAdmissionPolicySpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["MutatingAdmissionPolicySpec", dict]):
        """
        Specification of the desired behavior of the
        MutatingAdmissionPolicy.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MutatingAdmissionPolicySpec,
                MutatingAdmissionPolicySpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the MutatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_mutating_admission_policy",
            "create_mutating_admission_policy",
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
        Replaces the MutatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_mutating_admission_policy",
            "replace_mutating_admission_policy",
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
        Patches the MutatingAdmissionPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_mutating_admission_policy",
            "patch_mutating_admission_policy",
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
        Reads the MutatingAdmissionPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_mutating_admission_policy",
            "read_mutating_admission_policy",
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
        Deletes the MutatingAdmissionPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_mutating_admission_policy",
            "delete_mutating_admission_policy",
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

    def __enter__(self) -> "MutatingAdmissionPolicy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingAdmissionPolicyBinding(_kuber_definitions.Resource):
    """
    MutatingAdmissionPolicyBinding binds the
    MutatingAdmissionPolicy with parametrized resources.
    MutatingAdmissionPolicyBinding and the optional parameter
    resource together define how cluster administrators
    configure policies for clusters.

    For a given admission request, each binding will cause its
    policy to be evaluated N times, where N is 1 for
    policies/bindings that don't use params, otherwise N is the
    number of parameters selected by the binding. Each
    evaluation is constrained by a [runtime cost
    budget](https://kubernetes.io/docs/reference/using-
    api/cel/#runtime-cost-budget).

    Adding/removing policies, bindings, or params can not affect
    whether a given (policy, binding, param) combination is
    within its own CEL budget.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["MutatingAdmissionPolicyBindingSpec"] = None,
    ):
        """Create MutatingAdmissionPolicyBinding instance."""
        super(MutatingAdmissionPolicyBinding, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="MutatingAdmissionPolicyBinding",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else MutatingAdmissionPolicyBindingSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (MutatingAdmissionPolicyBindingSpec, None),
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
    def spec(self) -> "MutatingAdmissionPolicyBindingSpec":
        """
        Specification of the desired behavior of the
        MutatingAdmissionPolicyBinding.
        """
        return typing.cast(
            "MutatingAdmissionPolicyBindingSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["MutatingAdmissionPolicyBindingSpec", dict]):
        """
        Specification of the desired behavior of the
        MutatingAdmissionPolicyBinding.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MutatingAdmissionPolicyBindingSpec,
                MutatingAdmissionPolicyBindingSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the MutatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_mutating_admission_policy_binding",
            "create_mutating_admission_policy_binding",
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
        Replaces the MutatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_mutating_admission_policy_binding",
            "replace_mutating_admission_policy_binding",
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
        Patches the MutatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_mutating_admission_policy_binding",
            "patch_mutating_admission_policy_binding",
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
        Reads the MutatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_mutating_admission_policy_binding",
            "read_mutating_admission_policy_binding",
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
        Deletes the MutatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_mutating_admission_policy_binding",
            "delete_mutating_admission_policy_binding",
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

    def __enter__(self) -> "MutatingAdmissionPolicyBinding":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingAdmissionPolicyBindingList(_kuber_definitions.Collection):
    """
    MutatingAdmissionPolicyBindingList is a list of
    MutatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["MutatingAdmissionPolicyBinding"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create MutatingAdmissionPolicyBindingList instance."""
        super(MutatingAdmissionPolicyBindingList, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="MutatingAdmissionPolicyBindingList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, MutatingAdmissionPolicyBinding),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["MutatingAdmissionPolicyBinding"]:
        """
        List of PolicyBinding.
        """
        return typing.cast(
            typing.List["MutatingAdmissionPolicyBinding"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["MutatingAdmissionPolicyBinding"], typing.List[dict]
        ],
    ):
        """
        List of PolicyBinding.
        """
        cleaned: typing.List[MutatingAdmissionPolicyBinding] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MutatingAdmissionPolicyBinding,
                    MutatingAdmissionPolicyBinding().from_dict(item),
                )
            cleaned.append(typing.cast(MutatingAdmissionPolicyBinding, item))
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

    def __enter__(self) -> "MutatingAdmissionPolicyBindingList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingAdmissionPolicyBindingSpec(_kuber_definitions.Definition):
    """
    MutatingAdmissionPolicyBindingSpec is the specification of
    the MutatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        match_resources: typing.Optional["MatchResources"] = None,
        param_ref: typing.Optional["ParamRef"] = None,
        policy_name: typing.Optional[str] = None,
    ):
        """Create MutatingAdmissionPolicyBindingSpec instance."""
        super(MutatingAdmissionPolicyBindingSpec, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="MutatingAdmissionPolicyBindingSpec",
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
        matchResources limits what resources match this binding and
        may be mutated by it. Note that if matchResources matches a
        resource, the resource must also match a policy's
        matchConstraints and matchConditions before the resource may
        be mutated. When matchResources is unset, it does not
        constrain resource matching, and only the policy's
        matchConstraints and matchConditions must match for the
        resource to be mutated. Additionally,
        matchResources.resourceRules are optional and do not
        constraint matching when unset. Note that this is differs
        from MutatingAdmissionPolicy matchConstraints, where
        resourceRules are required. The CREATE, UPDATE and CONNECT
        operations are allowed.  The DELETE operation may not be
        matched. '*' matches CREATE, UPDATE and CONNECT.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchResources"),
        )

    @match_resources.setter
    def match_resources(self, value: typing.Union["MatchResources", dict]):
        """
        matchResources limits what resources match this binding and
        may be mutated by it. Note that if matchResources matches a
        resource, the resource must also match a policy's
        matchConstraints and matchConditions before the resource may
        be mutated. When matchResources is unset, it does not
        constrain resource matching, and only the policy's
        matchConstraints and matchConditions must match for the
        resource to be mutated. Additionally,
        matchResources.resourceRules are optional and do not
        constraint matching when unset. Note that this is differs
        from MutatingAdmissionPolicy matchConstraints, where
        resourceRules are required. The CREATE, UPDATE and CONNECT
        operations are allowed.  The DELETE operation may not be
        matched. '*' matches CREATE, UPDATE and CONNECT.
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
        paramRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in spec.ParamKind of the bound
        MutatingAdmissionPolicy. If the policy specifies a ParamKind
        and the resource referred to by ParamRef does not exist,
        this binding is considered mis-configured and the
        FailurePolicy of the MutatingAdmissionPolicy applied. If the
        policy does not specify a ParamKind then this field is
        ignored, and the rules are evaluated without a param.
        """
        return typing.cast(
            "ParamRef",
            self._properties.get("paramRef"),
        )

    @param_ref.setter
    def param_ref(self, value: typing.Union["ParamRef", dict]):
        """
        paramRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in spec.ParamKind of the bound
        MutatingAdmissionPolicy. If the policy specifies a ParamKind
        and the resource referred to by ParamRef does not exist,
        this binding is considered mis-configured and the
        FailurePolicy of the MutatingAdmissionPolicy applied. If the
        policy does not specify a ParamKind then this field is
        ignored, and the rules are evaluated without a param.
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
        policyName references a MutatingAdmissionPolicy name which
        the MutatingAdmissionPolicyBinding binds to. If the
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
        policyName references a MutatingAdmissionPolicy name which
        the MutatingAdmissionPolicyBinding binds to. If the
        referenced resource does not exist, this binding is
        considered invalid and will be ignored Required.
        """
        self._properties["policyName"] = value

    def __enter__(self) -> "MutatingAdmissionPolicyBindingSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingAdmissionPolicyList(_kuber_definitions.Collection):
    """
    MutatingAdmissionPolicyList is a list of
    MutatingAdmissionPolicy.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["MutatingAdmissionPolicy"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create MutatingAdmissionPolicyList instance."""
        super(MutatingAdmissionPolicyList, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="MutatingAdmissionPolicyList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, MutatingAdmissionPolicy),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["MutatingAdmissionPolicy"]:
        """
        List of ValidatingAdmissionPolicy.
        """
        return typing.cast(
            typing.List["MutatingAdmissionPolicy"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["MutatingAdmissionPolicy"], typing.List[dict]],
    ):
        """
        List of ValidatingAdmissionPolicy.
        """
        cleaned: typing.List[MutatingAdmissionPolicy] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MutatingAdmissionPolicy,
                    MutatingAdmissionPolicy().from_dict(item),
                )
            cleaned.append(typing.cast(MutatingAdmissionPolicy, item))
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

    def __enter__(self) -> "MutatingAdmissionPolicyList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingAdmissionPolicySpec(_kuber_definitions.Definition):
    """
    MutatingAdmissionPolicySpec is the specification of the
    desired behavior of the admission policy.
    """

    def __init__(
        self,
        failure_policy: typing.Optional[str] = None,
        match_conditions: typing.Optional[typing.List["MatchCondition"]] = None,
        match_constraints: typing.Optional["MatchResources"] = None,
        mutations: typing.Optional[typing.List["Mutation"]] = None,
        param_kind: typing.Optional["ParamKind"] = None,
        reinvocation_policy: typing.Optional[str] = None,
        variables: typing.Optional[typing.List["Variable"]] = None,
    ):
        """Create MutatingAdmissionPolicySpec instance."""
        super(MutatingAdmissionPolicySpec, self).__init__(
            api_version="admissionregistration/v1alpha1",
            kind="MutatingAdmissionPolicySpec",
        )
        self._properties = {
            "failurePolicy": failure_policy if failure_policy is not None else "",
            "matchConditions": match_conditions if match_conditions is not None else [],
            "matchConstraints": (
                match_constraints if match_constraints is not None else MatchResources()
            ),
            "mutations": mutations if mutations is not None else [],
            "paramKind": param_kind if param_kind is not None else ParamKind(),
            "reinvocationPolicy": (
                reinvocation_policy if reinvocation_policy is not None else ""
            ),
            "variables": variables if variables is not None else [],
        }
        self._types = {
            "failurePolicy": (str, None),
            "matchConditions": (list, MatchCondition),
            "matchConstraints": (MatchResources, None),
            "mutations": (list, Mutation),
            "paramKind": (ParamKind, None),
            "reinvocationPolicy": (str, None),
            "variables": (list, Variable),
        }

    @property
    def failure_policy(self) -> str:
        """
        failurePolicy defines how to handle failures for the
        admission policy. Failures can occur from CEL expression
        parse errors, type check errors, runtime errors and invalid
        or mis-configured policy definitions or bindings.

        A policy is invalid if paramKind refers to a non-existent
        Kind. A binding is invalid if paramRef.name refers to a non-
        existent resource.

        failurePolicy does not define how validations that evaluate
        to false are handled.

        Allowed values are Ignore or Fail. Defaults to Fail.
        """
        return typing.cast(
            str,
            self._properties.get("failurePolicy"),
        )

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        failurePolicy defines how to handle failures for the
        admission policy. Failures can occur from CEL expression
        parse errors, type check errors, runtime errors and invalid
        or mis-configured policy definitions or bindings.

        A policy is invalid if paramKind refers to a non-existent
        Kind. A binding is invalid if paramRef.name refers to a non-
        existent resource.

        failurePolicy does not define how validations that evaluate
        to false are handled.

        Allowed values are Ignore or Fail. Defaults to Fail.
        """
        self._properties["failurePolicy"] = value

    @property
    def match_conditions(self) -> typing.List["MatchCondition"]:
        """
        matchConditions is a list of conditions that must be met for
        a request to be validated. Match conditions filter requests
        that have already been matched by the matchConstraints. An
        empty list of matchConditions matches all requests. There
        are a maximum of 64 match conditions allowed.

        If a parameter object is provided, it can be accessed via
        the `params` handle in the same manner as validation
        expressions.

        The exact matching logic is (in order):
          1. If ANY matchCondition evaluates to FALSE, the policy is
        skipped.
          2. If ALL matchConditions evaluate to TRUE, the policy is
        evaluated.
          3. If any matchCondition evaluates to an error (but none
        are FALSE):
             - If failurePolicy=Fail, reject the request
             - If failurePolicy=Ignore, the policy is skipped
        """
        return typing.cast(
            typing.List["MatchCondition"],
            self._properties.get("matchConditions"),
        )

    @match_conditions.setter
    def match_conditions(
        self, value: typing.Union[typing.List["MatchCondition"], typing.List[dict]]
    ):
        """
        matchConditions is a list of conditions that must be met for
        a request to be validated. Match conditions filter requests
        that have already been matched by the matchConstraints. An
        empty list of matchConditions matches all requests. There
        are a maximum of 64 match conditions allowed.

        If a parameter object is provided, it can be accessed via
        the `params` handle in the same manner as validation
        expressions.

        The exact matching logic is (in order):
          1. If ANY matchCondition evaluates to FALSE, the policy is
        skipped.
          2. If ALL matchConditions evaluate to TRUE, the policy is
        evaluated.
          3. If any matchCondition evaluates to an error (but none
        are FALSE):
             - If failurePolicy=Fail, reject the request
             - If failurePolicy=Ignore, the policy is skipped
        """
        cleaned: typing.List[MatchCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MatchCondition,
                    MatchCondition().from_dict(item),
                )
            cleaned.append(typing.cast(MatchCondition, item))
        self._properties["matchConditions"] = cleaned

    @property
    def match_constraints(self) -> "MatchResources":
        """
        matchConstraints specifies what resources this policy is
        designed to validate. The MutatingAdmissionPolicy cares
        about a request if it matches _all_ Constraints. However, in
        order to prevent clusters from being put into an unstable
        state that cannot be recovered from via the API
        MutatingAdmissionPolicy cannot match MutatingAdmissionPolicy
        and MutatingAdmissionPolicyBinding. The CREATE, UPDATE and
        CONNECT operations are allowed.  The DELETE operation may
        not be matched. '*' matches CREATE, UPDATE and CONNECT.
        Required.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchConstraints"),
        )

    @match_constraints.setter
    def match_constraints(self, value: typing.Union["MatchResources", dict]):
        """
        matchConstraints specifies what resources this policy is
        designed to validate. The MutatingAdmissionPolicy cares
        about a request if it matches _all_ Constraints. However, in
        order to prevent clusters from being put into an unstable
        state that cannot be recovered from via the API
        MutatingAdmissionPolicy cannot match MutatingAdmissionPolicy
        and MutatingAdmissionPolicyBinding. The CREATE, UPDATE and
        CONNECT operations are allowed.  The DELETE operation may
        not be matched. '*' matches CREATE, UPDATE and CONNECT.
        Required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MatchResources,
                MatchResources().from_dict(value),
            )
        self._properties["matchConstraints"] = value

    @property
    def mutations(self) -> typing.List["Mutation"]:
        """
        mutations contain operations to perform on matching objects.
        mutations may not be empty; a minimum of one mutation is
        required. mutations are evaluated in order, and are
        reinvoked according to the reinvocationPolicy. The mutations
        of a policy are invoked for each binding of this policy and
        reinvocation of mutations occurs on a per binding basis.
        """
        return typing.cast(
            typing.List["Mutation"],
            self._properties.get("mutations"),
        )

    @mutations.setter
    def mutations(
        self, value: typing.Union[typing.List["Mutation"], typing.List[dict]]
    ):
        """
        mutations contain operations to perform on matching objects.
        mutations may not be empty; a minimum of one mutation is
        required. mutations are evaluated in order, and are
        reinvoked according to the reinvocationPolicy. The mutations
        of a policy are invoked for each binding of this policy and
        reinvocation of mutations occurs on a per binding basis.
        """
        cleaned: typing.List[Mutation] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Mutation,
                    Mutation().from_dict(item),
                )
            cleaned.append(typing.cast(Mutation, item))
        self._properties["mutations"] = cleaned

    @property
    def param_kind(self) -> "ParamKind":
        """
        paramKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If paramKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in MutatingAdmissionPolicyBinding, the
        params variable will be null.
        """
        return typing.cast(
            "ParamKind",
            self._properties.get("paramKind"),
        )

    @param_kind.setter
    def param_kind(self, value: typing.Union["ParamKind", dict]):
        """
        paramKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If paramKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in MutatingAdmissionPolicyBinding, the
        params variable will be null.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParamKind,
                ParamKind().from_dict(value),
            )
        self._properties["paramKind"] = value

    @property
    def reinvocation_policy(self) -> str:
        """
        reinvocationPolicy indicates whether mutations may be called
        multiple times per MutatingAdmissionPolicyBinding as part of
        a single admission evaluation. Allowed values are "Never"
        and "IfNeeded".

        Never: These mutations will not be called more than once per
        binding in a single admission evaluation.

        IfNeeded: These mutations may be invoked more than once per
        binding for a single admission request and there is no
        guarantee of order with respect to other admission plugins,
        admission webhooks, bindings of this policy and admission
        policies.  Mutations are only reinvoked when mutations
        change the object after this mutation is invoked. Required.
        """
        return typing.cast(
            str,
            self._properties.get("reinvocationPolicy"),
        )

    @reinvocation_policy.setter
    def reinvocation_policy(self, value: str):
        """
        reinvocationPolicy indicates whether mutations may be called
        multiple times per MutatingAdmissionPolicyBinding as part of
        a single admission evaluation. Allowed values are "Never"
        and "IfNeeded".

        Never: These mutations will not be called more than once per
        binding in a single admission evaluation.

        IfNeeded: These mutations may be invoked more than once per
        binding for a single admission request and there is no
        guarantee of order with respect to other admission plugins,
        admission webhooks, bindings of this policy and admission
        policies.  Mutations are only reinvoked when mutations
        change the object after this mutation is invoked. Required.
        """
        self._properties["reinvocationPolicy"] = value

    @property
    def variables(self) -> typing.List["Variable"]:
        """
        variables contain definitions of variables that can be used
        in composition of other expressions. Each variable is
        defined as a named CEL expression. The variables defined
        here will be available under `variables` in other
        expressions of the policy except matchConditions because
        matchConditions are evaluated before the rest of the policy.

        The expression of a variable can refer to other variables
        defined earlier in the list but not those after. Thus,
        variables must be sorted by the order of first appearance
        and acyclic.
        """
        return typing.cast(
            typing.List["Variable"],
            self._properties.get("variables"),
        )

    @variables.setter
    def variables(
        self, value: typing.Union[typing.List["Variable"], typing.List[dict]]
    ):
        """
        variables contain definitions of variables that can be used
        in composition of other expressions. Each variable is
        defined as a named CEL expression. The variables defined
        here will be available under `variables` in other
        expressions of the policy except matchConditions because
        matchConditions are evaluated before the rest of the policy.

        The expression of a variable can refer to other variables
        defined earlier in the list but not those after. Thus,
        variables must be sorted by the order of first appearance
        and acyclic.
        """
        cleaned: typing.List[Variable] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Variable,
                    Variable().from_dict(item),
                )
            cleaned.append(typing.cast(Variable, item))
        self._properties["variables"] = cleaned

    def __enter__(self) -> "MutatingAdmissionPolicySpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Mutation(_kuber_definitions.Definition):
    """
    Mutation specifies the CEL expression which is used to apply
    the Mutation.
    """

    def __init__(
        self,
        apply_configuration: typing.Optional["ApplyConfiguration"] = None,
        json_patch: typing.Optional["JSONPatch"] = None,
        patch_type: typing.Optional[str] = None,
    ):
        """Create Mutation instance."""
        super(Mutation, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="Mutation"
        )
        self._properties = {
            "applyConfiguration": (
                apply_configuration
                if apply_configuration is not None
                else ApplyConfiguration()
            ),
            "jsonPatch": json_patch if json_patch is not None else JSONPatch(),
            "patchType": patch_type if patch_type is not None else "",
        }
        self._types = {
            "applyConfiguration": (ApplyConfiguration, None),
            "jsonPatch": (JSONPatch, None),
            "patchType": (str, None),
        }

    @property
    def apply_configuration(self) -> "ApplyConfiguration":
        """
        applyConfiguration defines the desired configuration values
        of an object. The configuration is applied to the admission
        object using [structured merge
        diff](https://github.com/kubernetes-sigs/structured-merge-
        diff). A CEL expression is used to create apply
        configuration.
        """
        return typing.cast(
            "ApplyConfiguration",
            self._properties.get("applyConfiguration"),
        )

    @apply_configuration.setter
    def apply_configuration(self, value: typing.Union["ApplyConfiguration", dict]):
        """
        applyConfiguration defines the desired configuration values
        of an object. The configuration is applied to the admission
        object using [structured merge
        diff](https://github.com/kubernetes-sigs/structured-merge-
        diff). A CEL expression is used to create apply
        configuration.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ApplyConfiguration,
                ApplyConfiguration().from_dict(value),
            )
        self._properties["applyConfiguration"] = value

    @property
    def json_patch(self) -> "JSONPatch":
        """
        jsonPatch defines a [JSON patch](https://jsonpatch.com/)
        operation to perform a mutation to the object. A CEL
        expression is used to create the JSON patch.
        """
        return typing.cast(
            "JSONPatch",
            self._properties.get("jsonPatch"),
        )

    @json_patch.setter
    def json_patch(self, value: typing.Union["JSONPatch", dict]):
        """
        jsonPatch defines a [JSON patch](https://jsonpatch.com/)
        operation to perform a mutation to the object. A CEL
        expression is used to create the JSON patch.
        """
        if isinstance(value, dict):
            value = typing.cast(
                JSONPatch,
                JSONPatch().from_dict(value),
            )
        self._properties["jsonPatch"] = value

    @property
    def patch_type(self) -> str:
        """
        patchType indicates the patch strategy used. Allowed values
        are "ApplyConfiguration" and "JSONPatch". Required.
        """
        return typing.cast(
            str,
            self._properties.get("patchType"),
        )

    @patch_type.setter
    def patch_type(self, value: str):
        """
        patchType indicates the patch strategy used. Allowed values
        are "ApplyConfiguration" and "JSONPatch". Required.
        """
        self._properties["patchType"] = value

    def __enter__(self) -> "Mutation":
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
    ParamRef describes how to locate the params to be used as
    input to expressions of rules applied by a policy binding.
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        parameter_not_found_action: typing.Optional[str] = None,
        selector: typing.Optional["LabelSelector"] = None,
    ):
        """Create ParamRef instance."""
        super(ParamRef, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="ParamRef"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "parameterNotFoundAction": (
                parameter_not_found_action
                if parameter_not_found_action is not None
                else ""
            ),
            "selector": selector if selector is not None else LabelSelector(),
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
            "parameterNotFoundAction": (str, None),
            "selector": (LabelSelector, None),
        }

    @property
    def name(self) -> str:
        """
        `name` is the name of the resource being referenced.

        `name` and `selector` are mutually exclusive properties. If
        one is set, the other must be unset.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of the resource being referenced.

        `name` and `selector` are mutually exclusive properties. If
        one is set, the other must be unset.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        namespace is the namespace of the referenced resource.
        Allows limiting the search for params to a specific
        namespace. Applies to both `name` and `selector` fields.

        A per-namespace parameter may be used by specifying a
        namespace-scoped `paramKind` in the policy and leaving this
        field empty.

        - If `paramKind` is cluster-scoped, this field MUST be
        unset. Setting this field results in a configuration error.

        - If `paramKind` is namespace-scoped, the namespace of the
        object being evaluated for admission will be used when this
        field is left unset. Take care that if this is left empty
        the binding must not match any cluster-scoped resources,
        which will result in an error.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        namespace is the namespace of the referenced resource.
        Allows limiting the search for params to a specific
        namespace. Applies to both `name` and `selector` fields.

        A per-namespace parameter may be used by specifying a
        namespace-scoped `paramKind` in the policy and leaving this
        field empty.

        - If `paramKind` is cluster-scoped, this field MUST be
        unset. Setting this field results in a configuration error.

        - If `paramKind` is namespace-scoped, the namespace of the
        object being evaluated for admission will be used when this
        field is left unset. Take care that if this is left empty
        the binding must not match any cluster-scoped resources,
        which will result in an error.
        """
        self._properties["namespace"] = value

    @property
    def parameter_not_found_action(self) -> str:
        """
        `parameterNotFoundAction` controls the behavior of the
        binding when the resource exists, and name or selector is
        valid, but there are no parameters matched by the binding.
        If the value is set to `Allow`, then no matched parameters
        will be treated as successful validation by the binding. If
        set to `Deny`, then no matched parameters will be subject to
        the `failurePolicy` of the policy.

        Allowed values are `Allow` or `Deny` Default to `Deny`
        """
        return typing.cast(
            str,
            self._properties.get("parameterNotFoundAction"),
        )

    @parameter_not_found_action.setter
    def parameter_not_found_action(self, value: str):
        """
        `parameterNotFoundAction` controls the behavior of the
        binding when the resource exists, and name or selector is
        valid, but there are no parameters matched by the binding.
        If the value is set to `Allow`, then no matched parameters
        will be treated as successful validation by the binding. If
        set to `Deny`, then no matched parameters will be subject to
        the `failurePolicy` of the policy.

        Allowed values are `Allow` or `Deny` Default to `Deny`
        """
        self._properties["parameterNotFoundAction"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector can be used to match multiple param objects based
        on their labels. Supply selector: {} to match all resources
        of the ParamKind.

        If multiple params are found, they are all evaluated with
        the policy expressions and the results are ANDed together.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector can be used to match multiple param objects based
        on their labels. Supply selector: {} to match all resources
        of the ParamKind.

        If multiple params are found, they are all evaluated with
        the policy expressions and the results are ANDed together.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    def __enter__(self) -> "ParamRef":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Variable(_kuber_definitions.Definition):
    """
    Variable is the definition of a variable that is used for
    composition.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create Variable instance."""
        super(Variable, self).__init__(
            api_version="admissionregistration/v1alpha1", kind="Variable"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "name": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression is the expression that will be evaluated as the
        value of the variable. The CEL expression has access to the
        same identifiers as the CEL expressions in Validation.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression is the expression that will be evaluated as the
        value of the variable. The CEL expression has access to the
        same identifiers as the CEL expressions in Validation.
        """
        self._properties["expression"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of the variable. The name must be a valid
        CEL identifier and unique among all variables. The variable
        can be accessed in other expressions through `variables` For
        example, if name is "foo", the variable will be available as
        `variables.foo`
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the variable. The name must be a valid
        CEL identifier and unique among all variables. The variable
        can be accessed in other expressions through `variables` For
        example, if name is "foo", the variable will be available as
        `variables.foo`
        """
        self._properties["name"] = value

    def __enter__(self) -> "Variable":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

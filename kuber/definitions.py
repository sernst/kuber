import abc
import json
import pathlib
import typing
import uuid

import yaml
from kubernetes import client

PathLike = typing.Union[str, pathlib.Path]
OptionalPathLike = typing.Optional[PathLike]

API_VERSION_REMAPS = {"core/v1": "v1"}


# Protocol was added in 3.8 and needs to be gracefully handled for now
# without the Protocol class for static duck-typing. Eventually this
# should be replaced by:
# class ExecutionResponse(typing.Protocol):
class ExecutionResponse:
    """Structural type for kubernetes execution responses."""

    @property
    def status(self) -> "Definition":
        """Status from an execution response."""
        pass


class InternalValue(typing.NamedTuple):
    """
    Data structure that can be used for internal value states that help manage
    the state of user input versus internally set values.
    """

    #: Unique identifier for the internal value.
    name: str
    #: A brief description for the purpose of the internal value.
    description: str


#: Uniquely identifying value that can be used to represent a state where the
#: user has not modified the value. Useful in cases where `None` could
#: represent a significant change.
UNCHANGED_VALUE = InternalValue(
    name="UnchangedValue", description="No change is being made to this value."
)


class Definition:
    """Base class for all kubernetes definition objects."""

    def __init__(self, api_version: str, kind: str):
        """Initialize basic common properties"""
        self._api_version = api_version
        self._kind = kind
        self._properties: typing.Dict[str, typing.Any] = {}
        self._types: typing.Dict[str, typing.Any] = {}
        self._kuber_uid = str(uuid.uuid4())

    @property
    def kuber_uid(self) -> str:
        """Internal UID used to uniquely identify this object."""
        return self._kuber_uid

    def to_dict(self) -> typing.Optional[dict]:
        """
        Serializes the `Definition` object to a dictionary that can be
        rendered into json or yaml configuration file formats.
        """
        results = {
            p: serialize_property(v)
            for p, v in self._properties.items()
            if p in self._types
        }
        results = {
            p: v for p, v in results.items() if v or isinstance(v, bool) or v == 0
        }
        return results if results else None

    def from_dict(self, source: dict) -> "Definition":
        """Populates the resource from the source dictionary definition."""
        lower_keys = {k.lower(): k for k in self._types.keys()}
        for key, value in source.items():
            camel_key = to_camel_case(key)
            if key in self._types:
                prop_key = key
            elif camel_key in self._types:
                prop_key = camel_key
            elif camel_key.lower() in lower_keys:
                prop_key = lower_keys[camel_key.lower()]
            else:  # pragma: no cover
                continue

            self._properties[prop_key] = deserialize_property(
                value=value, data_type=self._types[prop_key]
            )

        return self


class Collection(Definition):
    """
    Base class for all kubernetes collection resources, which are synthetic
    resources that bundle together multiple standard resources.
    """

    def __init__(self, api_version: str, kind: str):
        """Initialize basic common properties."""
        super(Collection, self).__init__(api_version, kind)

    @property
    def metadata(self):
        """Must be implemented by subclasses"""
        return

    @metadata.setter
    def metadata(self, value):
        """Must be implemented by subclasses"""
        pass

    @property
    def api_version(self) -> str:
        """The Kubernetes API version in which the resource resides."""
        return self._api_version

    @property
    def kind(self) -> str:
        """Resource type identifier."""
        return self._kind

    def to_dict(self) -> dict:
        """
        Serializes the `Resource` object to a dictionary that can be
        rendered into json or yaml configuration file formats.
        """
        results = super(Collection, self).to_dict() or {}
        version = API_VERSION_REMAPS.get(self.api_version, self.api_version)
        return {"apiVersion": version, "kind": self.kind, **results}

    def to_json(self) -> str:
        """
        Serializes the `Resource` object to a json string that can be
        saved as a configuration file or used with other packages that
        interact with the Kubernetes API.
        """
        return json.dumps(self.to_dict(), indent=2)

    def to_yaml(self) -> str:
        """
        Serializes the `Resource` object to a yaml string that can be
        saved as a configuration file or used with other packages that
        interact with the Kubernetes API.
        """
        return yaml.dump(self.to_dict(), default_flow_style=False)

    @staticmethod
    @abc.abstractmethod
    def get_resource_api(api_client: client.ApiClient = None, **kwargs) -> typing.Any:
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        ...  # pragma: no cover


class Resource(Definition):
    """
    Base class for all kubernetes resource definition objects. All entities
    in the Kubernetes APIs are Definitions, but Resources are the top-level
    entities that have the standard `apiVersion`, `kind`, and `metadata`
    elements.
    """

    def __init__(self, api_version: str, kind: str):
        """Initialize basic common properties."""
        super(Resource, self).__init__(api_version, kind)

    @property
    def metadata(self):
        """Must be implemented by subclasses"""
        return

    @metadata.setter
    def metadata(self, value):
        """Must be implemented by subclasses"""
        pass

    @property
    def api_version(self) -> str:
        """The Kubernetes API version in which the resource resides."""
        return self._api_version

    @property
    def kind(self) -> str:
        """Resource type identifier."""
        return self._kind

    def to_dict(self) -> dict:
        """
        Serializes the `Resource` object to a dictionary that can be
        rendered into json or yaml configuration file formats.
        """
        results = super(Resource, self).to_dict() or {}
        version = API_VERSION_REMAPS.get(self.api_version, self.api_version)
        return {"apiVersion": version, "kind": self.kind, **results}

    def to_json(self) -> str:
        """
        Serializes the `Resource` object to a json string that can be
        saved as a configuration file or used with other packages that
        interact with the Kubernetes API.
        """
        return json.dumps(self.to_dict(), indent=2)

    def to_yaml(self) -> str:
        """
        Serializes the `Resource` object to a yaml string that can be
        saved as a configuration file or used with other packages that
        interact with the Kubernetes API.
        """
        return yaml.dump(self.to_dict(), default_flow_style=False)

    @abc.abstractmethod
    def create_resource(self, namespace: str = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @abc.abstractmethod
    def replace_resource(self, namespace: "str" = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @abc.abstractmethod
    def patch_resource(self, namespace: "str" = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @abc.abstractmethod
    def get_resource_status(self, namespace: str = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @abc.abstractmethod
    def delete_resource(self, namespace: str = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @abc.abstractmethod
    def read_resource(self, namespace: str = None):
        """Must be implemented by subclasses."""
        pass  # pragma: no cover

    @staticmethod
    @abc.abstractmethod
    def get_resource_api(api_client: client.ApiClient = None, **kwargs) -> typing.Any:
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        pass  # pragma: no cover


def serialize_property(value: typing.Any) -> typing.Any:
    """
    Converts a Definition property value into one compatible with the json
    and yaml configuration formats. Basic types are returned without any
    conversion, but Definition objects are converted to their dictionary
    representation and lists of non-basic types are converted down as well.

    :param value:
        Property value to be serialized for configuration file format
        compatibility.
    :return:
        Serialized version of the supplied value.
    """
    # Some falsy cases are meaningful and should be preserved.
    nulls: typing.Tuple[None, dict, list] = (None, {}, [])

    if hasattr(value, "to_dict"):
        return value.to_dict() or None

    if isinstance(value, (list, tuple)):
        raw_values = [serialize_property(v) for v in value]
        return [v for v in raw_values if v not in nulls] or None

    if isinstance(value, dict):
        raw_items = {k: serialize_property(v) for k, v in value.items()}
        return {k: v for k, v in raw_items.items() if v not in nulls} or None

    return None if value in nulls else value


def deserialize_property(value: typing.Any, data_type: tuple) -> typing.Any:
    """
    Converts the serialized configuration value into the given kuber data type.
    All Definition objects store data types internally to allow for easily
    mapping from serialized values during the loading of configuration file
    data.

    :param value:
        Serialized configuration value to be converted into the given data
        type.
    :param data_type:
        kuber data type to deserialize the given value into.
    :return:
        Deserialized form of the specified value.
    """
    if value is None:
        return None

    if issubclass(data_type[0], Definition):
        return data_type[0]().from_dict(value)

    if data_type[0] == list:
        return [deserialize_property(v, (data_type[1], None)) for v in value]

    return data_type[0](value)


def to_camel_case(source: str) -> str:
    """Converts kebab-case or snake_case to camelCase."""
    parts = source.replace("-", "_").split("_")
    return "".join([parts[0], *[p.capitalize() for p in parts[1:]]])

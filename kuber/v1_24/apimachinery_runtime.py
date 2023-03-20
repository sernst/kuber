import typing  # noqa: F401

from kubernetes import client  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401


class RawExtension(_kuber_definitions.Definition):
    """
    RawExtension is used to hold extensions in external
    versions.

    To use this, make a field which has RawExtension as its type
    in your external, versioned struct, and Object in your
    internal struct. You also need to register your various
    plugin types.

    // Internal package:

        type MyAPIObject struct {
                runtime.TypeMeta `json:",inline"`
                MyPlugin runtime.Object `json:"myPlugin"`
        }

        type PluginA struct {
                AOption string `json:"aOption"`
        }

    // External package:

        type MyAPIObject struct {
                runtime.TypeMeta `json:",inline"`
                MyPlugin runtime.RawExtension `json:"myPlugin"`
        }

        type PluginA struct {
                AOption string `json:"aOption"`
        }

    // On the wire, the JSON will look something like this:

        {
                "kind":"MyAPIObject",
                "apiVersion":"v1",
                "myPlugin": {
                        "kind":"PluginA",
                        "aOption":"foo",
                },
        }

    So what happens? Decode first uses json or yaml to unmarshal
    the serialized data into your external MyAPIObject. That
    causes the raw JSON to be stored, but not unpacked. The next
    step is to copy (using pkg/conversion) into the internal
    struct. The runtime package's DefaultScheme has conversion
    functions installed which will unpack the JSON stored in
    RawExtension, turning it into the correct object type, and
    storing it in the Object. (TODO: In the case where the
    object is of an unknown type, a runtime.Unknown object will
    be created and stored.)
    """

    def __init__(
        self,
    ):
        """Create RawExtension instance."""
        super(RawExtension, self).__init__(
            api_version="apimachinery/runtime", kind="RawExtension"
        )
        self._properties = {}
        self._types = {}

    def __enter__(self) -> "RawExtension":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

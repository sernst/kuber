import copy
import glob
import json
import os
import pathlib
import typing

import yaml

import kuber
from kuber import management


class ResourceBundleSettings:
    """
    A class that serves as a container for storing user-configured settings
    data that can be used in configuring the bundle.
    """

    def __init__(self, bundle: "management.ResourceBundle"):
        self._data: typing.Dict[typing.Any, typing.Any] = {}
        self._bundle = bundle

    def add(self, **kwargs) -> "ResourceBundleSettings":
        """
        Adds one or more variables to the settings object.

        :param kwargs:
            Keyword arguments to be added to the settings, which are name value
            pairs like standard keyword named arguments in Python. For example:

            ```
            put(a=1, b=False)
            ```

            would add two variables to the settings where the value of ``a``
            would be ``1`` and the value of ``b`` would be ``False``.
        """
        for key, value in kwargs.items():
            if value is None and key in self._data:
                del self._data[key]
            else:
                self._data[key] = value
        return self

    def add_from_file(self, path: "kuber.PathLike") -> "ResourceBundleSettings":
        """
        Loads, parses and adds the values from the given file path to
        the settings object.

        :param path:
            Path to the settings file to load.
        """
        p = pathlib.Path(path).expanduser().absolute()
        contents = p.read_text()

        if p.name.endswith((".yml", ".yaml")):
            return self.add(**yaml.load(contents, Loader=kuber.yaml_loader))

        if p.name.endswith(".json"):
            return self.add(**json.loads(contents))

        raise IOError(
            f'Unrecognized file format for path "{p}". '
            "Filenames should end with .yml, .yaml or .json."
        )

    def add_from_directory(
        self,
        directory: "kuber.PathLike",
        recursive: bool = False,
        ignores: typing.Optional[typing.List[str]] = None,
    ) -> "ResourceBundleSettings":
        """
        Adds all settings files (YAML and JSON) from the specified
        directory.

        :param directory:
            Directory in which to add settings files.
        :param recursive:
            Whether or not to include configuration files in subdirectories
            as well.
        :param ignores:
            Filenames to ignore when loading settings files.
        """
        glob_path = pathlib.Path(directory).expanduser().absolute()
        if recursive:
            glob_path = glob_path.joinpath("**")
        glob_path = glob_path.joinpath("*")
        paths = [
            path
            for path in glob.iglob(str(glob_path), recursive=recursive)
            if path.endswith((".yml", ".yaml", ".json"))
            and os.path.isfile(path)
            and os.path.basename(path) not in (ignores or [])
        ]

        for path in paths:
            self.add_from_file(path)
        return self

    def grab(self, *keys: str, default_value=None) -> typing.Tuple:
        """
        Returns a tuple containing multiple values from the settings specified
        by the keys arguments.

        :param keys:
            One or more variable names stored in the settings that should be
            returned by the grab function. The order of these arguments are
            preserved by the returned tuple.
        :param default_value:
            If one or more of the keys is not found, this value will be
            returned as the missing value.
        :return:
            A tuple containing values for each of the keys specified in the
            arguments.
        """
        return tuple([self.fetch(k, default_value) for k in keys])

    def fetch(self, key: str, default_value=None):
        """
        Retrieves the value of the specified variable from the settings.

        :param key:
            The name of the variable for which the value should be returned.
        :param default_value:
            The value to return if the variable does not exist.
        :return:
            The value of the specified key if it exists or the
            default_Value if it does not.
        """
        return self._data.get(key, default_value)

    def keys(self) -> typing.Iterable:
        """An iterable for all keys store in the settings object."""
        return self._data.keys()

    def values(self) -> typing.Iterable:
        """An iterable for all values stored in the settings object."""
        return self._data.values()

    def items(self) -> typing.Iterable:
        """An iterable for all key/value pairs found in the settings object."""
        return self._data.items()

    def to_dict(self) -> dict:
        """Returns the settings data serialized to dictionary format."""
        try:
            return copy.deepcopy(self._data)
        except Exception:
            return copy.copy(self._data)

    def to_yaml(self) -> str:
        """Renders the settings object as a YAML string."""
        return yaml.dump(self._data, default_flow_style=False)

    def __getitem__(self, item):
        return self._data.get(item)

    def __getattr__(self, item):
        return self._data.get(item)

    def __setitem__(self, key, value):
        self._data[key] = value

    def __setattr__(self, key, value):
        if key.startswith("_"):
            super(ResourceBundleSettings, self).__setattr__(key, value)
        else:
            self._data[key] = value

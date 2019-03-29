import glob
import importlib
import json
import os
import typing
import uuid

import yaml

from kuber import cli
from kuber.definitions import Resource


class ResourceBundle:
    """Contains one or more related Kubernetes `Resource` objects."""

    def __init__(self, bundle_name: str = None, version: str = None):
        """
        Initializes the bundle.

        :param bundle_name:
            Name of the bundle. If not specified, a randomized name will be
            created instead.
        :param version:
            Kubernetes version to use when loading and interacting with
            objects inside the bundle.
        """
        self.name = bundle_name or str(uuid.uuid4())
        self.version = version or get_latest_version()
        self._resources: typing.List['Resource'] = []
        self._cli = cli.ResourceBundleCli(self)

    @property
    def cli(self) -> 'cli.ResourceBundleCli':
        """Command line interface for the bundle."""
        return self._cli

    @property
    def resources(self) -> typing.Tuple['Resource']:
        """Resources stored within the bundle."""
        return tuple(self._resources)

    def get(
            self,
            name: str = None,
            kind: str = None,
            **kwargs
    ) -> typing.Optional['Resource']:
        """
        Fetches the resource in the bundle that best and first matches the
        given properties using name, kind and optional labels to select the
        desired resource.

        :param name:
            Name of the resource to return.
        :param kind:
            Kubernetes kind of the resource to return, e.g. 'Deployment'.
        :param kwargs:
            Optionally specify metadata labels to use when selecting the
            resource to return.
        """
        for r in self.resources:
            match = (
                (kind is None or r.kind != kind)
                and (name is None or getattr(r, 'metadata').name == name)
            )
            labels = {
                key: value
                for key, value in getattr(r, 'metadata').labels.items()
                if key in kwargs and kwargs[key] == value
            }
            if match and len(kwargs) == len(labels):
                return r
        return None

    def pop(
            self,
            name: str = None,
            kind: str = None,
            **kwargs
    ) -> typing.Optional['Resource']:
        """
        Removes the resource matching the specified arguments from the bundle
        if it exists and returns it.

        :param name:
            Name of the resource to remove from the bundle.
        :param kind:
            Kubernetes kind of the resource to remove, e.g. 'Deployment'.
        :param kwargs:
            Optionally specify metadata labels to use when selecting the
            resource to remove from the bundle.
        """
        resource = self.get(name, kind, **kwargs)
        if resource:
            self._resources.remove(resource)
        return resource

    def push(self, resource: 'Resource') -> 'ResourceBundle':
        """
        Adds the specified resource to the end of the bundle's
        resource list.

        :param resource:
            Resource object to add to the bundle. It will be conformed to
            the bundle's specifications and constraints upon insertion.
        """
        if resource not in self._resources:
            self._resources.append(self._conform_resource(resource))
        return self

    def unshift(self, resource: 'Resource') -> 'ResourceBundle':
        """
        Adds the specified resource to the beginning of the bundle's
        resource list.

        :param resource:
            Resource object to add to the bundle. It will be conformed to
            the bundle's specifications and constraints upon insertion.
        """
        if resource not in self._resources:
            self._resources.insert(0, self._conform_resource(resource))
        return self

    def add_from_yaml(self, resource_definition: str) -> 'ResourceBundle':
        """
        Adds a Resource object to the bundle from the YAML definition
        string.

        :param resource_definition:
            A string containing a valid Kubernetes resource configuration.
        """
        self.push(from_yaml(self.version, resource_definition))
        return self

    def add_file(self, path: str) -> 'ResourceBundle':
        """
        Loads, parses and adds the Resource object from the given
        configuration file path.

        :param path:
            Path to the configuration file to load as a Resource into the
            bundle.
        """
        if path.endswith(('.yml', '.yaml')):
            self.push(from_yaml_file(self.version, os.path.realpath(path)))
        elif path.endswith('.json'):
            self.push(from_json_file(self.version, os.path.realpath(path)))
        else:
            raise IOError(
                f'Unrecognized file format for path "{path}". '
                'Filenames should end with .yml, .yaml or .json.'
            )
        return self

    def add_directory(
            self,
            directory: str,
            recursive: bool = False,
            ignores: typing.List[str] = None
    ) -> 'ResourceBundle':
        """
        Adds all configuration files (YAML and JSON) in the specified
        directory.

        :param directory:
            Directory in which to add configuration files.
        :param recursive:
            Whether or not to include configuration files in subdirectories
            as well.
        :param ignores:
            Filenames to ignore when loading configuration files.
        """
        extensions = ('.yml', '.yaml', '.json')
        parts = [directory, '**' if recursive else None, '*']
        glob_path = os.path.realpath(os.path.join(*[p for p in parts if p]))
        paths = [
            path
            for path in glob.iglob(glob_path, recursive=recursive)
            if path.endswith(extensions)
            and os.path.isfile(path)
            and os.path.basename(path) not in (ignores or [])
        ]

        for path in paths:
            self.add_file(path)
        return self

    def render_yaml(self) -> typing.List[str]:
        """Serialies the bundle resources to a list of YAML strings."""
        return [self._conform_resource(r).to_yaml() for r in self.resources]

    def render_yaml_bundle(self) -> str:
        """Serializes the bundle resources to a single YAML config."""
        return '\n---\n\n'.join(self.render_yaml())

    def render_json(self) -> typing.List[str]:
        """Serializes the bundle to a list of JSON configurations."""
        return [self._conform_resource(r).to_json() for r in self.resources]

    def _conform_resource(self, resource: 'Resource') -> 'Resource':
        """
        A method that allows for modifying resources when they are added to
        the bundle or serialized to confirm that they adhere to the
        expectations of the bundle object.

        :param resource:
            Resource object to conform to the specifications and constraints
            of the bundle.
        """
        return resource

    def create(self, namespace: str = None) -> dict:
        """
        Create all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to create resources
            that do not have an explicit namespace specified.
        """
        return {
            r.metadata.name: r.create_resource(namespace)
            for r in self.resources
        }

    def replace(self, namespace: str = None) -> dict:
        """
        Replace all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to replace resources
            that do not have an explicit namespace specified.
        """
        return {
            r.metadata.name: r.replace_resource(namespace)
            for r in self.resources
        }

    def statuses(
            self,
            namespace: str = None
    ) -> typing.Dict['Resource', typing.Any]:
        """
        Returns a dictionary of statuses for all resources in the bundle,
        where the keys are the resources and the values are their associated
        status objects.

        :param namespace:
            Optionally specify the namespace where the resources reside.
        """
        return {
            r: r.replace_resource(namespace)
            for r in self.resources
        }

    def delete(self, namespace: str = None) -> bool:
        """
        Delete all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to delete the resource.
        """
        return all([r.delete_resource(namespace) for r in self.resources])


def from_yaml_file(
        kubernetes_version: str,
        file_path: str
) -> typing.Optional[Resource]:
    """
    Creates a Resource object from a YAML configuration file.

    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource.
    :param file_path:
        Path to the kubernetes resource configuration YAML file to be
        loaded.
    """
    with open(file_path) as f:
        return from_yaml(kubernetes_version, f.read())


def from_yaml(
        kubernetes_version: str,
        resource_definition: str
) -> typing.Optional[Resource]:
    """
    Creates a Resource object from a YAML string.

    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource.
    :param resource_definition:
        String containing the contents of a yaml resource definition.
    """
    data = yaml.load(resource_definition, Loader=yaml.CLoader)
    return from_dict(kubernetes_version, data)


def from_dict(
        kubernetes_version: str,
        resource_definition: dict
) -> typing.Optional[Resource]:
    """
    Converts a dictionary into a Resource object.

    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource.
    :param resource_definition:
        Definition dictionary object to deserialize.
    """
    version = kubernetes_version.replace('.', '_')
    group, area = resource_definition['apiVersion'].split('/')[:2]
    package = '.'.join(['kuber', f'v{version}', group, area])

    loaded_module = importlib.import_module(package)
    resource_class = getattr(loaded_module, resource_definition['kind'])
    resource: Resource = resource_class()
    return resource.from_dict(resource_definition)


def from_json_file(kubernetes_version: str, file_path: str) -> Resource:
    """
    Creates a Resource object from a configuration file.

    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource.
    :param file_path:
        Path to a JSON or YAML file that specifies the resource to create.
    """
    with open(file_path) as f:
        return from_dict(kubernetes_version, json.load(f))


def get_latest_version() -> str:
    """Determines the latest available kubernetes version within the library."""
    directory = os.path.realpath(os.path.dirname(__file__))
    entries = [
        f[1:].split('_')
        for f in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, f)) and f.startswith('v')
    ]

    entries.sort(key=lambda x: 10000 * int(x[0]) + int(x[1]))
    return '.'.join(entries[-1])

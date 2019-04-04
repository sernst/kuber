import datetime
import glob
import importlib
import json
import os
import typing
import uuid

import yaml

import kuber
from kuber import cli
from kuber import versioning as _versioning
from kuber.definitions import Resource

ResourceSubclass = typing.Union[Resource, typing.Any]


class ResourceBundle:
    """Contains one or more related Kubernetes `Resource` objects."""

    def __init__(
            self,
            bundle_name: str = None,
            kubernetes_version: 'kuber.VersionLabel' = 'latest'
    ):
        """
        Initializes the bundle.

        :param bundle_name:
            Name of the bundle. If not specified, a randomized name will be
            created instead.
        :param kubernetes_version:
            Kubernetes version to use when loading and interacting with
            resource objects inside the bundle. By default this will use the
            latest stable Kubernetes version available within the library.
        """
        self.name = bundle_name or str(uuid.uuid4())
        self._version = kubernetes_version
        self._resources: typing.List[ResourceSubclass] = []
        self._cli = cli.ResourceBundleCli(self)

    @property
    def kubernetes_version(self) -> '_versioning.KubernetesVersion':
        """
        Version of the kubernetes library to use when creating resources
        inside this bundle.
        """
        if isinstance(self._version, _versioning.KubernetesVersion):
            return self._version
        return _versioning.get_version_data(self._version or 'latest')

    @property
    def cli(self) -> 'cli.ResourceBundleCli':
        """Command line interface for the bundle."""
        return self._cli

    @property
    def resources(self) -> typing.Tuple[ResourceSubclass]:
        """Resources stored within the bundle."""
        return tuple(self._resources)

    def get(
            self,
            name: str = None,
            kind: str = None,
            **kwargs
    ) -> typing.Optional[ResourceSubclass]:
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
    ) -> typing.Optional[ResourceSubclass]:
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

    def add(
            self,
            api_version: str,
            kind: str,
            name: str,
            **kwargs
    ) -> 'ResourceBundle':
        """
        Adds an empty resource of the specified type.

        :param api_version:
            A standard Kubernetes configuration api version, e.g. "apps/v1".
        :param kind:
            The type of resource, e.g. "Deployment".
        :param name:
            Name to give the resource.
        :param kwargs:
            Labels to assign to the metadata of the new resource.
        """
        definition = {
            'apiVersion': api_version,
            'kind': kind,
            'metadata': {'name': name, 'labels': kwargs}
        }
        return self.push(from_dict(definition, self.kubernetes_version))

    def add_from_yaml(self, resource_definition: str) -> 'ResourceBundle':
        """
        Adds a Resource object to the bundle from the YAML definition
        string.

        :param resource_definition:
            A string containing a valid Kubernetes resource configuration.
        """
        self.push(from_yaml(resource_definition, self.kubernetes_version))
        return self

    def add_file(self, path: str) -> 'ResourceBundle':
        """
        Loads, parses and adds the Resource object from the given
        configuration file path.

        :param path:
            Path to the configuration file to load as a Resource into the
            bundle.
        """
        version = self.kubernetes_version
        if path.endswith(('.yml', '.yaml')):
            self.push(from_yaml_file(os.path.realpath(path), version))
        elif path.endswith('.json'):
            self.push(from_json_file(os.path.realpath(path), version))
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

    def _conform_resource(self, resource: 'Resource') -> ResourceSubclass:
        """
        A method that allows for modifying resources when they are added to
        the bundle or serialized to confirm that they adhere to the
        expectations of the bundle object.

        :param resource:
            Resource object to conform to the specifications and constraints
            of the bundle.
        """
        version = self.kubernetes_version
        resource.metadata.labels.update(
            kuber_library_version=kuber.__version__,
            kuber_api_version=version.label,
            kuber_kube_version=version.version,
            kuber_bundle_name=self.name,
            kuber_timestamp=f'{datetime.datetime.utcnow().isoformat()}Z'
        )
        return resource

    def create(self, namespace: str = None) -> list:
        """
        Create all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to create resources
            that do not have an explicit namespace specified.
        """
        return [r.create_resource(namespace) for r in self.resources]

    def replace(self, namespace: str = None) -> list:
        """
        Replace all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to replace resources
            that do not have an explicit namespace specified.
        """
        return [r.replace_resource(namespace) for r in self.resources]

    def statuses(
            self,
            namespace: str = None
    ) -> list:
        """
        Returns a list of statuses for all resources in the bundle.

        :param namespace:
            Optionally specify the namespace where the resources reside.
        """
        return [r.get_resource_status(namespace) for r in self.resources]

    def delete(self, namespace: str = None):
        """
        Delete all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to delete the resource.
        """
        for r in self.resources:
            r.delete_resource(namespace)


def from_yaml_file(
        file_path: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> ResourceSubclass:
    """
    Creates a Resource object from a YAML configuration file.

    :param file_path:
        Path to the kubernetes resource configuration YAML file to be
        loaded.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    with open(file_path) as f:
        return from_yaml(f.read(), kubernetes_version)


def from_yaml(
        resource_definition: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> ResourceSubclass:
    """
    Creates a Resource object from a YAML string.

    :param resource_definition:
        String containing the contents of a yaml resource definition.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    data = yaml.load(resource_definition, Loader=yaml.CLoader)
    return from_dict(data, kubernetes_version)


def new_resource(
    api_version: str,
    kind: str,
    name: str = None,
    kubernetes_version: 'kuber.VersionLabel' = None
) -> ResourceSubclass:
    """
    Creates an empty Kubernetes resource object of the specified type for
    the specified Kubernetes version.

    :param api_version:
        A standard Kubernetes configuration api version, e.g. "apps/v1", as
        to where to locate this resource within the Kubernetes API.
    :param kind:
        The type of resource, e.g. "Deployment". Case matches and should
        reflect the `kind` as specified in a Kubernetes configuration file.
    :param name:
        Name to give to the resource in its metadata.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    definition = {
        'apiVersion': api_version,
        'kind': kind,
        'metadata': {'name': name}
    }
    return from_dict(definition, kubernetes_version)


def from_dict(
        resource_definition: dict,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> ResourceSubclass:
    """
    Converts a dictionary into a Resource object.

    :param resource_definition:
        Definition dictionary object to deserialize.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    version = kubernetes_version or 'latest'
    version: str = getattr(version, 'label', version)
    if version.find('.') > 0 and not version.startswith('v'):
        version = f'v{version}'
    version = version.replace('.', '_')

    parts = (
        resource_definition['apiVersion']
        .replace('rbac.authorization.k8s.io/', 'rbac/')
        .split('/')[:2]
    )
    area = parts[-1]
    group = parts[0] if len(parts) > 1 else 'core'
    package = '.'.join(['kuber', f'{version}', f'{group}_{area}'])

    loaded_module = importlib.import_module(package)
    resource_class = getattr(loaded_module, resource_definition['kind'])
    resource: Resource = resource_class()
    return resource.from_dict(resource_definition)


def from_json_file(
        file_path: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> ResourceSubclass:
    """
    Creates a Resource object from a configuration file.

    :param file_path:
        Path to a JSON or YAML file that specifies the resource to create.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    with open(file_path) as f:
        return from_dict(json.load(f), kubernetes_version)

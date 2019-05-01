import datetime
import glob
import os
import typing
import uuid

import kuber
from kuber import execution
from kuber import interface
from kuber import versioning as _versioning
from kuber.definitions import Resource
from kuber.management import arrays
from kuber.management import configuration
from kuber.management import creation


class ResourceBundle:
    """Contains one or more related Kubernetes `Resource` objects."""

    def __init__(
            self,
            bundle_name: str = None,
            kubernetes_version: 'kuber.VersionLabel' = 'latest',
            namespace: str = None
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
        :param namespace:
            Kubernetes namespace in which the resources will/do reside.
        """
        self.name = bundle_name or str(uuid.uuid4())
        self.namespace = namespace
        self._version = kubernetes_version
        self._resources: typing.List['creation.ResourceSubclass'] = []
        self._cli = interface.ResourceBundleCli(self)
        self._settings = configuration.ResourceBundleSettings(self)
        self._array = arrays.ResourceArray(self)

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
    def settings(self) -> 'configuration.ResourceBundleSettings':
        """
        Contextual settings object for this bundle that contains any loaded
        settings data to be used in the dynamic configuration of the resources
        within this bundle.
        """
        return self._settings

    @property
    def cli(self) -> 'interface.ResourceBundleCli':
        """Command line interface for the bundle."""
        return self._cli

    @property
    def resources(self) -> 'arrays.ResourceArray':
        """Resources stored within the bundle."""
        return self._array

    def get(
            self,
            name: str = None,
            kind: str = None,
            namespace: str = None,
            **kwargs
    ) -> typing.Optional['creation.ResourceSubclass']:
        """
        Fetches the resource in the bundle that best and first matches the
        given properties using name, kind and optional labels to select the
        desired resource.

        :param name:
            Name of the resource to return.
        :param kind:
            Kubernetes kind of the resource to return, e.g. 'Deployment'.
        :param namespace:
            Namespace in which the resource is explicitly assigned.
        :param kwargs:
            Optionally specify metadata labels to use when selecting the
            resource to return.
        """
        for r in self.resources:
            match = (
                (kind is None or r.kind == kind)
                and (name is None or r.metadata.name == name)
                and (namespace is None or r.metadata.namespace == namespace)
            )
            labels = {
                key: value
                for key, value in getattr(r, 'metadata').labels.items()
                if key in kwargs and kwargs[key] == value
            }
            if match and len(kwargs) == len(labels):
                return r
        return None

    def get_many(
            self,
            name: str = None,
            kind: str = None,
            namespace: str = None,
            **kwargs
    ) -> typing.List['creation.ResourceSubclass']:
        """
        Fetches the resources in the bundle that matches the given properties
        using name, kind and optional labels to select the desired resources.

        :param name:
            Name of the resources to return.
        :param kind:
            Kubernetes kind of the resources to return, e.g. 'Deployment'.
        :param namespace:
            Namespace in which the resource is explicitly assigned.
        :param kwargs:
            Optionally specify metadata labels to use when selecting the
            resource to return.
        """
        results = []
        for r in self.resources:
            match = (
                (kind is None or r.kind == kind)
                and (name is None or r.metadata.name == name)
                and (namespace is None or r.metadata.namespace == namespace)
            )
            labels = {
                key: value
                for key, value in getattr(r, 'metadata').labels.items()
                if key in kwargs and kwargs[key] == value
            }
            if match and len(kwargs) == len(labels):
                results.append(r)
        return results

    def pop(
            self,
            name: str = None,
            kind: str = None,
            **kwargs
    ) -> typing.Optional['creation.ResourceSubclass']:
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
        self.remove(resource)
        return resource

    def remove(
            self,
            resource: 'Resource',
            *args: 'Resource'
    ) -> 'ResourceBundle':
        """
        Removes the specified resource object (or resource objects) from
        the bundle if they are currently in the bundle.

        :param resource:
            Resource object to remove from the bundle.
        :param args:
            Optionally specify additional resource objects to remove.
        :return:
            The ResourceBundle object.
        """
        resources = [resource] + list(args)
        for r in resources:
            if r and r in self._resources:
                self._resources.remove(r)
        return self

    def push(self, resource: 'Resource', *args: 'Resource') -> 'ResourceBundle':
        """
        Adds the specified resource to the end of the bundle's
        resource list.

        :param resource:
            Resource object to add to the bundle. It will be conformed to
            the bundle's specifications and constraints upon insertion.
        :param args:
            Additional Resource objects to add to the bundle. They will be
            pushed onto the bundle in the order they appear in the arguments.
        """
        resources = [resource] + list(args)
        for r in resources:
            if r not in self._resources:
                self._resources.append(self._conform_resource(r))
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
            **kwargs: str
    ) -> 'ResourceBundle':
        """
        Adds an empty resource of the specified type as the last entry
        to the bundle's resources list.

        :param api_version:
            A standard Kubernetes configuration api version, e.g. "apps/v1".
        :param kind:
            The type of resource, e.g. "Deployment".
        :param name:
            Name to give the resource.
        :param kwargs:
            Labels to assign to the metadata of the new resource.
        """
        return self.push(creation.new_resource(
            api_version=api_version,
            kind=kind,
            name=name,
            kubernetes_version=self.kubernetes_version,
            **kwargs
        ))

    def add_from_yaml(self, resource_definition: str) -> 'ResourceBundle':
        """
        Adds one or more Resources objects to the bundle from the YAML
        definition string, which may contain more than one YAML document.

        :param resource_definition:
            A string containing a valid Kubernetes resource configuration.
        """
        return self.push(*creation.from_yaml_multiple(
            resource_definition,
            self.kubernetes_version
        ))

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
            self.push(*creation.from_yaml_file_multiple(
                os.path.realpath(path),
                version
            ))
        elif path.endswith('.json'):
            self.push(creation.from_json_file(os.path.realpath(path), version))
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
        paths = sorted([
            path
            for path in glob.iglob(glob_path, recursive=recursive)
            if path.endswith(extensions)
            and os.path.isfile(path)
            and os.path.basename(path) not in (ignores or [])
        ])

        for path in paths:
            self.add_file(path)
        return self

    def add_directory_files(
            self,
            directory: str,
            filenames: typing.Iterable = None
    ) -> 'ResourceBundle':
        """
        Adds all of the resource configuration filenames listed in the
        ``filenames`` argument from within the specified directory in the
        order specified by the ``filenames`` argument. This is useful when
        the order of resources is important.

        :param directory:
            Directory where the filenames reside.
        :param filenames:
            A list of filenames in the given directory and the order in
            which they should be added.
        """
        for name in (filenames or []):
            self.add_file(os.path.realpath(os.path.join(directory, name)))
        return self

    def render_yaml(self) -> typing.List[str]:
        """Serializes the bundle resources to a list of YAML strings."""
        return [self._conform_resource(r).to_yaml() for r in self.resources]

    def render_yaml_bundle(self) -> str:
        """Serializes the bundle resources to a single YAML config."""
        return '\n---\n\n'.join(self.render_yaml())

    def render_json(self) -> typing.List[str]:
        """Serializes the bundle to a list of JSON configurations."""
        return [self._conform_resource(r).to_json() for r in self.resources]

    def _conform_resource(
            self,
            resource: 'Resource'
    ) -> 'creation.ResourceSubclass':
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
            kuber_timestamp=(
                f'{datetime.datetime.utcnow().isoformat()}Z'
                .replace(':', '-')
            )
        )
        return resource

    def create(
            self,
            namespace: str = None,
            echo: bool = False
    ) -> typing.List['execution.ResponseInfo']:
        """
        Create all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to create resources.
            Resources that have a namespace explicitly set in their
            metadata value will ignore this value and use that value instead.
            Will default to the namespace specified in this bundle if this is
            not specified and the namespace is not specified on the resource
            metadata directly.
        :param echo:
            Whether or not to pretty-print the response objects to stdout
            while creating resources.
        """
        default_namespace = namespace or self.namespace
        results = []
        for r in self.resources:
            ns = r.metadata.namespace or default_namespace
            results.append(execution.create_resource(r, ns, echo=echo))
        return results

    def replace(
            self,
            namespace: str = None,
            echo: bool = False
    ) -> typing.List['execution.ResponseInfo']:
        """
        Replace all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to replace resources.
            Resources that have a namespace explicitly set in their
            metadata value will ignore this value and use that value instead.
            Will default to the namespace specified in this bundle if this is
            not specified and the namespace is not specified on the resource
            metadata directly.
        :param echo:
            Whether or not to pretty-print the response objects to stdout
            while creating resources.
        """
        default_namespace = namespace or self.namespace
        results = []
        for r in self.resources:
            ns = r.metadata.namespace or default_namespace
            results.append(execution.replace_resource(r, ns, echo=echo))
        return results

    def statuses(
            self,
            namespace: str = None,
            echo: bool = False
    ) -> typing.List['execution.ResponseInfo']:
        """
        Returns a list of statuses for all resources in the bundle.

        :param namespace:
            Optionally specify the namespace where the resources reside.
            Resources that have a namespace explicitly set in their
            metadata value will ignore this value and use that value instead.
            Will default to the namespace specified in this bundle if this is
            not specified and the namespace is not specified on the resource
            metadata directly.
        :param echo:
            Whether or not to pretty-print the response objects to stdout
            while creating resources.
        """
        default_namespace = namespace or self.namespace
        results = []
        for r in self.resources:
            ns = r.metadata.namespace or default_namespace
            results.append(execution.get_resource_status(r, ns, echo=echo))
        return results

    def delete(
            self,
            namespace: str = None,
            echo: bool = False
    ) -> typing.List['execution.ResponseInfo']:
        """
        Delete all resources in the bundle.

        :param namespace:
            Optionally specify the namespace in which to delete the
            resources that have not had a namespace explicitly set in their
            metadata value. Will default to the namespace specified in this
            bundle if this is not specified and the namespace is not specified
            on the resource metadata directly.
        :param echo:
            Whether or not to pretty-print the response objects to stdout
            while creating resources.
        """
        default_namespace = namespace or self.namespace
        results = []
        for r in self.resources:
            ns = r.metadata.namespace or default_namespace
            results.append(execution.delete_resource(r, ns, echo=echo))
        return results

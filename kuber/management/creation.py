import importlib
import json
import typing

import yaml

import kuber
from kuber.definitions import Resource

ResourceSubclass = typing.Union[Resource, typing.Any]


def from_yaml_file(
        file_path: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.Optional[ResourceSubclass]:
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


def from_yaml_file_multiple(
        file_path: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.Optional[ResourceSubclass]:
    """
    Creates Resource objects for each document found in the YAML file.
    Empty documents will be ignored.

    :param file_path:
        Path to the kubernetes resources configuration YAML file to be
        loaded.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resources. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    with open(file_path) as f:
        return from_yaml_multiple(f.read(), kubernetes_version)


def from_yaml_multiple(
        resources_definitions: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.List[ResourceSubclass]:
    """
    Creates Resource objects for each document found in the YAML string.
    Empty documents will be ignored.

    :param resources_definitions:
        String containing the contents of one or more yaml resource
        definitions separated by ``\n---``.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resources. If
        omitted, the ``latest`` version will be used by default. Accepts
        either a string version label of a KubernetesVersion object.
    """
    resources = [
        from_yaml(d, kubernetes_version)
        for d in resources_definitions.split('\n---')
    ]
    return [r for r in resources if r is not None]


def from_yaml(
        resource_definition: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.Optional[ResourceSubclass]:
    """
    Creates a Resource object from a YAML string.

    :param resource_definition:
        String containing the contents of a yaml resource definition.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    data = yaml.load(resource_definition, Loader=kuber.yaml_loader)
    return from_dict(data, kubernetes_version)


def new_resource(
    api_version: str,
    kind: str,
    name: str = None,
    kubernetes_version: 'kuber.VersionLabel' = None,
    **kwargs: str
) -> typing.Optional[ResourceSubclass]:
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
    :param kwargs:
        Labels to assign to the metadata of the new resource.
    """
    definition = {
        'apiVersion': api_version,
        'kind': kind,
        'metadata': {'name': name, 'labels': kwargs}
    }
    return from_dict(definition, kubernetes_version)


def from_dict(
        resource_definition: dict,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.Optional[ResourceSubclass]:
    """
    Converts a dictionary into a Resource object.

    :param resource_definition:
        Definition dictionary object to deserialize.
    :param kubernetes_version:
        Version of the kubernetes API to use when creating the Resource. If
        omitted, the `latest` version will be used by default. Accepts either
        a string version label of a KubernetesVersion object.
    """
    if not resource_definition:
        return None

    version = kubernetes_version or 'latest'
    version: str = getattr(version, 'label', version)
    if version.find('.') > 0 and not version.startswith('v'):
        version = f'v{version}'
    version = version.replace('.', '_')

    parts = (
        resource_definition['apiVersion']
        .replace('rbac.authorization.k8s.io/', 'rbac/')
        .replace('apiregistration.k8s.io/', 'apiregistration/')
        .replace('storage.k8s.io/', 'storage/')
        .split('/')[:2]
    )
    area = parts[-1]
    group = parts[0] if len(parts) > 1 else 'core'
    package = '.'.join(['kuber', f'{version}', f'{group}_{area}'])

    try:
        loaded_module = importlib.import_module(package)
    except ModuleNotFoundError as error:  # pragma: no cover
        print(
            f'Error: Unable to import module "{package}" '
            f'for resource apiVersion: "{resource_definition["apiVersion"]}".'
        )
        raise error

    resource_class = getattr(loaded_module, resource_definition['kind'])
    resource: Resource = resource_class()
    return resource.from_dict(resource_definition)


def from_json_file(
        file_path: str,
        kubernetes_version: 'kuber.VersionLabel' = 'latest'
) -> typing.Optional[ResourceSubclass]:
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

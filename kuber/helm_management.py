import os
import subprocess
import typing
import uuid

import yaml

from kuber import definitions
from kuber import management


class Maintainer:
    """
    maintainers: # (optional)
      - name: The maintainer's name (required for each maintainer)
        email: The maintainer's email (optional for each maintainer)
        url: A URL for the maintainer (optional for each maintainer)
    """

    def __init__(self, name: str, email: str = None, url: str = None):
        """..."""
        self.name = name
        self.email = email
        self.url = url


class Chart:
    """..."""

    def __init__(
            self,
            name: str = None,
            version: str = '0.0.0',
            helm_api_version: str = 'v1',
            kube_version: str = None,
            description: str = None,
            keywords: typing.List[str] = None,
            home: str = None,
            sources: typing.List[str] = None,
            maintainers: typing.List['Maintainer'] = None,
            engine: str = None,
            icon: str = None,
            app_version: str = None,
            deprecated:  bool = None,
            tiller_version: str = None
    ):
        """..."""
        self._properties = {
            'apiVersion': helm_api_version or 'v1',
            'name': name or str(uuid.uuid4()),
            'version': version,
            'kubeVersion': kube_version,
            'description': description,
            'keywords': keywords or [],
            'home': home or '',
            'sources': sources or [],
            'maintainers': maintainers or [],
            'engine': engine,
            'icon': icon,
            'appVersion': app_version,
            'deprecated': deprecated,
            'tillerVersion': tiller_version
        }

    @property
    def api_version(self) -> str:
        """The chart API version, always "v1" (required)."""
        return self._properties['apiVersion']

    @api_version.setter
    def api_version(self, value: str):
        """The chart API version, always "v1" (required)."""
        self._properties['apiVersion'] = value

    @property
    def name(self) -> str:
        """The name of the chart."""
        return self._properties['name']

    @name.setter
    def name(self, value: str):
        """The name of the chart."""
        self._properties['name'] = value

    @property
    def version(self) -> str:
        """A SemVer 2 version (required)."""
        return self._properties['version']

    @version.setter
    def version(self, value: str):
        """A SemVer 2 version (required)."""
        self._properties['version'] = value

    @property
    def kube_version(self) -> str:
        """A SemVer range of compatible Kubernetes versions (optional)."""
        return self._properties['kubeVersion']

    @kube_version.setter
    def kube_version(self, value: str):
        """A SemVer range of compatible Kubernetes versions (optional)."""
        self._properties['kubeVersion'] = value

    @property
    def description(self) -> str:
        """A single-sentence description of this project (optional)."""
        return self._properties['description']

    @description.setter
    def description(self, value: str):
        """A single-sentence description of this project (optional)."""
        self._properties['description'] = value

    @property
    def keywords(self) -> typing.List[str]:
        """A list of keywords about this project (optional)."""
        return self._properties['keywords']

    @keywords.setter
    def keywords(self, value: typing.List[str]):
        """A list of keywords about this project (optional)."""
        self._properties['keywords'] = value

    @property
    def home(self) -> str:
        """The URL of this project's home page (optional)."""
        return self._properties['home']

    @home.setter
    def home(self, value: str):
        """The URL of this project's home page (optional)."""
        self._properties['home'] = value

    @property
    def sources(self) -> typing.List[str]:
        """A list of URLs to source code for this project (optional)."""
        return self._properties['sources']

    @sources.setter
    def sources(self, value: typing.List[str]):
        """A list of URLs to source code for this project (optional)."""
        self._properties['sources'] = value

    @property
    def maintainers(self) -> typing.List[Maintainer]:
        """A list of URLs to source code for this project (optional)."""
        return self._properties['maintainers']

    @maintainers.setter
    def maintainers(self, value: typing.List[Maintainer]):
        """A list of Maintainers."""
        self._properties['maintainers'] = value

    @property
    def engine(self) -> str:
        """The name of the template engine (optional, defaults to gotpl)."""
        return self._properties['engine']

    @engine.setter
    def engine(self, value: str):
        """The name of the template engine (optional, defaults to gotpl)."""
        self._properties['engine'] = value

    @property
    def icon(self) -> str:
        """A URL to an SVG or PNG image to be used as an icon (optional)."""
        return self._properties['icon']

    @icon.setter
    def icon(self, value: str):
        """A URL to an SVG or PNG image to be used as an icon (optional).."""
        self._properties['icon'] = value

    @property
    def app_version(self) -> str:
        """
        The version of the app that this contains (optional).
        This needn't be SemVer.
        """
        return self._properties['appVersion']

    @app_version.setter
    def app_version(self, value: str):
        """
        The version of the app that this contains (optional).
        This needn't be SemVer.
        """
        self._properties['appVersion'] = value

    @property
    def deprecated(self) -> bool:
        """Whether this chart is deprecated (optional, boolean)."""
        return self._properties['deprecated'] or False

    @deprecated.setter
    def deprecated(self, value: str):
        """Whether this chart is deprecated (optional, boolean)."""
        self._properties['deprecated'] = value

    @property
    def tiller_version(self) -> str:
        """
        The version of Tiller that this chart requires. This should be
        expressed as a SemVer range: ">2.0.0" (optional).
        """
        return self._properties['tillerVersion']

    @tiller_version.setter
    def tiller_version(self, value: str):
        """
        The version of Tiller that this chart requires. This should be
        expressed as a SemVer range: ">2.0.0" (optional).
        """
        self._properties['tillerVersion'] = value

    def load(self, path_or_directory: str) -> 'Chart':
        """..."""
        path = os.path.realpath(
            os.path.join(path_or_directory, 'Chart.yaml')
            if os.path.isdir(path_or_directory) else
            path_or_directory
        )
        data = yaml.load(path, yaml.CLoader)
        maintainers = [Maintainer(**m) for m in data.pop('maintainers', [])]
        self._properties = data
        self._properties['maintainers'] = maintainers
        return self


class ChartResourceBundle(management.ResourceBundle):
    """..."""

    def __init__(self, kube_api_version: str = None, chart: 'Chart' = None):
        super(ChartResourceBundle, self).__init__(version=kube_api_version)
        self._chart = chart or Chart(name='', version='0.0.0')

    @property
    def chart(self) -> 'Chart':
        return self._chart

    @chart.setter
    def chart(self, value: 'Chart'):
        self._chart = value

    def _conform_resource(self, resource: 'definitions.Resource'):
        """..."""
        labels = getattr(resource, 'metadata').labels
        expected_labels = {
            'app.kubernetes.io/name': '{{ template "name" . }}',
            'helm.sh/chart':
                '{{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}',
            'app.kubernetes.io/managed-by': '{{ .Release.Service }}',
            'app.kubernetes.io/instance': '{{ .Release.Name }}',
            'app.kubernetes.io/version': '{{ .Chart.AppVersion }}'
        }
        labels.update({
            name: value
            for name, value in expected_labels.items()
            if name not in labels
        })
        return resource

    def load_chart(self, directory: str):
        """..."""
        self._chart = Chart().load(directory)


def render_helm_chart(
        chart_path: str = None,
        name: str = None,
        namespace: str = None,
        values_file_path: str = None,
        is_upgrade: bool = False,
        kubernetes_version: str = None
) -> typing.List['definitions.Resource']:
    """..."""
    flags = {
        '--name': name,
        '--namespace': namespace,
        '--values': values_file_path,
        '--is-upgrade': 'true' if is_upgrade else None
    }

    default_values_path = os.path.realpath(os.path.join(
        chart_path,
        'values.yaml'
    ))
    if values_file_path is None and os.path.exists(default_values_path):
        flags['--values'] = default_values_path

    command = ['helm', 'template'] + [
        f'{k}={v}'
        for k, v in flags.items()
        if v is not None
    ]
    command.append(os.path.realpath(chart_path))
    print(command)
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode:
        print(result.stderr.decode())
        raise RuntimeError('Execution of helm failed for the above reason.')

    resources = []
    for definition in result.stdout.decode().split('\n---'):
        has_api_version = definition.find('\napiVersion') >= 0
        has_kind = definition.find('\nkind') >= 0
        if has_api_version and has_kind:
            resources.append(management.from_yaml(kubernetes_version, definition))

    return resources

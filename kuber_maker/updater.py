import base64
import json
import os
import typing
from collections import defaultdict

import requests
import semver

VERSION_URL = 'https://api.github.com/repos/kubernetes/kubernetes/tags'
DOWNLOAD_URL = (
    'https://raw.githubusercontent.com/kubernetes/kubernetes/{commit}'
    '/api/openapi-spec/swagger.json'
)


class Release(typing.NamedTuple):
    """Data structure for released versions."""

    name: str
    version: semver.VersionInfo
    api_version: str
    commit_sha: str
    data: dict


class ApiGroup(typing.NamedTuple):
    """Data structure for api release versions."""

    name: str
    version: semver.VersionInfo
    latest: Release
    pre: Release


def to_release_version(release_data: dict) -> typing.Optional[Release]:
    """..."""
    name = release_data['name']
    try:
        version = semver.parse_version_info(name[1:])
    except ValueError:
        return None

    return Release(
        name=name,
        version=version,
        api_version=f'{version.major}.{version.minor}',
        commit_sha=release_data['commit']['sha'],
        data=release_data
    )


def get_release_groups() -> typing.List[ApiGroup]:
    """..."""
    entries = []
    headers = {'Authorization': _get_authentication_header()}
    url = VERSION_URL
    while url is not None:
        response = requests.get(url, headers=headers)
        entries += response.json()
        url = response.links.get('next', {}).get('url')

    releases = [to_release_version(entry) for entry in entries]
    grouped = defaultdict(list)
    for r in releases:
        if r is not None:
            grouped[r.api_version].append(r)

    combined = []
    for version, entries in grouped.items():
        ordered = sorted(entries, reverse=True, key=lambda x: x.version)
        combined.append(ApiGroup(
            name=version,
            version=semver.parse_version_info(f'{version}.0'),
            pre=ordered[0],
            latest=next((e for e in ordered if not e.version.prerelease), None)
        ))

    return sorted(combined, reverse=True, key=lambda x: x.version)


def update_specs():
    """..."""
    groups = get_release_groups()
    limit = 4 if groups[0].latest else 5
    for group in groups[:limit]:
        release = group.latest or group.pre
        path = download_version(release, f'v{group.name}')
        print(f'Updated v{group.name}: {path}')

    pre = next((g.pre for g in groups if g.pre), None)
    path = download_version(pre, 'pre')
    print(f'Updated pre ({pre.name}): {path}')

    latest = next((g.latest for g in groups if g.latest), None)
    path = download_version(latest, 'latest')
    print(f'Updated latest ({latest.name}): {path}')


def download_version(release: Release, name: str = None) -> str:
    """
    Downloads the pre or latest version of the specified ApiGroup
    to the specs directory, overwriting anything that might already be
    stored there.
    """
    url = DOWNLOAD_URL.format(commit=release.commit_sha)
    response = requests.get(url)
    data = response.json()
    data['kuber'] = {
        'name': release.name,
        'api_version': release.api_version,
        'commit_sha': release.commit_sha,
        'version': str(release.version)
    }

    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'specs', f'{name}.json'
    ))
    with open(path, 'wb') as f:
        f.write(json.dumps(data, indent=2).encode())

    return path


def _get_authentication_header():
    """
    Retrieves Github authentication data from the local directory. Expects
    it to be a JSON file containing name and password keys.
    """
    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'github-api-auth.json'
    ))
    with open(path) as f:
        data = json.load(f)

    credentials = f'{data["user"]}:{data["password"]}'
    return 'Basic {}'.format(base64.b64encode(credentials.encode()).decode())
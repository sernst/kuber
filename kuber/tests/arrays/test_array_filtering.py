import kuber
import pathlib

from pytest import mark

RESOURCES_PATH = pathlib.Path(__file__).parent.joinpath('resources.yaml')

SCENARIOS = (
    {
        'filters': ['first/*'],
        'matches': set(),
    },
    {
        'filters': [],
        'matches': {
            'first/Pod/foo-pod-first',
            'first/Deployment/foo-deployment-first',
            'second/Pod/foo-pod-second',
            'second/Job/foo-job-second',
            'second/Pod/bar-pod-second',
            'second/Deployment/bar-deployment-second',
            'second/Job/bar-job-second',
        },
    },
    {
        'filters': ['*-job-*', '*-deployment-first'],
        'matches': {
            'first/Deployment/foo-deployment-first',
            'second/Job/foo-job-second',
            'second/Job/bar-job-second',
        },
    },
    {
        'filters': ['foo-*'],
        'matches': {
            'first/Pod/foo-pod-first',
            'first/Deployment/foo-deployment-first',
            'second/Pod/foo-pod-second',
            'second/Job/foo-job-second',
        },
    },
    {
        'filters': ['FIRST/*/*'],
        'matches': {
            'first/Pod/foo-pod-first',
            'first/Deployment/foo-deployment-first',
        },
    },
)


@mark.parametrize('scenario', SCENARIOS)
def test_array_filtering(scenario: dict):
    """Should filter down to the expected resources."""
    bundle = kuber.from_file(str(RESOURCES_PATH))
    matches = bundle.resources.matching(*scenario['filters'])

    assert scenario['matches'] == {
        f'{m.metadata.namespace}/{m.kind}/{m.metadata.name}'
        for m in matches.to_list()
    }

import os

import kuber
from kuber.latest import batch_v1beta1

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_get_containers_from_job():
    """Should get containers without error."""
    path = os.path.join(MY_DIRECTORY, 'cronjob.yaml')
    cron_job: batch_v1beta1.CronJob = kuber.from_yaml_file(path)
    assert len(cron_job.get_containers()) == 1

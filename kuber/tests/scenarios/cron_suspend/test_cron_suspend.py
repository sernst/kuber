from kuber.latest import batch_v1beta1


def test_cron_suspend():
    """Should preserve suspend value when false."""
    cron = batch_v1beta1.CronJob(
        spec=batch_v1beta1.CronJobSpec(
            suspend=True
        )
    )
    before = cron.to_yaml()
    cron.spec.suspend = False
    after = cron.to_yaml()
    assert 'suspend: true' in before
    assert 'suspend: false' in after

import time

from kuber.v1_13.apps import v1 as apps_v1
from kuber.v1_13.batch import v1 as batch_v1

# Configure a deployment
d = apps_v1.Deployment()

with d.metadata as md:
    md.name = 'my-deployment'
    md.labels.update(app='foo', component='application')

d.spec.selector.match_labels.update(app='foo')
d.spec.template.metadata.labels.update(app='foo')
d.append_container(name='app', image='my-app:1.0')
d.spec.replicas = 2

status = d.create_resource(namespace='default')
print('[CREATED]:', status is not None)
if status is not None:
    print('UNAVAILABLE REPLICAS:', status.unavailable_replicas)

time.sleep(1)
d.spec.replicas = 3
status = d.replace_resource(namespace='default')
print('[REPLACED]:', status is not None)
if status is not None:
    print('UNAVAILABLE REPLICAS:', status.unavailable_replicas)

time.sleep(2)
is_deleted = d.delete_resource(namespace='default')
print('[DELETED]:', is_deleted)


# Configure a job
j = batch_v1.Job()
j.spec.template.spec.restart_policy = 'Never'
with j.metadata as md:
    md.name = 'my-job'
    md.namespace = 'default'
    md.labels.update(app='my-job')

j.append_container(name='app', image='my-job:1.0')

status = j.create_resource()
print('[CREATED]:', status is not None)
if status is not None:
    print('ACTIVE:', status.active)

time.sleep(1)

is_deleted = j.delete_resource(namespace='default')
print('[DELETED]:', is_deleted)

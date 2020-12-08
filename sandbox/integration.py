import time
from pprint import pprint

import kuber
from kuber.v1_13 import apps_v1
from kuber.v1_13 import batch_v1

kuber.load_access_config()

# Configure a deployment
d = apps_v1.Deployment()

with d.metadata as md:
    md.name = "my-deployment"
    md.namespace = "default"
    md.labels.update(app="foo", component="application")

d.spec.selector.match_labels.update(app="foo")
d.spec.template.metadata.labels.update(app="foo")
d.append_container(name="app", image="my-app:1.0")
d.spec.replicas = 2

status = d.create_resource()
print("[CREATED]:")
pprint(status.to_dict())

status = d.get_resource_status()
print("[STATUS]:")
pprint(status.to_dict())

d.spec.replicas = 0
status = d.patch_resource()
print("[PATCHED]:")
pprint(status.to_dict())

status = d.replace_resource()
print("[REPLACED]:")
pprint(status.to_dict())

d.delete_resource()
print("[DELETED]:", d.metadata.name)


# Configure a job
j = batch_v1.Job()

with j.metadata as md:
    md.name = "my-job"
    md.namespace = "default"
    md.labels.update(app="my-job")

with j.spec.template as t:
    t.spec.restart_policy = "Never"
    t.metadata.name = "my-job-template"
    t.metadata.labels.update(job=j.metadata.name)

j.append_container(name="app", image="my-job:1.0")

status = j.create_resource()
print("[CREATED]:")
pprint(status.to_dict())

time.sleep(1)

status = j.get_resource_status()
print("[STATUS]:")
pprint(status.to_dict())

j.delete_resource(namespace="default")
print("[DELETED]:", j.metadata.name)

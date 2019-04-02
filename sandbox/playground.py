from kuber.v1_13 import apps_v1
from kuber.v1_13 import batch_v1
from kuber.v1_13.core_v1 import Container


j = batch_v1.Job()
j.metadata.labels.update(app='scott')
j.spec.template.spec.containers.append(Container(
    name='standard',
    image='swernst/cauldron:current-standard',
    image_pull_policy='Always',
    tty=True,
    ports=[
        apps_v1.ContainerPort(
            container_port=5010,
            host_port=9100,
            name='notebook'
        )
    ],
    resources=batch_v1.ResourceRequirements(
        limits={'cpu': '1', 'memory': '20Gi'},
        requests={'cpu': '1', 'memory': '20Gi'}
    )
))
j.append_container(
    name='miniconda',
    image='swernst/cauldron:current-miniconda',
    image_pull_policy='IfNotPresent'
)

c = j.get_container('miniconda')
c.resources = {
    'limits': {'cpu': '1', 'memory': '4Gi'}
}

print(j.to_yaml())


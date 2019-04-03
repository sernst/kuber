import kuber
from kuber.latest import apps_v1

# Load YAML configuration file into a Deployment object
d: apps_v1.Deployment = kuber.from_yaml_file(
    file_path='./my-deployment.yaml'
)

d.metadata.labels.update(app='foo')

with d.get_container('app') as c:
    c.resources.limits.update(cpu='1.5', memory='1Gi')
    c.resources.requests.update(cpu='1.5', memory='800Mi')
    c.ports.append(apps_v1.ContainerPort(container_port=8080, host_port=80))

# Render the results to YAML
print(d.to_yaml())

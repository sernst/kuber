import typing

import kuber
from kuber.latest import apps_v1
from kuber.latest import core_v1

# Load YAML configuration file into a Deployment object
d = typing.cast(
    apps_v1.Deployment,
    kuber.from_yaml_file(file_path="./my-deployment.yaml")
)

# Add an `app` label.
d.metadata.labels.update(app="foo")

# Create a container port to map port 8080 in
# the container to port 80 on the host.
port = apps_v1.ContainerPort(container_port=8080, host_port=80)

# Modify the container named "app" with resource
# limits/requests and an additional port mapping.
with typing.cast(core_v1.Container, d.get_container("app")) as c:
    c.resources.limits.update(cpu="1.5", memory="1Gi")
    c.resources.requests.update(cpu="1.5", memory="800Mi")
    c.ports.append(port)

# Render the results to YAML
print(d.to_yaml())

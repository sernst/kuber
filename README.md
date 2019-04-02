[![Documentation Status](https://readthedocs.org/projects/kuber/badge/?version=latest)](https://kuber.readthedocs.io/en/latest/?badge=latest)

## What is kuber?

_kuber_ is higher-level Python client for Kubernetes resource management that
integrates and maintains compatibility with the lower-level official 
[Kubernetes Python client](https://github.com/kubernetes-client/python). 
Additionally, _kuber_ supports managing groups of resources collectively as
a single entity directly in code.

## Main Features

Here are some key things that _kuber_ does well:

- A flexible workflow for managing Kubernetes resource configuration in Python 
  code.
- The ability to load resources directly from YAML or JSON configuration files,
  modify them in code and then use them or save them back to YAML/JSON files.
- Resource bundling for managing groups of resource configurations collectively.
- CRUD operations exposed directly on the resource objects to reduce the 
  overhead in managing low-level clients.
- Convenience functions that simplify common operations, e.g. managing 
  containers within pods from the root resource.
- Very thorough type-hinting and object structure to support creating accurate 
  resource configurations and catch errors before runtime.
- All resources and sub-resources support used in `with` blocks as context
  managers to simplify making multiple changes to a sub-resource.
- Simultaneous support for multiple Kubernetes API versions. Manage multiple
  Kubernetes API versions (e.g. while promoting new versions from development 
  to production) without having to pin and switch Python environments.

## Installation

_kuber_ available for installation with _pip_:

```bash
$ pip install kuber
```

## Quickstart

_kuber_ can be used to manage individual resources or a group of resources
collectively. _kuber_ is also very flexible about how resources are created
- either directly from Python or by loading and parsing YAML/JSON configuration
files. 

```python
import typing

import kuber
from kuber.latest import apps_v1

# Create a bundle object to load and manage resource configurations
resource_bundle = (
    kuber.create_bundle()
    .add_directory('app_configs')
    .add_file('secrets/app-secret.yaml')
)

# Modify the metadata labels on all resources in the bundle
for resource in resource_bundle.resources:
    resource.metadata.labels.update(environment='production')

# Update the replica count of the loaded deployment for production. Use
# type casting here to make type-hinting and checking more explicit when
# making changes to the deployment resource.
d = typing.cast(
    apps_v1.Deployment, 
    resource_bundle.get(name='my-app', kind='Deployment')
)
d.spec.replicas = 20

# Print the combined YAML configuration for the bundle of resources
print(resource_bundle.render_yaml_bundle())
```

Or managing resources individually:

```python
from kuber.latest import batch_v1

job = batch_v1.Job()

# Populate metadata using context manager syntax for brevity
with job.metadata as md:
    md.name = 'my-job'
    md.namespace = 'jobs'
    md.labels.update(component='backend-tasks', environment='production')

# Add a container to the job spec
job.spec.append_container(
    name='main',
    image='my-registry.com/projects/my-job:1.0.1',
    image_pull_policy='Always',
    env=[batch_v1.EnvVar('ENVIRONMENT', 'production')]
)

# Print the resulting YAML configuration for display
print(job.to_yaml())
```

Check out the [kuber documentation](https://kuber.readthedocs.io/en/latest/)
for more detailed documentation.

# Kuber

A high-level Python client for Kubernetes. 

## tl;dr

```python
import kuber
from kuber.v1_13.apps import v1 as apps_v1

# Create a bundle object to load and manage resource configurations
resource_bundle = (
    kuber.create_bundle(kubernetes_version='1.13')
    .add_directory('app_configs')
    .add_file('secrets/app-secret.yaml')
)

# Modify the metadata labels on all resources in the bundle
for resource in resource_bundle.resources:
    resource.metadata.labels.update(environment='production')

# Update the replica count of the loaded deployment for production
dep: apps_v1.Deployment = resource_bundle.get(name='my-app', kind='Deployment')
dep.spec.replicas = 20

# Print the combined YAML configuration for the bundle of resources
print(resource_bundle.render_yaml_bundle())

# Create all resources in the bundle
resource_bundle.create()
```

Or managing resources individually:

```python
from kuber.v1_13.batch import v1 as batch_v1

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

# Create the resource in the currently configured cluster
job.create_resource()
```

kuber supports the basic CRUD behaviors using the locally installed and
configured _kubectl_ as the intermediary. For more advanced and custom
operations, the resource configurations can always be serialized to YAML
or JSON and used in custom defined commands or just saved to disk for later
application. The resource configurations also have a `to_dict()` function
that serializes down to a Python dictionary that is compatible with the
low-level _kubernetes_ library client APIs (passed into the _body_ parameter).

## Background

The [Official Python Kubernetes client](https://github.com/kubernetes-client/python) 
exists to provide low-level access to the Kubernetes API. However, low-level
access can be clunky to use and require an additional barrier to entry for those
of us that are not Kubernetes API experts. Generally, the lower-level API 
functionality is abstracted away from us with tools like _kubectl_.

_kuber_ is a higher-level abstraction designed to be compliant with the general
usage level of someone comfortable working with Kubernetes configuration files
and managing them with tools like _kubectl_ (and _helm_). _kuber_ was created 
because we found that managing complex configurations through configuration 
files alone was causing friction and that introducing tools like _helm_ that 
rely on templating wasn't fully solving the problem.

## Configuring Resources

_kuber_ allows Kubernetes resources to be defined entirely in Python code,
or defined in configuration files and loaded and modified by code. Examples of
the two approaches are shown below:

### The Pure Python Approach

Here's an example of how a Deployment can be created with _kuber_:

```python
from kuber.v1_13.apps import v1 as apps_v1

# Create a deployment using Kubernetes version 1.13
# from the apps/v1 API version.
d = apps_v1.Deployment()

with d.metadata as md:
    md.name = 'my-deployment'
    md.namespace = 'my-app'
    md.labels.update(app='foo', component='application')

d.spec.selector.match_labels.update(app='foo')
d.spec.template.metadata.labels.update(app='foo')

d.append_container(
    name='app',
    image='my-app:1.0',
    ports=[apps_v1.ContainerPort(container_port=8080, host_port=80)],
    tty=True,
    image_pull_policy='Always',
    resources=apps_v1.ResourceRequirements(
        limits={'cpu': '1.5', 'memory': '1Gi'},
        requests={'cpu': '1.5', 'memory': '800Mi'},
    )
)

# Render the results to YAML
print(d.to_yaml())
```

The printed output of executing this would be:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: foo
    component: application
  name: my-deployment
  namespace: my-app
spec:
  template:
    spec:
      containers:
      - image: my-app:1.0
        imagePullPolicy: Always
        name: app
        ports:
        - containerPort: 8080
          hostPort: 80
        resources:
          limits:
            cpu: '1'
            memory: 1Gi
          requests:
            cpu: '1'
            memory: 800Mi
        tty: true
```

### The Hybrid Approach

In many cases it is convenient to use standard Kubernetes configuration as a
base template. The common approach in these cases used by projects like 
[Helm](https://helm.sh/) is to introduce a templating language into the 
configuration files that gets rendered prior to using the configuration. 
However, this approach has a number of drawbacks. Instead _Kuber_ facilitates
flexible modification and augmentation of resource configurations that have
been loaded from configuration files.

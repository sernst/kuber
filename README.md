# Kuber

A higher-level Python client for Kubernetes resource management that
integrates and maintains compatibility with the lower-level official 
[Kubernetes Python client](https://github.com/kubernetes-client/python).

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
resource_bundle.create(namespace='applications')
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

kuber supports the basic CRUD behaviors by wrapping around the available 
actions from the _Kubernetes Python client_. For more advanced and custom
operations, the resource configurations can always be serialized to YAML
or JSON and used in custom defined commands or just saved to disk for later
application. The resource configurations also have a `to_dict()` function
that serializes down to a Python dictionary that is compatible with the
_Kubernetes Python client_ functions (passed into the _body_ parameter).

## Background

The [Python Kubernetes client](https://github.com/kubernetes-client/python) 
exists to provide low-level access to the Kubernetes API. However, low-level
access can be clunky to use and require an additional effort to achieve parity
with common workflows provided by configuration-driven tooling.

_kuber_ is a higher-level abstraction designed to be compliant with the general
usage level of someone comfortable working with Kubernetes configuration files
and managing them with tools like _kubectl_ (and _helm_). _kuber_ was created 
because we found that managing complex configurations through configuration 
files alone was causing friction and that introducing tools like _helm_, that 
rely on templating, were not fully solving the problem.

At the individually resource level, _kuber_ provides the additional benefits:

- Support for multiple Kubernetes API version targets within a single library.
- The ability to load resources directly from YAML or JSON configuration files.
- All resources and sub-resources support used in `with` blocks as context
  managers to simplify making multiple changes to a sub-resource.
- More complete type-hinting to better assist in creating accurate resource
  configurations.
- CRUD operations exposed directly on the resource objects to reduce the 
  overhead in managing low-level clients.
- Convenience functions that simplify common operations like adding containers 
  to deployments.

Beyond the individual level, _kuber_ provides resource bundling functionality
that behaves like a lightweight, flexible package manager 
(like [Helm](https://helm.sh/) but replacing templating with Python code)
to more easily manage multiple resources.

## Configuring Individual Resources

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

# Render the results to YAML.
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
However, a templated approach has a number of drawbacks - a primary one being
that if the template doesn't support a necessary piece custom configuration it
means forking that template and managing yourself. Instead _Kuber_ facilitates
flexible modification and augmentation of resource configurations that have
been loaded from configuration files.

Following from the example above, let's say we have a YAML resource 
configuration file `my-deployment.yaml` with part of the contents from
the example above:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
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
        tty: true
```

We want to load that configuration file and modify the loaded definition
to match the results from the _Pure Python Approach_ example in the previous
section. That would look like this:

```python
import kuber
from kuber.v1_13.apps import v1 as apps_v1

# Load YAML configuration file into a Deployment object.
d: apps_v1.Deployment = kuber.from_yaml_file(
    kubernetes_version='1.13',
    file_path='./my-deployment.yaml'
)

d.metadata.labels.update(app='foo')

with d.get_container('app') as c:
    c.resources.limits.update(cpu='1.5', memory='1Gi')
    c.resources.requests.update(cpu='1.5', memory='800Mi')
    c.ports.append(apps_v1.ContainerPort(container_port=8080, host_port=80))

# Render the results to YAML.
print(d.to_yaml())
```

The printed configuration matches the configuration printed in the previous
example.

## Managing Multiple Resources

Often times multiple resources are needed to support a single application
within a Kubernetes cluster. This is where explicit configuration can get
increasingly complex and has resulted in a number of tools, like 
[Helm](https://helm.sh/), that try to simplify the process. _kuber_ supports
high-level constructs as well that make it easier to manage multiple resources
but without having to rely on templating.

```python
import kuber
from kuber.v1_13.apps import v1 as apps_v1
from kuber.v1_13.core import v1 as core_v1

# Load all YAML and/or JSON configuration files in the specified directory
# and return a kuber ResourceBundle object that contains those loaded
# resources.
bundle = kuber.from_directory('../my-application')

# Add environment label to all loaded resources.
for r in bundle.resources:
    r.metadata.labels.update(environment='production')

# Change the number of replicas in the deployment named "my-app" that has
# the label `component=web`.
d: apps_v1.Deployment = bundle.get(
    name='my-app', 
    kind='Deployment', 
    component='web'
)
d.spec.replicas = 20

# Change the service port to 443 for the service named "my-app" that has the
# label `component=web`.
s: core_v1.Service = bundle.get(
    name='my-app', 
    kind='Service',
    component='web'
)
s.spec.ports = [core_v1.ServicePort(port=443, target_port=8080)]

# Render to consolidated YAML configuration file
print(bundle.render_yaml_bundle())
```

The flexibility of this approach comes in part from the ability to define a
working base configuration in standard configuration files, but then load and 
modify that configuration before deployment.

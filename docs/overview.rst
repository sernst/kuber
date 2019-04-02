kuber Overview
==============

The `Python Kubernetes client <https://github.com/kubernetes-client/python>`_
exists to provide low-level access to the Kubernetes API. However, low-level
access can be clunky to use and require an additional effort to achieve parity
with common workflows provided by configuration-driven tooling.

kuber is a higher-level abstraction designed to be compliant with the general
usage level of someone comfortable working with Kubernetes configuration files
and managing them with tools like *kubectl* and/or *helm*.


Configuring Individual Resources
--------------------------------

kuber allows Kubernetes resources to be defined entirely in Python code,
or defined in configuration files and loaded and modified by code. Examples of
the two approaches are shown below:

The Pure Python Approach
~~~~~~~~~~~~~~~~~~~~~~~~

Here's an example of how a Deployment can be created with kuber:

.. code-block:: python

  from kuber.latest import apps_v1

  # Create a deployment using the most recent stable Kubernetes version
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

The printed output of executing this would be:

.. code-block:: yaml

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

The Hybrid Approach
~~~~~~~~~~~~~~~~~~~

In many cases it is convenient to use standard Kubernetes configuration as a
base template. The common approach in these cases used by projects like
`Helm <https://helm.sh/>`_ is to introduce a templating language into the
configuration files that gets rendered prior to using the configuration.
However, a templated approach has a number of drawbacks - a primary one being
that if the template doesn't support a necessary piece custom configuration it
means forking that template and managing yourself. Instead kuber facilitates
flexible modification and augmentation of resource configurations that have
been loaded from configuration files.

Following from the example above, let's say we have a YAML resource
configuration file *my-deployment.yaml* with part of the contents from
the example above:

.. code-block:: yaml

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

We want to load that configuration file and modify the loaded definition
to match the results from the *Pure Python Approach* example in the previous
section. That would look like this:

.. code-block:: python

  import kuber
  from kuber.latest import apps_v1

  # Load YAML configuration file into a Deployment object.
  d: apps_v1.Deployment = kuber.from_yaml_file('./my-deployment.yaml')

  d.metadata.labels.update(app='foo')

  with d.get_container('app') as c:
      c.resources.limits.update(cpu='1.5', memory='1Gi')
      c.resources.requests.update(cpu='1.5', memory='800Mi')
      c.ports.append(apps_v1.ContainerPort(container_port=8080, host_port=80))

  # Render the results to YAML.
  print(d.to_yaml())

The printed configuration matches the configuration printed in the previous
example.

Managing Multiple Resources
---------------------------

Often times multiple resources are needed to support a single application
within a Kubernetes cluster. This is where explicit configuration can get
increasingly complex and has resulted in a number of tools, like
`Helm <https://helm.sh/>`_, that try to simplify the process. kuber supports
high-level constructs as well that make it easier to manage multiple resources
but without having to rely on templating.

.. code-block:: python

  import kuber
  from kuber.latest import apps_v1
  from kuber.latest import core_v1

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

The flexibility of this approach comes in part from the ability to define a
working base configuration in standard configuration files, but then load and
modify that configuration before deployment.

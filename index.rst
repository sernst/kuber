Kuber
=====

kuber is higher-level Python client for Kubernetes resource management that
integrates and maintains compatibility with the lower-level official
`Kubernetes Python client <https://github.com/kubernetes-client/python>`_.
Additionally, kuber supports managing groups of resources collectively as
a single entity directly in code.

Main Features
-------------

Here are some key things that kuber does well:

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

Installation
------------

kuber available for installation with `pip <https://pypi.org/project/pip/>`_:

::

  $ pip install kuber

Quickstart
----------

kuber can be used to manage individual resources or a group of resources
collectively. kuber is also very flexible about how resources are created
- either directly from Python or by loading and parsing YAML/JSON configuration
files. The first example shows the multi-resource management path:

.. code-block:: python
  :linenos:

  import typing

  import kuber
  from kuber.latest import apps_v1

  # Create a bundle and load all resource definitions from the
  # `app_configs` directory as well as the `app-secret.yaml`
  # configuration file from the local `secrets` directory.
  resource_bundle = (
      kuber.create_bundle()
      .add_directory('app_configs')
      .add_file('secrets/app-secret.yaml')
  )

  # Modify the metadata labels on all resources in the bundle.
  for resource in resource_bundle.resources:
      resource.metadata.labels.update(environment='production')

  # Update the replica count of the loaded deployment named
  # "my-app" to the desired initial count.
  d: apps_v1.Deployment = resource_bundle.get(
      name='my-app',
      kind='Deployment'
  )
  d.spec.replicas = 20

  # Print the combined YAML configuration of all bundled resources.
  print(resource_bundle.render_yaml_bundle())

Or managing resources individually:

.. code-block:: python
  :linenos:

  import kuber
  from kuber.latest import batch_v1

  job = batch_v1.Job()

  # Populate metadata using context manager syntax for brevity.
  with job.metadata as md:
      md.name = 'my-job'
      md.namespace = 'jobs'
      md.labels.update(
          component='backend-tasks',
          environment='production'
      )

  # Add a container to the job spec.
  job.spec.append_container(
      name='main',
      image='my-registry.com/projects/my-job:1.0.1',
      image_pull_policy='Always',
      env=[batch_v1.EnvVar('ENVIRONMENT', 'production')]
  )

  # Print the resulting YAML configuration for display.
  print(job.to_yaml())

.. include:: contents.rst

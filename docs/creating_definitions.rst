Creating Resources
==================

.. toctree::
  :maxdepth: 2

kuber offers a number of different ways to create Kubernetes resources
depending upon the desired usage pattern. We'll start by looking at how
to create resources individually as that will be the most familiar, but
grouping resources into bundling is a useful alternative pattern shown
further below.

Individual Resources
--------------------

A high-level ``new_resource`` function exists to conveniently load resources
from the top-level package.

.. autofunction:: kuber.new_resource

.. code-block:: python

  import kuber
  from kuber.latest import apps_v1

  d: apps_v1.Deployment = kuber.new_resource(
      api_version='apps/v1',
      kind='Deployment',
      name='my-deployment'
  )


However, resources can also be created directly from an import in much the
same way:

.. code-block:: python

  from kuber.latest import batch_v1

  j = batch_v1.Job()
  j.metadata.name = 'my-job`

Both approaches end up producing the same result, an instance of the desired
Kubernetes resource on which to operate.

However, kuber also has a number of ways to load resources from configuration
data in JSON or YAML format.

.. autofunction:: kuber.from_yaml_file

.. code-block:: python

  import kuber
  from kuber.latest import batch_v1

  job: batch_v1.Job = kuber.from_yaml_file('my-job.yaml')
  job.metadata.labels.update(component='app')

.. autofunction:: kuber.from_yaml


.. code-block:: python

  import kuber
  from kuber.latest import batch_v1

  pod: core_v1.Pod = kuber.from_yaml(
      """
      apiVersion: core/v1
      kind: Pod
      metadata:
        name: my-pod
      spec:
        containers:
          - image: python:3.8
      """
  )
  pod.spec.containers[0].name = 'python'

.. autofunction:: kuber.from_json_file

.. code-block:: python

  import kuber
  from kuber.latest import core_v1

  service: core_v1.Service = kuber.from_yaml_file('my-service.yaml')
  service.spec.selector.update(environment='production')

.. autofunction:: kuber.from_dict

.. code-block:: python

  import kuber
  from kuber.latest import batch_v1

  pod: core_v1.Pod = kuber.from_yaml({
      'apiVersion': 'core/v1',
      'kind': 'Pod',
      'metadata': {'name': 'my-pod'},
      'spec': {
          'containers': [{'image': 'python:3.8'}]
      }
  })
  pod.spec.containers[0].name = 'python'


Multiple Resources
------------------

Creating and managing multiple resources collectively in kuber is done through
``ResourceBundle`` objects that contain a list of resource objects and have
convenience functions for managing that list of resources collectively. There
are a few top-level convenience functions available for initializing
bundles from existing configuration files:

.. autofunction:: kuber.from_file

.. autofunction:: kuber.from_directory

.. autofunction:: kuber.from_directory_files

Empty ``ResourceBundles`` can also be created and then populated after
creation using the same functionality available as methods on the bundle
object.

.. autofunction:: kuber.create_bundle

CRUD Operations
===============

.. toctree::
  :maxdepth: 2

kuber supports the basic CRUD behaviors by wrapping around the available
actions from the *Kubernetes Python client*. For more advanced and custom
operations, the resource configurations can always be serialized to YAML
or JSON and used in custom defined commands or just saved to disk for later
application. The resource configurations also have a `to_dict()` function
that serializes down to a Python dictionary that is compatible with the
*Kubernetes Python client* functions (passed into the _body_ parameter).

.. code-block:: python

  import kuber
  from kuber.latest import apps_v1
  from kubernetes import config

  config.load_kube_config()

  d = apps_v1.Deployment()

  with d.metadata as md:
      md.name = 'my-deployment'
      md.namespace = 'default'
      md.labels.update(app='foo', component='application')

  d.spec.selector.match_labels.update(app='foo')
  d.spec.template.metadata.labels.update(app='foo')
  d.append_container(name='app', image='my-app:1.0')
  d.spec.replicas = 2

  # Create the Deployment resource in the cluster.
  status = d.create_resource()
  print(status.to_dict())

  # Read status of the Deployment resource in the cluster.
  status = d.get_resource_status()
  print(status.to_dict())

  # Update (patch) the Deployment resource in the cluster.
  d.spec.replicas = 0
  status = d.patch_resource()
  print(status.to_dict())

  # Update (replace) the Deployment resource in the cluster.
  status = d.replace_resource()
  print(status.to_dict())

  # Delete the Deployment resource from the cluster.
  d.delete_resource()

Beyond CRUD
-----------

For more advanced operations beyond these basic cases, there are two
approaches:

1. Serialize the Resource object to a dictionary, which is compatible
   with the lower-level *kubernetes python client* library and carry
   out the operation that way, or
2. Serialize the Resource object to YAML or JSON configuration string or
   file and use that in other configuration-based tooling like *kubectl*
   or *helm*.

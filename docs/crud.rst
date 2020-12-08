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

Initialization
--------------

Before operating on the cluster, kuber needs to be configured with access to
the cluster. This is done with the `load_access_config` function:

.. autofunction:: kuber.load_access_config

Single Resource Operations
--------------------------

.. code-block:: python

  import kuber
  from kuber.latest import apps_v1

  # Initializes kuber with local kubeconfig for access.
  kuber.load_access_config()

  d = apps_v1.Deployment()

  with d.metadata as md:
      md.name = "my-deployment"
      md.namespace = "default"
      md.labels.update(app="foo", component="application")

  d.spec.selector.match_labels.update(app="foo")
  d.spec.template.metadata.labels.update(app="foo")
  d.append_container(name="app", image="my-app:1.0")
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


Bundled Resources CRUD
----------------------

When working with bundles, the ResourceBundle objects have CRUD methods
that operate on all resources within the bundle collectively.

.. code-block:: python

  import kuber

  kuber.load_access_config()

  bundle = kuber.from_directory("./some-directory")

  # Create resources within the currently configured cluster.
  bundle.create(echo=True)

  # Display current statuses of the resources in the cluster.
  bundle.statuses(echo=True)

  # Delete resources from the cluster.
  bundle.delete(echo=True)

The following are the CRUD methods available on ResourceBundle objects:

.. automethod:: kuber.management.ResourceBundle.create

.. automethod:: kuber.management.ResourceBundle.statuses

.. automethod:: kuber.management.ResourceBundle.replace

.. automethod:: kuber.management.ResourceBundle.delete

CRUD on the Command Line
------------------------

In addition to calling CRUD operations directly within code, it's easy to
turn a ResourceBundle object into a command line interface that exposes
those CRUD operations as arguments to the executed python script. The example
above could be rewritten for command line invocation as:

.. code-block:: python

  import kuber

  if __name__ == "__main__":
      kuber.load_access_config()
      bundle = kuber.from_directory("./some-directory")
      bundle.cli()

The ``bundle.cli()`` command here will parse arguments from the command line
and execute the CRUD operation based on those commands. If we saved the above
code to file as `resources.py`, we could then carry out the same CRUD
operations as the previous example from the command line as:

.. code-block:: bash

  $ python3 resource.py create

to create the resources in the cluster,

.. code-block:: bash

  $ python3 resource.py status

to get the statuses of the resources in the cluster, and

.. code-block:: bash

  $ python3 resource.py delete

to remove the resources from the cluster.

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

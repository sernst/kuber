Command Line Interface
======================

While kuber can be used in many different ways to manage resources, the most
common path is to generate a resource bundle and then manage that bundle on
the cluster with basic CRUD operations. To facilitate the ease of that
workflow, ``ResourceBundle`` objects have a `.cli()` method that exposes
the CRUD operations on that bundle to the command line. A basic example
of how this would work looks like this:

.. code-block:: python

  import kuber

  if __name__ == '__main__':
      # Load the current cluster configuration from `kubeconfig`
      # into kuber for access to operate on the cluster.
      kuber.load_access_config()

      # Load bundle resources from the configuration files
      # stored in the local *./some/directory* directory.
      bundle = kuber.from_directory('./some/directory')

      # Add environment labels to all of the loaded resources.
      for resource in bundle.resources:
          resource.metadata.labels.update(
              environment='production'
          )

      # Expose the bundle CRUD operations as a command
      # line interface.
      bundle.cli()

The ``bundle.cli()`` command here will parse arguments from the command line
and execute the CRUD operation based on those commands. If we saved the above
code to file as `resources.py`, we could then carry out CRUD operations from
the command line:

.. code-block:: bash

  $ python3 resource.py create

to create the resources in the cluster,

.. code-block:: bash

  $ python3 resource.py status

to get the statuses of the resources in the cluster, and

.. code-block:: bash

  $ python3 resource.py delete

to remove the resources from the cluster.

Advanced Command Line Interface
-------------------------------

In more complex scenarios, exposing additional command line interface
arguments would be helpful for more flexibility in how the resource
bundle is managed. In these cases, a callback can be used that will
allow for additional configuration of the bundle prior to the
command line action being carried out.

Consider the previous example where `environment='production'` was
essentially hard-coded into the bundle. If we wanted to make defining
the *environment* value part of the CLI, we could refactor the above
example like this:

.. code-block:: python

  import argparse

  import kuber


  def configure(action: kuber.CommandAction):
      """
      Configure the bundle based on additional command line flags.
      """
      parser = argparse.ArgumentParser()
      parser.add_argument('--environment', default='development')

      args = parser.parse_args(action.custom_args)

      bundle = action.bundle
      for resource in bundle.resources:
          resource.metadata.labels.update(
              environment=args.environment
          )


  if __name__ == '__main__':
      # Load the current cluster configuration from `kubeconfig`
      # into kuber for access to operate on the cluster.
      kuber.load_access_config()

      # Load bundle resources from the configuration files
      # stored in the local *./some/directory* directory.
      bundle = kuber.from_directory('./some/directory')

      # Expose the bundle CRUD operations as a command
      # line interface, but invoke the CLI with the
      # specified callback before executing the action
      # to allow for additional configuration based on
      # the custom command line arguments supplied.
      bundle.cli.invoke(configure)

The same result as the previous example can then be achieved with the
commands:

.. code-block:: bash

  $ python3 resource.py create --environment=production

to create the resources in the cluster,

.. code-block:: bash

  $ python3 resource.py status

to get the statuses of the resources in the cluster, and

.. code-block:: bash

  $ python3 resource.py delete

to remove the resources from the cluster.

Invocation-Only Command Line Interface
--------------------------------------

The advanced example from above can be refactored yet again such that
all of the configuration is carried out within the callback. In this
case there is a convenience function ``kuber.cli()`` that simplifies
bundle creation and CLI execution with the pre-execution callback.
Refactoring the example from above would look like this:

.. code-block:: python

  import argparse

  import kuber


  def configure(action: kuber.CommandAction):
      """
      Configure the bundle entirely within this callback function.
      An empty bundle was created already and passed into this
      function as a member of the `action` object. Whatever changes
      are made to the bundle within this function will be reflected
      when the command line interface action is carried out after
      this function execution is complete.
      """
      bundle = action.bundle

      parser = argparse.ArgumentParser()
      parser.add_argument('--environment', default='development')
      args = parser.parse_args(action.custom_args)

      # Load the current cluster configuration from `kubeconfig`
      # into kuber for access to operate on the cluster.
      kuber.load_access_config()

      # Load bundle resources from the configuration files
      # stored in the local *./some/directory* directory.
      bundle.add_directory('./some/directory')

      for resource in bundle.resources:
          resource.metadata.labels.update(
              environment=args.environment
          )


  if __name__ == '__main__':
      # Expose the bundle CRUD operations as a command
      # line interface, but invoke the CLI with the
      # specified callback before executing the action
      # to allow for additional configuration based on
      # the custom command line arguments supplied.
      kuber.cli(configure)

.. autofunction:: kuber.cli

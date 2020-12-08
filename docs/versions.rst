Kubernetes Versions
===================

Unlike the lower-level
`Kubernetes Python Client <https://github.com/kubernetes-client/python>`_,
a single version of the kuber library contains multiple Kubernetes API
version targets within a single installation. When loading/creating
resources or resource bundles, the desired version of Kubernetes can be
specified.

Specifying Versions
-------------------

Kubernetes versions in kuber can be specified in two interchangeable ways:

- **Version Labels**: Versions can be specified as strings, e.g. ``"1.20"``, or
- **KubernetesVersion**: an object that contains the version label string
  along with other version related information.

In most cases, either of these can used. If the version label is used, it will
be converted to a ``KubernetesVersion`` object internally.

.. autoclass:: kuber.KubernetesVersion
   :members:

Explicit Versions
-----------------

Explicit Kubernetes versions in kuber are represented by the ``Major_Minor``
version syntax and prefixed with a ``v``, e.g. ``v1.20`` for version
``1.20.x``. The latest available patch level for each Kubernetes version will
always be used when generating the configuration subpackages in kuber. Patch
level distinctions are ignored by kuber because the configuration API is
consistent across patch versions.

For example, to using Kubernetes version ``1.20`` in kuber would look like:

.. code-block:: python

  from kuber.v1.20 import core_v1

  service = core_v1.Service()
  config_map = core_v1.ConfigMap()

Or when dealing with resource bundles, the version is specified when
creating the bundle and that version will be used by all resources loaded
by that bundle:

.. code-block:: python

  import kuber

  bundle = kuber.from_directory(
      "./foo/",
      kubernetes_version="1.20"
  )

Floating Versions
-----------------

To keep pace with the ongoing development of Kubernetes there are also
two special versions available, ``latest`` and ``pre`` that will float
from version to version over time. The ``latest`` version will always point
to the most recent stable version of Kubernetes available at the time the
library was published. Similarly, the ``pre`` version will always point to
the latest pre-release (alpha or beta) version of Kubernetes available at
the time of publishing.

These special version can be used in exactly the same way as the explicit
versions within kuber:

.. code-block:: python

  import kuber
  from kuber.latest import core_v1

  service = core_v1.Service()
  config_map = core_v1.ConfigMap()

  bundle = kuber.create_bundle("latest")
  bundle.add(service, config_map)

or for the pre-release version:

 .. code-block:: python

  from kuber.pre import core_v1

  service = core_v1.Service()
  config_map = core_v1.ConfigMap()

  bundle = kuber.create_bundle("pre")
  bundle.add(service, config_map)

To find out the specific version information for any versions, explicit or
floating, you can import that version of the package and print the version
info object constant in that module. For example, to find out the specific
version of the ``pre`` subpackage:

.. code-block:: python

  from kuber import pre

  print(pre.KUBERNETES_VERSION.version)


Cluster-based Versioning
------------------------

Often times it is most useful to write configurations that use the version
of the cluster in which they will be deployed instead of hard-coding a
version - even if it is a floating one. For that, kuber has a convenience
function that returns a ``KubernetesVersion`` object, which can be used
in place of a hard-coded version value. The function will connect to the
currently configured cluster and return the ``KubernetesVersion`` object
that best matches the cluster version.

In the f

.. code-block:: python

  import kuber

  # Establich connection to the cluster currently
  # configured in the local `.kubeconfig` file.
  kuber.load_access_config()

  # Get the version of the connected cluster or
  # default to version 1.20 if unable to fetch
  # version data from the cluster.
  cluster_version = kuber.get_version_from_cluster("1.20")

  # Use the returned `KubernetesVersion` object
  # as the version for the cluster.
  bundle = kuber.from_directory(
      "./foo/",
      kubernetes_version=cluster_version
  )

.. autofunction:: kuber.get_version_from_cluster

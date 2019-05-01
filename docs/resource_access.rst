Accessing Resources
===================

When using resource bundles, the Kubernetes resources are stored within the
``resources`` property of the ``ResourceBundle``. This ``resources`` property
behaves like a normal Python list, but it has additional functionality for
conveniently accessing resources by *namespace*, *kind* and *name* filtering.

Consider a case where we have the following resource definition file:

.. code-block:: yaml

  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: web-configs
    namespace: alpha

  ---
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: settings
    namespace: alpha

  ---
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: settings
    namespace: bravo

  ---
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: settings
    namespace: charlie

Such that the defined resources are:

*alpha* namespace:

- ConfigMap/web-configs
- ConfigMap/settings

*bravo* namespace:

- ConfigMap/settings

*charlie* namespace:

- ConfigMap/settings

Using the ``ResourceBundle.get()`` method shown elsewhere in the documentation
we could retrieve the *web-configs* resource as:

.. code-block:: python

  config_map = bundle.get(name='web-configs', kind='ConfigMap')

but another way to access this resource would be to use the dynamic accessors
on the ``resources`` object:

.. code-block:: python

  config_map = bundle.resources.config_map.web_configs

Here the ``resources`` object can be filtered dynamically by *kind*, which
returns a filtered ``resources`` object that can be filtered by *name*.

In the case above where we want to get the *settings* resource in the *charlie*
namespace, we can add a ``.within('charlie')`` filter to the resources object:

.. code-block:: python

  settings = bundle.resources.within('charlie').config_map.settings

If the ``.within('charlie')`` namespace filter is omitted, the ``resources``
object will recognize that there are multiple resources that match the
*kind* = ConfigMap and *name* = settings and instead return a tuple of all
of those resources instead of just a single resource:

.. code-block:: python

  for settings in bundle.resources.config_map.settings:
      print(settings.metadata.namespace)

  alpha_settings = bundle.resources.config_map.settings[0]

Case Conventions
----------------

From the examples above you can see that the dynamic accessors use snake_case.
This is to make the accessors match conventional casing inside Python.
Internally the values are converted to PascalCase for *kind* values and
kebab-case for *name* values as are the
`Kubernetes conventions <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>`_.

Kubernetes names also allow for the ``.`` character, which cannot be
represented in a Python variable name. In those cases dictionary-style
accessors can be used instead:

.. code-block:: python

  job = bundle.resources.job['my.job-name']

The dictionary-style accessors will also accept PascalCase for *kind* values.
Therefore, the *web-configs* from the earlier example can be accessed in any
of the following ways:

.. code-block:: python

  web_configs = bundle.resources.config_map.web_configs
  web_configs = bundle.resources['ConfigMap'].web_configs
  web_configs = bundle.resources['ConfigMap']['web-configs']

  # This one works because order is preserved when loading resources and
  # the web-configs resource was the first one defined. However, it is usually
  # preferred to reference by name instead of relying on order preservation.
  web_configs = bundle.resources['ConfigMap'][0]

Advanced Filtering
------------------

Ultimately the dynamic accessing of resources is meant to be used in simple
cases, while the ``.get()`` and ``.get_many()`` methods of resource bundles
can be used to do the same thing, but also allow for filtering based on
metadata labels:

.. automethod:: kuber.ResourceBundle.get

.. automethod:: kuber.ResourceBundle.get_many

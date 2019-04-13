ConfigMap with Files
====================

This example shows how a ``ConfigMap`` can be populated from files on
disk using Python to do the heavy lifting instead of having to store
the file data inside a ``ConfigMap`` resource configuration file.

.. literalinclude:: ../../examples/config-map/config-map.py
  :language: python

Complete code for this example is available at:
`kuber/examples/config-map/
<https://github.com/sernst/kuber/tree/master/examples/config-map>`_

From Helm Chart (Experimental)
==============================

This example shows the currently experimental functionality of generating a bundle
from a helm chart. It requires a helm 3 executable to be available for external
command execution for this to work as the helm executable is used to render the
chart and the rendered output is loaded into the kuber bundle for additional
processing.

.. literalinclude:: ../../examples/from-helm-chart/from-helm-chart.py
  :language: python

Complete code for this example is available at:
`kuber/examples/from-helm-chart/
<https://github.com/sernst/kuber/tree/master/examples/from-helm-chart>`_

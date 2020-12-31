Custom Objects
==============

Custom objects, which are custom resource definitions not specified by the Kubernetes
standard API, can be utilized and managed in kuber with the ``custom_v1.CustomObject``
resource. Any unknown resource definition encountered by Kuber will be assumed to be
a custom object and loaded as a ``custom_v1.CustomObject``.

For example, given the custom object definition below:

.. code-block:: yaml

  apiVersion: argoproj.io/v1alpha1
  kind: Workflow
  metadata:
    generateName: steps-
  spec:
    entrypoint: hello
    templates:
    - name: hello
      steps:
      - - name: hello
          template: whalesay
          arguments:
            parameters: [{name: message, value: "hello1"}]
    - name: whalesay
      inputs:
        parameters:
        - name: message
      container:
        image: docker/whalesay
        command: [cowsay]
        args: ["{{inputs.parameters.message}}"]

this can be loaded into a ``CustomObject`` resource directly:

.. code-block:: python

  import pathlib
  import yaml

  from kuber.latest import custom_v1

  workflow = typing.cast(
      custom_v1.CustomObject,
      kuber.from_yaml_file(directory.joinpath("workflow.yaml"))
  )


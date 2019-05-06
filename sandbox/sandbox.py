# import kuber
#
# bundle = kuber.create_bundle('pre')
# bundle.add_from_yaml(
#     """
#     apiVersion: core/v1
#     kind: Pod
#     metadata:
#       name: test
#     """
# )
# p = bundle.get('test')
# print(p)
# print(p.to_yaml())
#
# d = bundle.add('apps/v1', 'Deployment', 'dep').get('dep')
# print(d)
# print(d.to_yaml())

import kuber
from kuber.latest import core_v1

d: core_v1.Pod  = kuber.new_resource(
    api_version='v1',
    kind='Pod',
    name='my-pod',
    kubernetes_version='1.15'
)

d.spec.append_container(
    name='c',
    image='swernst/cauldron:current-standard',
    ports=[
        core_v1.ContainerPort(host_port=5010, container_port=5010)
    ]
)

print(d.to_yaml())

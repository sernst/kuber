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

d = kuber.new_resource(
    api_version='v1',
    kind='Pod',
    name='my-pod',
    kubernetes_version='1.15'
)

print(d.to_yaml())

import kuber

bundle = kuber.from_directory("../samples", kubernetes_version="pre")

# print(bundle.kubernetes_version)
# print(bundle.kubernetes_version.label)
# print(bundle.get('foo'))
# print(bundle.get('scott'))
# print(bundle.get(app='genesis', foo='1'))
# print(bundle.get(app='genesis'))

# print('\n--- BUNDLE ---')
# print(bundle.render_yaml_bundle())

print(bundle.resources.job.scott[0].to_yaml())
print(bundle.resources.within("foo").job.scott.to_yaml())

print(bundle.resources.deployment[0].metadata.name)
print(bundle.resources.deployment["genesis"].metadata.name)
print(bundle.resources.deployment.genesis.metadata.name)

for r in bundle.resources.job:
    print(f"{r.kind}/{r.metadata.name}")

for r in bundle.resources.within("foo").job:
    print(f"{r.kind}/{r.metadata.name}")

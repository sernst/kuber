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

print(bundle.array.job.scott[0].to_yaml())
print(bundle.array.within("foo").job.scott.to_yaml())

print(bundle.array.deployment[0].metadata.name)
print(bundle.array.deployment["genesis"].metadata.name)
print(bundle.array.deployment.genesis.metadata.name)

for r in bundle.array.job:
    print(f"{r.kind}/{r.metadata.name}")

for r in bundle.array.within("foo").job:
    print(f"{r.kind}/{r.metadata.name}")

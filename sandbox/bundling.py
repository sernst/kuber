import kuber

bundle = kuber.from_directory('../samples', kubernetes_version='pre')

print(bundle.kubernetes_version)
print(bundle.get_version_info().version)
print(bundle.get('foo'))
print(bundle.get('scott'))
print(bundle.get(app='genesis', foo='1'))
print(bundle.get(app='genesis'))

print('\n--- BUNDLE ---')
print(bundle.render_yaml_bundle())

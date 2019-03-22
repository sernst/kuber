import kuber
from kuber.v1_13.apps import v1 as apps_v1

# bundle = (
#     kuber.create_bundle()
#     .add_file('../samples/job.yaml')
#     .add_file('../samples/deployment.yaml')
# )

bundle = kuber.from_directory('../samples')

print(bundle.version)
print(bundle.get('foo'))
print(bundle.get('scott'))
print(bundle.get(app='genesis', foo='1'))
print(bundle.get(app='genesis'))

print('\n--- BUNDLE ---')
print(bundle.render_yaml_bundle())

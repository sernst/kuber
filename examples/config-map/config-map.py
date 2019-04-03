from kuber.latest import core_v1

config_map = core_v1.ConfigMap()

with config_map.metadata as md:
    md.name = 'glossary'
    md.namespace = 'reference'
    md.labels.update(typ='kubernetes', version='1.0')

with open('./data.json') as f:
    config_map.data['data.json'] = f.read()

print(config_map.to_yaml())

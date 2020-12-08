import kuber

result = kuber.from_yaml_file_multiple("../samples/bundle.yaml")
print(result)

b = kuber.from_file("../samples/bundle.yaml")
print(b.resources)

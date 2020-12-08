from kuber.latest import core_v1

config_map = core_v1.ConfigMap()

# Populate the metadata on the ConfigMap.
with config_map.metadata as md:
    md.name = "glossary"
    md.namespace = "reference"
    md.labels.update(topic="kubernetes", version="1.0")

# Load file from disk and add it to the ConfigMap's data
# object with the key `data.json`.
with open("./data.json") as f:
    config_map.data["data.json"] = f.read()

# Display results.
print(config_map.to_yaml())

import kuber
from kuber.v1_20 import apps_v1


def configure_deployment():
    shared_labels = {"app": "foo"}
    d = apps_v1.Deployment()

    with d.metadata as md:
        md.name = "my-deployment"
        md.labels.update(shared_labels, component="application")

    with d.spec as s:
        s.selector.match_labels.update(shared_labels)
        s.template.metadata.labels.update(shared_labels)
        s.replicas = 2

    d.append_container(name="app", image="my-app:1.0")

    return d


if __name__ == "__main__":
    bundle = kuber.create_bundle(kubernetes_version="1.13")
    bundle.push(configure_deployment())
    bundle.cli()

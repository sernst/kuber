import pathlib

import kuber

directory = pathlib.Path(__file__).parent.absolute()


def populate(action: kuber.CommandAction):
    """Populate the bundle"""
    bundle = action.bundle
    bundle.namespace = bundle.namespace or bundle.name

    # Add a namespace in which the bundle will reside.
    with bundle.new("v1", "Namespace", bundle.namespace).metadata as md:
        md.labels["name"] = bundle.namespace

    bundle.add_from_helm(
        chart_name="deliveryhero/locust",
        values_path=directory.joinpath("values.yaml"),
        repos={"deliveryhero": "https://charts.deliveryhero.io/"},
        update=True,
    )


if __name__ == "__main__":
    kuber.load_access_config()
    version = kuber.get_version_from_cluster("latest")
    kuber.cli(
        callback=populate, kubernetes_version=version, bundle_name="locust-load-test"
    )

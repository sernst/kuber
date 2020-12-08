import kuber
from kuber.latest import apps_v1
from kuber.latest import core_v1


def populate(action: kuber.CommandAction):
    """
    Populate the empty bundle that was created by the
    cli function call prior to calling this function.
    The action argument contains the bundle along with
    information about the command line execution.
    """
    bundle = action.bundle
    bundle.namespace = "prometheus"
    bundle.add_file("./resources.yaml")

    # Get the server container from the server
    # deployment for modification.
    deployment: apps_v1.Deployment = bundle.get(
        name="prometheus-server", kind="Deployment"
    )
    server: core_v1.Container = deployment.get_container("prometheus-server")

    # Override default retention time to be 7 days.
    server.args.append("--storage.tsdb.retention.time=7d")


if __name__ == "__main__":
    kuber.load_access_config()
    version = kuber.get_version_from_cluster("latest")
    kuber.cli(callback=populate, kubernetes_version=version, bundle_name="prometheus")

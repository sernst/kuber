import os
import subprocess
import shutil

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
ROOT_DIRECTORY = os.path.realpath(os.path.join(MY_DIRECTORY, '..'))


def update_api_docs():
    """Rebuilds the API documentation for the kuber library."""
    directory = os.path.join(ROOT_DIRECTORY, 'docs', 'modules')
    if os.path.exists(directory):
        shutil.rmtree(directory)

    os.chdir(ROOT_DIRECTORY)
    cmd = ['sphinx-apidoc', 'kuber', '-o', directory]
    subprocess.run(cmd).check_returncode()

    build_docs()


def build_docs():
    """Generates local sphinx docs."""
    path = os.path.join(ROOT_DIRECTORY, '_build')
    cmd = ['sphinx-build', '-M', 'html', ROOT_DIRECTORY, path]
    subprocess.run(cmd).check_returncode()

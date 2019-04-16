import sys
import os
import subprocess
import shutil

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
ROOT_DIRECTORY = os.path.realpath(os.path.join(MY_DIRECTORY, '..'))


def deploy_release():
    """Deploys the current version to PyPi."""
    print('\n\n=== BUILD & DEPLOY RELEASE ===\n')
    directory = os.path.join(ROOT_DIRECTORY, 'dist')
    if os.path.exists(directory):
        shutil.rmtree(directory)

    os.chdir(ROOT_DIRECTORY)

    cmd = [sys.executable, 'setup.py', 'sdist', 'bdist_wheel']
    subprocess.run(cmd).check_returncode()

    cmd = ['twine', 'upload', 'dist/kuber*']
    os.system(' '.join(cmd))

    print('\nOperation Complete.\n\n')

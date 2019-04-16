import os
import re

from setuptools import find_packages
from setuptools import setup

MY_DIRECTORY = os.path.dirname(__file__)


def get_version():
    path = os.path.join(MY_DIRECTORY, 'kuber', '__init__.py')
    with open(path, 'r') as f:
        return (
            re.compile(r'\n__version__\s+=\s+\'(?P<version>[0-9.]+)\'')
            .search(f.read())
            .group('version')
        )


def readme():
    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        'README.md'
    ))
    with open(path) as f:
        return f.read()


def populate_extra_files():
    """
    Creates a list of non-python data files to include in package distribution
    """
    return []


setup(
    name='kuber',
    version=get_version(),
    description=(
        'High-level Kubernetes resource '
        'configuration and management library.'
    ),
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords=['kubernetes', 'containers', 'kubectl', 'k8s'],
    url='https://github.com/sernst/kuber',
    author='Scott Ernst',
    author_email='swernst@gmail.com',
    license='MIT',
    platforms='Linux, Mac OS X, Windows',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': populate_extra_files()},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration'
    ],
    install_requires=['pyyaml', 'kubernetes'],
    extras_require={},
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov']
)

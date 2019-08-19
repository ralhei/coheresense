#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = open('requirements.txt').read().split()
setup_requirements = ['pytest-runner', ]
test_requirements = open('requirements_dev.txt').read().split()

setup(
    author="Ralph Heinkel",
    author_email='rh@ralph-heinkel.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Heart Coherence DIY project",
    entry_points={
        'console_scripts': [
            'cs=cohersense.sensor_cli:cli',     # cs: Coheresense Sensor
            'ca=cohersense.analyzer_cli:cli',   # ca: Coheresense Analyzer
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cohersense',
    name='cohersense',
    packages=find_packages(include=['cohersense']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ralhei/cohersense',
    version='0.1.0',
    zip_safe=False,
)

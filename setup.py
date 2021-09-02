from setuptools import setup, find_packages

setup(
    name='hw2b',
    version='1.0.0',
    packages=find_packages(),
    license='none',
    description='Building a CI pipeline for hw 2b',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

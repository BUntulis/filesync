'''
@description: Setup script for the filesync package.
'''

from setuptools import setup, find_packages

setup(
    name='filesync',
    version='1.0.0',
    description='File synchronization script with backup and versioning',
    author='Benas Untulis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'filesync = filesync.cli:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        # If there are any dependencies, list them here
    ],
)

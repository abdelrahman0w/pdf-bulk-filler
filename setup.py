import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name='bulk-pdf-filler',
    description='''
                ''',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.1.0',
    packages=['bulk-filler'],
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=[],
    license='MIT',
)

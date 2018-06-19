"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='opedia',
    version='0.1.15',
    description='Opedia is an open source database service to integrate, visualize, and analyze ocean datasets such as satellite data, in-situ observations, and model outputs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mdashkezari/opedia/tree/master/pypi',
    author='Mohammad D. Ashkezari',
    author_email='demo.80@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='ocean oceanography database dataset satellite model in-situ remote sensing machine learning data visualization',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['matplotlib', 'numpy', 'pandas', 'scipy', 'bokeh', 'pyodbc', 'dropbox'],
)

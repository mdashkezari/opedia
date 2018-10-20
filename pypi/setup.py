from setuptools import setup, find_packages
from codecs import open
from setuptools.command.develop import develop
from setuptools.command.install import install
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def postPIP():
    #f=open('E:/here.txt','w')
    #f.write(here)
    #f.close()
    pass
    return

class PostDevelopCommand(develop):
    def run(self):
        postPIP()
        develop.run(self)

class PostInstallCommand(install):
    def run(self):
        postPIP()
        install.run(self)
        

setup(
    name='opedia',
    version='0.1.51',
    description='Opedia is an open source database service to integrate, visualize, and analyze ocean datasets such as satellite data, in-situ observations, and model outputs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mdashkezari/opedia/tree/master/pypi',
    author='Mohammad D. Ashkezari',
    author_email='demo.80@gmail.com',
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='ocean oceanography database dataset satellite model in-situ remote sensing machine learning data visualization',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['matplotlib', 'numpy', 'pandas', 'scipy', 'bokeh', 'docopt', 'tqdm', 'pyodbc', 'dropbox'],
)

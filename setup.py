# coding: utf-8
from setuptools import setup


setup(
    name='pysuru',
    version='0.0.1',
    description='Python library to interact with Tsuru API',
    long_description=open('README.rst', 'r').read(),
    keywords='tsuru',
    author='Rodrigo Machado',
    author_email='rcmachado@gmail.com',
    url='https://github.com/rcmachado/pysuru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'urllib3>=1.15',
        'certifi'
    ],
    packages=['pysuru'],
    platforms=['linux', 'osx']
)

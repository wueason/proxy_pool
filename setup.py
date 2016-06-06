#!/usr/bin/env python
from setuptools import setup

# Get the long description from the README file
with open('README.md') as f:
    long_description = f.read()

setup(
    name='proxy_pool',
    version='0.0.1',
    description='A proxy pool which you can get an avaiable proxy http server.',
    long_description=long_description,
    url='https://github.com/wueason/proxy_pool',
    author='wueason',
    author_email='eason991@gmail.com',

	# License
    license='MIT',

    keywords = 'proxy crawl proxy_pool',

    # Installation requirement
    install_requires=['gevent>=1.1.1'],

    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    packages=['proxy_pool'],
)

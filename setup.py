#!/usr/bin/env python
from setuptools import setup

long_description = '''
A proxy pool which you can get an avaiable proxy http server. 
When we run a crawler for data collecting purpose, we always get blocked. 
This module may help you get out of the trouble.'''

setup(
    name='proxy_pool',
    version='0.0.2',
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

NAME = 'scanrpc'
DESCRIPTION = 'Simple command line application to scan the RPC calls of a Substrate node'
URL = 'https://github.com/PureStake/substrate-scanrpc'
EMAIL = 'devops@purestake.com'
AUTHOR = 'PURESTAKE'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None
LICENSE = 'MIT'
REQUIRED = [
    'substrate-interface>=0.13.8'
]

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['scanrpc'],
    entry_points={
        'console_scripts': ['scanrpc=scanrpc:main'],
    },
    data_files=[('etc/scanrpc', ['default.conf'])],
    install_requires=REQUIRED,
    license=LICENSE,
    project_urls={ 
        'Bug Reports': f'{URL}/issues',
        'Source': f'{URL}',
    },
)

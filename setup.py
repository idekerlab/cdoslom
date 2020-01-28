#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


with open(os.path.join('cdoslom', '__init__.py')) as ver_file:
    for line in ver_file:
        if line.startswith('__version__'):
            version=re.sub("'", "", line[line.index("'"):])

requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cdoslom',
    version=version,
    description="Runs Oslom community detection algorithm in a container",
    long_description=readme + '\n\n' + history,
    author="Song Cao",
    author_email='soc038@ucsd.edu',
    url='https://github.com/idekerlab/cdoslom',
    packages=[
        'cdoslom',
    ],
    package_dir={'cdoslom':
                 'cdoslom'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='cdoslom',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    scripts=['cdoslom/cdoslom.py'],
    test_suite='tests',
    tests_require=test_requirements
)

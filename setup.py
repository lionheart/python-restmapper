#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015-2017 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.cmd import Command
import os
import re
import unittest

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata = {}
metadata_file = "restmapper/metadata.py"
exec(compile(open(metadata_file).read(), metadata_file, 'exec'), metadata)

url = metadata['__url__']

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as file:
    long_description = file.read()

    id_regex = re.compile(r"<\#([\w-]+)>")
    link_regex = re.compile(r"<(\w+)>")
    link_alternate_regex = re.compile(r"   :target: (\w+)")

    long_description = id_regex.sub(r"<{}#\1>".format(url), long_description)
    long_description = link_regex.sub(r"<{}/blob/master/\1>".format(url), long_description)
    long_description = link_regex.sub(r"<{}/blob/master/\1>".format(url), long_description)
    long_description = link_alternate_regex.sub(r"   :target: {}/blob/master/\1".format(url), long_description)

# http://pypi.python.org/pypi?:action=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    "Topic :: Utilities",
    "License :: OSI Approved :: Apache Software License",
]

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test_restmapper import TestRestMapper
        suite = unittest.TestLoader().loadTestsFromTestCase(TestRestMapper)
        unittest.TextTestRunner(verbosity=2).run(suite)


setup(
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    classifiers=classifiers,
    cmdclass={'test': TestCommand},
    description="RestMapper takes the pain out of integrating with RESTful APIs",
    install_requires=["requests>=2.0.0"],
    keywords="restmapper",
    license=metadata['__license__'],
    long_description=long_description,
    name='restmapper',
    package_data={'': ['LICENSE', 'README.rst']},
    packages=['restmapper'],
    url=url,
    version=metadata['__version__'],
)

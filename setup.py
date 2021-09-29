# Copyright 2021 Rashad Alston

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os
from distutils.core import setup
from setuptools import find_packages


def derive_dependencies_from_pipenvlock():
    pipenvlock = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Pipfile.lock")
    data = {}
    with open(pipenvlock, "r") as f:
        data = json.load(f)

    dependencies = []
    for package_name, metadata in data["default"].items():
        tag = package_name
        dependencies.append(tag)

    return dependencies


setup(
    name="xmrpy",
    version=os.environ["VERSION"],
    python_requires=">=3.8",
    description="Python impelementation of Monero wallet JSON RPC client library",
    install_requires=derive_dependencies_from_pipenvlock(),
    include_package_data=True,
    platforms="any",
    keywords="xmr, monero, privacy",
    long_description=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "docs", "README.md")).read(),
    long_description_content_type="text/markdown",
    author="Rashad Alston <aar3>",
    author_email="rashad.a.alston@gmail.com",
    license="MIT",
    url="https://github.com/aar3/xmrpy",
    packages=find_packages(exclude=["test/*", "examples/*"]),
)

#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="confclass",
    version="0.0.0",
    long_description="",
    long_description_content_type="text/markdown",
    author="Pixelsquare",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10",
    zip_safe=False,
    include_package_data=True,
)
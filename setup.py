# -*- coding: utf-8 -*-
"""
    Setup file for datedown.
"""
import sys
from setuptools import setup, find_packages

# Read the long description from README.rst
try:
    with open("README.rst", "r") as f:
        long_description = f.read()
except:
    long_description = "Small library to download files with date and time based filenames or folder structures."

if __name__ == "__main__":
    setup(
        name="datedown",
        version="0.4",  # Static version number
        description="Small library to download files with date and time based filenames or folder structures. In parallel using wget.",
        long_description=long_description,
        long_description_content_type="text/x-rst; charset=UTF-8",
        author="Christoph Paulik",
        author_email="cpaulikk@vandersat.com",
        license="mit",
        url="https://github.com/daberer/datedown",
        project_urls={
            "Documentation": "https://github.com/cpaulik/datedown",
        },
        platforms=["any"],
        packages=find_packages(),
        install_requires=[
            "pygeobase",
            "progressbar2",
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python",
        ],
    )

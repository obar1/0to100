#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup, find_packages

directory = Path(__file__).resolve().parent
with open(directory / "README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="0to100",
    version="0.5.3",
    author="obar1",
    packages=find_packages(),
    author_email="obar1+gh@pm.me",
    description="Simple python tool to learn everything and keep it local.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/obar1/0to100",
    install_requires=[line.strip() for line in open("requirements.txt")],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU AFFERO",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

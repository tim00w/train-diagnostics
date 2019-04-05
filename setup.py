import os
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["bonkie-diagnostics>=0.1.0", "pandas>=0.24.0"]

setup(
    name="bonkie-diagnostics-businessrules",
    version="0.0.1",
    author="Timo Lesterhuis",
    author_email="timolesterhuis@gmail.com",
    description="A toolbox to analyse diagnostic train data!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tim00w/train-diagnostics/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)

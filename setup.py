from setuptools import setup, find_packages


with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ticts"]

setup(
    name="train-diagnostics",
    version="0.1.0",
    author="Timo Lesterhuis",
    author_email="timolesterhuis@gmail.com",
    description="A toolbox to analyse diagnostic train data!",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="https://github.com/timolesterhuis/train-diagnostics/",
    packages=find_packages(where="src"),
    install_requires=requirements,
    license="MIT License",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)

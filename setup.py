
from setuptools import find_packages, setup


setup(name="ncurus",
      packages=find_packages(),
      description=__doc__,
      long_description=open("README.md", encoding="utf-8").read())

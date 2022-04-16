from distutils.core import setup
from setuptools import find_packages
from subprocess import Popen
from subprocess import PIPE


def has_gpu():
    try:
        p = Popen(["nvidia-smi"], stdout=PIPE)
        stdout, stderror = p.communicate()
        return True

    except Exception:
        return False


with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = ["numpy"]


setup(
    name="tf_metrics",
    version="0.0.1",
    author="Guillaume Genthial",
    description="Multi-class metrics for Tensorflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(exclude=["test"]),
    classifiers=(
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    install_requires=install_requires
)

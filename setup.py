from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    # Your implementation here
    pass

setup(
    name="GENDER_PREDICTION",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
    # Other parameters
)

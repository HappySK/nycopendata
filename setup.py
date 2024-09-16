from setuptools import find_packages, setup
from typing import List

DELIMITER="-e ."

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_handler:
        requirements = file_handler.readlines()
        packages = [package.replace('\n', '') for package in requirements]
        packages.remove(DELIMITER)
    return packages

REQUIREMENTS = 'requirements.txt'

setup(
    name="nycopendata",
    version="0.0.1",
    author="Sravan Kumar",
    author_email="shravanyoserene1729@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(REQUIREMENTS)
)
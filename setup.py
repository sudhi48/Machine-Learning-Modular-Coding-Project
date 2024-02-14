from typing import List

from setuptools import find_packages, setup

PROJECT_NAME="Machine Learning Project"
VERSION="0.0.1"
DESCRIPTION="This is Machine Learning Project In Modular Coding"
AUTHOR="Sudheesh A S"
AUTHOR_EMAIL="relicsdark@gmail.com"
REQUIREMENT_FILE_PATH="requirement.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_PATH) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()

)

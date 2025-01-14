from setuptools import find_packages,setup
from typing import List

def get_requirements(file:str)->List[str]:
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements



setup(

    name="ML Project",
    author="Ninad Abhyankar",
    version = "0.0.1",
    packages = find_packages(),
    install_requires=get_requirements('requirement.txt')
)
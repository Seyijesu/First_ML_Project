from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will retuen the list of requiremnts
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
name = "mlproject" ,
version = '0.0.1',
author= "Oluwaseyi",
author_email= "olalekeoluwaseyi@gmail.com",
packages=find_packages(),
install_reqiures = get_requirements("requirements.txt")


)
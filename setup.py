from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open ('requirements.txt','r') as file_obj:
            lines=file_obj.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
        return requirement_lst
    except FileNotFoundError:
        print('file not found')
print(get_requirement())



setup(
    name='Netoek security',
    version='0.0.1',
    author='dhanush',
    author_email='dk071849@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement()
)

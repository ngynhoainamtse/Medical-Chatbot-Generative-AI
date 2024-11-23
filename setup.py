# Set up project as local package 

from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version= '0.0.0',
    author= 'Hoai-Nam NGUYEN',
    author_email= 'ngynhoainam@gmail.com',
    packages= find_packages(), # search for __init__.py and consider folder 'src' as a local package  => import anything from src itself
    install_requires = []

)
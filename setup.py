from setuptools import find_packages, setup

# python setup.py bdist_wheel || python -m build
# python -m twine upload --repository pypi dist/*

setup(
    name='lib_ms_api',
    packages=find_packages(include=['lib_ms_api']),
    version='1.0.0',
    description='A Python library to build simple Microservices',
    author_email='uedsonreis@gmail.com',
    author='Uedson Reis',
    license='ISC',
)
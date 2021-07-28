from setuptools import _install_setup_requires, setup, version, find_packages

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="delivery",
    version='0.1.0',
    description="Sistema de pedidos Helio Pizza",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={
        'dev': read('requirements-dev.txt')
    },
)
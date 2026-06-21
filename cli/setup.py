from setuptools import setup, find_packages

setup(
    name='addbiomechanics',
    version='0.1',
    author='Keenon Werling',
    author_email='keenon@stanford.edu',
    description='A local-only command line interface for processing biomechanics data',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'addb=addbiomechanics.addb:main',
        ],
    },
    include_package_data=True,
    package_data={
        'addbiomechanics': ['data/**'],
    },
    install_requires=[]
)

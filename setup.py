from setuptools import setup, find_packages

setup(
    name='example-shu244',
    version='0.1.0',
    author="Shuhao Lai",
    author_email="Shuhaolai18@gmail.com",
    description="A small example package",
    packages=find_packages(include=['exampleproject', 'exampleproject.*', 'exampleproject2', 'exampleproject2.*']),
    install_requires=[
        'numpy>=1.14.5',
    ],
    extras_require={
        'interactive': ['matplotlib>=2.2.0'],
    },
    entry_points={
        'console_scripts': ['my-command=exampleproject.example:main']
    },
    package_data={'exampleproject': ['data/some_data.json']},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
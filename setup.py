from setuptools import find_packages, setup

setup(name='nesting',
    packages=find_packages(include=['nesting']),
    version='1.0.0',
    description='Managing elements in nested objects.',
    author='Gonzalo Fuertes Sémelas',
    author_email='gfsemelas@gmail.com',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
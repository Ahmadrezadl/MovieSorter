from setuptools import setup

setup(
    name='MovieSorter',
    version='2.2.0',
    author='Ahmadrezadl',
    author_email='ahmadrezakml@gmail.com',
    packages=['src','src/resources'],
    entry_points={
        'console_scripts': [
            'MovieSorterGUI=src.GUI:main',
            'MovieSorter=src.console:main',
        ],
    },
    url='http://pypi.python.org/pypi/MovieSorter/',
    license='LICENSE.txt',
    description='An awesome package for sorting movies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "click>=7.1.2",
        "EasySettings>=4.0.0"
    ],
)

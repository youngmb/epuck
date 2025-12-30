from setuptools import setup, find_packages

setup(
    name='epuck', 
    version='0.1', 
    packages=find_packages(),  # Automatically finds packages in the current directory
    install_requires=[
        'pyserial'
        ],  
    description='A library for controlling and interacting with e-pucks.',
    author='James Young',  
    author_email='young@cs.umanitoba.ca',
    url='https://github.com/yourusername/epuck',  # Optional, if you’re hosting it on GitHub or similar
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change to whatever license you use
        'Operating System :: OS Independent',
    ],
)
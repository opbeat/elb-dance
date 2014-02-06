#!/usr/bin/env python
"""
elb-dance
======

elb-dance is used to deregister and register instances with ELB.
It can register and block until the instance is back "In Service".

"""

from setuptools import setup, find_packages
from elb_dance.version import VERSION

tests_require = [
    'mock',
    'pep8',
]

install_requires = ['boto>=2.24.0']

setup(
    name='elb-dance',
    version=VERSION,
    author='Ron Cohen',
    author_email='ron@opbeat.com',
    url='http://github.com/opbeat/elb-dance',
    description='elb-dance is used to deregister and register instances with ELB',
    long_description=__doc__,
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'elb-dance = elb_dance.cli:cli_entry',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
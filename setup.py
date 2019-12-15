#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
#

from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='hejtado-config',
    version='0.1.0',
    description='Hejtado Config RESTful microservice based on Flask and Flask-RESTPlus',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/hejtado/config',
    author='Lumir Jasiok',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',
    include_package_data=True,
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    hejtado-config = hejtado.config.app:main
    """,
    install_requires=['setuptools==41.4.0', 'flask-restplus==0.13.0'],
)

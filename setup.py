"""
Standard Setup script
"""
import datetime

from setuptools import setup, find_packages

setup(
    name="Demo App",
    version="0.%s" % datetime.datetime.now().strftime("%s"),
    packages=find_packages(),
    author="William Clemens",

    install_requires=[
        'Flask-Cache>=0.13.1',
        'Flask-SQLAlchemy>=2.0',
        'Flask-Script>=2.0.5',
        'Flask>=0.10.1',
        #'redis>=2.10.3', # Needed if using redis as a cache engine
    ],

    package_data={
        'myapp': [
            'static/*',
            'templates/*',
        ],
    },

    entry_points={
        'console_scripts': [
            'myapp=myapp.command:main_cli',
        ]
    },
)

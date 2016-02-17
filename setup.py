import os
from setuptools import setup, find_packages


version = '0.0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as file:
    long_description = file.read()

setup(
    name="flask-sqlalchemy-rls",
    version=version,
    packages=find_packages(exclude=('examples')),
    install_requires=['flask_sqlalchemy', 'flask_login', 'flask'],
    package_data={'': ['*.rst']},
    author="Charlie Wolf",
    author_email="charlie@flow180.com",
    description="Flask-SQLAlchemy with row-level security",
    license="MIT+Tequilaware",
    keywords=["row level security"],
    url="https://github.com/flow180/flask-sqlalchemy-rls",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Topic :: Utilities",
    ],
)

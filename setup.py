"""
Flask-PyNgrok
-------------

Flask support for PyNgrok to expose local web server.
"""
from setuptools import setup

with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="Flask-PyNgrok",
    version="1.1.0",
    url="https://github.com/sidshrivastav/Flask-PyNgrok",
    license="MIT",
    author="Siddhant Shrivastav",
    author_email="siddhantshrivastava@outlook.com",
    description="Add tunneling support to your Flask Application.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["flask_pyngrok"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask", "pyngrok>=5.0.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

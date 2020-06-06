"""
Flask-PyNgrok
-------------

Flask support for PyNgrok to expose local web server.
"""
from setuptools import setup


setup(
    name='Flask-PyNgrok',
    version='1.0',
    url='',
    license='BSD',
    author='Siddhant Shrivastav',
    author_email='siddhantshrivastava@outlook.com',
    description='Add tunneling support to your Flask Application.',
    long_description=__doc__,
    packages=['flask_pyngrok'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pyngrok'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
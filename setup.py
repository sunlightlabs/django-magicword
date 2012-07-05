#!/usr/bin/env python

from distutils.core import setup

setup(
    name='magicword',
    version='1.0',
    description='Single word authentication',
    long_description='Use a single word to password protect a page or site.',
    license='BSD',
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    url='https://github.com/sunlightlabs/django-magicword',
    download_url='',
    packages=['magicword'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from codecs import open
import os
import re
from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()

with open(os.path.join('jpbizday', '__init__.py'), 'r', encoding='utf8') as f:
     version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name="jpbizday",
    version=version,
    url='https://github.com/sig9org/jpbizday',
    description='Pure-Python Japan Business Day Generator',
    long_description='{}'.format((open('README.rst', encoding='utf8').read())),
    author='sig9',
    author_email='sig9@sig9.org',
    license='MIT License',
    install_requires=_requires_from_file('requirements.txt'),
    keywords=['Business Day', 'Holiday', 'Japan'],
    maintainer='sig9',
    maintainer_email='sig9@sig9.org',
    packages=['jpbizday'],
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

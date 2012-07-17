#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='Butteur',
      version='0.1',
      description='a preprocessor to write beamers slide more easily',
      author='Laurent Peuch',
      long_description=open("README").read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/butteur',
      install_requires=['jinja2', 'ply'],
      license= 'gplv3+',
      scripts=['butteur'],
      keywords='latex beamer preprocessor',
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:

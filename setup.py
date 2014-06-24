#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
UTF8 Coq keyword translation filter for Pygments.
"""

from setuptools import setup

entry_points = """
[pygments.filters]
coqkwfilter = utf8CoqFilter.utf8CoqFilter:CoqUTFFilter
"""

setup(name = 'coqkwfilter',
  version  = '0.1',
  description  = __doc__,
  author       = "Alan Schmitt",
  packages     = ['utf8CoqFilter'],
  entry_points = entry_points)

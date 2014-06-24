#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
keyword rename filter for Pygments.
"""

from setuptools import setup

entry_points = """
[pygments.filters]
kwrenamefilter = KeywordRename:KWRenameFilter
"""

setup(name = 'kwrenamefilter',
  version  = '0.1',
  description  = __doc__,
  author       = "Alan Schmitt",
  packages     = ['KeywordRename'],
  entry_points = entry_points)

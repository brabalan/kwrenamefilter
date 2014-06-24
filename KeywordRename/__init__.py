# -*- coding: utf-8 -*-
from pygments.token import Keyword
from pygments.filter import Filter

class KWRenameFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
	    if ttype is Keyword and value == 'forall':
	        value = value.replace('forall',u'∀')
            elif ttype is Keyword and value == 'exists':
	        value = value.replace('exists',u'∃')
            yield ttype, value

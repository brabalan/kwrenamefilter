# -*- coding: utf-8 -*-
from pygments.token import Keyword
from pygments.filter import Filter

class CoqUTFFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
	    if ttype is Keyword and value == 'forall':
	        value = value.replace('forall',u'∀')
            yield ttype, value

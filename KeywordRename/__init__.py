# -*- coding: utf-8 -*-
from pygments.token import Keyword
from pygments.token import Operator
from pygments.filter import Filter

class KWRenameFilter(Filter):
    transdict = {'forall' : u'∀', 'exists' : u'∃', '->' : u'→', '~' : u'¬', '<->' : u'↔', '=>' : u'⇒', '/\\' : u'∧', '\\/' : u'∨'}

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
            v = value.encode('utf-8').__str__()
	    if (ttype is Keyword or ttype is Operator) and v in self.transdict:
	        value = value.replace(v,self.transdict[v])
            yield ttype, value

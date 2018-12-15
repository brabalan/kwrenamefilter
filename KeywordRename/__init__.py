# -*- coding: utf-8 -*-
from pygments.token import Keyword
from pygments.token import Operator
from pygments.token import Name
from pygments.filter import Filter

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

class KWRenameFilter(Filter):
    if PY2:
        transdict = {'forall' : u'∀', 'exists' : u'∃', '->' : u'→', '~' : u'¬', '<->' : u'↔', '=>' : u'⇒', '/\\' : u'∧', '\\/' : u'∨'}
    if PY3:
        transdict = {'forall' : '∀', 'exists' : '∃', '->' : '→', '~' : '¬', '<->' : '↔', '=>' : '⇒', '/\\' : '∧', '\\/' : '∨'}

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
            if PY2:
                v = value.encode('utf-8').__str__()
            if PY3:
                v = value.__str__()
            if (ttype is Keyword or ttype is Operator) and v in self.transdict:
                value = value.replace(v,self.transdict[v])
            yield ttype, value

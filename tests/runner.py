#!/usr/bin/env python
# -*- coding: utf-8 -*-


from commandlines import Command

import sys

from commandlines.library import Mops

m = Mops(['-abcda', 'b', 'c', 'c', 'd'])
print(m)
print(m.contains('a'))
print(m.contains('f'))

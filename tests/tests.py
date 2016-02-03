#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import shlex

from commandlines import Command

# command = "execute --help define -h --test=defarg lastpos"
# sys.argv = shlex.split(command)

c = Command()
print(c.defs)
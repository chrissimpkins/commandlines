#!/usr/bin/env python
# -*- coding: utf-8 -*-


from commandlines import Command

import sys
import shlex


test_command_1 = "executable -- lastpos -s another"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

set_sysargv(test_command_1)

c = Command()
print(c.obj_string())


#!/usr/bin/env python
# -*- coding: utf-8 -*-


from commandlines import Command

import sys
import shlex


test_command_1 = "executable subcmd -s --long -n shortdef --name longdef --nameeq=longdefeq lastpos"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

set_sysargv(test_command_1)

c = Command()
print(c.obj_string())


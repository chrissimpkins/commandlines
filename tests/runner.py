#!/usr/bin/env python
# -*- coding: utf-8 -*-


from commandlines import Command

import sys
import shlex


test_command_1 = "executable subcmd -s --long -n shortdef --name longdef --nameeq=longdefeq lastpos"
test_command_13 = "executable -o path1 -o path2 -t --flag"
test_command_18 = "executable -o path1 -o path2 --file tests/path1 --file tests/path2"
test_command_19 = "executable -mops -t --test=bogus --test=another --help me"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

set_sysargv(test_command_1)

c = Command()
print(c.obj_string())


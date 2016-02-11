#!/usr/bin/env python
# -*- coding: utf-8 -*-


from commandlines import Command

import sys
import shlex


test_command_1 = "executable --taylor swift"
test_command_13 = "executable -o path1 -o path2 -t --flag"
test_command_18 = "executable -o path1 -o path2 --file tests/path1 --file tests/path2"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

set_sysargv(test_command_18)

c = Command()
print(c.mdefs)


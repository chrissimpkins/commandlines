#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import sys
import pytest

from commandlines import Command
from commandlines.exceptions import MissingArgumentError

# TESTS OVERVIEW: Command object getter method tests

test_command_1 = "executable subcmd -s --long -n shortdef --name longdef --nameeq=longdefeq lastpos"
test_command_2 = "executable -s lastpos"
test_command_3 = "executable --long lastpos"
test_command_4 = "executable -v -V lastpos"
test_command_5 = "executable --test-option lastpos"
test_command_6 = "apt-get install git-all"
test_command_7 = "git commit -m 'initial commit'"
test_command_8 = "find . -name tests/aaa.txt"
test_command_9 = "executable -mops -t lastpos"
test_command_10 = "executable subcmd subsubcmd"
test_command_11 = "executable -t def1 -r def2 lastpos"
test_command_11 = "executable -t --name -- lastpos -n --long another"  # double dash command line idiom
test_command_12 = "executable --file path -- lastpos --test path2 another"
test_command_13 = "executable --f path -- lastpos -t path2 another"
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)


# BEGIN TESTS

def test_command_has_doubledash_false():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_double_dash() == False


def test_command_has_doubledash_present():
    set_sysargv(test_command_11)
    c = Command()
    assert c.has_double_dash() == True


def test_command_has_doubledash_present_2():
    set_sysargv(test_command_12)
    c = Command()
    assert c.has_double_dash() == True


def test_command_has_doubledash_present_3():
    set_sysargv(test_command_13)
    c = Command()
    assert c.has_double_dash() == True




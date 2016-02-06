#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import shlex
import pytest

from commandlines import Command

# TESTS OVERVIEW: Command object validation method tests

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
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"

test_commands_with_args = [
    test_command_1,
    test_command_2,
    test_command_3,
    test_command_4,
    test_command_5,
    test_command_6,
    test_command_7,
    test_command_8,
    test_command_9,
    test_command_10
]

test_commands_without_args = [
    test_command_empty_1,
    test_command_empty_2
]

test_commands_with_defs = [
    test_command_1,
    test_command_2,
    test_command_3,
    test_command_4,
    test_command_5,
    test_command_7,
    test_command_8,
    test_command_9
]

test_commands_without_defs = [
    test_command_6,
    test_command_10
]


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)


#
# Does not validate methods
#

def test_command_dnval_args():
    for command in test_commands_with_args:
        set_sysargv(command)
        c = Command()
        assert c.does_not_validate_missing_args() == False


def test_command_dnval_args_when_missing():
    for command in test_commands_without_args:
        set_sysargv(command)
        c = Command()
        assert c.does_not_validate_missing_args() == True
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import shlex
import pytest

from commandlines import Command

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
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

# BEGIN TESTS


def test_command_get_short_def():
    set_sysargv(test_command_2)
    c = Command()
    assert c.get_definition('s') == "lastpos"


def test_command_get_long_def():
    set_sysargv(test_command_3)
    c = Command()
    assert c.get_definition('long') == "lastpos"


def test_command_get_short_def_multioption_command():
    set_sysargv(test_command_1)
    c = Command()
    assert c.get_definition('n') == "shortdef"


def test_command_get_long_def_multioption_command():
    set_sysargv(test_command_1)
    c = Command()
    assert c.get_definition('name') == "longdef"


def test_command_get_alternate_short_def_syntax():
    set_sysargv(test_command_8)
    c = Command()
    assert c.get_definition('name') == "tests/aaa.txt"


def test_command_get_def_when_no_defs():
    set_sysargv(test_command_6)
    c = Command()
    assert c.get_definition('bogus') == ""  # should return empty string


def test_command_get_def_when_unavailable_def():
    set_sysargv(test_command_1)
    c = Command()
    assert c.get_definition('bogus') == ""  # should return empty string


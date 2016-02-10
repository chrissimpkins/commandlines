#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import sys
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


#
# _get_object_string_format_arg method
#

def test_command_get_formatted_obj_string():
    set_sysargv(test_command_1)
    c = Command()
    assert c._get_obj_string_format_arg("test") == "'test'"


def test_command_get_formatted_obj_string_empty():
    set_sysargv(test_command_1)
    c = Command()
    assert c._get_obj_string_format_arg("") == "''"


#
# obj_string method
#

def test_command_obj_string():
    set_sysargv(test_command_1)
    c = Command()
    returned_string = c.obj_string()
    returned_string_list = returned_string.split("\n")
    assert returned_string_list[0] == """obj.arguments = ['subcmd', '-s', '--long', '-n', 'shortdef', '--name', 'longdef', '--nameeq=longdefeq', 'lastpos']"""
    # sets/dicts are not ordered, __repr__ and __str__ methods are tested with fewer values in Mops and Switches test modules
    # assert returned_string_list[1] == """obj.switches = Switches({'s', 'name', 'long', 'n'})"""
    #assert returned_string_list[2] == """obj.defs = {'n': 'shortdef', 'nameeq': 'longdefeq', 'name': 'longdef'}"""
    assert returned_string_list[3] == """obj.mops = {}"""
    assert returned_string_list[4] == """obj.argc = 9"""
    assert returned_string_list[5] == """obj.arg0 = 'subcmd'"""
    assert returned_string_list[6] == """obj.arg1 = '-s'"""
    assert returned_string_list[7] == """obj.arg2 = '--long'"""
    assert returned_string_list[8] == """obj.arg3 = '-n'"""
    assert returned_string_list[9] == """obj.arg4 = 'shortdef'"""
    assert returned_string_list[10] == """obj.arglp = 'lastpos'"""
    assert returned_string_list[11] == """obj.subcmd = 'subcmd'"""
    assert returned_string_list[12] == """obj.subsubcmd = '-s'"""


def test_command_obj_string_2():
    set_sysargv(test_command_9)
    c = Command()
    returned_string = c.obj_string()
    returned_string_list = returned_string.split("\n")
    assert returned_string_list[9] == "obj.arg4 = ''"


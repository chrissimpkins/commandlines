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
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

# BEGIN TESTS

#
# Switches
#


def test_command_contains_switches_single():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_switches("s") == True


def test_command_contains_switches_multiple():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_switches("s", "long", "name") == True


def test_command_contains_switches_differentcase():
    set_sysargv(test_command_4)
    c = Command()
    assert c.contains_switches("v", "V") == True


def test_command_contains_switches_alt_long():
    set_sysargv(test_command_8)
    c = Command()
    assert c.contains_switches("name") == True


def test_command_contains_switches_when_switch_notpresent():
    set_sysargv(test_command_4)
    c = Command()
    assert c.contains_switches("bogus") == False


def test_command_contains_switches_when_one_switch_notpresent():
    set_sysargv(test_command_4)
    c = Command()
    assert c.contains_switches("v", "V", "bogus") == False


def test_command_contains_switches_noargs():
    set_sysargv(test_command_empty_1)
    c = Command()
    assert c.contains_switches("name") == False


#
# Definitions
#

def test_command_contains_defs_single_short():
    set_sysargv(test_command_2)
    c = Command()
    assert c.contains_definitions("s") == True


def test_command_contains_defs_multiple_short():
    set_sysargv(test_command_11)
    c = Command()
    assert c.contains_definitions("t", "r") == True


def test_command_contains_defs_single_long():
    set_sysargv(test_command_3)
    c = Command()
    assert c.contains_definitions("long") == True


def test_command_contains_defs_multiple_alt_long():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_definitions("nameeq") == True


def test_command_contains_defs_multiple_long():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_definitions("name", "nameeq") == True


def test_command_contains_defs_when_arg_multiword():
    set_sysargv(test_command_7)
    c = Command()
    assert c.contains_definitions("m") == True


def test_command_contains_defs_long_when_not_present():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_definitions("bogus") == False


def test_command_contains_defs_when_single_not_present():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_definitions("n", "name", "bogus") == False


def test_command_contains_defs_noargs():
    set_sysargv(test_command_empty_1)
    c = Command()
    assert c.contains_definitions("name") == False


#
# Code sequence
#

def test_command_contains_codeseq():
    set_sysargv(test_command_10)
    c = Command()
    assert c.has_command_sequence("subcmd", "subsubcmd") == True


def test_command_contains_codeseq_fail():
    set_sysargv(test_command_10)
    c = Command()
    assert c.has_command_sequence("subcmd", "bogus") == False


def test_command_contains_codeseq_with_options():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_command_sequence("subcmd", "-s", "--long") == True


def test_command_contains_codeseq_with_options_fail():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_command_sequence("subcmd", "-s", "bogus") == False


def test_command_contains_codeseq_with_dashes():
    set_sysargv(test_command_6)
    c = Command()
    assert c.has_command_sequence("install", "git-all") == True


def test_command_contains_codeseq_with_dashes_fail():
    set_sysargv(test_command_6)
    c = Command()
    assert c.has_command_sequence("install", "bogus") == False


def test_command_contains_codeseq_noargs():
    set_sysargv(test_command_empty_1)
    c = Command()
    assert c.has_command_sequence("name", "bogus") == False


#
# Has args after
#

def test_command_has_args_after_default_number_1():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_args_after("--name") == True


def test_command_has_args_after_default_number_1_fail():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_args_after("lastpos") == False


def test_command_has_args_after_default_number_1_parameter_noexist():
    set_sysargv(test_command_empty_1)
    c = Command()
    with pytest.raises(MissingArgumentError):
        c.has_args_after("bogus")


def test_command_has_args_after_number_2():
    set_sysargv(test_command_1)
    c = Command()
    assert c.has_args_after("--name", number=2) == True


def test_command_has_args_after_number_2_fail():
    set_sysargv(test_command_10)
    c = Command()
    assert c.has_args_after("subcmd", number=2) == False


def test_command_has_args_after_noargs():
    set_sysargv(test_command_empty_1)
    c = Command()
    with pytest.raises(MissingArgumentError):
        c.has_args_after("subcmd")


#
# Next arg is in
#

def test_command_next_arg_isin_correct():
    set_sysargv(test_command_10)
    c = Command()
    assert c.next_arg_is_in("subcmd", ['subsubcmd']) == True


def test_command_next_arg_isin_correct_multiple_possible():
    set_sysargv(test_command_10)
    c = Command()
    assert c.next_arg_is_in("subcmd", ['subsubcmd', 'test', 'bogus']) == True


def test_command_next_arg_isin_correct_notcontained():
    set_sysargv(test_command_10)
    c = Command()
    assert c.next_arg_is_in("subcmd", ['bogus']) == False


def test_command_next_arg_isin_correct_notcontained_multi():
    set_sysargv(test_command_10)
    c = Command()
    assert c.next_arg_is_in("subcmd", ['nope', 'test', 'bogus']) == False


def test_command_next_arg_isin_correct_badargument():
    set_sysargv(test_command_10)
    c = Command()
    with pytest.raises(MissingArgumentError):
        c.next_arg_is_in("bogus", ['subsubcmd', 'test', 'bogus'])
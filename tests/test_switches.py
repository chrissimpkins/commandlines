#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import pytest

from commandlines.library import Switches
from commandlines.exceptions import IndexOutOfRangeError, MissingArgumentError

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


def create_argv(argstring):
    return shlex.split(argstring)[1:]

# BEGIN TESTS


def test_switches_instantiation():
    switch = Switches(create_argv(test_command_1))
    assert isinstance(switch, set)
    assert len(switch) == 4
    assert ("s" in switch) == True
    assert ("long" in switch) == True
    assert ("n" in switch) == True
    assert ("name" in switch) == True


def test_switch_instantiation_noswitches():
    switch = Switches(create_argv(test_command_6))
    assert isinstance(switch, set)
    assert len(switch) == 0


def test_switch_instantiation_with_mops():
    switch = Switches(create_argv(test_command_9))
    assert isinstance(switch, set)
    assert len(switch) == 2
    assert ("t" in switch) == True
    assert ("mops" in switch) == True


def test_switches_contains():
    switch = Switches(create_argv(test_command_1))
    assert len(switch) == 4
    assert switch.contains(['s']) == True
    assert switch.contains(['long']) == True
    assert switch.contains(['n']) == True
    assert switch.contains(['name']) == True
    assert switch.contains(['s', 'long']) == True
    assert switch.contains(['long', 'name']) == True
    assert switch.contains(['bogus']) == False
    assert switch.contains(['s', 'long', 'bogus']) == False
    assert switch.contains(['']) == False


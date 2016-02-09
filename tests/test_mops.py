#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import pytest

from commandlines.library import Mops

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
test_command_11 = "executable -mops -test lastpos"
test_command_12 = "executable -mo -t lastpos"
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def create_argv(argstring):
    return shlex.split(argstring)[1:]

# BEGIN TESTS

def test_mops_repr_method():
    mops_set = Mops(create_argv(test_command_12))
    assert len(mops_set) == 2
    assert mops_set.__repr__() == """Mops({'m', 'o'})""" or mops_set.__repr__() == """Mops({'o', 'm'})"""


def test_mops_repr_method_empty():
    mops_set = Mops(create_argv(test_command_2))
    assert len(mops_set) == 0
    assert mops_set.__repr__() == """Mops({})"""


def test_mops_str_method():
    mops_set = Mops(create_argv(test_command_12))
    assert len(mops_set) == 2
    assert mops_set.__str__() == """Mops({'m', 'o'})""" or mops_set.__repr__() == """Mops({'o', 'm'})"""


def test_mops_str_method_empty():
    mops_set = Mops(create_argv(test_command_2))
    assert len(mops_set) == 0
    assert mops_set.__str__() == """Mops({})""" or mops_set.__repr__() == """Mops({})"""


def test_mops_instantiation():
    mops_set = Mops(create_argv(test_command_9))
    assert len(mops_set) == 4
    assert ("m" in mops_set) == True
    assert ("o" in mops_set) == True
    assert ("p" in mops_set) == True
    assert ("s" in mops_set) == True
    assert ("z" in mops_set) == False


def test_mops_instantiation_multiple_mops_in_command():
    mops_set = Mops(create_argv(test_command_11))
    assert len(mops_set) == 6    # set data type should eliminate multiple requested switches that are the same
    assert ("m" in mops_set) == True
    assert ("o" in mops_set) == True
    assert ("p" in mops_set) == True
    assert ("s" in mops_set) == True
    assert ("t" in mops_set) == True
    assert ("e" in mops_set) == True
    assert ("z" in mops_set) == False


def test_mops_contains():
    mops_set = Mops(create_argv(test_command_9))
    assert len(mops_set) == 4
    assert mops_set.contains(("m")) == True
    assert mops_set.contains(("m", "o")) == True
    assert mops_set.contains(("m", "o", "p")) == True
    assert mops_set.contains(("m", "o", "p", "s")) == True
    assert mops_set.contains(("b")) == False       # switch character that is not present should yield False
    assert mops_set.contains(("m", "b")) == False  # single missing switch character should yield False

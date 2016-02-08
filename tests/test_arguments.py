#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import pytest

from commandlines.library import Arguments
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


def test_argument_instantiation():
    argu = Arguments(create_argv(test_command_1))
    assert len(argu) == 9

    assert argu[0] == "subcmd"
    assert argu[1] == "-s"
    assert argu[2] == "--long"
    assert argu[3] == "-n"
    assert argu[4] == "shortdef"
    assert argu[5] == "--name"
    assert argu[6] == "longdef"
    assert argu[7] == "--nameeq=longdefeq"
    assert argu[8] == "lastpos"


def test_argument_get_argument_method():
    argu = Arguments(create_argv(test_command_1))
    assert argu.get_argument(0) == "subcmd"
    assert argu.get_argument(1) == "-s"
    assert argu.get_argument(2) == "--long"
    assert argu.get_argument(7) == "--nameeq=longdefeq"
    with pytest.raises(IndexOutOfRangeError):
        argu.get_argument(20) == ""


def test_argument_get_arg_position():
    argu = Arguments(create_argv(test_command_1))
    assert len(argu) == 9
    assert argu.get_arg_position("subcmd") == 0
    assert argu.get_arg_position("-s") == 1
    assert argu.get_arg_position("--long") == 2
    assert argu.get_arg_position("lastpos") == 8
    with pytest.raises(MissingArgumentError):
        argu.get_arg_position("bogus")


def test_argument_contains():
    argu = Arguments(create_argv(test_command_1))
    assert len(argu) == 9
    assert argu.contains('subcmd') == True
    assert argu.contains('subcmd', '-s') == True
    assert argu.contains('subcmd', '-s', '--long') == True
    assert argu.contains('bogus') == False   # missing argument test returns False
    assert argu.contains('subcmd', 'bogus') == False   # if any arguments are missing, returns False


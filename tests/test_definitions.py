#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import pytest

from commandlines.library import Definitions
from commandlines.exceptions import MissingDictionaryKeyError

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


def test_definitions_instantation():
    defin = Definitions(create_argv(test_command_1))
    assert isinstance(defin, dict)
    assert len(defin) == 3
    assert ("n" in defin.keys()) == True
    assert ("name" in defin.keys()) == True
    assert ("nameeq" in defin.keys()) == True
    assert defin['n'] == "shortdef"
    assert defin['name'] == "longdef"
    assert defin['nameeq'] == "longdefeq"


def test_definitions_instantiation_2():
    defin = Definitions(create_argv(test_command_8))
    assert isinstance(defin, dict)
    assert len(defin) == 1
    assert ("name" in defin.keys()) == True
    assert defin['name'] == "tests/aaa.txt"


def test_definitions_instantiation_nodefs():
    defin = Definitions(create_argv(test_command_6))
    assert isinstance(defin, dict)
    assert len(defin) == 0


def test_definitions_instantiation_emptyargs():
    defin = Definitions(create_argv(test_command_empty_1))
    assert isinstance(defin, dict)
    assert len(defin) == 0


#
# Defintions.contains method tests
#


def test_definitions_contains():
    defin = Definitions(create_argv(test_command_1))
    assert isinstance(defin, dict)
    assert len(defin) == 3
    assert defin.contains(['n']) == True
    assert defin.contains(['n', 'name', 'nameeq']) == True
    assert defin.contains(['bogus']) == False
    assert defin.contains(['n', 'bogus', 'name']) == False


def test_definitions_contains_nodefs():
    defin = Definitions(create_argv(test_command_6))
    assert isinstance(defin, dict)
    assert len(defin) == 0
    assert defin.contains(["bogus"]) == False


def test_definitions_contains_emptyargs():
    defin = Definitions(create_argv(test_command_empty_1))
    assert isinstance(defin, dict)
    assert len(defin) == 0
    assert defin.contains(["bogus"]) == False

#
# Definitions get_def_argument tests
#


def test_definitions_get_def_arg():
    defin = Definitions(create_argv(test_command_1))
    assert isinstance(defin, dict)
    assert len(defin) == 3
    assert defin.get_def_argument("n") == "shortdef"
    assert defin.get_def_argument("name") == "longdef"
    assert defin.get_def_argument("nameeq") == "longdefeq"


def test_definitions_get_def_arg_alternate():
    defin = Definitions(create_argv(test_command_8))
    assert isinstance(defin, dict)
    assert len(defin) == 1
    assert defin.get_def_argument("name") == "tests/aaa.txt"


def test_definitions_get_def_arg_nodefs():
    defin = Definitions(create_argv(test_command_6))
    assert isinstance(defin, dict)
    assert len(defin) == 0
    with pytest.raises(MissingDictionaryKeyError):
        defin.get_def_argument("bogus")   # should raise missing dict key execption


def test_definitions_get_def_arg_emptyargs():
    defin = Definitions(create_argv(test_command_empty_1))
    assert isinstance(defin, dict)
    assert len(defin) == 0
    with pytest.raises(MissingDictionaryKeyError):
        defin.get_def_argument("bogus")


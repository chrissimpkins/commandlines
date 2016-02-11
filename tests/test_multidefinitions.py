#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import shlex
import pytest

from commandlines.library import MultiDefinitions, Command
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
test_command_11 = "executable -t name -- -s other"  # double dash command line idiom
test_command_12 = "executable --file name -- --path other"  # double dash command line idiom

test_command_13 = "executable -o path1 -o path2 -t --flag"
test_command_14 = "executable --file path1 --file path2 -t --flag"
test_command_15 = "executable --file=path1 --file=path2 -t --flag"
test_command_16 = "executable --file path1 --file=path2 -- --fail bigtime --fail bigtime2"
test_command_17 = "executable -o path1 -o path2 -- -t failure -t failure2"
test_command_18 = "executable -o path1 -o path2 --file tests/path1 --file tests/path2"

test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def create_argv(argstring):
    return shlex.split(argstring)[1:]


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)

# BEGIN TESTS


#
# Command obj attribute tests
#

def test_mdefinitions_commandobj_none():
    set_sysargv(test_command_1)
    c = Command()
    assert len(c.mdefs) == 0


def test_mdefinitions_commandobj():
    set_sysargv(test_command_13)
    c = Command()
    assert len(c.mdefs) == 1
    assert c.mdefs['o'] == ['path1', 'path2']


#
# MultiDefinitions object instantiation tests
#


def test_mdefinitions_instantation_no_mdefs():
    mdefin = MultiDefinitions(create_argv(test_command_1))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 0


def test_mdefinitions_instantation_with_mdefs_1():
    mdefin = MultiDefinitions(create_argv(test_command_13))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert ("o" in mdefin.keys())
    assert (mdefin['o'] == ['path1', 'path2'])


def test_mdefinitions_instantation_with_mdefs_2():
    mdefin = MultiDefinitions(create_argv(test_command_14))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert ("file" in mdefin.keys())
    assert (mdefin['file'] == ['path1', 'path2'])


def test_mdefinitions_instantation_with_mdefs_3():
    mdefin = MultiDefinitions(create_argv(test_command_15))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert ("file" in mdefin.keys())
    assert (mdefin['file'] == ['path1', 'path2'])


def test_mdefinitions_instantation_with_mdefs_4():
    mdefin = MultiDefinitions(create_argv(test_command_16))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert ("file" in mdefin.keys())
    assert (mdefin['file'] == ['path1', 'path2'])


def test_mdefinitions_instantation_with_mdefs_5():
    mdefin = MultiDefinitions(create_argv(test_command_17))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert ("o" in mdefin.keys())
    assert (mdefin['o'] == ['path1', 'path2'])


def test_mdefinitions_instantation_with_mdefs_multiple():
    mdefin = MultiDefinitions(create_argv(test_command_18))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 2
    assert ("o" in mdefin.keys())
    assert ("file" in mdefin.keys())
    assert (mdefin['o'] == ['path1', 'path2'])
    assert (mdefin['file'] == ['tests/path1', 'tests/path2'])


#
# MultiDefintions.contains (inherited from Definitions object) method tests
#


def test_mdefinitions_contains():
    mdefin = MultiDefinitions(create_argv(test_command_13))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 1
    assert mdefin.contains(['o']) == True
    assert mdefin.contains(['t']) == False
    assert mdefin.contains(['flag']) == False


def test_mdefinitions_contains_emptyargs():
    mdefin = MultiDefinitions(create_argv(test_command_empty_1))
    assert isinstance(mdefin, dict)
    assert len(mdefin) == 0
    assert mdefin.contains(["bogus"]) == False


#
# Command object contains_multi_definitions method
#

def test_mdefinitions_contains_from_commandobj():
    set_sysargv(test_command_18)
    c = Command()
    assert c.contains_multi_definitions('o') == True
    assert c.contains_multi_definitions('file') == True
    assert c.contains_multi_definitions('o', 'file') == True
    assert c.contains_multi_definitions('bogus') == False
    assert c.contains_multi_definitions('o', 'bogus') == False


def test_mdefinitions_contains_from_commandobj_empty():
    set_sysargv(test_command_empty_1)
    c = Command()
    assert c.contains_multi_definitions('bogus') == False


#
# Command get_multiple_definitions method tests
#

def test_mdefinitions_get_multipledef_commandobj():
    set_sysargv(test_command_18)
    c = Command()
    assert c.get_multiple_definitions('o') == ['path1', 'path2']
    assert c.get_multiple_definitions('file') == ['tests/path1', 'tests/path2']
    with pytest.raises(MissingDictionaryKeyError):
        assert c.get_multiple_definitions('bogus')


#
# MultiDefinitions class get_def_args method (inherited from Definitions class)
#

def test_mdefinitions_get_multipledef_method():
    mdefin = MultiDefinitions(create_argv(test_command_18))
    assert mdefin.get_def_argument('o') == ['path1', 'path2']
    assert mdefin.get_def_argument('file') == ['tests/path1', 'tests/path2']
    with pytest.raises(MissingDictionaryKeyError):
        assert mdefin.get_def_argument('bogus')


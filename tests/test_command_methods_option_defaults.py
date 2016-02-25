#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import sys
import pytest

from commandlines import Command
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
test_command_11 = "executable -t def1 -r def2 lastpos"
test_command_11 = "executable -t --name -- lastpos -n --long another"  # double dash command line idiom
test_command_12 = "executable --file path -- lastpos --test path2 another"
test_command_13 = "executable --f path -- lastpos -t path2 another"
test_command_empty_1 = "executable"
test_command_empty_2 = "exe-dash"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)


# BEGIN TESTS

# instantiation tests

def test_command_optdefaults_undefined_size():
    set_sysargv(test_command_1)
    c = Command()
    assert len(c.defaults) == 0


def test_command_optdefaults_undefined_type():
    set_sysargv(test_command_1)
    c = Command()
    assert type(c.defaults) == dict


# definition by index tests

def test_command_optdefaults_define_by_index():
    set_sysargv(test_command_1)
    c = Command()
    c.defaults['test'] = 'value'
    assert len(c.defaults) == 1
    assert c.defaults['test'] == 'value'


def test_command_optdefaults_define_multi_by_index():
    set_sysargv(test_command_1)
    c = Command()
    c.defaults['test'] = 'value'
    c.defaults['another'] = 'more'
    assert len(c.defaults) == 2
    assert c.defaults['test'] == 'value'
    assert c.defaults['another'] == 'more'


def test_command_optdefaults_define_nonstring_by_index():
    set_sysargv(test_command_1)
    c = Command()
    c.defaults['test'] = 1
    assert c.defaults['test'] == 1


# Exception test for missing key accessed directly via Command.defaults attribute

def test_command_optdefaults_raises_keyerror_with_bad_index():
    set_sysargv(test_command_1)
    c = Command()
    c.defaults['test'] = 'value'
    with pytest.raises(KeyError):
        example = c.defaults['bogus']


# Method tests

def test_command_optdefaults_define_by_set_defaults_method():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value'})
    assert len(c.defaults) == 1
    assert c.defaults['test'] == 'value'


def test_command_optdefaults_define_multi_by_set_defaults_method():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value', 'another': 'more'})
    assert len(c.defaults) == 2
    assert c.defaults['test'] == 'value'
    assert c.defaults['another'] == 'more'


def test_command_optdefaults_define_nonstring_by_set_defaults_method():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 1})
    assert c.defaults['test'] == 1




def test_command_optdefaults_contains_default_when_empty():
    set_sysargv(test_command_1)
    c = Command()
    assert c.contains_defaults('test') == False


def test_command_optdefaults_contains_default_when_present():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value'})
    assert c.contains_defaults('test') == True


def test_command_optdefaults_contains_default_multi_tests_present():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value', 'another': 'more'})
    assert c.contains_defaults('test', 'another')


def test_command_optdefaults_contains_default_multi_tests_absent():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value', 'another': 'more'})
    assert c.contains_defaults('test', 'bogus') == False


def test_command_optdefaults_contains_default_multi_tests_absent_difforder():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value', 'another': 'more'})
    assert c.contains_defaults('bogus', 'test') == False


def test_command_optdefaults_contains_default_when_absent():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value'})
    assert c.contains_defaults('bogus') == False




def test_command_optdefaults_get_default_when_empty():
    set_sysargv(test_command_1)
    c = Command()
    with pytest.raises(MissingDictionaryKeyError):
        example = c.get_default('bogus')


def test_command_optdefaults_get_default_when_present():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value'})
    assert c.get_default('test') == 'value'


def test_command_optdefaults_get_default_when_not_string():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 1})
    assert c.get_default('test') == 1


def test_command_optdefaults_get_default_when_absent():
    set_sysargv(test_command_1)
    c = Command()
    c.set_defaults({'test': 'value'})
    with pytest.raises(MissingDictionaryKeyError):
        example = c.get_default('bogus')


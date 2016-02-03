#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import pytest

from commandlines import Command

test_command_1 = "executable subcmd -s --long -n shortdef --name longdef --nameeq=longdefeq lastpos"


def set_sys_argv():
    sys.argv = test_command_1.split(" ")


# ///////////////////////////////////////////
#
# TESTS : Mock sys.argv Setup
#
# ///////////////////////////////////////////

def test_sysargv_set():
    """Test: confirm that sys.argv is mocked appropriately with the test command"""
    # set the sys.argv
    set_sys_argv()
    assert sys.argv == ['executable', 'subcmd', '-s', '--long', '-n', 'shortdef', '--name', 'longdef', '--nameeq=longdefeq', 'lastpos']


# ////////////////////////////////////////////////////////////
#
# TESTS : Parsing >>> Command object property definition tests
#
# ////////////////////////////////////////////////////////////

def test_commandobj_property_argv():
    """Test: obj.argv Command object property uses 0 based index for first positional argument, not executable"""
    set_sys_argv()
    c = Command()
    assert c.argv == ['subcmd', '-s', '--long', '-n', 'shortdef', '--name', 'longdef', '--nameeq=longdefeq', 'lastpos']


def test_commandobj_property_argc():
    """Test: obj.argc is defined with appropriate argument length"""
    set_sys_argv()
    c = Command()
    assert c.argc == 9


def test_commandobj_property_arg0():
    """Test: obj.arg0 is defined as the first positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arg0 == "subcmd"


def test_commandobj_property_arg1():
    """Test: obj.arg1 is defined as second positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arg1 == "-s"


def test_commandobj_property_arg2():
    """Test: obj.arg2 is defined as the third positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arg2 == "--long"


def test_commandobj_property_arg3():
    """Test: obj.arg3 is defined as the fourth positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arg3 == "-n"


def test_commandobj_property_arg4():
    """Test: obj.arg4 is defined as the fifth positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arg4 == "shortdef"


def test_commandobj_property_arglp():
    """Test: obj.arglp is defined as the last positional argument"""
    set_sys_argv()
    c = Command()
    assert c.arglp == "lastpos"


def test_commandobj_property_subcmd():
    """Test: obj.subcmd is defined as the first positional argument"""
    set_sys_argv()
    c = Command()
    assert c.subcmd == "subcmd"


def test_commandobj_property_subsubcmd():
    """Test: obj.subsubcmd is defined as the second positional argument"""
    set_sys_argv()
    c = Command()
    assert c.subsubcmd == "-s"


def test_commandobj_property_has_args():
    """Test: obj.has_args is defined as True when arguments are present"""
    set_sys_argv()
    c = Command()
    assert c.has_args is True


# ////////////////////////////////////////////////////////////
#
# TESTS : Parsing >>> Command object Argument property
#
# ////////////////////////////////////////////////////////////

def test_commandobj_property_arguments():
    """Test: obj.arguments property is defined with instantiated Arguments object"""
    set_sys_argv()
    c = Command()
    assert isinstance(c.arguments, list)
    assert c.arguments == sys.argv       # the obj.arguments list is same as sys.argv


# ////////////////////////////////////////////////////////////
#
# TESTS : Parsing >>> Command object Switches property
#
# ////////////////////////////////////////////////////////////

def test_commandobj_property_switches():
    """Test: obj.switches property is defined with instantiated Switches object and includes correct strings"""
    set_sys_argv()
    c = Command()
    assert isinstance(c.switches, list)
    for x in ['s', 'long', 'n', 'name']:
        assert x in c.switches


# ////////////////////////////////////////////////////////////
#
# TESTS : Parsing >>> Command object Definitions property
#
# ////////////////////////////////////////////////////////////

def test_commandobj_property_definitions():
    """Test: obj.defs property is defined with instantiated Definitions object and includes correct key:value pairs"""
    set_sys_argv()
    c = Command()
    assert isinstance(c.defs, dict)
    expected_keys = ['n', 'name', 'nameeq']
    observed_keys = c.defs.keys()
    assert len(observed_keys) == len(expected_keys)
    for x in observed_keys:
        assert x in expected_keys

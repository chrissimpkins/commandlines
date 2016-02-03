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


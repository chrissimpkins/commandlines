#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import pytest

from commandlines import Command

test_command_1 = "executable subcmd -s --long -n shortdef --name longdef --nameeq=longdefeq lastpos"


def set_sys_argv():
    sys.argv = test_command_1.split(" ")


# TESTS : Mock sys.argv Setup

def test_sysargv_set():
    """Test: confirm that sys.argv is mocked appropriately with the test command"""
    # set the sys.argv
    set_sys_argv()
    assert sys.argv == ['executable', '-s', '--long', '-n', 'shortdef', '--name', 'longdef', '--nameq=longdef', 'lastpos']


# TESTS : Command object property definitions

def test_commandobj_property_argv():
    """Test: test obj.argv Command object property uses 0 based index for first positional argument, not executable"""
    set_sys_argv()
    c = Command()
    assert c.argv == ['-s', '--long', '-n', 'shortdef', '--name', 'longdef', '--nameq=longdef', 'lastpos']



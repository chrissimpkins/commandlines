#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shlex
import sys
import pytest

from commandlines import Command

# TESTS OVERVIEW: Command object getter method tests

test_command_help_1 = "executable --help"
test_command_help_2 = "executable -h"
test_command_usage_1 = "executable --usage"
test_command_version_1 = "executable --version"
test_command_version_2 = "executable -v"


def set_sysargv(argstring):
    sys.argv = shlex.split(argstring)


# BEGIN TESTS


def test_command_default_help_long():
    set_sysargv(test_command_help_1)
    c = Command()
    assert c.is_help_request() == True


def test_command_default_help_short():
    set_sysargv(test_command_help_2)
    c = Command()
    assert c.is_help_request() == True


def test_command_default_help_when_nothelp():
    set_sysargv(test_command_usage_1)
    c = Command()
    assert c.is_help_request() == False


def test_command_default_usage():
    set_sysargv(test_command_usage_1)
    c = Command()
    assert c.is_usage_request() == True


def test_command_default_usage_when_notusage():
    set_sysargv(test_command_help_2)
    c = Command()
    assert c.is_usage_request() == False


def test_command_default_version_long():
    set_sysargv(test_command_version_1)
    c = Command()
    assert c.is_version_request() == True


def test_command_default_version_short():
    set_sysargv(test_command_version_2)
    c = Command()
    assert c.is_version_request() == True


def test_command_default_version_when_notversion():
    set_sysargv(test_command_help_1)
    c = Command()
    assert c.is_version_request() == False

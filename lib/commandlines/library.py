#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Command(object):
    def __init__(self):
        self.argv = sys.argv[1:]  # removes executable from CL argument list
        self.arguments = Arguments(self.argv)  # create a positional arguments object
        self.switches = Switches(self.argv)    # create a list of command line switches
        self.defs = Definitions(self.argv)     # create a command line definition dictionary
        self.argc = len(self.argv)  # length of the argument list
        self.arg0 = self.arguments._get_argument(0)  # define the first positional argument
        self.arg1 = self.arguments._get_argument(1)  # define the second positional argument
        self.arg2 = self.arguments._get_argument(2)  # define the third postitional argument
        self.arg3 = self.arguments._get_argument(3)  # define the fourth positional argument
        self.arg4 = self.arguments._get_argument(4)  # define the fifth positional argument
        self.arglp = self.arguments._get_argument(self.argc - 1)  # define the last positional argument
        self.subcmd = self.arg0
        self.subsubcmd = self.arg1
        self.has_args = (len(self.arguments) > 0)  # test for presence of at least one argument (boolean)

    # ------------------------------------------------------------------------------------------
    # [ get_next_positional method ] (string)
    #  Return the NEXT positional argument to a command line argument
    #    arg_recipient = the positional argument (at list index n) to test for next positional argument
    #    returns next positional argument string at list index n + 1 or empty string if no next positional
    # ------------------------------------------------------------------------------------------
    def get_next_positional(self, arg_recipient):
        recipient_position = self.arguments._get_arg_position(arg_recipient)
        return self.arguments._get_arg_next(recipient_position)

    # ------------------------------------------------------------------------------------------
    # [ validates method ] (boolean)
    #    Test that there is at least one argument in the command string
    #    returns boolean for presence of one or more arguments to the executable
    # ------------------------------------------------------------------------------------------
    def validates(self):
        return self.argc > 0

    def validates_n(self, number):
        return self.argc == number

    def does_not_validate(self):
        return self.argc == 0

    def includes_switches(self):
        return len(self.switches) > 0

    def includes_definitions(self):
        return len(self.defs) > 0

    def contains_switch(self, switch_test_string):
        if switch_test_string in self.switches:
            return True
        else:
            return False

    def contains_definition(self, def_test_string):
        if def_test_string in self.defs.keys():
            return True
        else:
            return False

    def get_definition(self, def_name_string):
        if def_name_string in self.defs.keys():
            return self.defs[def_name_string]
        else:
            return ""

    # ------------------------------------------------------------------------------
    #  Default command line switch support for:
    #  -- help
    #  -- usage
    #  -- version
    # ------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # Help switches handler method
    # ------------------------------------------------------------------------------
    def is_help_request(self):
        if "--help" in self.switches or "-h" in self.switches:
            return True
        else:
            return False

    # ------------------------------------------------------------------------------
    # Usage switch handler method
    # ------------------------------------------------------------------------------
    def is_usage_request(self):
        if "--usage" in self.switches:
            return True
        else:
            return False

    # ------------------------------------------------------------------------------
    # Version switches handler method
    # ------------------------------------------------------------------------------
    def is_version_request(self):
        if "--version" in self.switches or "-v" in self.switches:
            return True
        else:
            return False

    # ------------------------------------------------------------------------------
    # print the arguments with their corresponding argv list position to std out
    # ------------------------------------------------------------------------------
    def show_args(self):
        x = 0
        for arg in self.argv:
            print("argv[" + str(x) + "] = " + arg)
            x += 1


# ------------------------------------------------------------------------------
# [ Arguments Class ]
#   All command line arguments
#   Object type: Python list (inherited)
# ------------------------------------------------------------------------------


class Arguments(list):
    def __init__(self, argv):
        self.argv = argv
        list.__init__(self, self.argv)

    #  return argument at position specified by the 'position' parameter
    def _get_argument(self, position):
        if self.argv and len(self.argv) > position:
            return self.argv[position]
        else:
            return ""

    # return position of user specified argument in the argument list
    def _get_arg_position(self, test_arg):
        if self.argv:
            if test_arg in self.argv:
                return self.argv.index(test_arg)
            else:
                return -1

    # return the argument at the next position following a user specified positional argument
    def _get_arg_next(self, position):
        if len(self.argv) > (position + 1):
            return self.argv[position + 1]
        else:
            return ""


# ------------------------------------------------------------------------------
# [ Switches Class ]
#   Command line switches
#   Object type: Python list (inherited)
#   Syntax included:  -s or --long
# ------------------------------------------------------------------------------


class Switches(list):
    def __init__(self, argv):
        self.argv = argv
        list.__init__(self, self._make_switch_list())

    # make a list of the options in the command (defined as anything that starts with "-" character)
    def _make_switch_list(self):
        switchargv = []
        for x in self.argv:
            if x.startswith("-") and "=" not in x:
                x = x.replace("-", "")  # remove the '-' character(s from the switch before adding to list
                switchargv.append(x)

        return switchargv


# ---------------------------------------------------------------------------------------------
# [ Definitions Class ]
#   Command line options with definition syntax
#   Object type: Python dictionary (inherited)
#   Syntax included: -x <positional def>   --something <positional def>  --something=definition
#   Mapping: {option1: definition1, option2: definition2, ... optionX: definitionX}
# ---------------------------------------------------------------------------------------------


class Definitions(dict):
    def __init__(self, argv):
        self.argv = argv
        dict.__init__(self, self._make_definitions_obj())

    def _make_definitions_obj(self):
        defmap = {}
        arglist_length = len(self.argv)
        counter = 0
        for x in self.argv:
            # defines -option=definition syntax
            if x.startswith("-") and "=" in x:
                split_def = x.split("=")
                cleaned_key = split_def[0].replace('-', '')
                defmap[cleaned_key] = split_def[1]
            # defines -d <positional def> or --define <positional def> syntax
            elif x.startswith("-") and counter < arglist_length:
                if not self.argv[counter + 1].startswith("-"):
                    x = x.replace('-', '')
                    defmap[x] = self.argv[counter + 1]

            counter += 1

        return defmap

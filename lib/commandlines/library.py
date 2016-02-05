#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Command(object):
    """An object that is parsed from a command line command string"""
    def __init__(self):
        self.argv = sys.argv[1:]                    # removes executable from CL argument list
        self.arguments = Arguments(self.argv)       # ordered positional args (list)
        self.switches = Switches(self.argv)         # short and long switches (set)
        self.mops = Mops(self.argv)                 # multi-option short syntax switches (set)
        self.defs = Definitions(self.argv)          # definitions (dict)
        self.argc = len(self.argv)                  # length of the argument list
        self.arg0 = self.arguments.get_argument(0)  # first positional argument
        self.arg1 = self.arguments.get_argument(1)  # second positional argument (or "")
        self.arg2 = self.arguments.get_argument(2)  # third postitional argument (or "")
        self.arg3 = self.arguments.get_argument(3)  # fourth positional argument (or "")
        self.arg4 = self.arguments.get_argument(4)  # fifth positional argument  (or "")
        self.arglp = self.arguments.get_argument(self.argc - 1)  # define the last positional argument
        self.subcmd = self.arg0                     # first positional argument if not option
        self.subsubcmd = self.arg1                  # second positional argument if not option
        self.has_args = (len(self.arguments) > 0)   # test for presence of at least one argument (boolean)

    # //////////////////////////////////////////////////////////////
    #
    #  Validation methods
    #
    # //////////////////////////////////////////////////////////////

    def does_not_validate_missingargs(self):
        """Command string validation for inclusion of at least one argument to the executable

        :returns: boolean"""
        return self.argc == 0

    def does_not_validate_n_args(self, number):
        """Command string validation for inclusion of exactly n arguments to executable.

           :param number: an integer that defines the number of expected arguments for this test
           :returns: boolean"""
        if self.argc == number:
            return False
        else:
            return True

    def validates_hasargs(self):
        """Command string validation for inclusion of at least one argument to the executable

        :returns: boolean"""
        return self.argc > 0

    def validates_n_args(self, number):
        """Command string validation for inclusion of exactly n arguments to executable.

        :param number: an integer that defines the number of expected arguments for this test
        :returns: boolean"""
        return self.argc == number

    def validates_mandatory_args(self, arglist):
        pass
        # TODO: implement mandatory argument test that supports short / long option alternatives

    # //////////////////////////////////////////////////////////////
    #
    # Presence of general argument types methods
    #
    # //////////////////////////////////////////////////////////////

    def includes_definitions(self):
        return len(self.defs) > 0

    def includes_mops(self):
        return len(self.mops) > 0

    def includes_switches(self):
        return len(self.switches) > 0

    # //////////////////////////////////////////////////////////////
    #
    # Presence of specific argument type X argument string methods
    #
    # //////////////////////////////////////////////////////////////

    def contains_switches(self, *switch_needles):
        """Returns boolean that indicates presence (True) or absence (False) of one or more switches.

        :param switch_needles: can be a string (single argument test) or list of strings (multi-argument test)
        :returns: boolean
           """
        return self.switches.contains(switch_needles)

    def contains_definitions(self, *def_needles):
        return self.defs.contains(def_needles)

    # //////////////////////////////////////////////////////////////
    #
    # Getter methods
    #
    # //////////////////////////////////////////////////////////////

    def get_definition(self, def_needle):
        return self.defs.get_def_argument(def_needle)

    def get_next_positional(self, target_arg):
        """Returns the next positional argument at position n + 1 to a command line argument at index position n

           :param target_arg: argument string for the search """
        recipient_position = self.arguments.get_arg_position(target_arg)
        return self.arguments.get_arg_next(recipient_position)

    # //////////////////////////////////////////////////////////////
    #
    # Application logic methods
    #
    # //////////////////////////////////////////////////////////////

    def has_command_sequence(self, *cmd_list):
        """Test for a sequence of command line tokens in the command string.  The test begins at index position 0
        of the argument list and is case-sensitive.

        :param cmd_list: tuple of expected commands in expected order starting at Command.argv index 0"""
        if len(cmd_list) > len(self.argv):   # request does not inlude more args than the Command.argv property includes
            return False
        else:
            index = 0
            for test_arg in cmd_list:
                if self.argv[index] == test_arg:   # test that argument at index position matches in parameter order
                    index += 1
                else:
                    return False
            return True

    def has_args_after_argument(self, argument_needle, number=1):
        """Test for presence of one or more positional arguments (indicated by numbers) following an existing
        argument (argument_needle).

        :param number: The number of expected arguments after the test argument that is known to be present
        :param argument_needle: The test argument that is known to be present in the command"""
        pass

    # /////////////////////////////////////////////////////////////
    #
    #  Default help, usage, and version parser methods
    #
    # /////////////////////////////////////////////////////////////

    def is_help_request(self):
        """Tests for -h and --help options.  Returns boolean"""
        if "help" in self.switches or "h" in self.switches:
            return True
        else:
            return False

    def is_usage_request(self):
        """Tests for --usage option.  Returns boolean"""
        if "usage" in self.switches:
            return True
        else:
            return False

    def is_version_request(self):
        """Tests for -v and --version options.  Returns boolean"""
        if "version" in self.switches or "v" in self.switches:
            return True
        else:
            return False


class Arguments(list):
    """A class that includes all command line arguments with positional order maintained.

      The class is derived from the Python list type.

      :param argv: ordered command line argument list with sys.argv index range [1:]"""
    def __init__(self, argv):
        self.argv = argv
        list.__init__(self, self.argv)

    #  return argument at position specified by the 'position' parameter
    def get_argument(self, position):
        if self.argv and len(self.argv) > position:
            return self.argv[position]
        else:
            return ""

    # return position of user specified argument in the argument list
    def get_arg_position(self, test_arg):
        if self.argv:
            if test_arg in self.argv:
                return self.argv.index(test_arg)
            else:
                return -1

    # return the argument at the next position following a user specified positional argument
    def get_arg_next(self, position):
        if len(self.argv) > (position + 1):
            return self.argv[position + 1]
        else:
            return ""

    def contains(self, *needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test arguments

        :returns: boolean"""
        missing_needles = False
        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                missing_needles = True
        if missing_needles is True:
            return False
        else:
            return True


class Switches(set):
    """A class that is instantiated with all command line switches that have the syntax `-s` or `--longswitch`

       The class is derived from the Python list type.

       :param argv: ordered command line argument list with sys.argv index range [1:]"""
    def __init__(self, argv):
        self.argv = argv
        self.missing_switches = []
        set.__init__(self, self._make_switch_set())

    # make a list of the options in the command (defined as anything that starts with "-" character)
    def _make_switch_set(self):
        switchset = set()
        for switch_candidate in self.argv:
            if switch_candidate.startswith("-") and "=" not in switch_candidate:
                prefix = switch_candidate[:2]  # will only replace up to the first 2 dash characters in the option
                suffix = switch_candidate[2:]
                prefix = prefix.replace("-", "")  # remove the '-' character(s) from the switch before adding to list
                switch_candidate = prefix + suffix
                switchset.add(switch_candidate)

        return switchset

    def contains(self, *needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test switches.
        Switch parameters in needle tuple should be passed without initial dash character(s) in the test switch
        argument name.

        :type needle: tuple of one or more switch strings for contains test
        :returns: boolean"""
        missing_needles = False
        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                missing_needles = True
        if missing_needles is True:
            return False
        else:
            return True


class Mops(set):
    """A class that is instantiated with unique switches from multi-option command line options that use the
    short syntax.

    Examples: -rnj -tlx

    The class is derived from the Python set type and the option switches are stored as set items.

    :param argv: ordered command line argument list with sys.argv index range [1:]"""
    def __init__(self, argv):
        self.argv = argv
        set.__init__(self, self._make_mops_set())

    def _make_mops_set(self):
        mopsset = set()
        for mops_candidate in self.argv:
            if mops_candidate.startswith("-") and "=" not in mops_candidate:
                if len(mops_candidate) > 2:  # the argument includes '-' and more than one character following dash
                    if mops_candidate[1] != "-":  # it is not long option syntax (e.g. --long)
                        mops_candidate = mops_candidate.replace("-", "")
                        for switch in mops_candidate:
                            mopsset.add(switch)
        return mopsset

    def contains(self, *needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test Mops syntax option
        switches.  These should be a single character list of one or more expected options without dashes.

        :type needle: tuple of one or more multiple option short syntax strings for contains test
        :returns: boolean"""
        missing_needles = False
        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                missing_needles = True
        if missing_needles is True:
            return False
        else:
            return True


class Definitions(dict):
    """A class that is instantiated with all command line definition options with syntax
       `-s <defintion argument>` or `--longoption <defintion argument>` or
        `--longoption=<definition argument>`

        This class is derived from the Python dictionary type.  The mapping is

        key = option string (with the '-' character(s) removed)
        value = definition argument string

        :param argv: ordered command line argument list with sys.argv index range [1:]"""
    def __init__(self, argv):
        self.argv = argv
        dict.__init__(self, self._make_definitions_obj())

    def _make_definitions_obj(self):
        defmap = {}
        arglist_length = len(self.argv)
        counter = 0
        for def_candidate in self.argv:
            # defines -option=definition syntax
            if def_candidate.startswith("-") and "=" in def_candidate:
                split_def = def_candidate.split("=")
                prefix = split_def[0][:2]  # will only remove dashes in first two positions of the string
                suffix = split_def[0][2:]
                prefix = prefix.replace("-", "")
                cleaned_key = prefix + suffix
                defmap[cleaned_key] = split_def[1]
            # defines -d <positional def> or --define <positional def> syntax
            elif def_candidate.startswith("-") and counter < arglist_length:
                if not self.argv[counter + 1].startswith("-"):
                    prefix = def_candidate[:2]  # will only remove dashes in first two positions of the string
                    suffix = def_candidate[2:]
                    prefix = prefix.replace('-', '')
                    def_candidate = prefix + suffix
                    defmap[def_candidate] = self.argv[counter + 1]

            counter += 1

        return defmap

    def contains(self, *needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test definitions.
        The definitions should be passed without initial dash characters in the definition argument name.

        :type needle: tuple of one or more definition argument strings for contains test
        :returns: boolean"""
        missing_needles = False
        for expected_definition in needle:
            if expected_definition in self.keys():
                pass
            else:
                missing_needles = True
        if missing_needles is True:
            return False
        else:
            return True

    def get_def_argument(self, needle):
        if needle in self.keys():
            return self[needle]
        else:
            return ""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from commandlines.exceptions import IndexOutOfRangeError, MissingArgumentError, MissingDictionaryKeyError


class Command(object):
    """An object that is parsed from a command line command string"""
    def __init__(self):
        self.argv = sys.argv[1:]
        self.arguments = Arguments(self.argv)
        self.switches = Switches(self.argv)
        self.mops = Mops(self.argv)
        self.defs = Definitions(self.argv)
        self.argc = len(self.argv)
        self.arg0 = self.arguments.get_argument_for_commandobj(0)
        self.arg1 = self.arguments.get_argument_for_commandobj(1)
        self.arg2 = self.arguments.get_argument_for_commandobj(2)
        self.arg3 = self.arguments.get_argument_for_commandobj(3)
        self.arg4 = self.arguments.get_argument_for_commandobj(4)
        self.arglp = self.arguments.get_argument_for_commandobj(self.argc - 1)
        self.subcmd = self.arg0
        self.subsubcmd = self.arg1
        self.has_args = (len(self.arguments) > 0)

        # v0.2.2
        # [X] refactor contains methods to fail early and return False
        # v0.3.0
        # TODO: add support for double dash command line idiom (e.g. -- -badfilename)
        # TODO: add support for multiple same option definitions (e.g. -o <path1> -o <path2>)
        # TODO: implement mandatory argument test that supports short / long option alternatives

    # //////////////////////////////////////////////////////////////
    #
    #  Validation methods
    #
    # //////////////////////////////////////////////////////////////

    def does_not_validate_missing_args(self):
        """Command string validation for missing arguments to the executable

        :returns: boolean"""

        return self.argc == 0

    def does_not_validate_missing_defs(self):
        """Command string validation for missing definitions to the executable

        :returns: boolean"""

        return len(self.defs) == 0

    def does_not_validate_missing_mops(self):
        """Command string validation for missing multi-option short syntax arguments to the executable

        :returns: boolean"""

        return len(self.mops) == 0

    def does_not_validate_missing_switches(self):
        """Command string validation for missing switches to the executable

        :returns: boolean"""

        return len(self.switches) == 0

    def does_not_validate_n_args(self, number):
        """Command string validation for inclusion of exactly n arguments to executable.

           :param number: an integer that defines the number of expected arguments for this test
           :returns: boolean"""

        if self.argc == number:
            return False
        else:
            return True

    def validates_includes_args(self):
        """Command string validation for inclusion of at least one argument to the executable

        :returns: boolean"""

        return self.argc > 0

    def validates_includes_definitions(self):
        """Command string validation for inclusion of at least one definition (option-argument) to the executable

        :returns: boolean"""

        return len(self.defs) > 0

    def validates_includes_mops(self):
        """Command string validation for inclusion of at least one multi-option short syntax argument to the
        executable.

        :returns: boolean"""

        return len(self.mops) > 0

    def validates_includes_switches(self):
        """Command string validation for inclusion of at least one switch argument to the executable.

        :returns: boolean"""

        return len(self.switches) > 0

    def validates_includes_n_args(self, number):
        """Command string validation for inclusion of exactly `number` arguments to executable.

        :param number: an integer that defines the number of expected arguments for this test
        :returns: boolean"""

        return self.argc == number

    # def validates_includes_mandatory_args(self, arglist):
    #     pass

    # //////////////////////////////////////////////////////////////
    #
    # Application logic methods
    #
    # //////////////////////////////////////////////////////////////

    def contains_switches(self, *switch_needles):
        """Returns boolean that indicates presence (True) or absence (False) of one or more switches.

        :param switch_needles: a tuple of one or more expected switch strings
        :returns: boolean"""

        return self.switches.contains(switch_needles)

    def contains_definitions(self, *def_needles):
        """Returns boolean that indicates presence (True) or absence (False) of one or more definition options

        :returns: boolean"""

        return self.defs.contains(def_needles)

    def has_command_sequence(self, *cmd_list):
        """Test for a sequence of command line tokens in the command string.  The test begins at index position 0
        of the argument list and is case-sensitive.

        :param cmd_list: tuple of expected commands in expected order starting at Command.argv index 0
        :returns: boolean"""

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

    def has_args_after(self, argument_needle, number=1):
        """Test for presence of at least one or more positional arguments (indicated by numbers) following an existing
        argument (argument_needle).

        :param number: The number of expected arguments after the test argument
        :param argument_needle: The test argument that is known to be present in the command
        :raises: MissingArgumentError when argument_needle is not found in the parsed argument list"""

        if argument_needle in self.arguments:
            position = self.arguments.get_arg_position(argument_needle)
            if len(self.argv) > (position + number):
                return True
            else:
                return False
        else:
            raise MissingArgumentError(argument_needle)

    def next_arg_is_in(self, start_argument, supported_at_next_position):
        """Test for the presence of a supported argument in the n+1 index position for a known argument at the
        n position.  start_argument is called as the full argument string including any expected dashes.

        :param start_argument: The argument string including any expected dashes
        :param supported_at_next_position: list of strings that define supported arguments in the n+1 index position
        :raises: MissingArgumentError when start_argument is not found in the parsed argument list"""

        if start_argument in self.arguments:
            position = self.arguments.get_arg_position(start_argument)
            test_argument = self.arguments.get_arg_next(position)
            if test_argument in supported_at_next_position:
                return True
            else:
                return False
        else:
            raise MissingArgumentError(start_argument)

    # //////////////////////////////////////////////////////////////
    #
    # Getter methods
    #
    # //////////////////////////////////////////////////////////////

    def get_definition(self, def_needle):
        """Returns the argument to an option that is part of an option-argument pair (defined as a definition
        argument here).

        :param def_needle: The option portion of the option-argument pair for the request
        :returns: string
        :raises: MissingDictionaryKeyError when the option is not found in the parsed definitions dictionary"""

        return self.defs.get_def_argument(def_needle)

    def get_arg_after(self, target_arg):
        """Returns the next positional argument at position n + 1 to a command line argument at index position n

           :param target_arg: argument string for the search
           :returns: string
           :raises: MissingArgumentError when target_arg is not found in the parsed argument list
           :raises: IndexOutOfRangeError when target_arg is the last positional argument"""

        if target_arg in self.argv:
            recipient_position = self.arguments.get_arg_position(target_arg)
            return self.arguments.get_arg_next(recipient_position)
        else:
            raise MissingArgumentError(target_arg)

    # /////////////////////////////////////////////////////////////
    #
    #  Default help, usage, and version parser methods
    #
    # /////////////////////////////////////////////////////////////

    def is_help_request(self):
        """Tests for -h and --help options in command string

        :returns: boolean"""

        if "help" in self.switches or "h" in self.switches:
            return True
        else:
            return False

    def is_usage_request(self):
        """Tests for --usage option in command string

        :returns: boolean"""

        if "usage" in self.switches:
            return True
        else:
            return False

    def is_version_request(self):
        """Tests for -v and --version options in command string.

        :returns: boolean"""

        if "version" in self.switches or "v" in self.switches:
            return True
        else:
            return False


class Arguments(list):
    """A class that includes all command line arguments with positional order maintained.  Instantiated with a list
    of strings.

      The class is derived from the Python list type."""
    def __init__(self, argv):
        list.__init__(self, argv)

    def get_argument_for_commandobj(self, position):
        """An argument parsing method for the instantation of the Command object.  This is not intended for public use.
        Public calls should use the get_argument() method instead.

        :param position: The command line index position
        :returns: string or empty string if the index position is out of the index range"""

        if (len(self) > position) and (position >= 0):
            return self[position]
        else:
            return ""   # intentionally set as empty string rather than raise exception for Command obj instantation

    def get_argument(self, position):
        """Returns argument by argument index position in the Argument object list.

        :param position: The command line index position
        :returns: string
        :raises: IndexOutOfRangeError if the requested index falls outside of the list index range"""

        if (len(self) > position) and (position >= 0):
            return self[position]
        else:
            raise IndexOutOfRangeError()

    def get_arg_position(self, test_arg):
        """Returns the index position of a candidate argument string (test_arg).  The argument string should include
        any expected dashes at the beginning of the argument string.

        :param test_arg: the argument string for which the index position is requested
        :returns: string
        :raises: MissingArgumentError if the requested argument is not in the Argument list"""

        if test_arg in self:
            return self.index(test_arg)
        else:
            raise MissingArgumentError(test_arg)

    def get_arg_next(self, position):
        """Returns the next argument at index position + 1 in the command sequence.

        :param position: the argument string for which the next positional argument is requested
        :returns: string
        :raises: IndexOutOfRangeError if the position + 1 falls outside of the index range"""

        if len(self) > (position + 1):
            return self[position + 1]
        else:
            raise IndexOutOfRangeError()

    def contains(self, needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test arguments

        :param needle: an iterable that contains one or more test argument strings
        :returns: boolean"""

        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                return False

        return True  # if all tests above pass


class Switches(set):
    """A class that is instantiated with all command line switches that have the syntax `-s`, `--longswitch`,
    or `-longswitch`

       The class is derived from the Python set type and arguments with this syntax are saved as set items."""
    def __init__(self, argv):
        set.__init__(self, self._make_switch_set(argv))

    def _make_switch_set(self, argv):
        """Returns a set that includes all switches that are parsed from the command string.

        :param argv: a list of ordered command line argument strings
        :returns: set"""

        switchset = set()
        for switch_candidate in argv:
            if switch_candidate.startswith("-") and "=" not in switch_candidate:
                switch_candidate = switch_candidate.lstrip("-")
                switchset.add(switch_candidate)

        return switchset

    def contains(self, needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test switches.
        Switch parameters in needle tuple should be passed without initial dash character(s) in the test switch
        argument name.

        :type needle: an iterable that contains one or more test argument strings
        :returns: boolean"""

        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                return False

        return True  # if all tests above pass


class Mops(set):
    """A class that is instantiated with unique switches from multi-option command line options that use the
    short syntax.

    Examples: -rnj -tlx

    The class is derived from the Python set type and the single character option switches are stored as set items."""

    def __init__(self, argv):
        set.__init__(self, self._make_mops_set(argv))

    def _make_mops_set(self, argv):
        """Returns a set of multi-option short syntax option characters that are parsed from a list of ordered
        command string arguments in argv

        :param argv: ordered list of command line arguments
        :returns: set"""

        mopsset = set()
        for mops_candidate in argv:
            if mops_candidate.startswith("-") and "=" not in mops_candidate:
                if len(mops_candidate) > 2:  # the argument includes '-' and more than one character following dash
                    if mops_candidate[1] != "-":  # it is not long option syntax (e.g. --long)
                        mops_candidate = mops_candidate.replace("-", "")
                        for switch in mops_candidate:
                            mopsset.add(switch)
        return mopsset

    def contains(self, needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test Mops syntax option
        switches.  These should be a single character list of one or more expected options without dashes.

        :type needle: an iterable that contains one or more test argument strings
        :returns: boolean"""

        for expected_argument in needle:
            if expected_argument in self:
                pass
            else:
                return False

        return True


class Definitions(dict):
    """A class that is instantiated with all command line definition options with syntax
       `-s <defintion argument>` or `--longoption <defintion argument>` or
        `--longoption=<definition argument>`

        This class is derived from the Python dictionary type.  The mapping is

        key = option string (with the '-' character(s) removed)
        value = definition argument string"""
    def __init__(self, argv):
        dict.__init__(self, self._make_definitions_obj(argv))

    def _make_definitions_obj(self, argv):
        """Parses definition options from a list of ordered command line arguments to define the dictionary that
        is used to instantiate the Definitions class.  Option string keys are stripped of dash characters before the
        first alphabetic character in the option name.

        :param argv: ordered list of command line string arguments
        :returns: dictionary with key = option string : value = definition argument string mapping"""

        defmap = {}
        arglist_length = len(argv)
        counter = 0
        for def_candidate in argv:
            # defines -option=definition syntax
            if def_candidate.startswith("-") and "=" in def_candidate:
                split_def = def_candidate.split("=")
                cleaned_key = split_def[0].lstrip("-")  # remove dash characters from the option
                defmap[cleaned_key] = split_def[1]
            # defines -d <positional def> or --define <positional def> syntax
            elif counter < (arglist_length - 1) and def_candidate.startswith("-"):
                if not argv[counter + 1].startswith("-"):
                    def_candidate = def_candidate.lstrip("-")
                    defmap[def_candidate] = argv[counter + 1]

            counter += 1

        return defmap

    def contains(self, needle):
        """Returns boolean that indicates the presence (True) or absence (False) of a tuple of test definitions.
        The definitions should be passed without initial dash characters in the definition argument name.

        :type needle: tuple of one or more definition argument strings for contains test
        :returns: boolean"""

        for expected_definition in needle:
            if expected_definition in self.keys():
                pass
            else:
                return False

        return True  # if all tests above pass returns True

    def get_def_argument(self, needle):
        """Returns the defintion option string for an option needle.  The needle parameter should not include
        dash characters at the beginning of the option string (i.e. use 'test' rather than '--test' and
        't' rather than '-t'.

        :param needle: the requested definition option string.
        :returns: string
        :raises: MissingDictionaryKeyError if the option needle is not a key defined in the Definitions object"""

        if needle in self.keys():
            return self[needle]
        else:
            raise MissingDictionaryKeyError(needle)

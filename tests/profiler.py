#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cProfile, pstats, StringIO


def profile():
    # ------------------------------------------------------------------------------
    # Setup a profile
    # ------------------------------------------------------------------------------
    pr = cProfile.Profile()
    # ------------------------------------------------------------------------------
    # Enter setup code below
    # ------------------------------------------------------------------------------
    # Optional: include setup code here

    import sys
    from commandlines import Command
    sys.argv = "executable test --long -s --other=alternate bogus -- -stuff -here --help"
    # ------------------------------------------------------------------------------
    # Start profiler
    # ------------------------------------------------------------------------------
    pr.enable()

    for _ in xrange(10000):
        c = Command()
        # "-" in xstring[0]
        # "-" in ystring[0]

    # ------------------------------------------------------------------------------
    # BEGIN profiled code block
    # ------------------------------------------------------------------------------
    # include profiled code here

    # ------------------------------------------------------------------------------
    # END profiled code block
    # ------------------------------------------------------------------------------
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.strip_dirs().sort_stats("time").print_stats()
    print(s.getvalue())


if __name__ == '__main__':
    profile()

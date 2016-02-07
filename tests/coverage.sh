#!/bin/sh

coverage run --source commandlines -m py.test
coverage report -m
coverage html
#codecov --token=$CODECOV_COMMANDLINES
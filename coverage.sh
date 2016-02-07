#!/bin/sh

coverage run --source commandlines -m py.test
coverage report -m
coverage html
coverage xml
codecov --token=$CODECOV_COMMANDLINES
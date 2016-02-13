## commandlines  [![Build Status](https://travis-ci.org/chrissimpkins/commandlines.svg?branch=master)](https://travis-ci.org/chrissimpkins/commandlines) [![Build status](https://ci.appveyor.com/api/projects/status/nabadxorf9s8n0h5/branch/master?svg=true)](https://ci.appveyor.com/project/chrissimpkins/commandlines/branch/master)  [![codecov.io](https://codecov.io/github/chrissimpkins/commandlines/coverage.svg?branch=master)](https://codecov.io/github/chrissimpkins/commandlines?branch=master) [![Code Health](https://landscape.io/github/chrissimpkins/commandlines/master/landscape.svg?style=flat)](https://landscape.io/github/chrissimpkins/commandlines/master)


<img src="https://raw.githubusercontent.com/chrissimpkins/commandlines/images/images/commandlines.png" width="740" alt="commandlines">


## What is commandlines?

Commandlines is a Python library for command line application development that supports command line argument parsing, command string validation testing, & application logic.  It has no external dependencies and provides broad Python interpreter support for Python 2.6+, Python 3.3+, pypy, and pypy3 across OS X, Linux, and Windows platforms.

## How Do I Use It?

Commandlines supports expressive (verbose) command line application source code that is simple to implement, instantly understandable, and easy to maintain.  The command line string is an object.


#### The Command Object

Instantiate a `commandlines` Command object:

```python
from commandlines import Command

c = Command()
```

and you have access to the following command line argument types:

#### Arguments

| Command Line Tokens/Idioms  | Example  | Accessed/Tested With |
| :------------: |:---------------:| :---------------:|
| Command suite sub-commands | `$ spam eggs` | `c.subcmd` |
| Command suite sub-sub-commands | `$ spam eggs overeasy` | `c.subsubcmd` |
| Short switch syntax | `$ spam -e` | `"e" in c.switches` |
| Long switch syntax | `$ spam --eggs` | `"eggs" in c.switches` | 
| Short opt-arg definition syntax | `$ spam -o eggs` | `c.get_definition('o')`|
| Long opt-arg definition syntax | `$ spam --out eggs` | `c.get_definition('out')`|
| Alt long opt-arg definition syntax | `$ spam --out=eggs` | `c.get_definition('out')`|

#### Command Line Idioms


















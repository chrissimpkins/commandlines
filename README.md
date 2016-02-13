## commandlines  [![Build Status](https://travis-ci.org/chrissimpkins/commandlines.svg?branch=master)](https://travis-ci.org/chrissimpkins/commandlines) [![Build status](https://ci.appveyor.com/api/projects/status/nabadxorf9s8n0h5/branch/master?svg=true)](https://ci.appveyor.com/project/chrissimpkins/commandlines/branch/master)  [![codecov.io](https://codecov.io/github/chrissimpkins/commandlines/coverage.svg?branch=master)](https://codecov.io/github/chrissimpkins/commandlines?branch=master) [![Code Health](https://landscape.io/github/chrissimpkins/commandlines/master/landscape.svg?style=flat)](https://landscape.io/github/chrissimpkins/commandlines/master)


<img src="https://raw.githubusercontent.com/chrissimpkins/commandlines/images/images/commandlines.png" width="740" alt="commandlines">


## What is commandlines?

Commandlines is a Python library for command line application development that supports command line argument parsing, command string validation testing, & application logic.  It has no external dependencies and provides broad Python interpreter support for Python 2.6+, Python 3.3+, pypy, and pypy3 across OS X, Linux, and Windows platforms.

## How Do I Use It?

Commandlines supports explicit, expressive command line application source code with a broad, permissive command syntax range. The goal is to make application logic simple to implement, instantly understandable, and easy to maintain.  The command line string is parsed to multiple objects that are derived from builtin Python container types.


#### The Command Object

Instantiate a `commandlines` Command object:

```python
from commandlines import Command

c = Command()
```

and you have access to:

#### Arguments

| Command Line Arguments  | Command Example  | Accessed/Tested With |
| :------------: |:---------------:| :---------------:|
| Command suite sub-commands | `$ spam eggs` | `c.subcmd` |
| Command suite sub-sub-commands | `$ spam eggs overeasy` | `c.subsubcmd` |
| Short switch syntax | `$ spam -e` | `"e" in c.switches` |
| Long switch syntax | `$ spam --eggs` | `"eggs" in c.switches` | 
| Short opt-arg definition syntax | `$ spam -o eggs` | `c.get_definition('o')`|
| Long opt-arg definition syntax | `$ spam --out eggs` | `c.get_definition('out')`|
| Alt long opt-arg definition syntax | `$ spam --out=eggs` | `c.get_definition('out')`|
| Multi-option short syntax switches | `$ spam -mpns eggs` | `"m" in c.mops` |

#### Command Line Idioms

| Command Line Idioms  | Command Example  | Accessed/Tested With |
| :------------: |:---------------:| :---------------:|
| Double dash idiom | `$ spam eggs -- -badfile` | `c.has_double_dash()` |
| Double dash arguments| `$ spam eggs -- -badfile` | `c.get_double_dash_args()` |
| Multiple same option args | `$ spam -o eggs -o omelets` | `c.get_multiple_definitions('o')` |

#### Application Logic Testing Methods

| Test Type  | Command Example  | Tested With |
| :------------: |:---------------:| :---------------:|
| Contains single switch | `$ spam -s` | `c.contains_switches('s')` |
| Contains multiple switches | `$ spam -s --eggs` | `c.contains_switches('s', 'eggs')` |
| Contains single definition | `$ spam -o eggs` | `c.contains_definitions('o')` |
| Contains multiple different definitions | `$ spam -o eggs --with bacon` | `c.contains_definitions('o', 'with')` |
| Contains multiple same definition types | `$ spam -o eggs -o bacon` | `c.contains_multi_definitions('o')`|

 
















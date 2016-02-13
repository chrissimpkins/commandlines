## commandlines  [![Build Status](https://travis-ci.org/chrissimpkins/commandlines.svg?branch=master)](https://travis-ci.org/chrissimpkins/commandlines) [![Build status](https://ci.appveyor.com/api/projects/status/nabadxorf9s8n0h5/branch/master?svg=true)](https://ci.appveyor.com/project/chrissimpkins/commandlines/branch/master)  [![codecov.io](https://codecov.io/github/chrissimpkins/commandlines/coverage.svg?branch=master)](https://codecov.io/github/chrissimpkins/commandlines?branch=master) [![Code Health](https://landscape.io/github/chrissimpkins/commandlines/master/landscape.svg?style=flat)](https://landscape.io/github/chrissimpkins/commandlines/master)


<img src="https://raw.githubusercontent.com/chrissimpkins/commandlines/images/images/commandlines.png" width="740" alt="commandlines">


## What is commandlines?

Commandlines is a Python library for command line application development that supports command line argument parsing, command string validation testing, & application logic.  It has no external dependencies and provides broad Python interpreter support for Python 2.6+, Python 3.3+, pypy, and pypy3 across OS X, Linux, and Windows platforms.

## Project Status

*Commandlines is in active development and, while it is tested and usable in the current release version, there is no assurance of a stable API and backward compatibility at this stage of development. Please freeze the library version in your deployment scripts or include the Commandlines library modules released in the master branch of the repository in your project if you elect to use it in a production environment.*

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
| Short switch syntax | `$ spam -e` | `c.contains_switches('e')` |
| Long switch syntax | `$ spam --eggs` | `c.contains_switches('eggs')` | 
| Multiple switches | `$ spam -e --eggs --bacon`| `c.contains_switches('e', 'eggs', 'bacon')`|
| Short opt-arg definition syntax | `$ spam -o eggs` | `c.get_definition('o')`|
| Long opt-arg definition syntax | `$ spam --out eggs` | `c.get_definition('out')`|
| Alt long opt-arg definition syntax | `$ spam --out=eggs` | `c.get_definition('out')`|
| Multiple same option definitions | `$ spam -o eggs -o omelets` | `c.get_multiple_definitions('o')` |
| Multi-option short syntax switches | `$ spam -mpns eggs` | `"m" in c.mops` |

#### Positional Arguments

Positional arguments use a 0 based index starting from the first argument to the executable (i.e. `sys.argv[1:]`) and are maintained as attributes in the Command object.  Support is provided for the first five positional arguments and the last positional argument.

| Positional Argument  | Command Example  | Accessed/Tested With |
| :------------: |:---------------:| :---------------:|
| Positional argument at index 0 | `$ spam eggs` | `c.arg0` |
| Positional argument at index 1 | `$ spam eggs bacon` | `c.arg1` |
| Positional argument at index 2 | `$ spam eggs bacon toast` | `c.arg2` |
| Positional argument at index 3 | `$ spam eggs bacon toast cereal` | `c.arg3` |
| Positional argument at index 4 | `$ spam eggs bacon toast cereal coffee` | `c.arg4` |
| Last positional argument | `$ spam eggs -b --toast filepath` | `c.arglp` |


#### Special Command Line Idioms

| Command Line Idioms  | Command Example  | Accessed/Tested With |
| :------------: |:---------------:| :---------------:|
| Double dash idiom | `$ spam eggs -- -badfile` | `c.has_double_dash()` |
| Double dash arguments| `$ spam eggs -- -badfile -badfile2` | `c.get_double_dash_args()` |

#### Application Logic Testing Methods

| Test Type  | Command Example  | Tested With |
| :------------: |:---------------:| :---------------:|
| Positional command sequence test | `$ spam eggs doit` | `c.has_command_sequence('eggs', 'doit')`|
| Single switch test | `$ spam -s` | `c.contains_switches('s')` |
| Multiple switch test | `$ spam -s --eggs` | `c.contains_switches('s', 'eggs')` |
| Single definition test | `$ spam -o eggs` | `c.contains_definitions('o')` |
| Multiple different definitions test | `$ spam -o eggs --with bacon` | `c.contains_definitions('o', 'with')` |
| Multiple same definitions test | `$ spam -o eggs -o bacon` | `c.contains_multi_definitions('o')`|
| Positional argument test | `$ spam eggs filepath` | `c.has_args_after('eggs')`|
| Acceptable positional arg test | `$ spam eggs toaster` | `c.next_arg_is_in('eggs', ['toaster', 'coffeepot'])` |

 
















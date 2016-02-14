
Commandlines Library Documentation
==================================

commandlines |Build Status| |Build status| |codecov.io| |Code Health|
---------------------------------------------------------------------

What is Commandlines?
---------------------

`Commandlines <https://github.com/chrissimpkins/commandlines>`__ is a Python library for command line application
development that supports command line argument parsing, command string
validation testing, & application logic. It has no external dependencies
and provides broad Python interpreter support for Python 2.6+, Python
3.3+, pypy, and pypy3 across OS X, Linux, and Windows platforms.

Project Status
--------------

Commandlines is in active development and, while it is tested and
usable in the current release version, there is no assurance of a stable
API or backwards compatibility across minor and patch versions at this
stage of development. Please freeze the library version in your
deployment/installation scripts or include the Commandlines library
modules released in the master branch of the repository as part of your
own project if you elect to use it in a production environment. This
message will disappear when this is no longer the case and at that stage
the library will be released as version 1.0.0 under `semantic versioning
specifications <http://semver.org/>`__.

How Do I Use It?
----------------

Commandlines supports explicit, expressive command line application
source code with a broad, permissive command syntax range. The goal is
to make application logic simple to implement, intuitive, and easy to
maintain.

The command line string to your executable script is parsed to multiple
objects that are derived from builtin Python types.

The Command Object
~~~~~~~~~~~~~~~~~~

Instantiate a ``commandlines`` Command object:

.. code:: python

    from commandlines import Command

    c = Command()

and you have access to:

Arguments
^^^^^^^^^

+-----------------+-----------------------------------+-------------------------------------+
| Command Line    | Command Example                   | Accessed/Tested                     |
| Arguments       |                                   | With                                |
+=================+===================================+=====================================+
| Length of arg   | ``$ spam eggs -t --out file``     | ``c.argc == 4``                     |
| list            |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Command suite   | ``$ spam eggs``                   | ``c.subcmd == "eggs"``              |
| sub-commands    |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Command suite   | ``$ spam eggs over easy``         | ``c.subsubcmd == "overeasy"``       |
| sub-sub-command |                                   |                                     |
| s               |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Short switch    | ``$ spam -e``                     | ``c.contains_switches('e')``        |
| syntax          |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Long switch     | ``$ spam --eggs``                 | ``c.contains_switches('eggs')``     |
| syntax          |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Multiple        | ``$ spam -e --eggs``              | ``c.contains_switches('e', 'eggs')``|
| switches        |                                   |                                     |
|                 |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Short opt-arg   | ``$ spam -o eggs``                | ``c.get_definition('o')``           |
| definition      |                                   |                                     |
| syntax          |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Long opt-arg    | ``$ spam --out egg s``            | ``c.get_definition('out')``         |
| definition      |                                   |                                     |
| syntax          |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Alt long        | ``$ spam --out=egg s``            | ``c.get_definition('out')``         |
| opt-arg         |                                   |                                     |
| definition      |                                   |                                     |
| syntax          |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Multiple same   | ``$ spam -o eggs -o omelets``     | ``c.get_multiple_definitions('o')`` |
| option          |                                   |                                     |
| definitions     |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Multi-option    | ``$ spam -mpns egg s``            | ``c.contains_mops('m')``            |
| short syntax    |                                   |                                     |
| switches        |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+
| Next positional | ``$ spam eggs test/path``         | ``c.get_arg_after('eggs')``         |
| argument        |                                   |                                     |
+-----------------+-----------------------------------+-------------------------------------+

Positional Arguments
^^^^^^^^^^^^^^^^^^^^

Positional arguments use a 0 based index starting at the first argument
to the executable (i.e. ``sys.argv[1:]``) and are maintained as
attributes in the Command object. Individual attribute support is
provided for the first five positional arguments and the last positional
argument. An ordered list of all positional arguments is available in
the ``arguments`` attribute.

+-----------------+----------------------------------------+--------------------+
| Positional      | Command Example                        | Accessed/Tested    |
| Argument        |                                        | With               |
+=================+========================================+====================+
| Positional      | ``$ spam eggs``                        | ``c.arg0``         |
| argument at     |                                        |                    |
| index 0         |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| Positional      | ``$ spam eggs bacon``                  | ``c.arg1``         |
| argument at     |                                        |                    |
| index 1         |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| Positional      | ``$ spam eggs bacon toast``            | ``c.arg2``         |
| argument at     |                                        |                    |
| index 2         |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| Positional      | ``$ spam eggs bacon toast cereal``     | ``c.arg3``         |
| argument at     |                                        |                    |
| index 3         |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| Positional      | ``$ spam eggs bacon toast cereal milk``| ``c.arg4``         |
| argument at     |                                        |                    |
| index 4         |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| Last positional | ``$ spam eggs -b --toast filepath``    | ``c.arglp``        |
| argument        |                                        |                    |
+-----------------+----------------------------------------+--------------------+
| All positional  | ``$ spam eggs -b - -toast filepath``   | ``c.arguments``    |
| arguments       |                                        |                    |
+-----------------+----------------------------------------+--------------------+

Special Command Line Idioms
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+----------------------------------------+----------------------------------------+
| Command Line    | Command Example                        | Accessed/Tested                        |
| Idioms          |                                        | With                                   |
+=================+========================================+========================================+
| Double dash     | ``$ spam eggs -- -badfile``            | ``c.has_double_dash()``                |
| idiom           |                                        |                                        |
+-----------------+----------------------------------------+----------------------------------------+
| Double dash     | ``$ spam eggs -- -badfile -badfile2``  | ``c.get_double_dash_args()``           |
| arguments       |                                        |                                        |
|                 |                                        |                                        |
+-----------------+----------------------------------------+----------------------------------------+

Application Logic Testing Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+----------------------------------------+--------------------------------------------------------+
| Test Type       | Command Example                        | Tested With                                            |
+=================+========================================+========================================================+
| Positional      | ``$ spam eggs doit``                   | ``c.has_command_sequence('eggs', 'doit')``             |
| command         |                                        |                                                        |
| sequence        |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Single switch   | ``$ spam -s``                          | ``c.contains_switches('s')``                           |
|                 |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Multiple switch | ``$ spam -s --eggs``                   | ``c.contains_switches('s', 'eggs')``                   |
|                 |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Single          | ``$ spam -o eggs``                     | ``c.contains_definitions('o')``                        |
| definition      |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Multiple        | ``$ spam -o eggs --with bacon``        | ``c.contains_definitions('o', 'with')``                |
| different       |                                        |                                                        |
| definitions     |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Multiple same   | ``$ spam -o eggs -o bacon``            | ``c.contains_multi_definitions('o')``                  |
| definitions     |                                        |                                                        |
|                 |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Positional      | ``$ spam eggs --coffee``               | ``c.has_args_after('eggs')``                           |
| argument        |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+
| Acceptable      | ``$ spam eggs toaster``                | ``c.next_arg_is_in('eggs', ['toaster', 'coffeepot'])`` |
| positional arg  |                                        |                                                        |
|                 |                                        |                                                        |
+-----------------+----------------------------------------+--------------------------------------------------------+

Command String Validation Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------+----------------------------------------------+
| Test Type       | Failure Example         | Tested With                                  |
+=================+=========================+==============================================+
| Missing         | ``$ spam``              | ``c.does_not_validate_missing_args()``       |
| arguments       |                         |                                              |
|                 |                         |                                              |
+-----------------+-------------------------+----------------------------------------------+
| Expected        | ``$ spam eggs``         | ``c.does_not_validate_n_args(2)``            |
| argument number |                         |                                              |
+-----------------+-------------------------+----------------------------------------------+
| Missing opt-arg | ``$ spam -o --eggs``    | ``c.does_not_validate_missing_defs()``       |
| definitions     |                         |                                              |
|                 |                         |                                              |
+-----------------+-------------------------+----------------------------------------------+
| Missing         | ``$ spam eggs``         | ``c.does_not_validate_missing_switches()``   |
| switches        |                         |                                              |
|                 |                         |                                              |
+-----------------+-------------------------+----------------------------------------------+
| Missing         | ``$ spam -o eggs``      | ``c.does_not_validate_missing_mops()``       |
| multi-option    |                         |                                              |
| short syntax    |                         |                                              |
| switches        |                         |                                              |
+-----------------+-------------------------+----------------------------------------------+

Help, Usage, and Version Request Testing Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------+------------------------+------------------------------+
| Test Type                | Command Example        | Tested With                  |
+==========================+========================+==============================+
| Help request, short      | ``$ spam -h``          | ``c.is_help_request()``      |
+--------------------------+------------------------+------------------------------+
| Help request, long       | ``$ spam --help``      | ``c.is_help_request()``      |
+--------------------------+------------------------+------------------------------+
| Usage request            | ``$ spam --usage``     | ``c.is_usage_request()``     |
+--------------------------+------------------------+------------------------------+
| Version request, short   | ``$ spam -v``          | ``c.is_version_request()``   |
+--------------------------+------------------------+------------------------------+
| Version request, long    | ``$ spam --version``   | ``c.is_version_request()``   |
+--------------------------+------------------------+------------------------------+

API Documentation
~~~~~~~~~~~~~~~~~

The Command class is designed to be the public facing library object.
You can view full documentation of this Python class
`here <https://commandlines.github.io/commandlines.library.html#commandlines.library.Command>`__.

If you would like to dig into lower level objects in the commandlines
package, you can view the `library API
documentation <https://commandlines.github.io/commandlines.library.html>`__.

Exceptions that are used in the commandlines package are documented
`here <https://commandlines.github.io/commandlines.exceptions.html>`__.

How to Include Commandlines in Your Project
-------------------------------------------

For Projects That Will Be Distributed to Others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the ``commandlines`` package dependency to your project ``setup.py``
file in the ``install_requires`` field like so:

.. code:: python

    setup(
        ...
        install_requires=["commandlines == x.x.x"],
        ...
    )

It is **highly recommended** that you explicitly define the library
version by replacing ``x.x.x`` with the version that you used for
testing. The project is in active development and backwards
compatibility is not assured at this stage.

Then, enter the following command to test your project locally:

::

    $ python setup.py develop

Import the ``commandlines`` package in your project and instantiate a
Command object by adding the following lines to your Python script:

.. code:: python

    from commandlines import Command

    c = Command()

And away you go...

The Commandlines package will be installed automatically for users who
install your releases via ``pip`` or your project ``setup.py`` file
(i.e. with the command ``$ python setup.py install``).

For Local Projects That Are Not Intended for Redistribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the Commandlines package with the command:

::

    $ pip install commandlines

Import the ``commandlines`` package in your project and instantiate a
Command object by adding the following lines to your Python script:

.. code:: python

    from commandlines import Command

    c = Command()

License
-------

Commandlines is licensed under the `MIT license <https://github.com/chrissimpkins/commandlines/blob/master/docs/LICENSE>`__.




.. |Build Status| image:: https://travis-ci.org/chrissimpkins/commandlines.svg?branch=master
   :target: https://travis-ci.org/chrissimpkins/commandlines
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/nabadxorf9s8n0h5/branch/master?svg=true
   :target: https://ci.appveyor.com/project/chrissimpkins/commandlines/branch/master
.. |codecov.io| image:: https://codecov.io/github/chrissimpkins/commandlines/coverage.svg?branch=master
   :target: https://codecov.io/github/chrissimpkins/commandlines?branch=master
.. |Code Health| image:: https://landscape.io/github/chrissimpkins/commandlines/master/landscape.svg?style=flat
   :target: https://landscape.io/github/chrissimpkins/commandlines/master

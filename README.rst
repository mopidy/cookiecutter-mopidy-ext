***********************
cookiecutter-mopidy-ext
***********************

`cookiecutter <https://cookiecutter.readthedocs.io/>`_ template for a
`Mopidy <https://mopidy.com/>`_ extension.

The template sets up a project with:

- a readme explaining how to install and configure the extension,
- a license file with the Apache License,
- a Python module with an empty Mopidy extension,
- an empty test suite executed with ``pytest``,
- continuous integration using `CircleCI <https://www.circleci.com/>`_,
- test coverage reporting to `Codecov <https://codecov.io/>`_, and
- a ``setup.py`` file for releasing and installing the extension as a Python
  package.


Usage
=====

#. Install `cookiecutter`::

       python3 -m pip install cookiecutter

#. Generate a Mopidy extension project::

       cookiecutter gh:mopidy/cookiecutter-mopidy-ext

#. Create a Git repo from the generated project.

#. Make your Mopidy extension do something.

#. Release the extension to `PyPI <https://pypi.org/>`_.


Further reading
===============

To learn more about creating Mopidy extensions, please read the docs on
`extension development <https://docs.mopidy.com/en/latest/extensiondev/>`_.

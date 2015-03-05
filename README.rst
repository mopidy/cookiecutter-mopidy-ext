***********************
cookiecutter-mopidy-ext
***********************

`cookiecutter <http://cookiecutter.readthedocs.org/>`_ template for a
`Mopidy <http://www.mopidy.com/>`_ extension.

The template sets up a project with:

- a readme explaining how to install and configure the extension,
- a license file with the Apache License,
- a Python module with an empty Mopidy extension,
- an empty test suite executed with ``py.test``,
- continuous integration using `Travis CI <https://www.travis-ci.org/>`_,
- test coverage reporting to `Coveralls <https://coveralls.io/>`_, and
- a ``setup.py`` file for releasing and installing the extension as a Python
  package.


Usage
=====

#. Install `cookiecutter` 0.9.0 or newer::

       pip install cookiecutter

#. Generate a Mopidy extension project::

       cookiecutter https://github.com/mopidy/cookiecutter-mopidy-ext.git

#. Create a Git repo from the generated project.

#. Make your Mopidy extension do something.

#. Release the extension to `PyPI <https://pypi.python.org/>`_.


Further reading
===============

To learn more about creating Mopidy extensions, please read the docs on
`extension development <https://docs.mopidy.com/en/latest/extensiondev/>`_.

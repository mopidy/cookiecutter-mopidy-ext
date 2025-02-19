***********************
cookiecutter-mopidy-ext
***********************

`Copier <https://copier.readthedocs.io/>`_ template for a
`Mopidy <https://mopidy.com/>`_ extension.

The template sets up a project with:

- a readme explaining how to install and configure the extension,
- a license file with the Apache License,
- a Python module with an empty Mopidy extension,
- an empty test suite executed with ``pytest``,
- continuous integration using GitHub Actions,
- test coverage reporting to `Codecov <https://codecov.io/>`_,
- a ``setup.py`` file for releasing and installing the extension as a Python
  package, and
- a GitHub Action to automatically upload packages to PyPI when a GitHub
  Release is created, if the GitHub repo has a `PYPI_TOKEN` secret set.


Usage
=====

#. Install `copier`::

       uv tool install copier
       # or
       pipx install copier

#. Generate a Mopidy extension project::

       copier copy gh:mopidy/cookiecutter-mopidy-ext my-extension-dir

#. Create a Git repo from the generated project.

#. Make your Mopidy extension do something.

#. Release the extension to `PyPI <https://pypi.org/>`_.


Further reading
===============

To learn more about creating Mopidy extensions, please read the docs on
`extension development <https://docs.mopidy.com/en/latest/extensiondev/>`_.

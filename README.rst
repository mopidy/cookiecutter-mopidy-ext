*******************
mopidy-ext-template
*******************

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

#. Create a new empty Git repo for your Mopidy extension::

       mkdir mopidy-foobar
       cd mopidy-foobar
       git init

#. Generate the skeleton of a new Mopidy extension by using `uv
   <https://docs.astral.sh/uv/>`_ to run `Copier
   <https://copier.readthedocs.io/>`__ with this extension template::

       uvx copier copy gh:mopidy/mopidy-ext-template .

#. Create a Git repo from the generated project.

#. Make your Mopidy extension do something. To learn more about creating Mopidy
   extensions, please read the docs on `extension development
   <https://docs.mopidy.com/latest/extensiondev/>`_.

#. Release the extension to `PyPI <https://pypi.org/>`_.

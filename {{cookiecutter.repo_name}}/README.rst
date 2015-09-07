****************************
{{ cookiecutter.dist_name }}
****************************

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.dist_name }}.svg?style=flat
    :target: https://pypi.python.org/pypi/{{ cookiecutter.dist_name }}/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.dist_name }}.svg?style=flat
    :target: https://pypi.python.org/pypi/{{ cookiecutter.dist_name }}/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat
   :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Test coverage

{{ cookiecutter.short_description }}


Installation
============

Install by running::

    pip install {{ cookiecutter.dist_name }}

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
{{ cookiecutter.dist_name }} to your Mopidy configuration file::

    [{{ cookiecutter.ext_name }}]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}>`_
- `Issue tracker <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/issues>`_
- `Development branch tarball <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/archive/master.tar.gz#egg={{ cookiecutter.dist_name }}-dev>`_


Changelog
=========

v{{ cookiecutter.version }} (UNRELEASED)
----------------------------------------

- Initial release.

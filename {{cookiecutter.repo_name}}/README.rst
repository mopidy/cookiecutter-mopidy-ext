****************************
{{ cookiecutter.dist_name }}
****************************

.. image:: https://pypip.in/v/{{ cookiecutter.dist_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ cookiecutter.dist_name }}/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/{{ cookiecutter.dist_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ cookiecutter.dist_name }}/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.png?branch=master
   :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
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
- `Download development snapshot <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/archive/master.tar.gz#egg={{ cookiecutter.dist_name }}-dev>`_


Changelog
=========

v{{ cookiecutter.version }} (UNRELEASED)
----------------------------------------

- Initial release.

****************************
{{ cookiecutter.dist_name }}
****************************

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.dist_name }}
    :target: https://pypi.org/project/{{ cookiecutter.dist_name }}/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/CI
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions
    :alt: CI build status

.. image:: https://img.shields.io/codecov/c/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Test coverage

{{ cookiecutter.short_description }}


Installation
============

Install by running::

    python3 -m pip install {{ cookiecutter.dist_name }}

See https://mopidy.com/ext/{{ cookiecutter.ext_name }}/ for alternative installation methods.


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
- `Changelog <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `{{ cookiecutter.author_full_name }} <https://github.com/{{ cookiecutter.github_username }}>`__
- Current maintainer: `{{ cookiecutter.author_full_name }} <https://github.com/{{ cookiecutter.github_username }}>`__
- `Contributors <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/graphs/contributors>`_

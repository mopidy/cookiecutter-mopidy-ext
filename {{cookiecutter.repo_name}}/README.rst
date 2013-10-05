{{ cookiecutter.dist_name }}
============================

{{ cookiecutter.short_description }}

Usage
-----

Install by running::

    pip install {{ cookiecutter.dist_name }}

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.

Before starting Mopidy, you must add configuration for
{{ cookiecutter.dist_name }} to your Mopidy configuration file::

    [{{ cookiecutter.ext_name }}]
    # TODO: Add example of extension config

Project resources
-----------------

- `Source code <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}>`_
- `Issue tracker <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/issues>`_
- `Download development snapshot <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}/tarball/master#egg={{ cookiecutter.dist_name }}-dev>`_

# mopidy-ext-template

[Copier](https://copier.readthedocs.io/) template for a
[Mopidy](https://mopidy.com/) extension.

The template sets up a project with:

- `README.md`: a readme explaining how to install and configure the extension,
  as well as how to contribute to the project,
- `LICENSE`: the Apache License, Version 2.0,
- `src/`: the skeleton of a Mopidy extension,
- `tests/`: the skeleton of a test suite,
- `pyproject.toml`: configuration for all of the development tools:

  - packaging and distribution with [setuptools](https://setuptools.pypa.io/),
  - testing with [pytest](https://pytest.org/),
  - type checking with [Pyright](https://microsoft.github.io/pyright/),
  - formatting and linting with [Ruff](https://docs.astral.sh/ruff/),
  - multi-environment testing with [tox](https://tox.wiki/),

- `.github/workflows/ci.yml`: a GitHub Actions workflow for continuous
  integration, running all the tox environments, with test coverage reporting to
  [Codecov](https://codecov.io/),
- `.github/workflows/release.yml`: a GitHub Actions workflow for automatically
  publishing the extension to PyPI when a GitHub Release is created.

## Creating a Mopidy extension

1. Create a new empty Git repo for your Mopidy extension:

   ```sh
   mkdir mopidy-foobar
   cd mopidy-foobar
   git init
   ```

2. Generate the skeleton of a new Mopidy extension by using
   [uv](https://docs.astral.sh/uv/) to run
   [Copier](https://copier.readthedocs.io/) with this extension template:

   ```sh
   uvx copier copy gh:mopidy/cookiecutter-mopidy-ext .
   ```

3. Make your Mopidy extension do something. To learn more about creating Mopidy
   extensions, please read the docs on [extension
   development](https://docs.mopidy.com/latest/extensiondev).

4. Release the extension to [PyPI](https://pypi.org/) by following the
   instructions in the generated `README.md` file.

## Updating a Mopidy extension

When this template is updated, you can update your extension to the latest
tagged version of this template by running:

```sh
cd mopidy-foobar
uvx copier update .
```

For details on how this works, see Copier's [update documentation
](https://copier.readthedocs.io/en/stable/updating/).

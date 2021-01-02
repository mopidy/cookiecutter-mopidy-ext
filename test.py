#!/usr/bin/env python

"""
Script to test that the cookiecutter can successfully render a project.
"""

from cookiecutter.main import cookiecutter

cookiecutter(
    ".",
    no_input=True,
    extra_context={
        "author_full_name": "Alice",
        "author_email": "alice@example.com",
        "github_username": "alice",
        "dist_name": "Mopidy-Example",
    },
    output_dir="test_result",
    overwrite_if_exists=True,
)

print("OK, see ./test_result/ for results.")

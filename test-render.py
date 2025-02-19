#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#     "copier",
#     "typer",
# ]
# ///

"""
Script to test that Copier can successfully render a project.
"""

import pathlib
import shutil

import copier
import typer


def main(dst: pathlib.Path | None = None):
    if dst is None:
        dst = pathlib.Path(__file__).parent / "test-result"

    if dst.exists():
        print(f"Deleting: {dst}")
        shutil.rmtree(dst)

    copier.run_copy(
        "template",
        dst,
        data={
            "author_full_name": "Alice",
            "author_email": "alice@example.com",
            "github_username": "alice",
            "dist_name": "Mopidy-Example",
            "repo_name": "mopidy-example",
            "ext_name": "example",
            "version": "0.1.0",
        },
    )

    print(f"Done. Copied to: {dst}")


if __name__ == "__main__":
    typer.run(main)

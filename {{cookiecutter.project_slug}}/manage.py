#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import {{cookiecutter.project_slug}}
    from aioworkers import cli
    cli.context.config.load(*{{cookiecutter.project_slug}}.configs)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

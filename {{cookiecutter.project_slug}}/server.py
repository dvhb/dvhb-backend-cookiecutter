#!/usr/bin/env python

from aiohttp import web


if __name__ == '__main__':
    web.main(['{{cookiecutter.project_slug}}.app:Application'])
else:
    from {{cookiecutter.project_slug}}.app import Application

    app = Application()

import collections
import os

import django
import aiohttp_jinja2
import jinja2
import aioworkers_aiohttp.app

from dvhb_hybrid.config import dirs
from dvhb_hybrid.amodels import AppModels

from .settings import BASE_DIR

import {{cookiecutter.project_slug}}

from aiohttp_wsgi import WSGIHandler

wsgi_handler = WSGIHandler({{cookiecutter.project_slug}}.wsgi.application)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_slug}}.settings')
django.setup()

AppModels.import_all_models_from_packages({{cookiecutter.project_slug}})


class Application(aioworkers_aiohttp.app.Application):
    def __init__(self, config, *args, **kwargs):
        from {{cookiecutter.project_slug}}.router import create_router
        router = create_router()
        router.add_route("*", "/{path_info:(admin|static|media).*}", wsgi_handler)

        super().__init__(config, *args, router=router, **kwargs)
        self['state'] = collections.Counter()

        aiohttp_jinja2.setup(
            self, loader=jinja2.FileSystemLoader(
                dirs(self.context.config.path.templates, base_dir=BASE_DIR)),
        )

    @property
    def name(self):
        return self.config.name

    @property
    def sessions(self):
        return self.get('sessions')

    @property
    def redis(self):
        return self.get('redis')

    @property
    def db(self):
        return self.get('db')

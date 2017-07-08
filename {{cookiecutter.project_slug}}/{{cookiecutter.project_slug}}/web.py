import collections
import os

import django
import aiopg.sa
import aioredis
import aiohttp_jinja2
import jinja2
import aioworkers.http
from aiohttp_apiset.middlewares import jsonify

from dvhb_hybrid.config import dirs
from dvhb_hybrid.amodels import AppModels

from .settings import BASE_DIR

import {{cookiecutter.project_slug}}

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_slug}}.settings')
django.setup()

AppModels.import_all_models_from_packages({{cookiecutter.project_slug}})


class Application(aioworkers.http.Application):
    def __init__(self, **kwargs):
        kwargs['debug'] = kwargs['config'].debug
        from {{cookiecutter.project_slug}}.router import create_router
        router = create_router()

        super().__init__(router=router, **kwargs, middlewares=[jsonify])

        self['state'] = collections.Counter()

        self.models = self.m = AppModels(self)

        aiohttp_jinja2.setup(
            self, loader=jinja2.FileSystemLoader(
                dirs(self.config.path.templates, base_dir=BASE_DIR)),
        )

        cls = type(self)
        self.on_startup.append(cls.startup_database)
        self.on_startup.append(cls.startup_redis)
        self.on_cleanup.append(cls.cleanup_database)
        self.on_cleanup.append(cls.cleanup_redis)

    async def startup_redis(self):
        config = self.config.redis.default
        self['redis'] = await aioredis.create_pool(
            (config.host, config.port),
            db=config.db,
            minsize=config.minsize,
            maxsize=config.maxsize,
            loop=self.loop)
        config = self.config.redis.sessions
        self['sessions'] = await aioredis.create_pool(
            (config.host, config.port),
            db=config.db,
            minsize=config.minsize,
            maxsize=config.maxsize,
            loop=self.loop)

    async def cleanup_redis(self):
        await self['redis'].clear()
        await self['sessions'].clear()

    async def startup_database(self):
        dbparams = self.config.databases.default.config
        self['db'] = await aiopg.sa.create_engine(**dbparams)
        self.models = self.m = AppModels(self)

    async def cleanup_database(self):
        async with self['db']:
            pass

    @property
    def name(self):
        return self.config.app.name

    @property
    def sessions(self):
        return self.get('sessions')

    @property
    def redis(self):
        return self.get('redis')

    @property
    def db(self):
        return self.get('db')

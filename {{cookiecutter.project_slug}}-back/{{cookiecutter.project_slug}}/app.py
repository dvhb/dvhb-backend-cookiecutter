import collections
import os

import aiopg.sa
import aioredis
import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_apiset import SwaggerRouter
from aiohttp_apiset.middlewares import jsonify
from dvhb_hybrid.config import absdir, dirs
from dvhb_hybrid.amodels import AppModels

from .settings import config, PROJECT_DIR

import {{cookiecutter.project_slug}}
AppModels.import_all_models_from_packages({{cookiecutter.project_slug}})


class Application(web.Application):
    def __init__(self, *args, config=config, **kwargs):
        if 'router' not in kwargs:
            router = SwaggerRouter(search_dirs=[
                '{{cookiecutter.project_slug}}/api',
                '{{cookiecutter.project_slug}}'
            ], default_validate=True)
            kwargs['router'] = router
        self.config = config

        middlewares = kwargs.setdefault('middlewares', [])
        middlewares.append(jsonify)

        super().__init__(**kwargs)

        router.include('v1.yaml')
        self['state'] = collections.Counter()

        aiohttp_jinja2.setup(
            self, loader=jinja2.FileSystemLoader(
                dirs(self.config.path.templates, base_dir=PROJECT_DIR)),
        )
        cls = type(self)
        static_root = absdir(config.path.static, base_dir=PROJECT_DIR)
        if not os.path.exists(static_root):
            os.makedirs(static_root)
        self.router.add_static('/static/', static_root, name='static')

        media_root = absdir(config.path.media, base_dir=PROJECT_DIR)
        if not os.path.exists(media_root):
            os.makedirs(media_root)
        self.router.add_static('/media/', media_root, name='media')

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

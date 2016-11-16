import os

import aiopg.sa
import aioredis
import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_apiset import SwaggerRouter
from dvhb_hybrid.config import absdir, dirs
from dvhb_hybrid import files

from {{cookiecutter.project_slug}}.settings import config, PROJECT_DIR


class Application(web.Application):
    def __init__(self, *args, config=config, **kwargs):
        if 'router' not in kwargs:
            router = SwaggerRouter(search_dirs=[
                '{{cookiecutter.project_slug}}/settings/api',
                '{{cookiecutter.project_slug}}'
            ])
            router.include('v1.yaml')

            router.add_search_dir(
                os.path.dirname(os.path.dirname(files.__file__)))
            router.include(
                'files/swagger/routes.yaml', basePath='/api/1',
                operationId_mapping=files.opid,
            )

            kwargs['router'] = router
        self.config = config

        super().__init__(**kwargs)

        aiohttp_jinja2.setup(
            self, loader=jinja2.FileSystemLoader(
                dirs(self.config.path.templates, base_dir=PROJECT_DIR)),
            extensions=['pyjade.ext.jinja.PyJadeExtension'],
        )
        cls = type(self)
        self.on_startup.append(cls.startup_routing)
        self.on_startup.append(cls.startup_database)
        self.on_startup.append(cls.startup_redis)
        self.on_cleanup.append(cls.cleanup_database)
        self.on_cleanup.append(cls.cleanup_redis)

    async def startup_routing(self):
        static_root = absdir(config.path.static, base_dir=PROJECT_DIR)
        if not os.path.exists(static_root):
            os.makedirs(static_root)
        self.router.add_static('/static/', static_root, name='static')

        media_root = absdir(config.path.media, base_dir=PROJECT_DIR)
        if not os.path.exists(media_root):
            os.makedirs(media_root)
        self.router.add_static('/media/', media_root, name='media')

    async def startup_redis(self):
        config = self.config.redis.default
        self['redis'] = await aioredis.create_pool(
            (config.host, config.port),
            db=config.db,
            minsize=config.minsize,
            maxsize=config.maxsize,
            loop=self.loop)

    async def cleanup_redis(self):
        await self['redis'].clear()

    async def startup_database(self):
        dbparams = self.config.databases.default.config
        self['db'] = await aiopg.sa.create_engine(**dbparams)

    async def cleanup_database(self):
        async with self['db']:
            pass


def init(args):
    app = Application()
    return app
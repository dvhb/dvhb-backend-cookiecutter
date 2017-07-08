from aiohttp_apiset import SwaggerRouter
from aiohttp_apiset.swagger.loader import deref


def create_router():
    router = SwaggerRouter(search_dirs=[
        '{{cookiecutter.project_slug}}',
    ], encoding='utf-8', default_validate=True, swagger_ui='/api/1/apidoc/')

    router.include('api.yaml')

    return router


_router = create_router()


def get_definition(definition):
    schema = deref(_router._swagger_data['/api/1']['definitions'].get(definition), _router._swagger_data['/api/1'])
    return schema

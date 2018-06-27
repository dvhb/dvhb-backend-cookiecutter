import pytest
from aioworkers import cli
from aioworkers.core.context import Context, GroupResolver
from dvhb_hybrid.tests import AuthClient

pytest_plugins = ['dvhb_hybrid.tests']


@pytest.fixture(scope='session')
def config():
    return cli.context.config


@pytest.fixture
def groups():
    return dict(
        include={'web'},
    )


@pytest.fixture
def context(loop, groups, config):
    gr = GroupResolver(**groups)
    with Context(config, loop=loop, group_resolver=gr) as ctx:
        yield ctx


@pytest.fixture
def app(context):
    return context.app


class TestClient(AuthClient):
    base_path = '/api/1'

    async def ensure_user(self, new_user=False, **kwargs):
        pass


@pytest.fixture
def client_class():
    return TestClient


@pytest.fixture
def user():
    return {
        'email': 'user@example.com',
        'password': 'password',
    }


@pytest.fixture
def admin_user():
    return {
        'email': 'admin@example.com',
        'password': 'password'
    }

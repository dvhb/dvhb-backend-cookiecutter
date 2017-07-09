import py
import pytest
import requests

from requests.exceptions import ConnectionError


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope='session')
def integration_project(cookies):
    result = cookies.bake(extra_context={'project_name': 'testapp'})
    py.path.local('tests/docker').copy(result.project)
    return result.project


@pytest.fixture(scope='session')
def docker_compose_file(integration_project, pytestconfig):
    return integration_project.join('docker-compose.yml')


@pytest.fixture(scope='session')
def admin_service(docker_services):
    url = f'http://localhost:{docker_services.port_for("admin", 8000)}/admin'
    docker_services.wait_until_responsive(
       timeout=15.0, pause=0.1,
       check=lambda: is_responsive(url)
    )
    return url


def test_admin(admin_service):
    response = requests.get(admin_service)
    response.raise_for_status()

import os
import pytest
import sh


@pytest.fixture
def context():
    return {
        'project_name': 'Project',
        'project_slug': 'project',
    }


def check_project_result(result):
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()

    try:
        sh.flake8(str(result.project))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    check_project_result(result)


def test_disabled_users_app(cookies, context):
    context.update({'users_app': 'n'})
    result = cookies.bake(extra_context=context)
    check_project_result(result)

    # Check that users app not added to application
    users_app_folder = os.path.join(result.project, context['project_slug'], 'users')
    assert not os.path.isdir(users_app_folder)


def test_disabled_invoke_tasks(cookies, context):
    context.update({'invoke_tasks': 'n'})
    result = cookies.bake(extra_context=context)
    check_project_result(result)

    # Check that tasks file was not added
    tasks_file = os.path.join(result.project, 'tasks.py')
    assert not os.path.isfile(tasks_file)

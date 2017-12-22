from pathlib import Path
import pytest
import sh


def check_project_result(result):
    """
    Method to common project baking verification
    """
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()

    # Check project with flake8
    try:
        sh.flake8(str(result.project))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    check_project_result(result)

    # requirements file used by default
    path = Path(result.project)
    assert (path / 'requirements').exists()
    assert not (path / 'Pipfile').exists()


def test_disabled_users_app(cookies, context):
    context.update({'users_app': 'n'})
    result = cookies.bake(extra_context=context)
    check_project_result(result)

    # Check that users app not added to application
    path = Path(result.project)
    assert not (path / context['project_slug'] / 'users').exists()


def test_pipfile(cookies, context):
    context.update({'use_pipfile': 'y'})
    result = cookies.bake(extra_context=context)
    check_project_result(result)

    # Check that users app not added to application
    path = Path(result.project)
    assert not (path / 'requirements').exists()
    assert (path / 'Pipfile').exists()

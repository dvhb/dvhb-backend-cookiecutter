import pytest
import sh


@pytest.fixture
def context():
    return {
        'project_name': 'Project',
        'project_slug': 'project',
    }


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['project_slug'] + '-back'
    assert result.project.isdir()

    try:
        sh.flake8(str(result.project))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)

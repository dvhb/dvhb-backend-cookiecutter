import shutil
from pathlib import Path

PROJECT_PATH = Path.cwd()

if '{{ cookiecutter.users_app }}'.lower() == 'n':
    # Remove folder with user app
    shutil.rmtree(str(PROJECT_PATH / '{{ cookiecutter.project_slug }}' / 'users'))


if '{{ cookiecutter.use_pipfile }}'.lower() == 'y':
    # Remove folder with requirements if project uses Pipfile to store requirements
    shutil.rmtree(str(PROJECT_PATH / 'requirements'))
else:
    (PROJECT_PATH / 'Pipfile').unlink()

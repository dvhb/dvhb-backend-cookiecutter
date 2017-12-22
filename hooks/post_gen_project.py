import shutil
from pathlib import Path

PROJECT_PATH = Path.cwd()

if '{{ cookiecutter.users_app }}'.lower() == 'n':
    shutil.rmtree(str(PROJECT_PATH / '{{ cookiecutter.project_slug }}' / 'users'))


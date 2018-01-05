import shutil
from pathlib import Path

PROJECT_PATH = Path.cwd()


if '{{ cookiecutter.use_pipfile }}'.lower() == 'y':
    # Remove folder with requirements if project uses Pipfile to store requirements
    shutil.rmtree(str(PROJECT_PATH / 'requirements'))
else:
    (PROJECT_PATH / 'Pipfile').unlink()

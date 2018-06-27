import os
from pathlib import Path

try:
    from .version import VERSION as __version__
except ImportError:
    __version__ = 'DEV'


BASE = Path(__file__).parent

configs = (
    BASE / 'config.yaml',
)
for i in ('TEST_CONF', '{{ cookiecutter.project_name.upper() }}_CONF'):
    if os.getenv(i):
        configs += Path(os.getenv(i)).absolute(),

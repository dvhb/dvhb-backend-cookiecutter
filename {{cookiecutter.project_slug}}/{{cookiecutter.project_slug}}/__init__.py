from pathlib import Path

from . import wsgi  # noqa
from aioworkers.core.config import Config

try:
    from .version import VERSION as __version__
except ImportError:
    __version__ = 'DEV'


BASE = Path(__file__).parent

configs = (
    BASE / 'config.yaml',
)


def get_config():
    return Config().load(*configs)

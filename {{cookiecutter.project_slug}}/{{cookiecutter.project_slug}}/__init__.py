from . import wsgi  # noqa

try:
    from .version import VERSION as __version__
except ImportError:
    __version__ = 'DEV'

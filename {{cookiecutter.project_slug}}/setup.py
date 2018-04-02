import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent
for i in (here / '{{cookiecutter.project_slug}}' / 'version.py').open('rt'):
    i = i.strip()
    if i.startswith("VERSION"):
        version = i.lstrip('VERSION').strip(" ='")
        break
else:
    raise RuntimeError('Unable to determine version.')

setup(
    name='{{cookiecutter.project_slug}}',
    version=version,
    packages=['{{cookiecutter.project_slug}}'],
    python_requires='>=3.5.3',
    include_package_data=True,
    scripts=['manage.py'],
)

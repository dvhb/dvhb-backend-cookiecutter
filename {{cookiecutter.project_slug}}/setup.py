import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent
for i in (here / '{{cookiecutter.project_slug}}' / 'version.py').open('rt'):
    i = i.strip()
    if i.startswith("VERSION"):
        version = i.lstrip('VERSION').strip(" ='")
        break
else:
    raise RuntimeError('Unable to determine version.')

name = '{{cookiecutter.project_slug}}'

setup(
    name=name,
    version=version,
    packages=[i for i in find_packages() if i.startswith(name)],
    python_requires='>=3.5.3',
    include_package_data=True,
    scripts=['manage.py'],
)

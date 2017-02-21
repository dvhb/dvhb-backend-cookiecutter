from invoke import task
from {{cookiecutter.project_slug}}.settings import config


@task
def initdb(ctx):
    """Initialize db for development"""
    fixtures = ' '.join(config.fixtures)
    db_name = config['databases']['default']['database']
    ctx.run(f'dropdb --if-exists {db_name}')
    ctx.run(f'createdb {db_name}')
    ctx.run('rm -rf {{cookiecutter.project_slug}}/*/migrations/0*.py')
    ctx.run('python manage.py makemigrations')
    ctx.run('python manage.py migrate')
    ctx.run(f'python manage.py loaddata {fixtures}')

import subprocess

from django.core.management import call_command
from django.core.management.base import BaseCommand

from {{cookiecutter.project_slug}}.settings import config


class Command(BaseCommand):
    help = 'Initialize development database'

    def handle(self, *args, **options):
        db_name = config['databases']['default']['database']
        subprocess.run(['dropdb', '--if-exists', db_name], stdout=self.stdout)
        subprocess.run(['createdb', db_name], stdout=self.stdout)
        subprocess.run(['rm', '-rf', '{{cookiecutter.project_slug}}/*/migrations/0*.py'], stdout=self.stdout)
        call_command('makemigrations')
        call_command('migrate')
        call_command('loaddata', *config.fixtures)

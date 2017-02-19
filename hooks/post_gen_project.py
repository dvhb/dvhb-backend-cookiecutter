import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_users_files():
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}', 'users'
    ))


if '{{ cookiecutter.users_app }}'.lower() != 'y':
    remove_users_files()

if '{{ cookiecutter.invoke_tasks }}'.lower() != 'y':
    os.remove(os.path.join(
        PROJECT_DIRECTORY, 'tasks.py'
    ))

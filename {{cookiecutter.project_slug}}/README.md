# {{ cookiecutter.project_name }}

## Dependencies
* Python 3.6 or above
* PostgreSQL 10 or above
* Redis 3 or above

## Prepare dev environment

```bash
python3.6 -m venv env
. env/bin/activate
pip install -U pip pipenv
pipenv install -d
```

## Prepare database on PostgreSQL

```bash
python manage.py initdb
```

## Run backend

```bash
aioworkers {{cookiecutter.project_slug}} -g --logging info
```
Go to [http://localhost:8080/apidoc/](http://localhost:8080/apidoc/)

## Django Admin

Go to [http://localhost:8080/admin](http://localhost:8080/admin)

## Run tests

```bash
pytest
```

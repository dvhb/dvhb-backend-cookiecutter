# {{ cookiecutter.project_name }}

## Dependencies
* Python 3.6 or above
* PostgreSQL 9.5 or above
* Redis 2.8 or above

## Prepare environment

```bash
python3.6 -m venv venv
. venv/bin/activate
pip install -r requirements/base.txt
```

## Prepare database on PostgreSQL

```bash
python manage.py initdb
```

## Run asyncio API

```bash
python -m aioworkers.cli -c {{cookiecutter.project_slug}}/config.yaml -g --logging info
```
Go to [http://localhost:8080/api/1/apidoc/](http://localhost:8080/api/1/apidoc/)

## Django Admin

```bash
python manage.py runserver
```

Go to [http://localhost:8000/admin](http://localhost:8000/admin)

## Run tests

```bash
$ {{ cookiecutter.project_name.upper() }}_CONF=conf/test.yaml pytest
```

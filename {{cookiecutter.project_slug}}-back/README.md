# {{ cookiecutter.project_name }}

## Install dependencies

```bash
python3.6 -m venv venv
. venv/bin/activate
pip install -r requirements/base.txt
```

## Prepare database on PostgreSQL

```bash
createdb {{cookiecutter.project_slug}}
python manage.py makemigrations
python manage.py migrate
```

## Run asyncio API

```bash
python -m {{cookiecutter.project_slug}}
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
# {{ cookiecutter.project_name }}

## Install dependencies

```bash
python3.6 -m venv venv
. venv/bin/activate
pip install -r requirements/base.txt
```

## Run asyncio API

```bash
python -m {{cookiecutter.project_slug}}
```
Go to http://localhost:8080/api/1/apidoc/

## Django Admin

```bash
python manage.py runserver
```

Go to http://localhost:8000/admin
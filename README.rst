.. image:: https://travis-ci.org/dvhb/dvhb-backend-cookiecutter.svg?branch=master
     :target: https://travis-ci.org/dvhb/dvhb-backend-cookiecutter?branch=master
     :alt: Build Status

Cookiecutter template to create projects based on dvhb-hybrid (https://github.com/dvhb/dvhb-hybrid).

Features
--------

* Based on Python 3.6.
* YAML configs for application.
* Uses aiohttp-apiset to create REST API based on swagger specification.

Install cookiecutter in you venv:

    $ pip install cookiecutter

Run it over template repository:

    $ cookiecutter git@github.com:dvhb/dvhb-backend-cookiecutter.git

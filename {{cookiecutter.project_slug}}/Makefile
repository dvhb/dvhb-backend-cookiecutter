RELEASE=latest
PACKAGE={{cookiecutter.project_slug}}
VERSION=$(shell git describe --always --tags)

PYTHON=/opt/python3.6/bin/python3
ENVDIR=./env

all:
	$(PYTHON) -m venv $(ENVDIR)
	$(ENVDIR)/bin/pip install -U pip pipenv
	$(ENVDIR)/bin/pipenv install -d

.PHONY: all docker {{cookiecutter.project_slug}}/version.py

docker: dist/$(PACKAGE)-$(VERSION).tar.gz
	cp $< docker/{{cookiecutter.project_slug}}.tar.gz
	cp Pipfile* docker/
	sudo docker build docker -t {{cookiecutter.project_slug}}:$(RELEASE)

{{cookiecutter.project_slug}}/version.py:
	echo "VERSION = '$(VERSION)'" > $@

dist/$(PACKAGE)-%.tar.gz: {{cookiecutter.project_slug}}/version.py
	python setup.py sdist

clean:
	rm -fr dist

recut: ../{{cookiecutter.project_slug}}
	cd .. \
	&& rm -fr {{cookiecutter.project_slug}} \
	&& cookiecutter . \
	&& cd {{cookiecutter.project_slug}} \
	&& pipenv install

RELEASE=latest
PACKAGE={{cookiecutter.project_slug}}
VERSION=$(shell git describe --always --tags)

all:

.PHONY: all docker

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

recut:
	cd .. \
	&& rm -fr {{cookiecutter.project_slug}} \
	&& cookiecutter . \
	&& cd {{cookiecutter.project_slug}} \
	&& pipenv install

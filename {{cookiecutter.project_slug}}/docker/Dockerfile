FROM python:3.6-alpine

RUN apk add --update \
    bash \
    git \
    build-base gcc \
    openssl-dev \
    postgresql-dev \
    yaml-dev \
    jpeg-dev \
    zlib-dev \
    && rm -rf /var/cache/apk/*
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    LANGUAGE=C.UTF-8
RUN pip install -U pip pipenv

ENV DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings \
    STATIC_ROOT=/static \
    MEDIA_ROOT=/media
WORKDIR /project
ADD Pipfile /project/
ADD Pipfile.lock /project/
RUN pipenv install --system --deploy

ENV DJANGO_SETTINGS_MODULE=servier.settings \
    STATIC_ROOT=/static \
    MEDIA_ROOT=/media

COPY {{cookiecutter.project_slug}}.tar.gz /project/
RUN pip install {{cookiecutter.project_slug}}.tar.gz && \
    django-admin collectstatic -l

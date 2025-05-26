#!/usr/bin/env bash

set -o errexit

pipenv install

python3 manage.py migrate

python3 manage.py collectstatic --no-input

python3 manage.py createsuperuser --noinput
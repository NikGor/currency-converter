install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 converter

build:
	poetry build

selfcheck:
	poetry check

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

dev:
	export FLASK_APP=converter.api
	export FLASK_ENV=development
	flask run

start:
	poetry run uvicorn converter.app:app

ALL: lint install build




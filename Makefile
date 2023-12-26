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
	export FLASK_APP=converter.app
	export FLASK_ENV=development
	flask run

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:5000 converter.app:app
	poetry run uvicorn converter.app:app --host

ALL: lint install build




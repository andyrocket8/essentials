# Make file for shortcut commands

lint:
	poetry run isort .
	poetry run flake8 -v --config setup.cfg
	poetry run black .
	poetry run mypy .

test:
	poetry run pytest -s

coverage:
	poetry run coverage run -m pytest
	poetry run coverage html
test:
	pytest tests/test_.py

linter:
	flake8 .

mypy:
	mypy .

test:
	pytest tests

test_cov:
	pytest --cov=src tests

linter:
	flake8 .

mypy:
	mypy src/

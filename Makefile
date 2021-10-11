MYPY_OPTIONS = --config-file pyproject.toml

.PHONY: test
test:
	poetry run pytest tests

.PHONY: lint-check
lint-check:
	poetry run flake8 src tests

.PHONY: type-check
type-check:
	poetry run mypy ${MYPY_OPTIONS} src tests

.PHONY: install
install:
	poetry install

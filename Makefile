.PHONY: test
test:
	poetry run pytest tests

.PHONY: install
install:
	poetry install

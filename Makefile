.SILENT:

.PHONY: clean
clean:
	find . -iname '*.pyc' -delete

.PHONY: docs
docs:
	$(MAKE) --directory=docs html

.PHONY: lint
lint:
	flake8 pysuru

.PHONY: test
test:
	py.test

.PHONY: coverage
coverage:
	py.test --cov=pysuru --cov-report=term-missing

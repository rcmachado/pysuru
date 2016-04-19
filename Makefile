.SILENT:

.PHONY: docs
docs:
	$(MAKE) --directory=docs html

.PHONY: test
test:
	py.test

.PHONY: coverage
coverage:
	py.test --cov=pysuru --cov-report=term-missing

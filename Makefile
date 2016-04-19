.SILENT:

test:
	py.test

.PHONY: coverage
coverage:
	py.test --cov=pysuru --cov-report=term-missing

env:
	pip install --upgrade pip
	pip install --editable .
	pip install -r requirements-dev.txt

coveragereport:
	pytest --cov --cov-report xml
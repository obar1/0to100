install:
	pip install --upgrade pip && pip install -r requirements-dev.txt

test:
	python -m pytest zero_to_one_hundred

format:
	black zero_to_one_hundred

lint:
	pylint --disable=R,C,W0702,W0621,W1203 zero_to_one_hundred

refactor: format lint
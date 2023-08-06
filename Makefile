venv0:
	virtualenv venv && true
	@echo "$  . ./venv/bin/activate"

install:
	pip install --upgrade pip && pip install -r requirements.txt
	pre-commit install

test:
	python -m pytest zero_to_one_hundred/tests/test_*.py

format:
	black zero_to_one_hundred

lint:
	pylint --disable=R,C,W0702,W0621,W1203 zero_to_one_hundred

pcommit: format lint

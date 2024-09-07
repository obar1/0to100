install:
	pip install --upgrade pip && pip install -r requirements-dev.txt

test:
	python -m pytest zero_to_one_hundred

testint:
	bash demo.sh 0to100 && bash demo.sh 0to100_sb

format:
	black zero_to_one_hundred

lint:
	pylint --disable=C0116,C0115,W0702,C0114,C0301,C0103,C0209,R0913,R0902,R0903,E1101,W0612,W0718,R0801,W0150,W0613,W1203 zero_to_one_hundred

refactor: format lint

pr: format lint test testint install

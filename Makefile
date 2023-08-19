venv0:
	virtualenv venv && true
	@echo "$  . ./venv/bin/activate"

install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	cd zero_to_one_hundred/tests/resources &&  pytest --log-cli-level=DEBUG --capture=tee-sys  ..

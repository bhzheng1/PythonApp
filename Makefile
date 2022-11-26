install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

# Test function
test:
	python -m pytest -vv test_hello.py

format:
	black *.py


# Test format
lint:
	pylint --disable=R,C hello.py

all:
	instlal lint test format
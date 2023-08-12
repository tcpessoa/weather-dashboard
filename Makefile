.PHONY: test clean run
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip


run: venv
	$(PYTHON) main.py

venv: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

test: venv
	${PYTHON} -m pytest

clean:
	rm -rf __pycache__
	rm -rf $(VENV)


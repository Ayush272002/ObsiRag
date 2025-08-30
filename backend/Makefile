PYTHON=python3
VENV_DIR=venv
REQUIREMENTS=requirements.txt

.PHONY: install start clean

install:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r $(REQUIREMENTS)

start:
	. $(VENV_DIR)/bin/activate && $(PYTHON) main.py

clean:
	rm -rf $(VENV_DIR)
	find . -type d -name '__pycache__' -exec rm -rf {} +
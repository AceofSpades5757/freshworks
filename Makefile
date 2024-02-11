PROJECT_NAME = "freshworks"

VENV_DIR = .venv

ifeq ($(OS),Windows_NT)
	PYTHON = py
	VENV_BIN = ./$(VENV_DIR)/Scripts
else
	PYTHON = python3
	VENV_BIN = ./$(VENV_DIR)/bin
endif
VENV_PYTHON = $(VENV_DIR)/Scripts/python
VENV_PIP = $(VENV_DIR)/Scripts/pip

venv:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --upgrade virtualenv
	$(PYTHON) -m virtualenv .venv
	-$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	$(VENV_PIP) install -r dev-requirements.txt

clean:
	@echo "Removing temporary files, caches, and build files."
	# Build Directories
	rm -rf build/
	rm -rf dist/
	# Temporary Files
	rm -rf __pycache__/
	rm -rf */**/__pycache__/
	rm -rf *.egg-info/
	rm -rf */**/*.egg-info/
	rm -rf .mypy_cache/
	# Logs
	rm -rf logs/
	rm -rf */**/logs/
	rm -rf *.log
	rm -rf */**/*.log

build:
	@echo "Building $(PROJECT_NAME)."
	# Build
	$(VENV_PYTHON) setup.py sdist bdist_wheel

publish: build
	@echo "Deploying $(PROJECT_NAME) to PyPi."
	$(VENV_PIP) install --upgrade twine
	$(VENV_PYTHON) -m twine upload dist/*

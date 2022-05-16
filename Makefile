PROJECT_NAME = "freshworks"

PYTHON = py
VENV_DIR = .venv
VENV_PYTHON = ${VENV_DIR}/Scripts/python.exe
VENV_PIP = ${VENV_DIR}/Scripts/pip.exe

# Settings
.DEFAULT_GOAL = help

help:
	@echo Manage $(PROJECT_NAME). Usage:
	@echo
	@echo make test - Test $(PROJECT_NAME).
	@echo make venv - Create virtual environment.
	@echo make clean - Remove caches, temp files, build files, etc.
	@echo make build - Build wheels.
	@echo make publish - Publish to PyPi.

venv:
	-${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --upgrade virtualenv
	${PYTHON} -m virtualenv .venv
	-${VENV_PIP} install --upgrade pip
	${VENV_PIP} install -r requirements.txt
	${VENV_PIP} install -r dev-requirements.txt

test:
	${VENV_PYTHON} -m unittest discover --start-directory tests --pattern *_test.py

clean:
	@echo "Removing temporary files, caches, and build files."
	# Build Directories
	rm -rf build/
	rm -rf dist/
	# Temporary Files
	rm -rf __pycache__/
	rm -rf **/__pycache__/
	rm -rf *.egg-info/
	rm -rf **/*.egg-info/
	rm -rf .mypy_cache/
	# Logs
	rm -rf logs/
	rm -rf **/logs/
	rm -rf *.log
	rm -rf **/*.log

build:
	@echo "Building $(PROJECT_NAME)."
	# Build
	${VENV_PYTHON} setup.py sdist bdist_wheel

publish: build
	@echo "Deploying $(PROJECT_NAME) to PyPi."
	${VENV_PIP} install --upgrade twine
	${VENV_PYTHON} -m twine upload dist/*

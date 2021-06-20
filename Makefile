APP_NAME = xmrpy
SOURCE = .
PWD = $(shell pwd)
REQUIREMENTS_DIR = $(PWD)/requirements
PYTHON = $(PWD)/venv/bin/python
PIP = $(PWD)/venv/bin/python -m pip

# pip requirements
CMD_PIP_OUTDATED = $(PIP) list --outdated --format=columns
CMD_PIP_UPDATE = $(CMD_PIP_OUTDATED) | tail -n +3 | cut -d' ' -f1 | xargs -r pip install --upgrade --trusted-host pypi.python.org
CMD_PIP_INSTALL_LOCK = $(PYTHON) -m pip install -r $(REQUIREMENTS_DIR)/requirements.lock --trusted-host pypi.python.org
CMD_PIP_INSTALL = $(foreach file, $(wildcard $(REQUIREMENTS_DIR)/*), $(PIP) install -r $(file) --trusted-host pypi.python.org;)
CMD_PIP_FREEZE = $(PIP) freeze > $(REQUIREMENTS_DIR)/requirements.lock

# code style, linting, and formatting
CMD_BLACK_FORMAT = find . -type d -path ./venv -prune -false -o -name "*.py" | xargs $(PYTHON) -m black -l 120
CMD_PYLINT = find . -type d -path ./venv -prune -false -o -name "*.py" | xargs $(PYTHON) -m pylint --rcfile $(SOURCE)/.pylintrc
CMD_MYPY_INIT = $(PYTHON) -m mypy --config-file $(PWD)/mypy.ini xmrpy/

# test suite
CMD_PYTEST = python -m pytest -s -v -rxs test/*.py

.PHONY: format \
freeze \
install \
installock \
lint \
test \
typing 

format:
	$(CMD_BLACK_FORMAT)

install:
	$(CMD_PIP_INSTALL)

installock:
	$(CMD_PIP_INSTALL_LOCK)

freeze:
	$(CMD_PIP_FREEZE)

typing:
	$(CMD_MYPY_INIT)

test:
	$(CMD_PYTEST)

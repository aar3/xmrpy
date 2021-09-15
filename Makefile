# Copyright 2021 Rashad Alston

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

APP_NAME = xmrpy
SOURCE = .
PWD = $(shell pwd)
REQUIREMENTS_DIR = $(PWD)/requirements
PYTHON = $(PWD)/venv/bin/python
PIP = /usr/local/bin/pipenv

# pip requirements
# CMD_PIP_OUTDATED = $(PIP) list --outdated --format=columns
# CMD_PIP_UPDATE = $(CMD_PIP_OUTDATED) | tail -n +3 | cut -d' ' -f1 | xargs -r pip install --upgrade --trusted-host pypi.python.org

# CMD_PIP_INSTALL_LOCK = $(PYTHON) -m pip install -r $(REQUIREMENTS_DIR)/requirements.lock --trusted-host pypi.python.org
# CMD_PIP_INSTALL = $(foreach file, $(wildcard $(REQUIREMENTS_DIR)/*), $(PIP) install -r $(file) --trusted-host pypi.python.org;)
CMD_PIP_INSTALL_LOCK = $(PIP) install --ignore-pipfile
CMD_PIP_INSTALL = $(PIP) install
CMD_PIP_FREEZE = $(PIP) lock --requirements

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

lint:
	$(CMD_PYLINT)
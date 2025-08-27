# ---- Data Service Catalog Makefile ----
# Goals:
#   make setup     -> create a local Python env & install deps
#   make validate  -> run schema validation on services/*
#   make build     -> generate build/catalog.json
#   make serve     -> preview the website at http://localhost:8080
#   make clean     -> remove build artifacts and caches
#   make help      -> list commands

SHELL := /bin/bash

# Choose Python; create a local venv in .venv
PYTHON ?= python3
VENV = .venv
VPY = $(VENV)/bin/python
VPIP = $(VENV)/bin/pip

# Detect scripts automatically (works with your repo layout)
# If you later rename scripts, just adjust these variables.
VALIDATE_CMD = \
	if [ -f scripts/validate.py ]; then $(VPY) scripts/validate.py; \
	elif [ -f tools/validate.sh ]; then bash tools/validate.sh; \
	elif [ -f pipelines/validate.py ]; then $(VPY) pipelines/validate.py; \
	else echo "No validate script found (looked in scripts/, tools/, pipelines/)."; exit 1; fi

BUILD_CMD = \
	if [ -f scripts/build.py ]; then $(VPY) scripts/build.py; \
	elif [ -f tools/build.sh ]; then bash tools/build.sh; \
	elif [ -f pipelines/build.py ]; then $(VPY) pipelines/build.py; \
	else echo "No build script found (looked in scripts/, tools/, pipelines/)."; exit 1; fi

.PHONY: help
help:
	@echo ""
	@echo "Makefile for Data Service Catalog"
	@echo "---------------------------------"
	@echo "make setup     Create .venv and install Python requirements"
	@echo "make validate  Validate services/*.yaml against schemas/catalog.schema.json"
	@echo "make build     Generate build/catalog.json"
	@echo "make serve     Serve docs/ locally at http://localhost:8080"
	@echo "make clean     Remove build artifacts and caches"
	@echo ""

.PHONY: setup
setup:
	@echo ">> Creating virtual environment in $(VENV) (first run only)…"
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	@echo ">> Installing requirements (if requirements.txt exists)…"
	@test -f requirements.txt && $(VPIP) install -r requirements.txt || echo "No requirements.txt found—skipping."

.PHONY: validate
validate:
	@echo ">> Validating services against schemas/catalog.schema.json…"
	@$(VALIDATE_CMD)
	@echo ">> Validation complete."

.PHONY: build
build:
	@echo ">> Building catalog (producing build/catalog.json)…"
	@mkdir -p build
	@$(BUILD_CMD)
	@test -f build/catalog.json && echo ">> build/catalog.json created." || (echo "Expected build/catalog.json was not found."; exit 1)

.PHONY: serve
serve:
	@echo ">> Serving docs/ at http://localhost:8080 (Ctrl+C to stop)"
	@cd docs && $(PYTHON) -m http.server 8080

.PHONY: clean
clean:
	@echo ">> Cleaning build artifacts and caches…"
	@rm -rf build/ htmlcov/ .coverage
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo ">> Done."

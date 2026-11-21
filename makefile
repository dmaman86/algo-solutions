PYTHON_TEST_DIR = tests/python
UNAME_S := $(shell uname -s)
SHELL := /bin/bash

# Python version used to create ./venv (and by CI). Active environments may also
# use any version in SUPPORTED_PYTHON_VERSIONS: every pinned dependency ships
# binary wheels for them.
PYTHON_VERSION := 3.12
SUPPORTED_PYTHON_VERSIONS := 3.11 3.12
VENV_BOOTSTRAP_PYTHON := python$(PYTHON_VERSION)

# Python environment selection:
#   - an activated virtualenv (VIRTUAL_ENV) or Conda env (CONDA_PREFIX) is used as-is;
#   - otherwise ./venv, created by `make install-python` with Python $(PYTHON_VERSION).
# The Conda base environment is refused (see check-python-env).
ifneq ($(VIRTUAL_ENV),)
  PYTHON := $(VIRTUAL_ENV)/bin/python
else ifneq ($(CONDA_PREFIX),)
  PYTHON := $(CONDA_PREFIX)/bin/python
else
  PYTHON := venv/bin/python
  VENV_DEP := venv/bin/python
endif

.PHONY: setup install-python install-js check-python-env check-python-ready setup-cpp \
	compile-requirements upgrade-requirements check-requirements \
	test test-js test-python test-cpp visualize clean help

setup: install-python install-js setup-cpp

# --- Python ---------------------------------------------------------------

# Refuses the Conda base environment and Python versions without wheels for the pins.
check-python-env:
	@if [ -z "$(VIRTUAL_ENV)" ] && [ "$(CONDA_DEFAULT_ENV)" = "base" ]; then \
		echo "Refusing to use the Conda 'base' environment."; \
		echo "Run 'conda activate algo-solutions', or 'conda deactivate' to use ./venv."; \
		exit 1; \
	fi
	@if [ -x "$(PYTHON)" ]; then \
		version=$$($(PYTHON) -c 'import sys; print("%d.%d" % sys.version_info[:2])'); \
		case " $(SUPPORTED_PYTHON_VERSIONS) " in \
			*" $$version "*) ;; \
			*) echo "Python $$version at $(PYTHON) is not supported (supported: $(SUPPORTED_PYTHON_VERSIONS))."; \
			   exit 1 ;; \
		esac; \
	fi

venv/bin/python:
	@command -v $(VENV_BOOTSTRAP_PYTHON) >/dev/null 2>&1 || { \
		echo "Python $(PYTHON_VERSION) is required to create ./venv, but '$(VENV_BOOTSTRAP_PYTHON)' was not found on PATH."; \
		echo "Install it (e.g. 'brew install python@$(PYTHON_VERSION)' or 'uv python install $(PYTHON_VERSION)'),"; \
		echo "or activate a Conda env/virtualenv with a supported Python ($(SUPPORTED_PYTHON_VERSIONS))."; \
		exit 1; \
	}
	@echo "Creating virtual environment in ./venv with $(VENV_BOOTSTRAP_PYTHON)..."
	@$(VENV_BOOTSTRAP_PYTHON) -m venv --upgrade-deps venv

# Installs exactly what requirements.txt declares into the selected environment.
# A no-op when everything is already satisfied.
install-python: check-python-env $(VENV_DEP)
	@echo "Installing Python dependencies into $$($(PYTHON) -c 'import sys; print(sys.prefix)')..."
	@$(PYTHON) -m pip install --disable-pip-version-check -r requirements.txt
	@$(PYTHON) -m pip check

# Test targets never install: they only require an existing, supported environment.
check-python-ready: check-python-env
	@[ -x "$(PYTHON)" ] || { \
		echo "No Python environment found at $(PYTHON). Run 'make install-python' first."; \
		exit 1; \
	}

# --- Python dependency maintenance (pip-tools) -----------------------------
# requirements.in lists the direct dependencies; requirements.txt is generated
# from it by pip-compile and committed. pip-tools is a maintenance tool: it lives
# in its own ./.venv-tools (Python $(PYTHON_VERSION)) and never in the project
# environment. Installing and testing never run pip-compile.
PIP_TOOLS_VERSION := 7.7.0
TOOLS_VENV := $(CURDIR)/.venv-tools
PIP_COMPILE := CUSTOM_COMPILE_COMMAND="make compile-requirements" \
	$(TOOLS_VENV)/bin/pip-compile --quiet --strip-extras --no-emit-index-url

$(TOOLS_VENV)/bin/pip-compile:
	@command -v $(VENV_BOOTSTRAP_PYTHON) >/dev/null 2>&1 || { \
		echo "'$(VENV_BOOTSTRAP_PYTHON)' was not found on PATH; it is required to resolve dependencies for Python $(PYTHON_VERSION)."; \
		exit 1; \
	}
	@echo "Installing pip-tools $(PIP_TOOLS_VERSION) into ./.venv-tools..."
	@$(VENV_BOOTSTRAP_PYTHON) -m venv --upgrade-deps $(TOOLS_VENV)
	@$(TOOLS_VENV)/bin/python -m pip install --quiet --disable-pip-version-check pip-tools==$(PIP_TOOLS_VERSION)

# Regenerates requirements.txt from requirements.in, keeping existing pins.
# Upgrade specific packages with: make compile-requirements P="pytest pluggy"
# (other pins are kept, so list any dependency that must move along with them).
compile-requirements: $(TOOLS_VENV)/bin/pip-compile
	@$(PIP_COMPILE) $(foreach p,$(P),--upgrade-package $(p)) requirements.in --output-file requirements.txt

# Upgrades every pin to the newest versions allowed by requirements.in.
upgrade-requirements: $(TOOLS_VENV)/bin/pip-compile
	@$(PIP_COMPILE) --upgrade requirements.in --output-file requirements.txt

# Fails if requirements.txt is not what requirements.in currently resolves to.
# Works on a temporary copy: tracked files are never modified.
check-requirements: $(TOOLS_VENV)/bin/pip-compile
	@tmp=$$(mktemp -d) && trap 'rm -rf "$$tmp"' EXIT && \
	cp requirements.in requirements.txt "$$tmp"/ && \
	(cd "$$tmp" && $(PIP_COMPILE) requirements.in --output-file requirements.txt) && \
	diff -u requirements.txt "$$tmp"/requirements.txt && \
	echo "requirements.txt is up to date with requirements.in."

# --- JavaScript -----------------------------------------------------------

# Explicit clean install from package-lock.json.
install-js:
	@npm ci

# Reinstalls only when package.json or package-lock.json change.
node_modules/.package-lock.json: package.json package-lock.json
	@npm ci

# --- C++ ------------------------------------------------------------------

setup-cpp:
	@echo "Checking C++ dependencies..."
	@PKG_EXISTS=$$(command -v pkg-config >/dev/null 2>&1 && echo 1 || echo 0); \
	if [ $$PKG_EXISTS -eq 1 ]; then \
		CPP_DEPS_CHECK=$$(pkg-config --exists gtest && echo 1 || test -f /usr/lib/libgtest.a || test -f /usr/local/lib/libgtest.a && echo 1 || echo 0); \
	else \
		CPP_DEPS_CHECK=$$(test -f /usr/lib/libgtest.a || test -f /usr/local/lib/libgtest.a && echo 1 || echo 0); \
	fi; \
	if [ $$CPP_DEPS_CHECK -eq 0 ]; then \
		echo "C++ dependencies missing. Installing..."; \
		$(MAKE) install-cpp-$(UNAME_S); \
	else \
		echo "C++ dependencies are already installed."; \
	fi

install-cpp-Linux:
	@echo "Detected Linux. Installing googletest and nlohmann-json..."
	@sudo apt-get update && sudo apt-get install -y libgtest-dev nlohmann-json3-dev pkg-config
	@if [ ! -f "/usr/lib/libgtest.a" ] && [ ! -f "/usr/local/lib/libgtest.a" ]; then \
		cd /usr/src/gtest && sudo cmake . && sudo make && sudo cp lib/*.a /usr/lib; \
	fi

install-cpp-Darwin:
	@echo "Detected macOS. Installing googletest and nlohmann-json..."
	@if ! command -v pkg-config >/dev/null 2>&1; then \
		echo "Installing pkg-config..."; \
		brew install pkg-config; \
	fi
	@brew install googletest nlohmann-json

install-cpp-Windows_NT:
	@echo "Detected Windows. Installing googletest and nlohmann-json using vcpkg..."
	@if not exist "C:\vcpkg" ( \
		echo "vcpkg not found. Please install it first: https://vcpkg.io/en/getting-started.html"; \
		exit 1; \
	) else ( \
		vcpkg install googletest nlohmann-json \
	)

# --- Tests ----------------------------------------------------------------

test: test-js test-python test-cpp

test-js: node_modules/.package-lock.json
	@echo "Running JS tests with npm..."
	@npm test

test-python: check-python-ready
	@echo "Running Python tests with pytest..."
	@$(PYTHON) -m pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings

test-cpp: setup-cpp
	@echo "Running C++ tests with CMake..."
	@mkdir -p build
	@cd build && cmake .. && make && ctest --output-on-failure

# Graphviz's `dot` executable is required only for --visualize.
visualize: check-python-ready
	@command -v dot >/dev/null 2>&1 || { \
		echo "Graphviz 'dot' executable not found; it is required for visualizations."; \
		echo "Install it with one of:"; \
		echo "  macOS:  brew install graphviz"; \
		echo "  Linux:  sudo apt-get install graphviz"; \
		echo "  Conda:  conda install -n algo-solutions -c conda-forge graphviz"; \
		exit 1; \
	}
	@echo "Running Python tests with visualizations..."
	@$(PYTHON) -m pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings --visualize

clean:
	@echo "Cleaning build directories..."
	@rm -rf build
	@find . -type d -name '__pycache__' -exec rm -rf {} +

help:
	@echo "Usage:"
	@echo "  make setup          - Install all dependencies (Python, JavaScript, C++)"
	@echo "  make install-python - Install Python dependencies from requirements.txt (creates ./venv with Python 3.12 if no env is active)"
	@echo "  make install-js     - Clean install of npm dependencies from package-lock.json"
	@echo "  make compile-requirements [P=\"pkg ...\"] - Regenerate requirements.txt from requirements.in (P upgrades the listed packages)"
	@echo "  make upgrade-requirements - Upgrade all pins within the ranges in requirements.in"
	@echo "  make check-requirements   - Verify requirements.txt matches requirements.in (modifies nothing)"
	@echo "  make test           - Run all tests, without visualizations"
	@echo "  make test-js        - Run JavaScript tests with npm"
	@echo "  make test-python    - Run Python tests with pytest"
	@echo "  make test-cpp       - Run C++ tests with CMake"
	@echo "  make visualize      - Run Python tests and generate visualizations (requires Graphviz)"
	@echo "  make clean          - Clean temporary files"

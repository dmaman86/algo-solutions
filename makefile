JS_TEST_DIR = tests/__tests__
PYTHON_TEST_DIR = tests/python
UNAME_S := $(shell uname -s)
SHELL := /bin/bash
IS_CONDA=$(shell python -c 'import sys; print("1" if "conda" in sys.version else "0")')

setup: setup-python setup-cpp

setup-python:
	@if [ "$(IS_CONDA)" -eq "1" ]; then \
		echo "Detected Anaconda environment."; \
	else \
		echo "Checking virtual environment..."; \
		[ -d "venv" ] || $(MAKE) create-venv; \
	fi
	@if [ -n "$$($(MAKE) check-missing)" ]; then \
		$(MAKE) install-missing; \
	else \
		echo "All dependencies are already installed."; \
	fi

create-venv:
	@echo "Creating virtual environment..."
	@python3 -m venv venv

check-missing:
	@if [ "$(IS_CONDA)" -eq "1" ]; then \
		comm -23 <(grep -Eo '^[^>=<]+' requirements.txt | tr '[:upper:]' '[:lower:]' | sort) <(conda list | awk '{print tolower($$1)}' | sort) || true; \
	else \
		comm -23 <(grep -Eo '^[^>=<]+' requirements.txt | tr '[:upper:]' '[:lower:]' | sort) <(pip list --format=freeze | cut -d= -f1 | tr '[:upper:]' '[:lower:]' | sort) || true; \
	fi

install-missing:
	@echo "Installing missing dependencies..."
	@MISSING=$$($(MAKE) check-missing); \
	if [ -n "$$MISSING" ]; then \
		if [ "$(IS_CONDA)" -eq "1" ]; then \
			conda install -c conda-forge -y $$MISSING; \
		else \
			. venv/bin/activate && pip install $$MISSING; \
		fi; \
	else \
		echo "No missing dependencies."; \
	fi
	@echo "Ensuring pip is up to date..."
	@pip install --upgrade pip wheel


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
		cd /usr/src/gtest && sudo cmake . && sudo make && sudo cp *.a /usr/lib; \
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

test: test-js test-python test-cpp

test-js:
	@echo "Running JS tests with npm..."
	@cd $(JS_TEST_DIR) && npm install && npm test

test-python: setup-python
	@echo "Running Python tests with pytest..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings

test-cpp: setup-cpp
	@echo "Running C++ tests with CMake..."
	@mkdir -p build
	@cd build && cmake .. && make && ctest --output-on-failure

visualize: setup-python
	@echo "Running Python tests with visualizations..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings --visualize

clean:
	@echo "Cleaning build directories..."
	@rm -rf build
	@find . -type d -name '__pycache__' -exec rm -rf {} +

help:
	@echo "Usage:"
	@echo "  make setup       - Install all dependencies (Python, C++)"
	@echo "  make test        - Run all tests, without visualizations"
	@echo "  make test-js     - Run JavaScript tests with npm"
	@echo "  make test-python - Run Python tests with pytest"
	@echo "  make test-cpp    - Run C++ tests with CMake"
	@echo "  make visualize   - Run Python tests and generate visualizations"
	@echo "  make clean       - Clean temporary files"

JS_TEST_DIR = tests/__tests__
PYTHON_TEST_DIR = tests/python
UNAME_S := $(shell uname -s)

setup: setup-python setup-cpp

setup-python:
	@PYTHON_DEPS_CHECK=$$(python3 -m pip list | grep -E 'pytest|numpy' | wc -l); \
	if [ $$PYTHON_DEPS_CHECK -eq 0 ]; then \
		echo "Installing Python dependencies..."; \
		python3 -m pip install -r requirements.txt; \
	else \
		echo "Python dependencies are already installed."; \
	fi

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

install-cpp-linux:
	@echo "Detected Linux. Installing googletest and nlohmann-json..."
	@sudo apt-get update && sudo apt-get install -y libgtest-dev nlohmann-json3-dev pkg-config
	@cd /usr/src/gtest && sudo cmake . && sudo make && sudo cp *.a /usr/lib

install-cpp-Darwin:
	@echo "Detected macOS. Installing googletest and nlohmann-json..."
	@brew install googletest nlohmann-json pkg-config

install-cpp-Windows_NT:
	@echo "Detected Windows. Installing googletest and nlohmann-json using vcpkg..."
	@vcpkg install googletest nlohmann-json

test: test-js test-python test-cpp

test-js:
	@echo "Running JS tests with npm..."
	@cd $(JS_TEST_DIR) && npm install && npm test

test-python: setup-python
	@echo "Running Python tests with pytest..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings

test-cpp: setup-cpp
	@echo "Running C++ tests with CMake..."
	@rm -rf build
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

JS_TEST_DIR = tests/__tests__
PYTHON_TEST_DIR = tests/python

all: test

test: test-js test-python test-cpp

test-js:
	@echo "Running JS tests with npm..."
	@cd $(JS_TEST_DIR) && npm install && npm test

test-python:
	@echo "Running Python tests with pytest..."
	@pytest $(PYTHON_TEST_DIR)

test-cpp:
	@echo "Running C++ tests with CMake..."
	@mkdir -p build
	@cd build && cmake .. && make && ctest --output-on-failure

clean:
	@echo "Cleaning build directories..."
	@rm -rf build
	@find . -type d -name '__pycache__' -exec rm -rf {} +

help:
	@echo "Usage:"
	@echo "  make test        - Run all tests"
	@echo "  make test-js     - Run JavaScript tests with npm"
	@echo "  make test-python - Run Python tests with pytest"
	@echo "  make test-cpp    - Run C++ tests with CMake"
	@echo "  make clean       - Clean temporary files"

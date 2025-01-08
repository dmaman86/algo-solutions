JS_TEST_DIR = tests/__tests__
PYTHON_TEST_DIR = tests/python
VISUALIZATION_DIR = visualization
OUTPUT_IMAGES_DIR = output_images
RESULTS_DIR = tests/results

ROOT_DIR := $(shell pwd)
PYTHON := python

all: test

test: test-js test-python test-cpp

test-js:
	@echo "Running JS tests with npm..."
	@cd $(JS_TEST_DIR) && npm install && npm test

test-python:
	@echo "Running Python tests with pytest..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings

test-cpp:
	@echo "Running C++ tests with CMake..."
	@mkdir -p build
	@cd build && cmake .. && make && ctest --output-on-failure


visualize:
	@echo "Running Python tests with visualizations..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings --visualize


clean:
	@echo "Cleaning build directories..."
	@rm -rf build
	@find . -type d -name '__pycache__' -exec rm -rf {} +

help:
	@echo "Usage:"
	@echo "  make test        - Run all tests, without visualizations"
	@echo "  make test-js     - Run JavaScript tests with npm"
	@echo "  make test-python - Run Python tests with pytest"
	@echo "  make test-cpp    - Run C++ tests with CMake"
	@echo "  make visualize   - Run Python tests and generate visualizations"
	@echo "  make clean       - Clean temporary files"

JS_TEST_DIR = tests/__tests__
PYTHON_TEST_DIR = tests/python

all: install-python-deps test

install-python-deps:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt

test: test-js test-python test-cpp

test-js:
	@echo "Running JS tests with npm..."
	@cd $(JS_TEST_DIR) && npm install && npm test

test-python: install-python-deps
	@echo "Running Python tests with pytest..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings

test-cpp:
	@echo "Running C++ tests with CMake..."
	@mkdir -p build
	@cd build && cmake .. && make && ctest --output-on-failure

visualize: install-python-deps
	@echo "Running Python tests with visualizations..."
	@pytest $(PYTHON_TEST_DIR) --tb=short -q --disable-warnings --visualize

clean:
	@echo "Cleaning build directories..."
	@rm -rf build
	@find . -type d -name '__pycache__' -exec rm -rf {} +

help:
	@echo "Usage:"
	@echo "  make install-python-deps - Install Python dependencies"
	@echo "  make test        - Run all tests, without visualizations"
	@echo "  make test-js     - Run JavaScript tests with npm"
	@echo "  make test-python - Run Python tests with pytest"
	@echo "  make test-cpp    - Run C++ tests with CMake"
	@echo "  make visualize   - Run Python tests and generate visualizations"
	@echo "  make clean       - Clean temporary files"

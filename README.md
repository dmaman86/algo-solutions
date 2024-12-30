# AlgoExpert Solutions

<!-- START_TABLE -->
| Problem               | Topic   | Difficulty | Languages               |
|-----------------------|---------|------------|-------------------------|
| [Four Number Sum](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum) | Arrays | Hard | [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum/cpp), [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum/js) |
| [Sorted Squared Array](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/sorted_squared_array) | Arrays | Easy | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/sorted_squared_array/js) |
| [Tournament Winner](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner) | Arrays | Easy | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner/js), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner/cpp) |
| [Two Number Sum](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/two_number_sum) | Arrays | Easy | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/two_number_sum/js) |
| [Validate Subsequence](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence) | Arrays | Easy | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence/python) |
| [Repair Bst](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst) | Binary search_trees | Hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst/python) |
| [Dijkstras Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm) | Famous algorithms | Hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/cpp) |
| [Kadanes Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm) | Famous algorithms | Normal | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm/js), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm/cpp) |
| [Kruskals Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm) | Famous algorithms | Hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/cpp) |
| [Prims Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm) | Famous algorithms | Hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/cpp) |
| [Topological Sort](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort) | Famous algorithms | Hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/cpp) |
| [Astar Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm) | Famous algorithms | Very hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/cpp) |
| [Airport Connections](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections) | Graphs | Very hard | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/cpp) |
<!-- END_TABLE -->

## **Makefile Usage**

This project includes a **Makefile** to simplify common tasks, such as
running tests and cleaning up temporary files. Below is an
explanation of the available rules.

### **Available Rules**

1. **`make test`**:

- Runs all tests in the project for supported languages (JavaScript, Python, C++).
- Each language's tests are executed as follows:
  - **JavaScript**: Runs with `npm test`.
  - **Python**: Runs with `pytest`.
  - **C++**: Uses `cmake`, `make`, and `ctest`.

**Example**:

```bash
make test
```

2. **`make test-js`**:

- Runs only JavaScript tests.
- Executes tests in the `tests/__tests__` directory.

**Example**:

```bash
make test-js
```

3. **`make test-python`**:

- Runs only Python tests using `pytest`.
- Executes tests in the `tests/python` directory.

**Example**:

```bash
make test-python
```

4. **`make test-cpp`**:

- Runs C++ tests.
- Creates a `build` directory in the project root to store temporary build files.
- Executes tests using `ctest --output-on-failure` to display detailed error
  messages if tests fail.

**Example**:

```bash
make test-cpp
```

5. **`make clean`**:

- Cleans up temporary files and build directories, including:
  - `build`
  - Python temporary files (`__pycache__`).

**Example**:

```bash
make clean
```

---

### **Project Structure for the Makefile**

The project is organized to separate tests and build files clearly.
The tests for each language are located in the following directories:

```plaintext
tests/
|-- __tests__/    # Tests for JavaScript (configured with Jest)
|-- cpp/          # Tests for C++ (configured with CMake and CTest)
|-- python/       # Tests for Python (configured with pytest)
build/            # Build directory generated automatically by the Makefile
```

---

### **Example Workflow**

1. **Run all tests**:

```bash
make test
```

2. **Run tests for a specific language**:

- **JavaScript**:

  ```bash
  make test-js
  ```

- **Python**:

  ```bash
  make test-python
  ```

- **C++**:
  ```bash
  make test-cpp
  ```

3. **Clean temporary files**:

```bash
make clean
```

---

### **Prerequisites**

Before using the Makefile, ensure the following tools are installed:

- **JavaScript**:

  - Node.js and npm (for running tests with Jest).
  - Install dependencies using:
    ```bash
    npm install
    ```

- **Python**:

  - Python 3.x with `pytest` installed.
  - Install `pytest` using:
    ```bash
    pip install pytest
    ```

- **C++**:
  - CMake (version 3.14 or higher).
  - A compiler supporting C++17 (e.g., GCC or Clang).
  - Google Test (`GTest`) and `nlohmann/json` libraries installed.

---

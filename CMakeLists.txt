cmake_minimum_required(VERSION 3.14)

project(algo-solutions)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(GTest REQUIRED)
find_package(nlohmann_json REQUIRED)

set(TEST_CASES_DIR "${PROJECT_SOURCE_DIR}/tests/test_cases")

set(ARRAYS_DIR ${PROJECT_SOURCE_DIR}/problems/arrays)
set(BST_DIR ${PROJECT_SOURCE_DIR}/problems/binary_search_trees)
set(BT_DIR ${PROJECT_SOURCE_DIR}/problems/binary_trees)
set(FAMOUS_ALGORITHMS_DIR ${PROJECT_SOURCE_DIR}/problems/famous_algorithms)
set(GRAPHS_DIR ${PROJECT_SOURCE_DIR}/problems/graphs)
set(GREEDY_ALGORITHMS_DIR ${PROJECT_SOURCE_DIR}/problems/greedy_algorithms)
set(DYNAMIC_PROGRAMMING_DIR ${PROJECT_SOURCE_DIR}/problems/dynamic_programming)

enable_testing()

add_subdirectory(tests/cpp)

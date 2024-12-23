cmake_minimum_required(VERSION 3.14)

#Nombre del proyecto
project(algo-solutions)

#Configuración general de C++
set(CMAKE_CXX_STANDARD 17) 
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(GTest REQUIRED)
find_package(nlohmann_json REQUIRED)

set(TEST_CASES_DIR "${PROJECT_SOURCE_DIR}/tests/test_cases")

enable_testing()

set(ARRAYS_DIR ${PROJECT_SOURCE_DIR}/problems/arrays)
# set(BST_DIR ${PROJECT_SOURCE_DIR}/problems/bst)

#Incluir subdirectorios para compilación
add_subdirectory(tests/cpp)

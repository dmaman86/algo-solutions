
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

function(configure_test TEST_SOURCE PROBLEM_DIR)
  get_filename_component(TEST_NAME ${TEST_SOURCE} NAME_WE)
  string(REGEX REPLACE "^test_" "" PROBLEM_NAME ${TEST_NAME})

  add_executable(${TEST_NAME}
  ${TEST_SOURCE}
  ${PROBLEM_DIR}/${PROBLEM_NAME}/cpp/${PROBLEM_NAME}.cpp)

  target_include_directories(${TEST_NAME} PRIVATE ${PROBLEM_DIR}/${PROBLEM_NAME}/cpp)

  target_link_libraries(${TEST_NAME} PRIVATE GTest::GTest GTest::Main nlohmann_json::nlohmann_json)

  target_compile_definitions(${TEST_NAME} PRIVATE TEST_CASES_DIR="${TEST_CASES_DIR}")

  message(STATUS "Configuring test ${TEST_NAME} for problem ${PROBLEM_NAME}")
  add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME})
endfunction()

add_subdirectory(arrays)
add_subdirectory(binary_search_trees)
add_subdirectory(binary_trees)
add_subdirectory(famous_algorithms)
add_subdirectory(graphs)

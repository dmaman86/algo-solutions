
set(PROBLEM_DIR ${ARRAYS_DIR})

file(GLOB TEST_SOURCE "*.cpp")

foreach(TEST_FILE ${TEST_SOURCE})
  configure_test(${TEST_FILE} ${PROBLEM_DIR})
endforeach()


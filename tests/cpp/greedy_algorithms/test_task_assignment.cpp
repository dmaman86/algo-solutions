#include "../../../problems/greedy_algorithms/task_assignment/cpp/task_assignment.h"
#include "../jsontestbase.h"

#include <set>
#include <vector>

class TaskAssignmentTest : public JsonTestBase {
public:
  TaskAssignmentTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/greedy_algorithms/task_assignment.json";
  }
};

std::set<std::set<int>>
convertToSet(const std::vector<std::vector<int>> &pairs) {
  std::set<std::set<int>> result;
  for (const auto &pair : pairs) {
    result.insert({pair[0], pair[1]});
  }
  return result;
}

bool isValidResult(const std::vector<std::vector<int>> &result,
                   const std::vector<std::vector<int>> &expected) {
  auto expectedSet = convertToSet(expected);

  for (const auto &pair : result) {
    std::set<int> directPair = {pair[0], pair[1]};
    if (expectedSet.find(directPair) == expectedSet.end()) {
      bool partialMatch = false;
      for (const auto &expectedPair : expectedSet) {
        if (expectedPair.count(pair[0]) > 0 ||
            expectedPair.count(pair[1]) > 0) {
          partialMatch = true;
          break;
        }
      }
      if (!partialMatch)
        return false;
    }
  }
  return true;
}

TEST_F(TaskAssignmentTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto k = test["k"].get<int>();
    auto tasks = test["tasks"].get<std::vector<int>>();
    auto expected = test["expected"].get<std::vector<std::vector<int>>>();

    auto result = taskAssignment(k, tasks);

    EXPECT_TRUE(isValidResult(result, expected))
        << "Failed for test case: " << test.dump(2);
  }
}

#include "../../../problems/arrays/four_number_sum/cpp/four_number_sum.h"
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class TestFourNumberSum : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file =
        std::string(TEST_CASES_DIR) + "/arrays/four_number_sum.json";
    std::ifstream f(test_file);

    if (!f.is_open()) {
      throw std::runtime_error("Could not open test file: " + test_file);
    }
    test_cases = json::parse(f);
  }
  json test_cases;
};

bool areCombinationSetsEquivalent(
    const std::vector<std::vector<int>> &result,
    const std::vector<std::vector<int>> &expected) {
  if (result.size() != expected.size())
    return false;

  return std::is_permutation(
      result.begin(), result.end(), expected.begin(),
      [](const std::vector<int> &a, const std::vector<int> &b) {
        return std::is_permutation(a.begin(), a.end(), b.begin());
      });
};

TEST_F(TestFourNumberSum, TestCases) {
  FourNumberSumSolver solver;
  for (const auto &test : test_cases) {
    std::vector<int> array = test["array"];
    int target_sum = test["targetSum"];
    std::vector<std::vector<int>> expected = test["expected"];
    std::vector<std::vector<int>> result =
        solver.fourNumberSum(array, target_sum);
    ASSERT_TRUE(areCombinationSetsEquivalent(result, expected))
        << "Failed for test case: " << test.dump(2);
  }
}

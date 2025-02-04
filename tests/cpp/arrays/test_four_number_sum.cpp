#include "../../../problems/arrays/four_number_sum/cpp/four_number_sum.h"
#include "../jsontestbase.h"

#include <algorithm>
#include <vector>

class TestFourNumberSum : public JsonTestBase {
public:
  TestFourNumberSum() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/four_number_sum.json";
  }
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
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
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

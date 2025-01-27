#include "../../../problems/dynamic_programming/longest_increasing_subsequence/cpp/longest_increasing_subsequence.h"
#include "../jsontestbase.h"

#include <vector>

class LongestIncreasingSubsequenceTest : public JsonTestBase {
public:
  LongestIncreasingSubsequenceTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/dynamic_programming/longest_increasing_subsequence.json";
  }
};

TEST_F(LongestIncreasingSubsequenceTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto array = test["array"].get<std::vector<int>>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto result = longestIncreasingSubsequence(array);

    EXPECT_EQ(result, expected) << "Failed test case: " << test.dump(2);
  }
}

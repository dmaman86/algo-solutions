#include "../../../problems/dynamic_programming/maximum_sum_submatrix/cpp/maximum_sum_submatrix.h"
#include "../jsontestbase.h"

#include <vector>

class MaximumSumSubmatrixTest : public JsonTestBase {
public:
  MaximumSumSubmatrixTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/dynamic_programming/maximum_sum_submatrix.json";
  }
};

TEST_F(MaximumSumSubmatrixTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto matrix = test["matrix"].get<std::vector<std::vector<int>>>();
    int size = test["size"].get<int>();
    int expected = test["expected"].get<int>();

    int result = maximumSumSubmatrix(matrix, size);

    EXPECT_EQ(result, expected) << "Failed test case: " << test.dump(2);
  }
}

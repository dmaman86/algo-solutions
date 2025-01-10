#include "../../../problems/graphs/minimum_passes_of_matrix/cpp/minimum_passes_of_matrix.h"
#include "../jsontestbase.h"

#include <vector>

class MinimumPassesOfMatrixTest : public JsonTestBase {
public:
  MinimumPassesOfMatrixTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/graphs/minimum_passes_of_matrix.json";
  }
};

TEST_F(MinimumPassesOfMatrixTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto matrix = test["matrix"].get<std::vector<std::vector<int>>>();
    auto expected = test["expected"].get<int>();

    auto result = minimumPassesOfMatrix(matrix);

    EXPECT_EQ(result, expected)
        << "Failed test case at index: " << test.dump(2);
  }
}

#include "../../../problems/binary_search_trees/right_smaller_than/cpp/right_smaller_than.h"
#include "../jsontestbase.h"

#include <vector>

class RightSmallerThanTest : public JsonTestBase {
public:
  RightSmallerThanTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_search_trees/right_smaller_than.json";
  }
};

TEST_F(RightSmallerThanTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto array = test["array"].get<std::vector<int>>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto result = rightSmallerThan(array);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}

#include "../../../problems/binary_trees/max_path_sum_in_bt/cpp/max_path_sum_in_bt.h"
#include "../jsontestbase.h"
#include "./utility.h"

class MaxPathSumInBtTest : public JsonTestBase {
public:
  MaxPathSumInBtTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_trees/max_path_sum_in_bt.json";
  }
};

TEST_F(MaxPathSumInBtTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    const auto &treeJson = test["tree"];
    auto expected = test["expected"].get<int>();

    auto root = buildBT(treeJson);

    auto result = maxPathSum(*root);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);

    deleteBT(root);
  }
}

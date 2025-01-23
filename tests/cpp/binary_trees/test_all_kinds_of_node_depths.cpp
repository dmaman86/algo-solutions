#include "../../../problems/binary_trees/all_kinds_of_node_depths/cpp/all_kinds_of_node_depths.h"
#include "../jsontestbase.h"
#include "./utility.h"

class AllKindsOfNodeDepthsTest : public JsonTestBase {
public:
  AllKindsOfNodeDepthsTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_trees/all_kinds_of_node_depths.json";
  }
};

TEST_F(AllKindsOfNodeDepthsTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded!";

  for (const auto &test : test_cases) {
    auto treeJson = test["tree"];
    auto expected = test["expected"].get<int>();

    auto root = buildBT(treeJson);

    auto result = allKindsOfNodeDepths(root);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);

    deleteBT(root);
  }
}

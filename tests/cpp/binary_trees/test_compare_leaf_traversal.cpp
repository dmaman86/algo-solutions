#include "../../../problems/binary_trees/compare_leaf_traversal/cpp/compare_leaf_traversal.h"
#include "../jsontestbase.h"
#include "./utility.h"

class CompareLeafTraversalTest : public JsonTestBase {
public:
  CompareLeafTraversalTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_trees/compare_leaf_traversal.json";
  }
};

TEST_F(CompareLeafTraversalTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty!";

  for (const auto &test : test_cases) {
    auto treeJson1 = test["tree1"];
    auto treeJson2 = test["tree2"];
    auto expected = test["expected"];

    auto root1 = buildBT(treeJson1);
    auto root2 = buildBT(treeJson2);

    auto result = compareLeafTraversal(root1, root2);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);

    deleteBT(root1);
    deleteBT(root2);
  }
}

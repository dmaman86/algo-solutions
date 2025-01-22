#include "../../../problems/binary_trees/right_sibling_tree/cpp/right_sibling_tree.h"
#include "../jsontestbase.h"
#include "./utility.h"

class RightSiblingTreeTest : public JsonTestBase {
public:
  RightSiblingTreeTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_trees/right_sibling_tree.json";
  }
};

bool areEqual(const BinaryTree *root1, const BinaryTree *root2) {
  if (!root1 && !root2)
    return true;

  if (!root1 || !root2)
    return false;
  if (root1->value != root2->value)
    return false;
  return areEqual(root1->left, root2->left) &&
         areEqual(root1->right, root2->right);
}

TEST_F(RightSiblingTreeTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    const auto &treeJson = test["tree"];
    const auto &expectedJson = test["expected"];

    auto root = buildBT(treeJson);
    auto expectedRoot = buildBT(expectedJson);

    auto result = rightSiblingTree(root);

    ASSERT_TRUE(areEqual(result, expectedRoot))
        << "Failed for test case: " << test.dump(2);
    deleteBTCycle(root);
    deleteBTCycle(expectedRoot);
  }
}

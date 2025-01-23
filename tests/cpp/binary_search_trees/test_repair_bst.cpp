#include "../../../problems/binary_search_trees/repair_bst/cpp/repair_bst.h"
#include "../jsontestbase.h"
#include "./utility.h"

class RepairBstTest : public JsonTestBase {
public:
  RepairBstTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_search_trees/repair_bst.json";
  }
};

bool areEqual(BST *root1, BST *root2) {
  if (!root1 && !root2)
    return true;

  if (!root1 || !root2 || root1->value != root2->value)
    return false;

  return areEqual(root1->left, root2->left) &&
         areEqual(root1->right, root2->right);
}

TEST_F(RepairBstTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  BSTRepair bstRepair;
  for (const auto &test : test_cases) {
    auto treeJson = test["tree"];
    auto expectedJson = test["expected"];

    auto root = buildBST(treeJson);
    auto expected = buildBST(expectedJson);

    auto result = bstRepair.repair(root);

    ASSERT_TRUE(areEqual(result, expected))
        << "Failed for test case: " << test.dump(2);
    deleteBST(root);
    deleteBST(expected);
  }
}

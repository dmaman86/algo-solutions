#include "../../../problems/binary_trees/flatten_binary_tree/cpp/flatten_binary_tree.h"
#include "../jsontestbase.h"
#include "./utility.h"

#include <unordered_set>

class FlattenBinaryTreeTest : public JsonTestBase {
public:
  FlattenBinaryTreeTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_trees/flatten_binary_tree.json";
  }
};

bool areBTsEqual(BinaryTree *bt1, BinaryTree *bt2,
                 std::unordered_set<BinaryTree *> &visited) {
  if (!bt1 && !bt2)
    return true;

  if (!bt1 || !bt2 || bt1->value != bt2->value)
    return false;

  if (visited.count(bt1) || visited.count(bt2))
    return true;

  visited.insert(bt1);
  visited.insert(bt2);

  return areBTsEqual(bt1->left, bt2->left, visited) &&
         areBTsEqual(bt1->right, bt2->right, visited);
}

bool areBTsEqual(BinaryTree *bt1, BinaryTree *bt2) {
  std::unordered_set<BinaryTree *> visited;
  return areBTsEqual(bt1, bt2, visited);
}

TEST_F(FlattenBinaryTreeTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    const auto &treeJson = test["tree"];
    const auto &expectedJson = test["expected"];

    auto root = buildBT(treeJson);
    auto expected = buildBT(expectedJson);

    auto result = flattenBinaryTree(root);

    ASSERT_TRUE(areBTsEqual(result, expected))
        << "Failed for test case: " << test.dump(2);

    deleteBTCycle(root);
    deleteBTCycle(expected);
  }
}

#include "../../../problems/binary_trees/compare_leaf_traversal/cpp/compare_leaf_traversal.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <unordered_map>

using json = nlohmann::json;

class CompareLeafTraversalTest : public JsonTestBase {
public:
  CompareLeafTraversalTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_trees/compare_leaf_traversal.json";
  }
};

BinaryTree *buildBT(const json &treeJson) {
  const auto &nodes = treeJson["nodes"];
  const std::string &rootId = treeJson["root"];

  std::unordered_map<std::string, BinaryTree *> nodeMap;

  for (const auto &node : nodes) {
    const std::string &id = node["id"];
    nodeMap[id] = new BinaryTree(node["value"]);
  }

  for (const auto &node : nodes) {
    std::string id = node["id"];
    BinaryTree *bstNode = nodeMap[id];

    if (!node["left"].is_null()) {
      std::string leftId = node["left"];
      bstNode->left = nodeMap[leftId];
    }
    if (!node["right"].is_null()) {
      std::string rightId = node["right"];
      bstNode->right = nodeMap[rightId];
    }
  }
  return nodeMap[rootId];
}

void deleteBT(BinaryTree *root) {
  if (!root)
    return;
  deleteBT(root->left);
  deleteBT(root->right);
  delete root;
}

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

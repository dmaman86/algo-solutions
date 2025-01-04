#include "../../../problems/binary_search_trees/repair_bst/cpp/repair_bst.h"
#include "../jsontestbase.h"
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

#include <unordered_map>

using json = nlohmann::json;

class RepairBstTest : public JsonTestBase {
public:
  RepairBstTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_search_trees/repair_bst.json";
  }
};

BST *buildBST(const json &treeJson) {
  const auto &nodes = treeJson["nodes"];
  const std::string &rootId = treeJson["root"];

  std::unordered_map<std::string, BST *> nodeMap;

  for (const auto &node : nodes) {
    const std::string &id = node["id"];
    nodeMap[id] = new BST(node["value"]);
  }

  for (const auto &node : nodes) {
    std::string id = node["id"];
    BST *bstNode = nodeMap[id];

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

void deleteBST(BST *root) {
  if (!root)
    return;
  deleteBST(root->left);
  deleteBST(root->right);
  delete root;
}

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

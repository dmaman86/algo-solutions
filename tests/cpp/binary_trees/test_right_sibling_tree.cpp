#include "../../../problems/binary_trees/right_sibling_tree/cpp/right_sibling_tree.h"
#include "../jsontestbase.h"

#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

#include <unordered_map>
#include <unordered_set>

using json = nlohmann::json;

class RightSiblingTreeTest : public JsonTestBase {
public:
  RightSiblingTreeTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_trees/right_sibling_tree.json";
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
    BinaryTree *btNode = nodeMap[id];

    if (!node["left"].is_null()) {
      const std::string &leftId = node["left"];
      btNode->left = nodeMap[leftId];
    }
    if (!node["right"].is_null()) {
      const std::string &rightId = node["right"];
      btNode->right = nodeMap[rightId];
    }
  }
  return nodeMap[rootId];
}

void deleteBT(BinaryTree *root, std::unordered_set<BinaryTree *> &visited) {
  if (!root || visited.count(root))
    return;
  visited.insert(root);

  deleteBT(root->left, visited);
  deleteBT(root->right, visited);
  delete root;
}

void deleteBT(BinaryTree *root) {
  std::unordered_set<BinaryTree *> visited;
  deleteBT(root, visited);
}

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
    deleteBT(root);
    deleteBT(expectedRoot);
  }
}

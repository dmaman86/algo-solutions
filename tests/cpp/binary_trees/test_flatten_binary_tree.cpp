#include "../../../problems/binary_trees/flatten_binary_tree/cpp/flatten_binary_tree.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <unordered_set>

using json = nlohmann::json;

class FlattenBinaryTreeTest : public JsonTestBase {
public:
  FlattenBinaryTreeTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_trees/flatten_binary_tree.json";
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
      btNode->left = nodeMap[node["left"]];
    }

    if (!node["right"].is_null()) {
      btNode->right = nodeMap[node["right"]];
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

    deleteBT(root);
    deleteBT(expected);
  }
}

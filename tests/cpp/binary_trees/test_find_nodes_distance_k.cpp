#include "../../../problems/binary_trees/find_nodes_distance_k/cpp/find_nodes_distance_k.h"
#include "../jsontestbase.h"

#include <algorithm>
#include <nlohmann/json.hpp>
#include <unordered_map>
#include <vector>

using json = nlohmann::json;

class FindNodesDistanceKTest : public JsonTestBase {
public:
  FindNodesDistanceKTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_trees/find_nodes_distance_k.json";
  }
};

BinaryTree *buildBT(const json &treeJson) {
  const auto &nodes = treeJson["nodes"];
  const std::string &root_id = treeJson["root"];

  std::unordered_map<std::string, BinaryTree *> node_map;

  for (const auto &node : nodes) {
    const std::string &id = node["id"];
    node_map[id] = new BinaryTree(node["value"]);
  }

  for (const auto &node : nodes) {
    std::string id = node["id"];
    BinaryTree *btNode = node_map[id];

    if (!node["left"].is_null()) {
      btNode->left = node_map[node["left"]];
    }

    if (!node["right"].is_null()) {
      btNode->right = node_map[node["right"]];
    }
  }
  return node_map[root_id];
}

void deleteBT(BinaryTree *root) {
  if (!root)
    return;

  deleteBT(root->left);
  deleteBT(root->right);
  delete root;
}

TEST_F(FindNodesDistanceKTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto treeJson = test["tree"];
    auto target = test["target"].get<int>();
    auto k = test["k"].get<int>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto root = buildBT(treeJson);
    auto result = findNodesDistanceK(root, target, k);

    std::sort(result.begin(), result.end());
    std::sort(expected.begin(), expected.end());

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);

    deleteBT(root);
  }
}

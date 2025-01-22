#include "../../../problems/binary_trees/assets/BinaryTree.h"

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <unordered_set>

using json = nlohmann::json;

inline BinaryTree *buildBT(const json &treeJson) {
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

inline void deleteBT(BinaryTree *root) {
  if (!root)
    return;
  deleteBT(root->left);
  deleteBT(root->right);
  delete root;
}

inline void deleteBT(BinaryTree *root,
                     std::unordered_set<BinaryTree *> &visited) {
  if (!root || visited.count(root))
    return;
  visited.insert(root);

  deleteBT(root->left, visited);
  deleteBT(root->right, visited);
  delete root;
}

inline void deleteBTCycle(BinaryTree *root) {
  std::unordered_set<BinaryTree *> visited;
  deleteBT(root, visited);
}

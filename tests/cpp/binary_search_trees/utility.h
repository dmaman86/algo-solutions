#include "../../../problems/binary_search_trees/assets/BST.h"

#include <nlohmann/json.hpp>
#include <unordered_map>

using json = nlohmann::json;

inline BST *buildBST(const json &treeJson) {
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

inline void deleteBST(BST *root) {
  if (!root)
    return;
  deleteBST(root->left);
  deleteBST(root->right);
  delete root;
}

#include "flatten_binary_tree.h"
#include <functional>
#include <utility>

BinaryTree *flattenBinaryTree(BinaryTree *root) {
  if (!root)
    return nullptr;

  auto connectNodes = [](BinaryTree *first, BinaryTree *second) -> void {
    if (first)
      first->right = second;
    if (second)
      second->left = first;
  };

  std::function<std::pair<BinaryTree *, BinaryTree *>(BinaryTree *)>
      flattenInOrder =
          [&](BinaryTree *node) -> std::pair<BinaryTree *, BinaryTree *> {
    if (!node)
      return {nullptr, nullptr};

    auto leftList = flattenInOrder(node->left);
    auto rightList = flattenInOrder(node->right);

    connectNodes(leftList.second, node);
    connectNodes(node, rightList.first);

    BinaryTree *head = leftList.first ? leftList.first : node;
    BinaryTree *tail = rightList.second ? rightList.second : node;

    return {head, tail};
  };

  return flattenInOrder(root).first;
}

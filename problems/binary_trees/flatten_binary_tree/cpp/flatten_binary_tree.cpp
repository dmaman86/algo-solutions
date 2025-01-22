#include "flatten_binary_tree.h"

void flattenInOrder(BinaryTree *node, BinaryTree *&prev) {
  if (!node)
    return;

  flattenInOrder(node->left, prev);

  if (prev) {
    prev->right = node;
    node->left = prev;
  }
  prev = node;
  flattenInOrder(node->right, prev);
}

BinaryTree *flattenBinaryTree(BinaryTree *root) {
  BinaryTree *prev = nullptr;

  flattenInOrder(root, prev);

  BinaryTree *leftMost = root;
  while (leftMost->left)
    leftMost = leftMost->left;

  return leftMost;
}

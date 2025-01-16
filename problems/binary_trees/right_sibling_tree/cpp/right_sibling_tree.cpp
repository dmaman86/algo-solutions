#include "right_sibling_tree.h"

void helper(BinaryTree *node, BinaryTree *parent, bool is_left) {
  if (!node)
    return;

  BinaryTree *left = node->left;
  BinaryTree *right = node->right;

  helper(left, node, true);

  if (!parent)
    node->right = nullptr;
  else if (is_left)
    node->right = parent->right;
  else {
    node->right =
        (parent->right && parent->right->left) ? parent->right->left : nullptr;
  }
  helper(right, node, false);
}

BinaryTree *rightSiblingTree(BinaryTree *root) {
  helper(root, nullptr, false); // start with no sibling for the root
  return root;
}

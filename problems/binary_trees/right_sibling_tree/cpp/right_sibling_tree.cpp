#include "right_sibling_tree.h"
#include <functional>

BinaryTree *rightSiblingTree(BinaryTree *root) {

  std::function<void(BinaryTree *, BinaryTree *, bool)> helper =
      [&](BinaryTree *node, BinaryTree *parent, bool is_left) -> void {
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
      node->right = (parent->right && parent->right->left) ? parent->right->left
                                                           : nullptr;
    }
    helper(right, node, false);
  };

  helper(root, nullptr, false); // start with no sibling for the root
  return root;
}

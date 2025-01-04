#include "repair_bst.h"
#include <utility>

void BSTRepair::inorder(BST *node) {
  if (!node)
    return;

  inorder(node->left);

  if (prev && prev->value > node->value) {
    if (!first)
      first = prev;
    second = node;
  }
  prev = node;

  inorder(node->right);
}

BST *BSTRepair::repair(BST *root) {
  first = second = prev = nullptr;
  inorder(root);
  if (first && second) {
    std::swap(first->value, second->value);
  }
  return root;
}

#include "compare_leaf_traversal.h"

void collectLeafNodes(BinaryTree *root, std::vector<int> &storedLeaf) {
  if (!root)
    return;

  if (!root->left && !root->right) {
    storedLeaf.push_back(root->value);
  }

  collectLeafNodes(root->left, storedLeaf);
  collectLeafNodes(root->right, storedLeaf);
}

bool compareLeafTraversal(BinaryTree *tree1, BinaryTree *tree2) {
  std::vector<int> leafTree1, leafTree2;

  collectLeafNodes(tree1, leafTree1);
  collectLeafNodes(tree2, leafTree2);

  return leafTree1 == leafTree2;
}

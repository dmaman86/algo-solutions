#include "compare_leaf_traversal.h"
#include <functional>
#include <vector>

bool compareLeafTraversal(BinaryTree *tree1, BinaryTree *tree2) {

  std::function<void(BinaryTree *, std::vector<int> &)> collectLeafNodes =
      [&](BinaryTree *root, std::vector<int> &storedLeaf) -> void {
    if (!root)
      return;

    if (!root->left && !root->right)
      storedLeaf.push_back(root->value);

    collectLeafNodes(root->left, storedLeaf);
    collectLeafNodes(root->right, storedLeaf);
  };

  std::vector<int> leafTree1, leafTree2;
  collectLeafNodes(tree1, leafTree1);
  collectLeafNodes(tree2, leafTree2);

  return leafTree1 == leafTree2;
}

#include "right_smaller_than.h"
#include <algorithm>

int BST::insert(Node *&node, int value) {
  if (!node) {
    node = new Node(value);
    return 0;
  }
  if (value <= node->value) {
    node->leftSize++;
    return insert(node->left, value);
  } else {
    int count = node->leftSize + 1;
    return count + insert(node->right, value);
  }
}

int BST::insert(int value) { return insert(root, value); }

std::vector<int> rightSmallerThan(const std::vector<int> &array) {
  std::vector<int> result;
  BST bst;
  for (int i = array.size() - 1; i >= 0; i--) {
    result.push_back(bst.insert(array[i]));
  }
  std::reverse(result.begin(), result.end());
  return result;
}

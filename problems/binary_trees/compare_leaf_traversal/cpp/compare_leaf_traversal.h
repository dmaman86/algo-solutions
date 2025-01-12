#include <vector>

class BinaryTree {
public:
  int value;
  BinaryTree *left;
  BinaryTree *right;

  BinaryTree(int value) { this->value = value; }
};

void collectLeafNodes(BinaryTree *, std::vector<int> &);

bool compareLeafTraversal(BinaryTree *, BinaryTree *);

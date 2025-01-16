
class BinaryTree {
public:
  int value;
  BinaryTree *left = nullptr;
  BinaryTree *right = nullptr;

  BinaryTree(int value) { this->value = value; }
};

void helper(BinaryTree *, BinaryTree *, bool);
BinaryTree *rightSiblingTree(BinaryTree *);

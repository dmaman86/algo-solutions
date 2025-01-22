
class BinaryTree {
public:
  int value;
  BinaryTree *left = nullptr;
  BinaryTree *right = nullptr;

  BinaryTree(int value) { this->value = value; }
};

void flattenInOrder(BinaryTree *, BinaryTree *&);
BinaryTree *flattenBinaryTree(BinaryTree *);

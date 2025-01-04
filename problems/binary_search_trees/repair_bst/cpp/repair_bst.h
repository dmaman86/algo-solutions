

class BST {
public:
  int value;
  BST *left = nullptr;
  BST *right = nullptr;

  BST(int value) { this->value = value; }
};

class BSTRepair {
private:
  BST *first, *second, *prev;
  void inorder(BST *);

public:
  BSTRepair() : first(nullptr), second(nullptr), prev(nullptr) {}
  BST *repair(BST *);
};

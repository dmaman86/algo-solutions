#include "../../assets/BST.h"

class BSTRepair {
private:
  BST *first, *second, *prev;
  void inorder(BST *);

public:
  BSTRepair() : first(nullptr), second(nullptr), prev(nullptr) {}
  BST *repair(BST *);
};

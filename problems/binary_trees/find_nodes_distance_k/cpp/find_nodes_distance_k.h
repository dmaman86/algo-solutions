
#include <unordered_map>
#include <vector>

class BinaryTree {
public:
  int value;
  BinaryTree *left = nullptr;
  BinaryTree *right = nullptr;

  BinaryTree(int value) { this->value = value; }
};

void findParents(BinaryTree *, std::unordered_map<BinaryTree *, BinaryTree *> &,
                 BinaryTree * = nullptr);
BinaryTree *findTarget(BinaryTree *, int);

std::vector<int> findNodesDistanceK(BinaryTree *, int, int);

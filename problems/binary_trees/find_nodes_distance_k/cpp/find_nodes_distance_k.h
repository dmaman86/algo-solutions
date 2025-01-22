#include "../../assets/BinaryTree.h"
#include <unordered_map>
#include <vector>

void findParents(BinaryTree *, std::unordered_map<BinaryTree *, BinaryTree *> &,
                 BinaryTree * = nullptr);
BinaryTree *findTarget(BinaryTree *, int);

std::vector<int> findNodesDistanceK(BinaryTree *, int, int);

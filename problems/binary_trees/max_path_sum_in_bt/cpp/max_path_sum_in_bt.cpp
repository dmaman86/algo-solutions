#include "max_path_sum_in_bt.h"

#include <algorithm>
#include <climits>

int maxPathSumHelper(BinaryTree *node, int &globalMax) {
  if (!node)
    return 0;

  int leftMax = std::max(maxPathSumHelper(node->left, globalMax), 0);
  int rightMax = std::max(maxPathSumHelper(node->right, globalMax), 0);

  int localMax = node->value + leftMax + rightMax;
  globalMax = std::max(globalMax, localMax);

  return node->value + std::max(leftMax, rightMax);
}

int maxPathSum(BinaryTree tree) {
  int globalMax = INT_MIN;
  maxPathSumHelper(&tree, globalMax);

  return globalMax;
}

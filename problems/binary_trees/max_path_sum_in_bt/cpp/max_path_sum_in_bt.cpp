#include "max_path_sum_in_bt.h"

#include <algorithm>
#include <climits>
#include <functional>

int maxPathSum(BinaryTree tree) {
  int globalMax = INT_MIN;

  std::function<int(BinaryTree *)> maxPathSumHelper =
      [&](BinaryTree *node) -> int {
    if (!node)
      return 0;

    int leftMax = std::max(maxPathSumHelper(node->left), 0);
    int rightMax = std::max(maxPathSumHelper(node->right), 0);

    int max = node->value + leftMax + rightMax;
    globalMax = std::max(globalMax, max);

    return node->value + std::max(leftMax, rightMax);
  };

  maxPathSumHelper(&tree);

  return globalMax;
}

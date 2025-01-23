#include "all_kinds_of_node_depths.h"

#include <functional>
#include <tuple>

int allKindsOfNodeDepths(BinaryTree *root) {
  int result = 0;

  std::function<std::tuple<int, int>(BinaryTree *)> preorderTraversal =
      [&](BinaryTree *node) -> std::tuple<int, int> {
    if (!node)
      return {0, 0};

    auto [depth_sum_left, size_left] = preorderTraversal(node->left);
    auto [depth_sum_right, size_right] = preorderTraversal(node->right);

    // calculate depth sum and size for the current node
    int depth_sum = depth_sum_left + depth_sum_right;
    int size = size_left + size_right + 1;

    // update the global result with the depth sum for this subtree
    result += depth_sum;

    // return the depth sum including the current node and its size
    return std::make_tuple(depth_sum + size, size);
  };

  preorderTraversal(root);

  return result;
}

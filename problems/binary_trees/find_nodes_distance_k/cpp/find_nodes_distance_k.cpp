#include "find_nodes_distance_k.h"
#include <functional>
#include <queue>
#include <unordered_map>
#include <utility>

// function to find all nodes at distance K from the target node
std::vector<int> findNodesDistanceK(BinaryTree *tree, int target, int k) {

  if (!tree)
    return {}; // if the tree is empty, return an empty vector

  // map to store the parent of each node
  std::unordered_map<BinaryTree *, BinaryTree *> parentMap;

  std::function<void(BinaryTree *, BinaryTree *)> findParents =
      [&](BinaryTree *node, BinaryTree *parent) -> void {
    if (!node)
      return;

    parentMap[node] = parent;
    findParents(node->left, node);
    findParents(node->right, node);
  };

  findParents(tree, nullptr);

  std::function<BinaryTree *(BinaryTree *, int)> findTarget =
      [&](BinaryTree *node, int target) -> BinaryTree * {
    if (!node)
      return nullptr;
    if (node->value == target)
      return node;
    BinaryTree *leftResult = findTarget(node->left, target);
    return leftResult ? leftResult : findTarget(node->right, target);
  };

  // find the target node
  BinaryTree *targetNode = findTarget(tree, target);
  if (!targetNode)
    return {}; // if target node is not found, return an empty vector

  // map to track visited nodes and avoid cycles
  std::unordered_map<BinaryTree *, bool> visited;
  // queue to perform BFS, storing each node and its distance from the target
  std::queue<std::pair<BinaryTree *, int>> q;
  q.push({targetNode, 0});
  visited[targetNode] = true;

  // vecto to store the result
  std::vector<int> result;

  // lambda to add nodes to the queue if unvisited
  auto addToQueue = [&](BinaryTree *node, int currentDistance) -> void {
    if (node && !visited[node]) {
      visited[node] = true;
      q.push({node, currentDistance + 1});
    }
  };

  // BFS
  while (!q.empty()) {
    auto [currentNode, currentDistance] = q.front();
    q.pop();

    // if the current distance equals k, add the node's value to the result
    if (currentDistance == k)
      result.push_back(currentNode->value);

    addToQueue(currentNode->left, currentDistance);
    addToQueue(currentNode->right, currentDistance);
    addToQueue(parentMap[currentNode], currentDistance);
  }

  return result;
}

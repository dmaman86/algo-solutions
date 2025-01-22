#include "find_nodes_distance_k.h"
#include <queue>
#include <utility>

// helper function to map each node to its parent node
void findParents(BinaryTree *node,
                 std::unordered_map<BinaryTree *, BinaryTree *> &parentMap,
                 BinaryTree *parent) {
  if (!node)
    return;

  // map the current node to its parent
  parentMap[node] = parent;
  findParents(node->left, parentMap, node);
  findParents(node->right, parentMap, node);
}

// helper function to find the target node in the tree
BinaryTree *findTarget(BinaryTree *node, int target) {
  if (!node)
    return nullptr;

  // if the current node is the target, return it
  if (node->value == target)
    return node;

  // seach in the left subtree
  BinaryTree *leftResult = findTarget(node->left, target);
  if (leftResult)
    return leftResult;
  // if not found in the left subtree, search in the right subtree
  return findTarget(node->right, target);
}

// function to find all nodes at distance K from the target node
std::vector<int> findNodesDistanceK(BinaryTree *tree, int target, int k) {
  // map to store the parent of each node
  std::unordered_map<BinaryTree *, BinaryTree *> parentMap;
  findParents(tree, parentMap);

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
  auto addToQueue = [&](BinaryTree *node, int currentDistance) {
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

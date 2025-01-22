export const findNodesDistanceK = (() => {
  // helper function to map each node to its parent node
  const findParents = (node, parentMap, parent = null) => {
    if (!node) return;

    // map the current node to its parent
    parentMap.set(node, parent);

    findParents(node.left, parentMap, node);
    findParents(node.right, parentMap, node);
  };

  // helper function to find the target node in the tree
  const findTarget = (node, target) => {
    if (!node) return null;

    // if the current node is the target, return it
    if (node.value === target) return node;

    // search in the left subtree
    const leftResult = findTarget(node.left, target);
    if (leftResult) return leftResult;

    // if not found in the left subtree, seach in the right subtree
    return findTarget(node.right, target);
  };

  return (tree, target, k) => {
    const parentMap = new Map();
    // populate the parent map
    findParents(tree, parentMap);

    // find the target node
    const targetNode = findTarget(tree, target);
    if (!targetNode) return []; // if the target node is not found, return an empty array

    const visited = new Set();
    const queue = [[targetNode, 0]]; // queue stores [node, currentDistance]
    visited.add(targetNode);

    const result = [];

    // lambda to add nodes to the queue if unvisited
    const addToQueue = (node, currentDistance) => {
      if (node && !visited.has(node)) {
        visited.add(node);
        queue.push([node, currentDistance + 1]);
      }
    };

    // BFS
    while (queue.length) {
      const [currentNode, currentDistance] = queue.shift();

      // if the current distance equals k, add the node's value to the result
      if (currentDistance === k) result.push(currentNode.value);

      // add the left, right and parent nodes to the queue
      addToQueue(currentNode.left, currentDistance);
      addToQueue(currentNode.right, currentDistance);
      addToQueue(parentMap.get(currentNode), currentDistance);
    }
    return result;
  };
})();

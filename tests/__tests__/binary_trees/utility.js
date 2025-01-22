import { BinaryTree } from "@/binary_trees/assets/BinaryTree.js";

export const buildBT = (nodes, rootId) => {
  const idToNode = {};

  nodes.forEach((node) => {
    idToNode[node.id] = new BinaryTree(node.value);
  });

  nodes.forEach((node) => {
    const btNode = idToNode[node.id];
    btNode.left = node.left ? idToNode[node.left] : null;
    btNode.right = node.right ? idToNode[node.right] : null;
  });

  return idToNode[rootId];
};

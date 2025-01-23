import { BST } from "@/binary_search_trees/assets/BST.js";

export const buildBST = (nodes, rootId) => {
  const idToNode = {};

  nodes.forEach((node) => {
    idToNode[node.id] = new BST(node.value);
  });

  nodes.forEach((node) => {
    const bstNode = idToNode[node.id];
    bstNode.left = node.left ? idToNode[node.left] : null;
    bstNode.right = node.right ? idToNode[node.right] : null;
  });

  return idToNode[rootId];
};

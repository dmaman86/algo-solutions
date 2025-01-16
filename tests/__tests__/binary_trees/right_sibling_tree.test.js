import {
  BinaryTree,
  rightSiblingTree,
} from "@/binary_trees/right_sibling_tree/js/right_sibling_tree";

import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/right_sibling_tree.json";

const buildBT = (nodes, rootId) => {
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

const areBSTsEqual = (bst1, bst2) => {
  if (!bst1 && !bst2) return true;

  if (!bst1 || !bst2 || bst1.value !== bst2.value) return false;

  return (
    areBSTsEqual(bst1.left, bst2.left) && areBSTsEqual(bst1.right, bst2.right)
  );
};

describe("Right Sibling Tree", () => {
  testCases.forEach(({ tree, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBT(tree.nodes, tree.root);
      const expectedRoot = buildBT(expected.nodes, expected.root);

      const result = rightSiblingTree(root);

      const areNodesEqual = areBSTsEqual(result, expectedRoot);
      expect(areNodesEqual).toBe(true);
    });
  });
});

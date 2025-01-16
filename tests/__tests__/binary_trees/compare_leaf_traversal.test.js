import {
  BinaryTree,
  compareLeafTraversal,
} from "@/binary_trees/compare_leaf_traversal/js/compare_leaf_traversal";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/compare_leaf_traversal.json";

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

describe("Compare leaf traversal", () => {
  testCases.forEach(({ tree1, tree2, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root1 = buildBT(tree1.nodes, tree1.root);
      const root2 = buildBT(tree2.nodes, tree2.root);

      const result = compareLeafTraversal(root1, root2);
      expect(result).toBe(expected);
    });
  });
});

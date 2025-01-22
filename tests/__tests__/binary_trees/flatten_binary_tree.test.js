import { flattenBinaryTree } from "@/binary_trees/flatten_binary_tree/js/flatten_binary_tree.js";
import { buildBT } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/flatten_binary_tree.json";

const areBTsEqual = (bt1, bt2, visited = new Set()) => {
  // if both are null, they are equal
  if (!bt1 && !bt2) return true;

  // if one is null or values are not equal, they are not equal
  if (!bt1 || !bt2 || bt1.value !== bt2.value) return false;

  // if the current node has already been visited, avoid infinite recursion
  if (visited.has(bt1) || visited.has(bt2)) return true;

  // mark the current nodes as visited
  visited.add(bt1);
  visited.add(bt2);

  return (
    areBTsEqual(bt1.left, bt2.left, visited) &&
    areBTsEqual(bt1.right, bt2.right, visited)
  );
};

describe("Flatten Binary Tree", () => {
  testCases.forEach(({ tree, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBT(tree.nodes, tree.root);
      const expectedRoot = buildBT(expected.nodes, expected.root);

      const result = flattenBinaryTree(root);

      const areNodesEqual = areBTsEqual(result, expectedRoot);

      expect(areNodesEqual).toBe(true);
    });
  });
});

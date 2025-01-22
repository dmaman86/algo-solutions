import {
  BinaryTree,
  findNodesDistanceK,
} from "@/binary_trees/find_nodes_distance_k/js/find_nodes_distance_k.js";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/find_nodes_distance_k.json";

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

describe("Find Nodes Distance K", () => {
  testCases.forEach(({ tree, target, k, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBT(tree.nodes, tree.root);
      const result = findNodesDistanceK(root, target, k);

      result.sort((a, b) => a - b);
      expected.sort((a, b) => a - b);

      expect(result).toEqual(
        expected,
        `Failed test case ${idx}: target=${target}, k=${k}`,
      );
    });
  });
});

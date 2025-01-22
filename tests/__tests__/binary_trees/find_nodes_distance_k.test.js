import { findNodesDistanceK } from "@/binary_trees/find_nodes_distance_k/js/find_nodes_distance_k.js";
import { buildBT } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/find_nodes_distance_k.json";

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

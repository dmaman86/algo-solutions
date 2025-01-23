import { allKindsOfNodeDepths } from "@/binary_trees/all_kinds_of_node_depths/js/all_kinds_of_node_depths.js";
import { buildBT } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/all_kinds_of_node_depths.json";

describe("All Kinds of Node Depths", () => {
  testCases.forEach(({ tree, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBT(tree.nodes, tree.root);
      const result = allKindsOfNodeDepths(root);

      expect(result).toEqual(expected, `Test case ${idx} failed`);
    });
  });
});

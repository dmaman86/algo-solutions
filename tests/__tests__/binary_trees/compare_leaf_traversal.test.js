import { compareLeafTraversal } from "@/binary_trees/compare_leaf_traversal/js/compare_leaf_traversal";
import { buildBT } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/compare_leaf_traversal.json";

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

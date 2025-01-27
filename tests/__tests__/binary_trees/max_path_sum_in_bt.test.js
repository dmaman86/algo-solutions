import { maxPathSum } from "@/binary_trees/max_path_sum_in_bt/js/max_path_sum_in_bt";
import { buildBT } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_trees/max_path_sum_in_bt.json";

describe("Max Path Sum in Binary Tree", () => {
  testCases.forEach(({ tree, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBT(tree.nodes, tree.root);
      const result = maxPathSum(root);

      expect(result).toEqual(
        expected,
        `Test case ${idx} failed. Expected "${expected}", got "${result}"`,
      );
    });
  });
});

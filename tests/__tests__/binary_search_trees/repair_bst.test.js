import { repairBST } from "@/binary_search_trees/repair_bst/js/repair_bst";
import { buildBST } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_search_trees/repair_bst.json";

const areBSTsEqual = (bst1, bst2) => {
  if (!bst1 && !bst2) return true;

  if (!bst1 || !bst2 || bst1.value !== bst2.value) return false;

  return (
    areBSTsEqual(bst1.left, bst2.left) && areBSTsEqual(bst1.right, bst2.right)
  );
};

describe("Repair BST", () => {
  testCases.forEach(({ tree, expected }, idx) => {
    test(`Test Case ${idx + 1}`, () => {
      const result = repairBST(buildBST(tree.nodes, tree.root));
      const expectedBST = buildBST(expected.nodes, expected.root);

      const areNodesEqual = areBSTsEqual(result, expectedBST);
      expect(areNodesEqual).toBe(true);
    });
  });
});

import { validateThreeNodes } from "@/binary_search_trees/validate_three_nodes/js/validate_three_nodes";
import { buildBST } from "./utility";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_search_trees/validate_three_nodes.json";

const findNode = (root, targetValue) => {
  if (!root) return null;

  if (root.value === targetValue) return root;
  const nextNode = targetValue > root.value ? root.right : root.left;
  return findNode(nextNode, targetValue);
};

describe("Test validateThreeNodes()", () => {
  testCases.forEach(({ tree, nodeOne, nodeTwo, nodeThree, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const root = buildBST(tree.nodes, tree.root);
      const nodeOneNode = findNode(root, Number(nodeOne));
      const nodeTwoNode = findNode(root, Number(nodeTwo));
      const nodeThreeNode = findNode(root, Number(nodeThree));

      const result = validateThreeNodes(
        nodeOneNode,
        nodeTwoNode,
        nodeThreeNode,
      );

      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected "${expected}", got "${result}"`,
      );
    });
  });
});

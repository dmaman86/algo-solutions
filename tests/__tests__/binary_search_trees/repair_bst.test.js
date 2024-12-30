import { BST, repairBST } from "@/binary_search_trees/repair_bst/js/repair_bst";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_search_trees/repair_bst.json";

const buildBST = (nodes, rootId) => {
  const idToNode = {};

  // Crear todos los nodos del árbol
  nodes.forEach((node) => {
    idToNode[node.id] = new BST(node.value);
  });

  // Conectar los hijos
  nodes.forEach((node) => {
    const bstNode = idToNode[node.id];
    bstNode.left = node.left ? idToNode[node.left] : null;
    bstNode.right = node.right ? idToNode[node.right] : null;
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

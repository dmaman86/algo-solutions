import {
  AncestralTree,
  getYoungestCommonAncestor,
} from "@/graphs/youngest_common_ancestor/js/youngest_common_ancestor";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/youngest_common_ancestor.json";

const buildMap = (treeJson) => {
  const nodes = treeJson.nodes;
  const nodeMap = new Map();

  nodes.forEach(({ name }) => {
    nodeMap.set(name, new AncestralTree(name));
  });

  nodes.forEach(({ name, ancestor }) => {
    if (ancestor) {
      const ancestorName = ancestor;
      const ancestorNode = nodeMap.get(ancestorName);
      const descendantNode = nodeMap.get(name);
      ancestorNode.addAsAncestor([descendantNode]);
    }
  });

  return nodeMap;
};

const findNode = (nodeMap, targetName) => nodeMap.get(targetName) || null;

describe("Youngest Common Ancestor", () => {
  testCases.forEach(
    (
      { topAncestor, descendantOne, descendantTwo, ancestralTree, expected },
      idx,
    ) => {
      test(`Test case ${idx}`, () => {
        const treeMap = buildMap(ancestralTree);
        const topAncestorNode = findNode(treeMap, topAncestor);
        const descendantOneNode = findNode(treeMap, descendantOne);
        const descendantTwoNode = findNode(treeMap, descendantTwo);

        const result = getYoungestCommonAncestor(
          topAncestorNode,
          descendantOneNode,
          descendantTwoNode,
        );
        expect(result.name).toBe(expected["nodeId"], `Failed test case ${idx}`);
      });
    },
  );
});

import { cycleInGraph } from "@/graphs/cycle_in_graph/js/cycle_in_graph";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/cycle_in_graph.json";

describe("Cycle in Graph", () => {
  testCases.forEach(({ edges, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = cycleInGraph(edges);
      expect(result).toBe(expected);
    });
  });
});

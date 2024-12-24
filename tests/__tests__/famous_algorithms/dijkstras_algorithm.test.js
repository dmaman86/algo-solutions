import { dijkstrasAlgorithm } from "@/famous_algorithms/dijkstras_algorithm/js/dijkstras_algorithm";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/dijkstras_algorithm.json";

describe("Dijkstra Algorithm", () => {
  testCases.forEach(({ start, edges, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = dijkstrasAlgorithm.dijkstrasAlgorithm(start, edges);

      expect(result.sort()).toEqual(expected.sort());
    });
  });
});

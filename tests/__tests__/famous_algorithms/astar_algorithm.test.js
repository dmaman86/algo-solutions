import { aStarAlgorithm } from "@/famous_algorithms/astar_algorithm/js/astar_algorithm.js";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/astar_algorithm.json";

describe("A* Algorithm", () => {
  testCases.forEach(
    ({ startRow, startCol, endRow, endCol, graph, expected }, idx) => {
      test(`Test case ${idx + 1}`, () => {
        const path = aStarAlgorithm(startRow, startCol, endRow, endCol, graph);
        expect(path).toEqual(expected);
      });
    },
  );
});

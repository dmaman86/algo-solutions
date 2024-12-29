import { kruskalsAlgorithm } from "@/famous_algorithms/kruskals_algorithm/js/kruskals_algorithm";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/kruskals_algorithm.json";

describe("Kruskal's Algorithm", () => {
  testCases.forEach(({ edges, expected }, idx) => {
    test(`Test Case ${idx + 1}`, () => {
      const result = kruskalsAlgorithm(edges);
      expect(result).toEqual(expected);
    });
  });
});

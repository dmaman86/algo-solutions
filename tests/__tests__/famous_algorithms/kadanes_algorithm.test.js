import { kadanesAlgorithm } from "@/famous_algorithms/kadanes_algorithm/js/kadanes_algorithm";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/kadanes_algorithm.json";

describe("Kadane's Algorithm", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = kadanesAlgorithm(array);
      expect(result).toEqual(expected);
    });
  });
});

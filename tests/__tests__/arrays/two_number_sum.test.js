import { twoNumberSum } from "@/arrays/two_number_sum/js/two_number_sum.js";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/two_number_sum.json";

describe("Two Number Sum", () => {
  testCases.forEach(({ array, targetSum, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = twoNumberSum(array, targetSum);

      expect(result.sort()).toEqual(expected.sort());
    });
  });
});

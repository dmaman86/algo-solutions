import { sameBsts } from "@/binary_search_trees/same_bsts/js/same_bsts.js";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_search_trees/same_bsts.json";

describe("Test sameBsts()", () => {
  testCases.forEach(({ arrayOne, arrayTwo, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = sameBsts(arrayOne, arrayTwo);

      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected}, got ${result}`,
      );
    });
  });
});

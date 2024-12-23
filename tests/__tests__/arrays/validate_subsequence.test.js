import { isValidSubsequence } from "@/arrays/validate_subsequence/js/validate_subsequence";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/validate_subsequence.json";

describe("Is Valid Subsequence", () => {
  testCases.forEach(({ array, sequence, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = isValidSubsequence(array, sequence);
      expect(result).toEqual(expected);
    });
  });
});

import { longestIncreasingSubsequence } from "@/dynamic_programming/longest_increasing_subsequence/js/longest_increasing_subsequence";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/dynamic_programming/longest_increasing_subsequence.json";

describe("Longest Increasing Subsequence", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = longestIncreasingSubsequence(array);

      expect(result).toEqual(
        expected,
        `Failed case ${idx}. Expected ${expected}, got ${result}`,
      );
    });
  });
});

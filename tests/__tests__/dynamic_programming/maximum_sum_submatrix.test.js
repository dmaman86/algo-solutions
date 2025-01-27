import { maximumSumSubmatrix } from "@/dynamic_programming/maximum_sum_submatrix/js/maximum_sum_submatrix";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/dynamic_programming/maximum_sum_submatrix.json";

describe("Max Sum Submatrix", () => {
  testCases.forEach(({ matrix, size, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = maximumSumSubmatrix(matrix, size);

      expect(result).toBe(expected, `Test case ${idx} failed`);
    });
  });
});

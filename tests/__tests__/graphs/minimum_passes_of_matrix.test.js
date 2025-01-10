import { minimumPassesOfMatrix } from "@/graphs/minimum_passes_of_matrix/js/minimum_passes_of_matrix";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/minimum_passes_of_matrix.json";

describe("Minimum passes of matrix", () => {
  testCases.forEach(({ matrix, expected }, idx) => {
    test(`Test Case ${idx}`, () => {
      expect(minimumPassesOfMatrix(matrix)).toBe(expected);
    });
  });
});

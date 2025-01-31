import { countSquares } from "@/arrays/count_squares/js/count_squares";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/count_squares.json";

describe("Count Squares", () => {
  testCases.forEach(({ points, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = countSquares(points);

      expect(result).toBe(expected, `Test case ${idx} failed`);
    });
  });
});

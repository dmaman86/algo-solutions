import { lineThroughPoints } from "@/arrays/line_through_points/js/line_through_points";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/line_through_points.json";

describe("Line through points", () => {
  testCases.forEach(({ points, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = lineThroughPoints(points);

      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected} but got ${result}`,
      );
    });
  });
});

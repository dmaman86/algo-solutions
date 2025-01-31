import { classPhotos } from "@/greedy_algorithms/class_photos/js/class_photos";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/class_photos.json";

describe("Class Photos", () => {
  testCases.forEach(({ redShirtHeights, blueShirtHeights, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = classPhotos(redShirtHeights, blueShirtHeights);
      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected} but got ${result}`,
      );
    });
  });
});

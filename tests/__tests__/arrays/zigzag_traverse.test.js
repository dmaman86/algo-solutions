import { zigzagTraverse } from "@/arrays/zigzag_traverse/js/zigzag_traverse";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/zigzag_traverse.json";

describe("Zigzag Traverse", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = zigzagTraverse(array);
      expect(result).toEqual(expected, `Test case ${idx} failed`);
    });
  });
});

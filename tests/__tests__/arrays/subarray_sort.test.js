import { subarraySort } from "@/arrays/subarray_sort/js/subarray_sort";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/subarray_sort.json";

describe("Subarray Sort", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = subarraySort(array);
      expect(result).toEqual(expected);
    });
  });
});

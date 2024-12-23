import { sortedSquaredArray } from "@/arrays/sorted_squared_array/js/sorted_squared_array";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/sorted_squared_array.json";

describe("Sorted Squared Array", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test ${idx}`, () => {
      const result = sortedSquaredArray(array);
      expect(result.sort()).toEqual(expected.sort());
    });
  });
});

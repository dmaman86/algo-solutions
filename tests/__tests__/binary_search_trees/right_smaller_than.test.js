import { rightSmallerThan } from "@/binary_search_trees/right_smaller_than/js/right_smaller_than";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/binary_search_trees/right_smaller_than.json";

describe("right smaller than", () => {
  testCases.forEach(({ array, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = rightSmallerThan(array);
      expect(result).toEqual(expected);
    });
  });
});

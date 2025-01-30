import { validStartingCity } from "@/greedy_algorithms/valid_starting_city/js/valid_starting_city";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/valid_starting_city.json";

describe("Valid Starting City", () => {
  testCases.forEach(({ distances, fuel, mpg, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = validStartingCity(distances, fuel, mpg);

      expect(result).toBe(expected, `Failed for test case ${idx + 1}`);
    });
  });
});

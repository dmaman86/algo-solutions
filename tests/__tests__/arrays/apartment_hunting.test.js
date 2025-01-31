import { apartmentHunting } from "@/arrays/apartment_hunting/js/apartment_hunting";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/apartment_hunting.json";

describe("Apartment Hunting", () => {
  testCases.forEach(({ blocks, reqs, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = apartmentHunting(blocks, reqs);

      expect(result).toBe(expected, `Test case ${idx} failed`);
    });
  });
});

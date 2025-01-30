import { tandemBicycle } from "@/greedy_algorithms/tandem_bicycle/js/tandem_bicycle";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/tandem_bicycle.json";

describe("Tandem Bicycle", () => {
  testCases.forEach(
    ({ redShirtSpeeds, blueShirtSpeeds, fastest, expected }, idx) => {
      test(`Test case ${idx}`, () => {
        const result = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest);
        expect(result).toBe(
          expected,
          `Test case ${idx} failed. Expected ${expected} but got ${result}`,
        );
      });
    },
  );
});

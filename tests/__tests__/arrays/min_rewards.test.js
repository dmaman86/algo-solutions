import { minRewards } from "@/arrays/min_rewards/js/min_rewards";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/min_rewards.json";

describe("Testing minRewards function", () => {
  testCases.forEach(({ scores, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = minRewards(scores);

      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected} but got ${result}`,
      );
    });
  });
});

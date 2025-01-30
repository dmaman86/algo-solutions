import { optimalFreelancing } from "@/greedy_algorithms/optimal_freelancing/js/optimal_freelancing";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/optimal_freelancing.json";

describe("Optimal Freelancing", () => {
  testCases.forEach(({ jobs, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = optimalFreelancing(jobs);

      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected}, got ${result}`,
      );
    });
  });
});

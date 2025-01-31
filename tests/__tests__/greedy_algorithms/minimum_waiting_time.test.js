import { minimumWaitingTime } from "@/greedy_algorithms/minimum_waiting_time/js/minimum_waiting_time";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/minimum_waiting_time.json";

describe("Minimum Waiting Time", () => {
  testCases.forEach(({ queries, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = minimumWaitingTime(queries);
      expect(result).toBe(
        expected,
        `Test case ${idx} failed. Expected ${expected} but got ${result}`,
      );
    });
  });
});

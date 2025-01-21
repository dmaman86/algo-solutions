import { knapsackProblem } from "@/dynamic_programming/knapsack_problem/js/knapsack_problem";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/dynamic_programming/knapsack_problem.json";

describe("Knapsack Problem", () => {
  testCases.forEach(({ items, capacity, expected }, idx) => {
    test(`Test Case ${idx}`, () => {
      const result = knapsackProblem(items, capacity);

      expect(result[0][0]).toBe(expected[0]);

      const resultItemsSorted = [...result[0][1]].sort((a, b) => a - b);
      const expectedItemsSorted = [...expected[1]].sort((a, b) => a - b);

      expect(resultItemsSorted).toEqual(expectedItemsSorted);
    });
  });
});

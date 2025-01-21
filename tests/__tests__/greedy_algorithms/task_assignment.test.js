import { taskAssignment } from "@/greedy_algorithms/task_assignment/js/task_assignment";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/greedy_algorithms/task_assignment.json";

const convertToSet = (pairs) => {
  const result = new Set();

  for (const [x, y] of pairs) result.add(new Set([x, y]));

  return result;
};

const areSetsEqual = (setA, setB) => {
  if (setA.size !== setB.size) return false;
  for (const element of setA) if (!setB.has(element)) return false;

  return true;
};

const isValidResult = (result, expected) => {
  const expectedSet = convertToSet(expected);

  for (const [x, y] of result) {
    const directPair = new Set([x, y]);

    if (![...expectedSet].some((pair) => areSetsEqual(pair, directPair))) {
      const partialMatch = [...expectedSet].some(
        (pair) => pair.has(x) || pair.has(y),
      );
      if (!partialMatch) return false;
    }
  }
  return true;
};

describe("Task Assignment", () => {
  testCases.forEach(({ k, tasks, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = taskAssignment(k, tasks);

      const areEquivalent = isValidResult(result, expected);
      expect(areEquivalent).toBe(true);
    });
  });
});

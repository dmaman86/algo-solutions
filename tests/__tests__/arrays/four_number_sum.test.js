import { fourNumberSum } from "@/arrays/four_number_sum/js/four_number_sum";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/four_number_sum.json";

const areCombinationSetsEquivalent = (result, expected) => {
  if (result.length !== expected.length) return false;

  const normalize = (combinations) => {
    return combinations.map((combination) =>
      combination
        .slice()
        .sort((a, b) => a - b)
        .join(","),
    );
  };

  const resultNormalized = normalize(result).sort();
  const expectedNormalized = normalize(expected).sort();

  return (
    JSON.stringify(resultNormalized) === JSON.stringify(expectedNormalized)
  );
};

describe("Four Number Sum Test", () => {
  testCases.forEach(({ array, targetSum, expected }, idx) => {
    test(`Test ${idx}`, () => {
      const result = fourNumberSum(array, targetSum);
      const areEquivalent = areCombinationSetsEquivalent(result, expected);

      expect(result).toBeTruthy();
      if (!areEquivalent) {
        console.error(`Failed for test case #${idx}`);
        console.error(`Result: ${JSON.stringify(result, null, 2)}`);
        console.error(`Expected: ${JSON.stringify(expected, null, 2)}`);
      }
    });
  });
});

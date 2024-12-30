import { primsAlgorithm } from "@/famous_algorithms/prims_algorithm/js/prims_algorithm";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/prims_algorithm.json";

const arePermutations = (listOne, listTwo) => {
  if (listOne.length !== listTwo.length) return false;

  const sortedListOne = listOne
    .map((sublist) =>
      sublist.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]),
    )
    .sort();
  const sortedListTwo = listTwo
    .map((sublist) =>
      sublist.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]),
    )
    .sort();

  return JSON.stringify(sortedListOne) === JSON.stringify(sortedListTwo);
};

describe("Prims Algorithm Test", () => {
  testCases.forEach(({ edges, expected }, index) => {
    test(`Test case ${index + 1}`, () => {
      const result = primsAlgorithm(edges);
      expect(arePermutations(result, expected)).toBe(true);
    });
  });
});

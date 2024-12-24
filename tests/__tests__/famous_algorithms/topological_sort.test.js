import { topologicalSort } from "@/famous_algorithms/topological_sort/js/topological_sort";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/famous_algorithms/topological_sort.json";

describe("Topological Sort", () => {
  testCases.forEach(({ jobs, deps, expected }, idx) => {
    test(`Test case ${idx + 1}`, () => {
      const result = topologicalSort.topologicalSort(jobs, deps);
      expect(result.sort()).toEqual(expected.sort());
    });
  });
});

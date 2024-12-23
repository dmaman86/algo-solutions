import { tournamentWinner } from "@/arrays/tournament_winner/js/tournament_winner";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/tournament_winner.json";

describe("Tournament Winner", () => {
  testCases.forEach(({ competitions, results, expected }, idx) => {
    test(`Test ${idx}`, () => {
      const result = tournamentWinner(competitions, results);
      expect(result).toEqual(expected);
    });
  });
});

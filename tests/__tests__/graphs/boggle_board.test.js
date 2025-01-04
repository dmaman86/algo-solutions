import { boggleBoard } from "@/graphs/boggle_board/js/boggle_board";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/boggle_board.json";

describe("Boggle Board", () => {
  testCases.forEach(({ board, words, expected }, idx) => {
    test(`Test Case ${idx}`, () => {
      const result = boggleBoard(board, words);
      expect([...new Set(result)].sort()).toEqual(
        [...new Set(expected)].sort(),
      );
    });
  });
});

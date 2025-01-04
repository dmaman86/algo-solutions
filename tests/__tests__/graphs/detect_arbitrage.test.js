import { detectArbitrage } from "@/graphs/detect_arbitrage/js/detect_arbitrage";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/graphs/detect_arbitrage.json";

describe("Detect Arbitrage", () => {
  testCases.forEach(({ exchangeRates, expected }, idx) => {
    test(`Test Case ${idx}`, () => {
      expect(detectArbitrage(exchangeRates)).toBe(expected);
    });
  });
});

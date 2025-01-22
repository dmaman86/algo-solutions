import { maxProfitWithKTransactions } from "@/dynamic_programming/max_profit_with_k_transactions/js/max_profit_with_k_transactions";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/dynamic_programming/max_profit_with_k_transactions.json";

describe("Max Profit With K Transactions", () => {
  testCases.forEach(({ prices, k, expected }, idx) => {
    test(`Test case ${idx}`, () => {
      const result = maxProfitWithKTransactions(prices, k);

      expect(result).toBe(expected, `Test case ${idx} failed`);
    });
  });
});

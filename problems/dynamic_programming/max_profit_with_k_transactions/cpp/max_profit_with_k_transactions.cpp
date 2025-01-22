#include "max_profit_with_k_transactions.h"

#include <algorithm>

int maxProfitWithKTransactions(std::vector<int> &prices, int k) {
  if (prices.empty())
    return 0;

  int n = prices.size();

  // optimization for large k: treat as unlimited transactions
  if (k >= n / 2) {
    int profit = 0;
    for (int i = 1; i < n; i++) {
      profit += std::max(prices[i] - prices[i - 1], 0);
    }
    return profit;
  }

  // dp table: dp[i][j] represents the maximum profit with i transactions
  // on the first j days
  std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n, 0));

  // fill the dp table
  for (int i = 1; i <= k; i++) {
    int max_diff =
        -prices[0]; // tracks the maximum difference for this transaction level
    for (int j = 1; j < n; j++) {
      dp[i][j] = std::max(dp[i][j - 1], prices[j] + max_diff);
      max_diff = std::max(max_diff, dp[i - 1][j] - prices[j]);
    }
  }

  // the result is the maximum profit with k transactions on the last day
  return dp[k][n - 1];
}

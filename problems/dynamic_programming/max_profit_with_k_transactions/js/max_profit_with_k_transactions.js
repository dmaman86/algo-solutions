export const maxProfitWithKTransactions = (prices, k) => {
  if (!prices.length) return 0;

  const n = prices.length;

  if (k >= Math.floor(n / 2)) {
    let profit = 0;
    for (let i = 1; i < n; i++) {
      profit += Math.max(prices[i] - prices[i - 1], 0);
    }
    return profit;
  }

  const dp = Array.from({ length: k + 1 }, () => Array(n).fill(0));

  for (let i = 1; i <= k; i++) {
    let max_diff = -prices[0];
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.max(dp[i][j - 1], prices[j] + max_diff);
      max_diff = Math.max(max_diff, dp[i - 1][j] - prices[j]);
    }
  }
  return dp[k][n - 1];
};

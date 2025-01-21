export const knapsackProblem = (() => {
  /**
   * Builds the DP matrix for the knapsack problem
   * @param {number[][]} items - Arrray of items where each item is [value, weight]
   * @param {number} capacity - The maximum weight the knapsack can carry
   * @returns {number[][]} - DP matrix
   * */
  const fillDpMatrix = (items, capacity) => {
    const n = items.length;
    const dp = Array.from({ length: n + 1 }, () => Array(capacity + 1).fill(0));

    for (let i = 1; i <= n; i++) {
      const currentItemValue = items[i - 1][0];
      const currentItemWeight = items[i - 1][1];

      for (let c = 0; c <= capacity; c++) {
        if (currentItemWeight > c) {
          dp[i][c] = dp[i - 1][c]; // cannot include the current item
        } else {
          dp[i][c] = Math.max(
            dp[i - 1][c], // exclude the item
            dp[i - 1][c - currentItemWeight] + currentItemValue, // include the item
          );
        }
      }
    }
    return dp;
  };

  /**
   * Reconstructs the selected items based on the DP matrix
   * @param {number[][]} dp - DP matrix
   * @param {number[][]} items - Array of items where each item is [value, weight]
   * @param {number} capacity - Maximum weight the knapsack can carry
   * @returns {number[]} - Indices of selected items
   */
  const getSelectedItems = (dp, items, capacity) => {
    const selectedItems = [];
    let n = items.length;
    let c = capacity;

    while (n > 0 && c > 0) {
      if (dp[n][c] !== dp[n - 1][c]) {
        // the item was included in the optimal solution
        selectedItems.push(n - 1);
        c -= items[n - 1][1]; // reduce the capacity
      }
      n--; // move to the previous item
    }
    return selectedItems;
  };

  /**
   * Solves the knapsack problem
   * @param {number[][]} items - Array of items where each item is [value, weight]
   * @param {number} capacity - Maximum weight the knapsack can carry
   * @returns {number[][]} - Result in the format [[totalValue], [selectedItemIndices]]
   */
  return (items, capacity) => {
    const dp = fillDpMatrix(items, capacity);
    const selectedItems = getSelectedItems(dp, items, capacity);

    return [[dp[items.length][capacity], selectedItems]];
  };
})();

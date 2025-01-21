#include "knapsack_problem.h"

#include <algorithm>

// Builds the DP matrix for the knapsack problem
vector2DInt fillDpMatrix(const vector2DInt &items, int capacity) {
  int n = items.size();
  vector2DInt dp(n + 1, vectorInt(capacity + 1, 0));

  for (size_t i = 1; i <= n; i++) {
    auto currentItemValue = items[i - 1][0];
    auto currentItemWeight = items[i - 1][1];

    for (size_t c = 0; c <= capacity; c++) {
      if (currentItemWeight > c)
        dp[i][c] =
            dp[i - 1]
              [c]; // Item weight exceeds capacity; carry forward previous value
      else
        dp[i][c] = std::max(
            dp[i - 1][c],
            dp[i - 1][c - currentItemWeight] +
                currentItemValue); // include or exclude the current item
    }
  }
  return dp;
}

// retrieves the selected items based on the DP matrix
vectorInt getSelectedItems(const vector2DInt &dp, const vector2DInt &items,
                           int capacity) {
  vectorInt selectedItems;
  int n = items.size(), c = capacity;

  while (n > 0 && c > 0) {
    if (dp[n][c] != dp[n - 1][c]) {
      // item was included; add its index and reduce capacity
      selectedItems.push_back(n - 1);
      c -= items[n - 1][1];
    }
    n--; // move to the previous item
  }
  return selectedItems;
}

// solves the knapsack problem and returns the result as a vector<vector<int>>
vector2DInt knapsackProblem(vector2DInt items, int capacity) {
  vector2DInt dp = fillDpMatrix(items, capacity);
  vectorInt selectedItems = getSelectedItems(dp, items, capacity);

  // result: {total value, selected item indices}
  return {{dp[items.size()][capacity]}, selectedItems};
};

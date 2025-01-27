#include "maximum_sum_submatrix.h"
#include <climits>

vector2DInt buildDp(const vector2DInt &matrix) {
  int rows = matrix.size();
  int cols = matrix[0].size();

  vector2DInt dp(rows + 1, std::vector<int>(cols + 1, 0));

  for (int i = 1; i <= rows; i++) {
    for (int j = 1; j <= cols; j++) {
      dp[i][j] =
          matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1];
    }
  }
  return dp;
}

int findMaxSum(const vector2DInt &dp, int size, const Dimensions &dimensions) {
  int max_sum = INT_MIN;

  for (int i = 1; i <= dimensions.first - size + 1; i++) {
    for (int j = 1; j <= dimensions.second - size + 1; j++) {
      int sum = dp[i + size - 1][j + size - 1] - dp[i - 1][j + size - 1] -
                dp[i + size - 1][j - 1] + dp[i - 1][j - 1];

      if (sum > max_sum)
        max_sum = sum;
    }
  }
  return max_sum;
}
int maximumSumSubmatrix(vector2DInt matrix, int size) {
  vector2DInt dp = buildDp(matrix);

  return findMaxSum(dp, size, {matrix.size(), matrix[0].size()});
}

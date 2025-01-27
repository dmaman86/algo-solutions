export const maximumSumSubmatrix = (() => {
  const buildDp = (matrix) => {
    const rows = matrix.length;
    const cols = matrix[0].length;

    const dp = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));

    for (let i = 1; i <= rows; i++) {
      for (let j = 1; j <= cols; j++) {
        dp[i][j] =
          matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1];
      }
    }
    return dp;
  };

  const findMaxSum = (dp, size, dimensions) => {
    let maxSum = -Infinity;
    const [rows, cols] = dimensions;

    for (let i = 1; i <= rows - size + 1; i++) {
      for (let j = 1; j <= cols - size + 1; j++) {
        const sum =
          dp[i + size - 1][j + size - 1] -
          dp[i - 1][j + size - 1] -
          dp[i + size - 1][j - 1] +
          dp[i - 1][j - 1];

        if (sum > maxSum) maxSum = sum;
      }
    }
    return maxSum;
  };

  return (matrix, size) => {
    const dp = buildDp(matrix);

    return findMaxSum(dp, size, [matrix.length, matrix[0].length]);
  };
})();

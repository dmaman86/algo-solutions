def buildDp(matrix: list[list[int]]) -> list[list[int]]:
    rows, cols = len(matrix), len(matrix[0])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dp[i][j] = (
                matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            )

    return dp


def find_max(dp: list[list[int]], size: int, dimensions: tuple[int, int]) -> int:
    max_sum = float("-inf")
    [rows, cols] = dimensions

    for i in range(1, rows - size + 2):
        for j in range(1, cols - size + 2):
            current_sum = (
                dp[i + size - 1][j + size - 1]
                - dp[i - 1][j + size - 1]
                - dp[i + size - 1][j - 1]
                + dp[i - 1][j - 1]
            )

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


def maximumSumSubmatrix(matrix: list[list[int]], size: int) -> int:
    dp = buildDp(matrix)

    return find_max(dp, size, (len(matrix), len(matrix[0])))

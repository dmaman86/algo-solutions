def fill_dp_matrix(items: list[list[int]], capacity: int) -> list[list[int]]:
    n = len(items)
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        current_value = items[i - 1][0]
        current_weight = items[i - 1][1]

        for c in range(capacity + 1):
            if current_weight > c:
                # cannot include the current item
                dp[i][c] = dp[i - 1][c]
            else:
                # include or exclude the current item
                dp[i][c] = max(
                    dp[i - 1][c], dp[i - 1][c - current_weight] + current_value
                )

    return dp


def get_selected_items(
    dp: list[list[int]], items: list[list[int]], capacity: int
) -> list[int]:
    selected_items: list[int] = []
    n = len(items)
    c = capacity

    while n > 0 and c > 0:
        if dp[n][c] != dp[n - 1][c]:
            # the item was included
            selected_items.append(n - 1)
            c -= items[n - 1][1]  # reduce the capacity
        n -= 1  # move to the previous item

    return selected_items


def knapsack_problem(items: list[list[int]], capacity: int) -> list[list[int]]:
    dp = fill_dp_matrix(items, capacity)
    selected_items = get_selected_items(dp, items, capacity)

    return [dp[len(items)][capacity], selected_items]

def minRewards(scores: list[int]) -> int:
    n = len(scores)
    rewards = [1] * n

    def traverse(startIdx: int, endIdx: int, step: int) -> None:
        for i in range(startIdx, endIdx, step):
            if scores[i] > scores[i - step]:
                rewards[i] = (
                    rewards[i - step] + 1
                    if step == 1
                    else max(rewards[i], rewards[i - step] + 1)
                )

    traverse(1, n, 1)
    traverse(n - 2, -1, -1)

    return sum(rewards)

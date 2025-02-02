from problems.arrays.min_rewards.python.min_rewards import minRewards
from tests.python.utility import load_test_cases


def test_min_rewards() -> None:
    test_cases = load_test_cases("arrays/min_rewards.json")

    for idx, test in enumerate(test_cases):
        scores: list[int] = test["scores"]
        expected: int = test["expected"]

        result: int = minRewards(scores)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

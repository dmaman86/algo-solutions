from problems.dynamic_programming.longest_increasing_subsequence.python.longest_increasing_subsequence import \
    longestIncreasingSubsequence
from tests.python.utility import load_test_cases


def test_longest_increasing_subsequence() -> None:

    test_cases = load_test_cases(
        "dynamic_programming/longest_increasing_subsequence.json"
    )

    for idx, test in enumerate(test_cases):
        array: list[int] = test["array"]
        expected: list[int] = test["expected"]

        result: list[int] = longestIncreasingSubsequence(array)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

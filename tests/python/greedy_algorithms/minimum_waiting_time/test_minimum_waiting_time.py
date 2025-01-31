from problems.greedy_algorithms.minimum_waiting_time.python.minimum_waiting_time import \
    minimumWaitingTime
from tests.python.utility import load_test_cases


def test_minimum_waiting_time() -> None:
    test_cases = load_test_cases("greedy_algorithms/minimum_waiting_time.json")

    for idx, test in enumerate(test_cases):
        queries: list[int] = test["queries"]
        expected: int = test["expected"]

        result: int = minimumWaitingTime(queries)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

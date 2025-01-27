from problems.dynamic_programming.maximum_sum_submatrix.python.maximum_sum_submatrix import \
    maximumSumSubmatrix
from tests.python.utility import load_test_cases


def test_maximum_sum_submatrix() -> None:
    test_cases = load_test_cases("dynamic_programming/maximum_sum_submatrix.json")

    for idx, test in enumerate(test_cases):
        matrix = test["matrix"]
        size = test["size"]
        expected = test["expected"]

        result = maximumSumSubmatrix(matrix, size)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

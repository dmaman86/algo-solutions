from problems.arrays.count_squares.python.count_squares import countSquares
from tests.python.utility import load_test_cases


def test_count_squares() -> None:
    test_cases = load_test_cases("arrays/count_squares.json")

    for idx, test in enumerate(test_cases):
        points: list[list[int]] = test["points"]
        expected: int = test["expected"]

        result: int = countSquares(points)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

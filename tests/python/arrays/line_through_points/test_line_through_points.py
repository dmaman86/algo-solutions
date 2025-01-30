from problems.arrays.line_through_points.python.line_through_points import \
    lineThroughPoints
from tests.python.utility import load_test_cases


def test_line_through_points() -> None:
    test_cases = load_test_cases("arrays/line_through_points.json")

    for idx, test in enumerate(test_cases):
        points: list[list[int]] = test["points"]
        expected: int = test["expected"]

        result: int = lineThroughPoints(points)

        assert result == expected, f"Test case {idx} failed"

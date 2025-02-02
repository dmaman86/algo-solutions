from problems.arrays.zigzag_traverse.python.zigzag_traverse import \
    zigzagTraverse
from tests.python.utility import load_test_cases


def test_zigzag_traverse() -> None:
    test_cases = load_test_cases("arrays/zigzag_traverse.json")

    for idx, test in enumerate(test_cases):
        array: list[list[int]] = test["array"]
        expected: list[int] = test["expected"]

        result: list[int] = zigzagTraverse(array)

        assert result == expected, f"Test case {idx} failed"

from problems.binary_search_trees.same_bsts.python.same_bsts import sameBsts
from tests.python.utility import load_test_cases


def test_same_bsts() -> None:
    test_cases = load_test_cases("binary_search_trees/same_bsts.json")

    for idx, test in enumerate(test_cases):
        arrayOne = test["arrayOne"]
        arrayTwo = test["arrayTwo"]
        expected = test["expected"]

        result = sameBsts(arrayOne, arrayTwo)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

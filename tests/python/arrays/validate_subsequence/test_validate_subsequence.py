import pytest

from problems.arrays.validate_subsequence.python.validate_subsequence import \
    isValidSubsequence
from tests.python.utility import load_test_cases


def test_validate_subsequence(visualize: bool = False) -> None:

    test_cases = load_test_cases("arrays/validate_subsequence.json")

    for idx, test in enumerate(test_cases):
        array = test["array"]
        sequence = test["sequence"]
        expected = test["expected"]
        result = isValidSubsequence(array, sequence)

        assert (
            result == expected
        ), f"Test case {idx} failed. Expected: {expected}, got: {result}"

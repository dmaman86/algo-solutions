import pytest

from problems.arrays.subarray_sort.python.subarray_sort import subarray_sort
from tests.python.utility import load_test_cases


def test_subarray_sort(visualize: bool = False) -> None:

    test_cases = load_test_cases("arrays/subarray_sort.json")

    for idx, test in enumerate(test_cases):
        array = test["array"]
        expected = test["expected"]
        result = subarray_sort(array)

        assert (
            result == expected
        ), f"Test case {idx} failed. Expected: {expected}, got: {result}"

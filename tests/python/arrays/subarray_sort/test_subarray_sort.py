import argparse

from problems.arrays.subarray_sort.python.subarray_sort import subarray_sort
from tests.python.utility import load_test_cases


def test_subarray_sort() -> None:
    test_cases = load_test_cases("arrays/subarray_sort.json")

    for idx, test in enumerate(test_cases):
        array = test["array"]
        expected = test["expected"]
        result = subarray_sort(array)

        assert result == expected, f"Test case failed ar index {idx}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run test for the subarray_sort function"
    )
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save the results of the tests in the results folder",
    )
    args = parser.parse_args()
    test_subarray_sort()

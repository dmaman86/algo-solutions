import argparse

from problems.arrays.validate_subsequence.python.validate_subsequence import \
    isValidSubsequence
from tests.python.utility import load_test_cases


def test_validate_subsequence() -> None:

    test_cases = load_test_cases("arrays/validate_subsequence.json")

    for idx, case in enumerate(test_cases):
        array: list[int] = case["array"]
        sequence: list[int] = case["sequence"]
        expected: bool = case["expected"]
        assert (
            isValidSubsequence(array, sequence) == expected
        ), f"Test case {idx + 1} failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run test for the validate_subsequence function"
    )
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save the results of the tests in the results folder",
    )
    test_validate_subsequence()

from utility import load_test_cases
from validate_subsequence.python.validate_subsequence import isValidSubsequence


def test_validate_subsequence() -> None:

    test_cases = load_test_cases("arrays/validate_subsequence.json")

    for idx, case in enumerate(test_cases):
        array: list[int] = case["array"]
        sequence: list[int] = case["sequence"]
        expected: bool = case["expected"]
        assert (
            isValidSubsequence(array, sequence) == expected
        ), f"Test case {idx + 1} failed"

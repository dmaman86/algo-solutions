import json
import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parents[3]
sys.path.append(str(root_dir))


from problems.arrays.validate_subsequence.python.validate_subsequence import \
    isValidSubsequence


def test_validate_subsequence():
    json_path = Path("tests/test_cases/arrays/validate_subsequence.json")
    with open(json_path, "r") as file:
        test_cases = json.load(file)

    for idx, case in enumerate(test_cases):
        array = case["array"]
        sequence = case["sequence"]
        expected = case["expected"]
        assert (
            isValidSubsequence(array, sequence) == expected
        ), f"Test case {idx + 1} failed"

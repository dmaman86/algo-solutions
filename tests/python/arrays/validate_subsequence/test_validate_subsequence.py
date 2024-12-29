import json
from pathlib import Path

from validate_subsequence.python.validate_subsequence import isValidSubsequence


def load_test_cases(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "arrays" / filename
    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    with json_path.open("r") as file:
        return json.load(file)


def test_validate_subsequence() -> None:

    test_cases = load_test_cases("validate_subsequence.json")

    for idx, case in enumerate(test_cases):
        array: list[int] = case["array"]
        sequence: list[int] = case["sequence"]
        expected: bool = case["expected"]
        assert (
            isValidSubsequence(array, sequence) == expected
        ), f"Test case {idx + 1} failed"

from problems.arrays.apartment_hunting.python.apartment_hunting import \
    apartmentHunting
from tests.python.utility import load_test_cases


def test_apartment_hunting() -> None:
    test_cases = load_test_cases("arrays/apartment_hunting.json")

    for idx, test in enumerate(test_cases):
        blocks: list[dict[str, bool]] = test["blocks"]
        reqs: list[str] = test["reqs"]
        expected: int = test["expected"]

        result: int = apartmentHunting(blocks, reqs)

        assert result == expected, f"Test case {idx} failed"

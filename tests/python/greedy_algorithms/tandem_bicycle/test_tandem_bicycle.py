from problems.greedy_algorithms.tandem_bicycle.python.tandem_bicycle import \
    tandemBicycle
from tests.python.utility import load_test_cases


def test_tandem_bicycle() -> None:
    test_cases = load_test_cases("greedy_algorithms/tandem_bicycle.json")

    for idx, test in enumerate(test_cases):
        redShirtSpeeds: list[int] = test["redShirtSpeeds"]
        blueShirtSpeeds: list[int] = test["blueShirtSpeeds"]
        fastest: bool = test["fastest"]
        expected: int = test["expected"]

        result: int = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

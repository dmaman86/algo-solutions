from problems.greedy_algorithms.valid_starting_city.python.valid_starting_city import \
    validStartingCity
from tests.python.utility import load_test_cases


def test_valid_starting_city() -> None:

    test_cases = load_test_cases("greedy_algorithms/valid_starting_city.json")

    for idx, test in enumerate(test_cases):
        distances: list[int] = test["distances"]
        fuel: list[int] = test["fuel"]
        mpg: int = test["mpg"]
        expected: int = test["expected"]

        result: int = validStartingCity(distances, fuel, mpg)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

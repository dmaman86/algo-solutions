import pytest

from problems.graphs.minimum_passes_of_matrix.python.minimum_passes_of_matrix import \
    minimum_passes_of_matrix
from tests.python.utility import load_test_cases


def test_minimum_passes_of_matrix(visualize: bool) -> None:

    test_cases = load_test_cases("graphs/minimum_passes_of_matrix.json")

    for idx, test in enumerate(test_cases):
        matrix = test["matrix"]
        expected = test["expected"]

        passes, history = minimum_passes_of_matrix(matrix)

        assert passes == expected, f"Test case failed at index {idx}"

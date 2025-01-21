from collections import Counter

from problems.dynamic_programming.knapsack_problem.python.knapsack_problem import \
    knapsack_problem
from tests.python.utility import load_test_cases


def test_knapsack_problem() -> None:

    test_cases = load_test_cases("dynamic_programming/knapsack_problem.json")

    for idx, test in enumerate(test_cases):
        items = test["items"]
        capacity = test["capacity"]
        expected = test["expected"]

        result = knapsack_problem(items, capacity)

        assert result[0] == expected[0], f"Failed at case {idx}"

        assert Counter(result[1]) == Counter(expected[1]), f"Failed at case {idx}"

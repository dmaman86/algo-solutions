from problems.greedy_algorithms.task_assignment.python.task_assignment import \
    task_assignment
from tests.python.utility import load_test_cases


def convert_to_set(pairs: list[list[int]]) -> set[frozenset[int]]:
    result = set()
    for x, y in pairs:
        result.add(frozenset([x, y]))

    return result


def is_valid_result(result: list[list[int]], expected: list[list[int]]) -> bool:
    expected_set = convert_to_set(expected)

    for x, y in result:
        direct_pair = frozenset([x, y])

        if direct_pair not in expected_set:
            partial_match = any(x in pair or y in pair for pair in expected_set)
            if not partial_match:
                return False

    return True


def test_task_assignment() -> None:
    test_cases = load_test_cases("greedy_algorithms/task_assignment.json")

    for idx, test in enumerate(test_cases):
        k = test["k"]
        tasks = test["tasks"]
        expected = test["expected"]

        result = task_assignment(k, tasks)

        is_valid = is_valid_result(result, expected)

        assert (
            is_valid == True
        ), f"Test case {idx} failed: expected {expected}, got {result}"

from problems.greedy_algorithms.optimal_freelancing.python.optimal_freelancing import \
    optimalFreelancing
from tests.python.utility import load_test_cases


def test_optimal_freelancing() -> None:
    test_cases = load_test_cases("greedy_algorithms/optimal_freelancing.json")

    for idx, test in enumerate(test_cases):
        jobs: list[dict] = test["jobs"]
        expected: int = test["expected"]

        result: int = optimalFreelancing(jobs)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

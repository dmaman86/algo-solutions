import argparse
from collections import Counter

from problems.famous_algorithms.topological_sort.python.topological_sort import \
    topological_sort
from tests.python.utility import load_test_cases, save_results


def test_topological_sort(save_results_flag: bool = False) -> None:
    test_cases = load_test_cases("famous_algorithms/topological_sort.json")
    results: list[dict] = []

    for idx, test in enumerate(test_cases):
        jobs = test["jobs"]
        deps = test["deps"]
        expected = test["expected"]

        [result, graph] = topological_sort(jobs, deps)

        if save_results_flag:
            results.append({"sorted_jobs": result, "graph": graph})
        assert Counter(result) == Counter(
            expected
        ), f"Test case {idx} failed: {result=}, {expected=}"

    if save_results_flag:
        save_results("famous_algorithms/topological_sort.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Topological Sort")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/famous_algorithms/topological_sort.json",
    )

    args = parser.parse_args()
    test_topological_sort(save_results_flag=args.save_results)

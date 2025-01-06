import argparse

from problems.famous_algorithms.prims_algorithm.python.prims_algorithm import \
    primsAlgorithm
from tests.python.utility import load_test_cases, save_results

AdjacencyList = list[list[list[int]]]


def are_permutations(list1: AdjacencyList, list2: AdjacencyList) -> bool:
    if len(list1) != len(list2):
        return False

    sorted_list1 = sorted([sorted(sublist) for sublist in list1])
    sorted_list2 = sorted([sorted(sublist) for sublist in list2])
    return sorted_list1 == sorted_list2


def test_prims_algorithm(save_results_flag: bool = False) -> None:

    test_cases = load_test_cases("famous_algorithms/prims_algorithm.json")
    results: list[dict] = []

    for idx, case in enumerate(test_cases):
        edges: AdjacencyList = case["edges"]
        expected: AdjacencyList = case["expected"]

        result: AdjacencyList = primsAlgorithm(edges)

        if save_results_flag:
            results.append({"mst": result})
        assert are_permutations(expected, result), f"Test case {idx + 1} failed"

    if save_results_flag:
        save_results("famous_algorithms/prims_algorithm.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Prim's Algorithm")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/famous_algorithms/prims_algorithm.json",
    )

    args = parser.parse_args()
    test_prims_algorithm(save_results_flag=args.save_results)

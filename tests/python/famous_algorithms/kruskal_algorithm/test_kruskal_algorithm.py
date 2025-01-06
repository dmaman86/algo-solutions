import argparse

from problems.famous_algorithms.kruskals_algorithm.python.kruskal_algorithm import \
    kruskalsAlgorithm
from tests.python.utility import load_test_cases, save_results

AdjacencyList = list[list[tuple[int, int]]]
Edge = tuple[int, int, int]
MSTResult = tuple[list[Edge], AdjacencyList]


def are_permutations(list1: AdjacencyList, list2: AdjacencyList) -> bool:
    if len(list1) != len(list2):
        return False

    sorted_list1 = sorted([sorted(sublist) for sublist in list1])
    sorted_list2 = sorted([sorted(sublist) for sublist in list2])
    return sorted_list1 == sorted_list2


def test_kruskal_algorithm(save_results_flag: bool = False) -> None:

    test_cases = load_test_cases("famous_algorithms/kruskals_algorithm.json")
    results: list[dict] = []

    for idx, case in enumerate(test_cases):
        edges: AdjacencyList = case["edges"]
        expected: AdjacencyList = case["expected"]
        [mst_edges, mst] = kruskalsAlgorithm(edges)

        if save_results_flag:
            results.append({"mst": mst})
        mst_as_lists = [[list(edge) for edge in sublist] for sublist in mst]

        assert are_permutations(mst_as_lists, expected), (
            f"Test case failed at index {idx}\n" f"Expected: {expected}\n" f"Got: {mst}"
        )

    if save_results_flag:
        save_results("famous_algorithms/kruskals_algorithm.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Kruskal's Algorithm")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/famous_algorithms/kruskals_algorithm.json",
    )

    args = parser.parse_args()
    test_kruskal_algorithm(save_results_flag=args.save_results)

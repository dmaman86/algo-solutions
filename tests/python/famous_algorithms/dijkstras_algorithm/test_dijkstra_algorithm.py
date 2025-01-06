import argparse

from problems.famous_algorithms.dijkstras_algorithm.python.dijkstras_algorithm import \
    dijkstra_algorithm
from tests.python.utility import load_test_cases, save_results


def test_dijkstra_algorithm(save_results_flag: bool = False) -> None:
    test_cases = load_test_cases("famous_algorithms/dijkstras_algorithm.json")
    results: list[dict] = []

    for idx, case in enumerate(test_cases):
        start = case["start"]
        edges = case["edges"]
        expected = case["expected"]

        [distances, previous] = dijkstra_algorithm(start, edges)
        if save_results_flag:
            results.append({"distances": distances, "previous": previous})
        assert distances == expected, f"Test case {idx} failed for distances"

    if save_results_flag:
        save_results("famous_algorithms/dijkstras_algorithm.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Dijkstra's Algorithm")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/famous_algorithms/dijkstras_algorithm.json",
    )

    args = parser.parse_args()
    test_dijkstra_algorithm(save_results_flag=args.save_results)

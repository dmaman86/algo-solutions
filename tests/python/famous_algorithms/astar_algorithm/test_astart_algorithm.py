import argparse

from problems.famous_algorithms.astar_algorithm.python.astar_algorithm import \
    aStarAlgorithm
from tests.python.utility import load_test_cases, save_results


def test_astar_algorithm(save_results_flag: bool = False) -> None:
    test_cases = load_test_cases("famous_algorithms/astar_algorithm.json")
    results: list[dict] = []

    for idx, test in enumerate(test_cases):
        startRow = test["startRow"]
        startCol = test["startCol"]
        endRow = test["endRow"]
        endCol = test["endCol"]
        graph = test["graph"]
        path = aStarAlgorithm(startRow, startCol, endRow, endCol, graph)

        if save_results_flag:
            results.append({"path": path})
        assert path == test["expected"], f"Test case {idx} failed"

    if save_results_flag:
        save_results("famous_algorithms/astar_algorithm.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test A* Algorithm")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/famous_algorithms/astar_algorithm.json",
    )

    args = parser.parse_args()
    test_astar_algorithm(save_results_flag=args.save_results)

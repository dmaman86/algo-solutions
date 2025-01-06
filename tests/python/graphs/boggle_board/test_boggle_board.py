import argparse

from problems.graphs.boggle_board.python.boggle_board import boggleBoard
from tests.python.utility import load_test_cases, save_results


def test_boggle_board(save_results_flag: bool = False) -> None:

    test_cases = load_test_cases("graphs/boggle_board.json")
    results: list[dict] = []

    for idx, test in enumerate(test_cases):
        board = test["board"]
        words = test["words"]
        expected = test["expected"]

        result = boggleBoard(board, words)

        if save_results_flag:
            results.append(result)

        assert set(result["words"].keys()) == set(
            expected
        ), f"Test case failed at index {idx}!"

    if save_results_flag:
        save_results("graphs/boggle_board.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Boggle Board")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/graphs/boggle_board.json",
    )

    args = parser.parse_args()
    test_boggle_board(save_results_flag=args.save_results)

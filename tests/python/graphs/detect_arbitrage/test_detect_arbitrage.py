import argparse

from problems.graphs.detect_arbitrage.python.detect_arbitrage import \
    detectArbitrage
from tests.python.utility import load_test_cases


def test_detect_arbitrage() -> None:
    test_cases = load_test_cases("graphs/detect_arbitrage.json")

    for idx, test in enumerate(test_cases):
        exchangeRates = test["exchangeRates"]
        expected = test["expected"]

        result = detectArbitrage(exchangeRates)
        assert result == expected, f"Test case failed at index {idx}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run test for the detect_arbitrage function"
    )
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save the results of the tests in the results folder",
    )
    args = parser.parse_args()
    test_detect_arbitrage()

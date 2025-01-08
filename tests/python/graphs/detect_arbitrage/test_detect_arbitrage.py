import pytest

from problems.graphs.detect_arbitrage.python.detect_arbitrage import \
    detectArbitrage
from tests.python.utility import load_test_cases


def test_detect_arbitrage(visualize: bool) -> None:

    test_cases = load_test_cases("graphs/detect_arbitrage.json")

    for idx, test in enumerate(test_cases):
        exchangeRates = test["exchangeRates"]
        expected = test["expected"]

        result = detectArbitrage(exchangeRates)
        assert result == expected, f"Test case failed at index {idx}!"

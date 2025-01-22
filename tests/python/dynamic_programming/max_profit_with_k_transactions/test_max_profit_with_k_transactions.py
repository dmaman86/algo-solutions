from problems.dynamic_programming.max_profit_with_k_transactions.python.max_profit_with_k_transactions import \
    maxProfitWithKTransactions
from tests.python.utility import load_test_cases


def test_max_profit_with_k_transactions() -> None:
    test_cases = load_test_cases(
        "dynamic_programming/max_profit_with_k_transactions.json"
    )

    for idx, test in enumerate(test_cases):
        prices = test["prices"]
        k = test["k"]
        expected = test["expected"]

        result = maxProfitWithKTransactions(prices, k)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

import argparse

from problems.graphs.airport_connections.python.airport_connections import \
    airport_connections
from tests.python.utility import load_test_cases, save_results


def test_airports_connections(save_results_flag: bool = False) -> None:
    test_cases = load_test_cases("graphs/airports_connections.json")
    results: list[dict] = []

    for idx, case in enumerate(test_cases):
        airports = case["airports"]
        routes = case["routes"]
        starting_airport = case["startingAirport"]
        expected = case["expected"]

        result = airport_connections(airports, routes, starting_airport)

        if save_results_flag:
            results.append({"connections": result})
        assert len(result) == expected, f"Test case {idx} failed"

    if save_results_flag:
        save_results("graphs/airports_connections.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test Airport Connections")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save test results to results/graphs/airports_connections.json",
    )

    args = parser.parse_args()
    test_airports_connections(save_results_flag=args.save_results)

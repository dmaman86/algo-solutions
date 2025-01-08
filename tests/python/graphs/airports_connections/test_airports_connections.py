from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import pytest

from problems.graphs.airport_connections.python.airport_connections import \
    airport_connections
from tests.python.utility import load_test_cases


def build_graph(airports: list[str], routes: list[list[str]]) -> nx.DiGraph:
    G = nx.DiGraph()

    for airport in airports:
        G.add_node(airport)

    for route in routes:
        G.add_edge(route[0], route[1])

    return G


def draw_graph(graph: nx.DiGraph, pos: dict, title: str, ax: plt.Axes) -> None:
    nx.draw_networkx_nodes(
        graph, pos, node_size=700, node_color="skyblue", alpha=0.9, ax=ax
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=graph.edges(),
        arrowstyle="-|>",
        arrowsize=20,
        edge_color="gray",
        alpha=0.7,
        ax=ax,
    )
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif", ax=ax)
    ax.set_title(title)


def display_graph(
    airports: list[str],
    routes: list[list[str]],
    connections: list[tuple[str, str]],
    filename: str,
) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "airports_connections_images"
    base_path.mkdir(parents=True, exist_ok=True)

    graph_original = build_graph(airports, routes)
    pos_original = nx.spring_layout(graph_original)

    graph_connections = build_graph(airports, routes)
    pos_connections = nx.spring_layout(graph_connections)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    draw_graph(graph_original, pos_original, "Original Graph", axes[0])
    draw_graph(graph_connections, pos_connections, "Connections Graph", axes[1])

    for connection in connections:
        graph_connections.add_edge(connection[0], connection[1])

    nx.draw_networkx_edges(
        graph_connections,
        pos_connections,
        edgelist=connections,
        arrowstyle="-|>",
        arrowsize=20,
        edge_color="red",
        alpha=0.7,
        style="dashed",
        ax=axes[1],
    )

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graph saved in {output_file}")


def test_airports_connections(visualize: bool) -> None:

    test_cases = load_test_cases("graphs/airports_connections.json")

    for idx, test in enumerate(test_cases):
        airports = test["airports"]
        routes = test["routes"]
        starting_airport = test["startingAirport"]
        expected = test["expected"]

        result = airport_connections(airports, routes, starting_airport)

        assert (
            len(result) == expected
        ), f"Test case failed {idx}. Expected: {expected}, got: {result}"

        if visualize:
            display_graph(airports, routes, result, f"result_airport_connections_{idx}")

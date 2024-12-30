import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from airport_connections.python.airport_connections import airport_connections


def load_test_cases() -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "graphs" / "airports_connections.json"
    if not json_path.exists():
        raise FileNotFoundError("File not found")

    with json_path.open("r") as file:
        return json.load(file)


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
    output_dir: str = "output_images",
) -> None:
    base_path = Path(__file__).parent / output_dir
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


def test_airports_connections() -> None:
    test_cases = load_test_cases()

    for idx, case in enumerate(test_cases):
        airports = case["airports"]
        routes = case["routes"]
        starting_airport = case["startingAirport"]
        expected = case["expected"]

        result = airport_connections(airports, routes, starting_airport)
        filename = f"test_case_{idx}"
        display_graph(airports, routes, result, filename)

        assert len(result) == expected, f"Test case {idx} failed"

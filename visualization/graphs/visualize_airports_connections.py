from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json


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
    root_dir = Path(__file__).parents[2] / "output_images"
    base_path = root_dir / "graphs" / "airports_connections"
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


def visualize_airports_connections(test_cases_file: str, results_file: str) -> None:
    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for idx, (test, result) in enumerate(zip(test_cases, results)):
        airports = test["airports"]
        routes = test["routes"]
        connections = result["connections"]

        filename = f"test_case_{idx}"
        display_graph(airports, routes, connections, filename)


def main():
    test_cases_file = "test_cases/graphs/airports_connections.json"
    results_file = "results/graphs/airports_connections.json"

    visualize_airports_connections(test_cases_file, results_file)


if __name__ == "__main__":
    main()

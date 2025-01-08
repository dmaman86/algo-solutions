from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import pytest

from problems.famous_algorithms.dijkstras_algorithm.python.dijkstras_algorithm import \
    dijkstra_algorithm
from tests.python.utility import load_test_cases


def draw_graph(
    graph: nx.DiGraph, title: str, color: str, edge_color: str, ax: plt.Axes
) -> None:
    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=color,
        node_size=700,
        edge_color=edge_color,
        linewidths=1,
        font_size=15,
        font_weight="bold",
        ax=ax,
    )
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, ax=ax)
    ax.set_title(title)


def plot_graphs(
    edges: list[list[tuple[int, int]]],
    previous: list[int],
    distances: list[int],
    filename: str,
) -> None:

    base_path = Path(__file__).parent
    base_path = base_path / "dijkstras_algorithm_images"
    base_path.mkdir(parents=True, exist_ok=True)

    G = nx.DiGraph()

    for u, neighbors in enumerate(edges):
        for edge in neighbors:
            if len(edge) != 2:
                continue
            v, weight = edge
            G.add_edge(u, v, weight=weight)

    G_min_paths = nx.DiGraph()

    for i in range(len(previous)):
        if previous[i] != -1:
            G_min_paths.add_edge(
                previous[i], i, weight=distances[i] - distances[previous[i]]
            )

    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    draw_graph(G, f"Original Graph for Test Case", "skyblue", "black", axs[0])
    draw_graph(G_min_paths, f"Minimum Paths for Test Case", "lightcoral", "red", axs[1])

    output_path = base_path / f"{filename}.png"
    plt.savefig(output_path, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graphs for test case saved to {output_path}")


def test_dijkstra_algorithm(visualize: bool) -> None:

    test_cases = load_test_cases("famous_algorithms/dijkstras_algorithm.json")

    for idx, test in enumerate(test_cases):
        start = test["start"]
        edges = test["edges"]
        expected = test["expected"]

        [distances, previous] = dijkstra_algorithm(start, edges)
        assert (
            distances == expected
        ), f"Test case failed at index {idx}! Expected: {expected}, got: {distances}"

        if visualize:
            plot_graphs(edges, previous, distances, f"result_case_dijsktra_{idx}")

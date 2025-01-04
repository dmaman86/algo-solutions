from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from dijkstras_algorithm.python.dijkstras_algorithm import dijkstra_algorithm
from utility import load_test_cases


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
    index: int,
    filename: str,
    output_dir: str = "output_images",
) -> None:

    base_path = Path(__file__).parent / output_dir
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
    draw_graph(G, f"Original Graph for Test Case {index}", "skyblue", "black", axs[0])
    draw_graph(
        G_min_paths, f"Minimum Paths for Test Case {index}", "lightcoral", "red", axs[1]
    )

    output_path = base_path / f"{filename}.png"
    plt.savefig(output_path, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graphs for test case {index} saved to {output_path}")


def test_dijkstra_algorithm() -> None:
    test_cases = load_test_cases("famous_algorithms/dijkstras_algorithm.json")

    for idx, case in enumerate(test_cases):
        start = case["start"]
        edges = case["edges"]
        expected = case["expected"]

        [distances, previous] = dijkstra_algorithm(start, edges)
        filename = f"test_case_{idx}"
        plot_graphs(edges, previous, distances, idx, filename)
        assert distances == expected, f"Test case {idx} failed for distances"

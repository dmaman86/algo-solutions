from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json


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
) -> None:

    base_path = Path(__file__).parents[2] / "output_images"
    base_path = base_path / "famous_algorithms" / "dijkstras_algorithm"
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


def visualize_graph(test_cases_file: str, results_file: str) -> None:

    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for idx, (test, result) in enumerate(zip(test_cases, results)):

        edges = test["edges"]
        distances = result["distances"]
        previous = result["previous"]

        filename = f"result_case_{idx}"
        plot_graphs(edges, previous, distances, idx, filename)


def main():
    test_cases_file = "test_cases/famous_algorithms/dijkstras_algorithm.json"
    results_file = "results/famous_algorithms/dijkstras_algorithm.json"

    visualize_graph(test_cases_file, results_file)


if __name__ == "__main__":
    main()

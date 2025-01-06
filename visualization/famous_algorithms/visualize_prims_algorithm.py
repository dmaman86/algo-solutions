from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json

AdjacencyList = list[list[list[int]]]


def buildGraph(adj_list: AdjacencyList) -> nx.Graph:
    graph = nx.Graph()
    for i, neighbors in enumerate(adj_list):
        for neighbor, weight in neighbors:
            graph.add_edge(i, neighbor, weight=weight)

    return graph


def drawGraph(graph: nx.Graph, pos: dict, title: str, color: str) -> None:
    nx.draw(graph, pos, with_labels=True, node_color=color, node_size=500, font_size=10)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)


def visualize_graph(
    edges: AdjacencyList,
    mst: AdjacencyList,
    filename: str,
) -> None:
    root_dir = Path(__file__).parents[2] / "output_images"
    base_path = root_dir / "famous_algorithms" / "prims_algorithm"
    base_path.mkdir(parents=True, exist_ok=True)

    original_graph = buildGraph(edges)
    mst_graph = buildGraph(mst)

    pos = nx.spring_layout(original_graph)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    drawGraph(original_graph, pos, "Original Graph", "lightblue")
    plt.subplot(122)
    drawGraph(mst_graph, pos, "Minimum Spanning Tree (MST)", "lightgreen")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graphs saved to {output_file}")


def visualize_prims_algorithm(test_cases_file: str, results_file: str) -> None:

    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for idx, (test, result) in enumerate(zip(test_cases, results)):
        edges: AdjacencyList = test["edges"]
        mst: AdjacencyList = result["mst"]

        filename = f"result_case_{idx}"
        visualize_graph(edges, mst, filename)


def main():
    test_cases_file = "test_cases/famous_algorithms/prims_algorithm.json"
    results_file = "results/famous_algorithms/prims_algorithm.json"

    visualize_prims_algorithm(test_cases_file, results_file)


if __name__ == "__main__":
    main()

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json

AdjacencyList = list[list[tuple[int, int]]]
Edge = tuple[int, int, int]
MSTResult = tuple[list[Edge], AdjacencyList]


def build_graph(adj_list: AdjacencyList) -> nx.Graph:
    graph = nx.Graph()
    for u in range(len(adj_list)):
        for v, w in adj_list[u]:
            if not graph.has_edge(u, v):
                graph.add_edge(u, v, weight=w)
    return graph


def draw_graph(graph: nx.Graph, pos: dict, title: str, color: str) -> None:
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=color,
        node_size=500,
        font_size=10,
    )
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)


def visualize_graph(
    edges: AdjacencyList,
    mst: AdjacencyList,
    filename: str,
) -> None:

    base_path = Path(__file__).parents[2] / "output_images"
    base_path = base_path / "famous_algorithms" / "kruskals_algorithm"
    base_path.mkdir(parents=True, exist_ok=True)

    original_graph = build_graph(edges)
    mst_graph = build_graph(mst)

    pos = nx.spring_layout(original_graph)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    draw_graph(original_graph, pos, "Original Graph", "lightblue")

    plt.subplot(122)
    draw_graph(mst_graph, pos, "Minimum Spanning Tree (MST)", "lightgreen")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graphs saved to: {output_file}")


def visualize_kruskal_graph(test_cases_file: str, results_file: str) -> None:

    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for idx, (test, result) in enumerate(zip(test_cases, results)):
        edges: AdjacencyList = test["edges"]
        mst = result["mst"]
        filename = f"test_case_{idx}"
        visualize_graph(edges, mst, filename)


def main():
    test_cases_file = "test_cases/famous_algorithms/kruskals_algorithm.json"
    results_file = "results/famous_algorithms/kruskals_algorithm.json"

    visualize_kruskal_graph(test_cases_file, results_file)


if __name__ == "__main__":
    main()

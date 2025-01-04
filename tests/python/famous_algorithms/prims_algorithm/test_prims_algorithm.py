from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from prims_algorithm.python.prims_algorithm import primsAlgorithm
from utility import load_test_cases

AdjacencyList = list[list[list[int]]]


def are_permutations(list1: AdjacencyList, list2: AdjacencyList) -> bool:
    if len(list1) != len(list2):
        return False

    sorted_list1 = sorted([sorted(sublist) for sublist in list1])
    sorted_list2 = sorted([sorted(sublist) for sublist in list2])
    return sorted_list1 == sorted_list2


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
    output_dir: str = "output_images",
) -> None:
    base_path = Path(__file__).parent / output_dir
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


def test_prims_algorithm() -> None:

    test_cases = load_test_cases("famous_algorithms/prims_algorithm.json")

    for idx, case in enumerate(test_cases):
        edges: AdjacencyList = case["edges"]
        expected: AdjacencyList = case["expected"]

        result: AdjacencyList = primsAlgorithm(edges)
        filename = f"test_case_{idx}"
        visualize_graph(edges, result, filename)
        assert are_permutations(expected, result), f"Test case {idx + 1} failed"

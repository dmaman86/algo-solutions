import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from kruskals_algorithm.python.kruskal_algorithm import kruskalsAlgorithm

AdjacencyList = list[list[tuple[int, int]]]
Edge = tuple[int, int, int]
MSTResult = tuple[list[Edge], AdjacencyList]


def load_test_cases(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "famous_algorithms" / filename
    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    with json_path.open("r") as file:
        return json.load(file)


def are_permutations(list1: AdjacencyList, list2: AdjacencyList) -> bool:
    if len(list1) != len(list2):
        return False

    sorted_list1 = sorted([sorted(sublist) for sublist in list1])
    sorted_list2 = sorted([sorted(sublist) for sublist in list2])
    return sorted_list1 == sorted_list2


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
    output_dir: str = "output_images",
) -> None:

    base_path = Path(__file__).parent / output_dir
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


def test_kruskal_algorithm() -> None:

    test_cases = load_test_cases("kruskals_algorithm.json")

    for idx, case in enumerate(test_cases):
        edges: AdjacencyList = case["edges"]
        expected: AdjacencyList = case["expected"]
        [mst_edges, mst] = kruskalsAlgorithm(edges)

        mst_as_lists = [[list(edge) for edge in sublist] for sublist in mst]

        filename = f"test_case_{idx}"
        visualize_graph(edges, mst, filename)
        assert are_permutations(mst_as_lists, expected), (
            f"Test case failed at index {idx}\n" f"Expected: {expected}\n" f"Got: {mst}"
        )

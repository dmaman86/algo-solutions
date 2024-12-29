import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from topological_sort.python.topological_sort import topological_sort


def load_test_cases(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "famous_algorithms" / filename

    if not json_path.exists():
        raise FileNotFoundError(f"{json_path} not found.")

    with json_path.open() as file:
        return json.load(file)


def buildGraph(graph: dict[int, list[int]], jobs: list[int]) -> nx.DiGraph:
    G = nx.DiGraph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    for job in jobs:
        if job not in G:
            G.add_node(job)

    return G


def drawGraph(graph: nx.DiGraph, pos: dict, title: str, ax) -> None:
    nx.draw(
        graph,
        pos,
        ax=ax,
        with_labels=True,
        node_size=500,
        node_color="skyblue",
        font_size=16,
        font_color="black",
        font_weight="bold",
        arrowsize=20,
        arrowstyle="->",
        edge_color="gray",
        arrows=True,
    )
    ax.set_title(title, fontsize=14)


def visualizeGraph(
    jobs: list[int],
    graph: dict[int, list[int]],
    sorted_job: list[int],
    index: int,
    filename: str,
    output_dir: str = "output_images",
) -> None:
    base_path = Path(__file__).parent / output_dir
    base_path.mkdir(parents=True, exist_ok=True)

    original_graph = buildGraph(graph, jobs)
    pos_original = nx.spring_layout(original_graph)

    pos_topological = (
        {node: (i, 0) for i, node in enumerate(sorted_job)} if sorted_job else {}
    )
    topological_graph = buildGraph(graph, jobs) if sorted_job else nx.DiGraph()

    plt.figure(figsize=(12, 6))
    ax1 = plt.subplot(121)
    drawGraph(original_graph, pos_original, "Original Graph", ax1)
    ax2 = plt.subplot(122)
    drawGraph(topological_graph, pos_topological, "Topological Order", ax2)

    plt.suptitle(f"Test Case {index}: {sorted_job}", fontsize=16)
    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Saved {output_file}")


def test_topological_sort() -> None:
    test_cases = load_test_cases("topological_sort.json")

    for idx, test_case in enumerate(test_cases):
        jobs = test_case["jobs"]
        deps = test_case["deps"]
        expected = test_case["expected"]

        [result, graph] = topological_sort(jobs, deps)

        filename = f"topological_sort_{idx}"
        visualizeGraph(jobs, graph, result, idx, filename)
        assert Counter(result) == Counter(
            expected
        ), f"Test case {idx} failed: {result=}, {expected=}"

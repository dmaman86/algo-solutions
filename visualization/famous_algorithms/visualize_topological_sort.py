from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json


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
) -> None:
    root_dir = Path(__file__).parents[2] / "output_images"
    base_path = root_dir / "famous_algorithms" / "topological_sort"
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


def visualize_topological_sort(test_cases_file: str, results_file: str) -> None:
    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for idx, (test, result) in enumerate(zip(test_cases, results)):
        jobs = test["jobs"]
        graph = result["graph"]
        new_graph = {int(k): v for k, v in graph.items()}
        sorted_jobs = result["sorted_jobs"]

        filename = f"topological_sort_{idx}"
        visualizeGraph(jobs, new_graph, sorted_jobs, idx, filename)


def main():
    test_cases_file = "test_cases/famous_algorithms/topological_sort.json"
    results_file = "results/famous_algorithms/topological_sort.json"

    visualize_topological_sort(test_cases_file, results_file)


if __name__ == "__main__":
    main()

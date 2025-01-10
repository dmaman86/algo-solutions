from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from problems.graphs.cycle_in_graph.python.cycle_in_graph import cycleInGraph
from tests.python.utility import load_test_cases


def display_graph(edges: list[list[int]], filename: str) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "cycle_in_graph_images"
    base_path.mkdir(parents=True, exist_ok=True)

    edges_list = [
        (i, neighbor) for i, neighbors in enumerate(edges) for neighbor in neighbors
    ]

    G = nx.DiGraph()
    G.add_edges_from(edges_list)

    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=20,
        font_weight="bold",
        arrows=True,
    )

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Graph saved to {output_file}")


def test_cycle_in_graph(visualize: bool) -> None:
    test_cases = load_test_cases("graphs/cycle_in_graph.json")

    for idx, test in enumerate(test_cases):
        edges = test["edges"]
        expected = test["expected"]

        result = cycleInGraph(edges)

        assert result == expected, f"Test case {idx} failed!"

        if visualize:
            display_graph(edges, f"graph_{idx}")

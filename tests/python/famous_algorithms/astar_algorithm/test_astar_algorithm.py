from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import pytest

from problems.famous_algorithms.astar_algorithm.python.astar_algorithm import \
    aStarAlgorithm
from tests.python.utility import load_test_cases


def create_graph_from_matrix(matrix: list[list[int]]) -> nx.Graph:
    G = nx.Graph()
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                G.add_node((row, col))
                if row > 0 and matrix[row - 1][col] == 0:
                    G.add_edge((row, col), (row - 1, col))
                if row < rows - 1 and matrix[row + 1][col] == 0:
                    G.add_edge((row, col), (row + 1, col))
                if col > 0 and matrix[row][col - 1] == 0:
                    G.add_edge((row, col), (row, col - 1))
                if col < cols - 1 and matrix[row][col + 1] == 0:
                    G.add_edge((row, col), (row, col + 1))

    return G


def draw_graph(
    graph: nx.Graph,
    filename: str,
    path: list[list[int]] | None = None,
) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "astar_algorithm_images"
    base_path.mkdir(parents=True, exist_ok=True)

    pos = {node: (node[1], -node[0]) for node in graph.nodes()}
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=500,
        font_size=10,
        node_color="lightblue",
        font_weight="bold",
    )

    if path:
        edges_in_path = [
            ((path[i][0], path[i][1]), (path[i + 1][0], path[i + 1][1]))
            for i in range(len(path) - 1)
        ]
        nx.draw_networkx_edges(
            graph, pos, edgelist=edges_in_path, edge_color="r", width=2
        )

    plt.gca().invert_yaxis()
    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()


def test_astar_algorithm(visualize: bool) -> None:

    test_cases = load_test_cases("famous_algorithms/astar_algorithm.json")

    for idx, test in enumerate(test_cases):
        startRow = test["startRow"]
        startCol = test["startCol"]
        endRow = test["endRow"]
        endCol = test["endCol"]
        graph = test["graph"]
        expected = test["expected"]
        path = aStarAlgorithm(startRow, startCol, endRow, endCol, graph)

        assert (
            path == expected
        ), f"Test case failed at index: {idx}! Expected: {expected}, got: {path}"

        if visualize:
            G = create_graph_from_matrix(graph)
            draw_graph(G, f"astar_algorithm_result_{idx}", path)

import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from astar_algorithm.python.astar_algorithm import aStarAlgorithm


def load_test_cases(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "famous_algorithms" / filename

    if not json_path.exists():
        raise FileNotFoundError(f"{json_path} not found.")

    with json_path.open() as file:
        return json.load(file)


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
    output_dir: str = "output_images",
) -> None:
    base_path = Path(__file__).parent / output_dir
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


def test_astar_algorithm() -> None:
    test_cases = load_test_cases("astar_algorithm.json")

    for idx, test in enumerate(test_cases):
        startRow = test["startRow"]
        startCol = test["startCol"]
        endRow = test["endRow"]
        endCol = test["endCol"]
        graph = test["graph"]
        G = create_graph_from_matrix(graph)
        filename = f"astar_algorithm_{idx}"
        path = aStarAlgorithm(startRow, startCol, endRow, endCol, graph)
        draw_graph(G, filename, path)
        assert path == test["expected"], f"Test case {idx} failed"

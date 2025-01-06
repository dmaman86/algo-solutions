from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from visualization.utility import load_json


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
    root_dir = Path(__file__).resolve().parents[2] / "output_images"
    base_path = root_dir / "famous_algorithms" / "astar_algorithm"
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


def visualize_graph(test_cases_file: str, results_file: str) -> None:
    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for i, (test_case, result) in enumerate(zip(test_cases, results)):
        original_graph = test_case["graph"]
        result_path = result["path"]

        graph = create_graph_from_matrix(original_graph)
        filename = f"astar_algorithm_result_{i}"
        draw_graph(graph, filename, result_path)


def main():
    test_cases_file = "test_cases/famous_algorithms/astar_algorithm.json"
    results_file = "results/famous_algorithms/astar_algorithm.json"

    visualize_graph(test_cases_file, results_file)


if __name__ == "__main__":
    main()

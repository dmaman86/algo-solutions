from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_search_trees.right_smaller_than.python.right_smaller_than import (
    BST, Node, right_smaller_than)
from tests.python.utility import load_test_cases


def add_nodes_edges(node: Node, graph: graphviz.Digraph, parent: Node = None) -> None:
    if node:
        node_label = f"{node.value}\n (left_size: {node.left_size})"
        graph.node(str(id(node)), node_label)

        if parent:
            graph.edge(str(id(parent)), str(id(node)))

        add_nodes_edges(node.left, graph, node)
        add_nodes_edges(node.right, graph, node)


def graphviz_to_image(graph: graphviz.Digraph) -> None:
    image_data = BytesIO(graph.pipe(format="png"))
    return plt.imread(image_data, format="png")


def visualize_bst(bst: BST, filename: str) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "right_smaller_than_images"
    base_path.mkdir(parents=True, exist_ok=True)

    graph = graphviz.Digraph(format="png")
    add_nodes_edges(bst.root, graph)

    result_img = graphviz_to_image(graph)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(result_img)
    ax.axis("off")
    ax.set_title("Binary Search Tree")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, bbox_inches="tight", format="png")
    plt.close()


def test_right_smaller_than(visualize: bool) -> None:
    test_cases = load_test_cases("binary_search_trees/right_smaller_than.json")

    for idx, test in enumerate(test_cases):
        array = test["array"]
        expected = test["expected"]

        result, bst = right_smaller_than(array)

        assert result == expected, f"Test case {idx} failed"

        if visualize:
            visualize_bst(bst, f"right_smaller_than_{idx}")

import copy
from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_trees.compare_leaf_traversal.python.compare_leaf_traversal import (
    BinaryTree, compareLeafTraversal)
from tests.python.utility import load_test_cases


def build_bt(nodes: list[dict], root_id: str) -> BinaryTree:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BinaryTree(node["value"])

    for node in nodes:
        bt_node = id_to_node[node["id"]]
        bt_node.left = id_to_node.get(node["left"])
        bt_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]


def generate_dot(
    bt_root: BinaryTree, dot: graphviz.Digraph = None, label: str = ""
) -> graphviz.Digraph:
    if dot is None:
        dot = graphviz.Digraph()

    if bt_root:
        dot.node(str(bt_root.value))
        if bt_root.left:
            dot.edge(str(bt_root.value), str(bt_root.left.value))
            generate_dot(bt_root.left, dot)
        if bt_root.right:
            dot.edge(str(bt_root.value), str(bt_root.right.value))
            generate_dot(bt_root.right, dot)

    return dot


def graphviz_to_image(dot_graph: graphviz.Digraph) -> None:
    image_data = BytesIO(dot_graph.pipe(format="png"))
    return plt.imread(image_data, format="png")


def visualize_bt(root1: BinaryTree, root2: BinaryTree, filename: str) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "compare_leaf_traversal_images"
    base_path.mkdir(parents=True, exist_ok=True)

    first_dot = generate_dot(root1, label="Tree 1")
    second_dot = generate_dot(root2, label="Tree 2")

    first_img = graphviz_to_image(first_dot)
    second_img = graphviz_to_image(second_dot)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(first_img)
    axes[0].axis("off")
    axes[0].set_title("Tree 1")

    axes[1].imshow(second_img)
    axes[1].axis("off")
    axes[1].set_title("Tree 2")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, bbox_inches="tight", format="png")
    plt.close()
    print(f"Saved visualization to {output_file}")


def test_compare_leaf_traversal(visualize: bool) -> None:

    test_cases = load_test_cases("binary_trees/compare_leaf_traversal.json")

    for idx, test in enumerate(test_cases):
        tree1 = test["tree1"]
        tree2 = test["tree2"]
        expected = test["expected"]

        bt1 = build_bt(tree1["nodes"], tree1["root"])
        bt2 = build_bt(tree2["nodes"], tree2["root"])

        result = compareLeafTraversal(bt1, bt2)

        assert result == expected, f"Test case {idx} failed"

        if visualize:
            visualize_bt(bt1, bt2, f"test_case_{idx}")

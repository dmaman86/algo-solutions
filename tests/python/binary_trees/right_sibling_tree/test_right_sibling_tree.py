import copy
from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_trees.right_sibling_tree.python.right_sibling_tree import (
    BinaryTree, rightSiblingTree)
from tests.python.utility import load_test_cases


def build_bt(nodes: list[dict], root_id: str) -> BinaryTree:
    id_to_node: dict[str, BinaryTree] = {}

    for node in nodes:
        id_to_node[node["id"]] = BinaryTree(node["value"])

    for node in nodes:
        bt_node = id_to_node[node["id"]]
        bt_node.left = id_to_node.get(node["left"])
        bt_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]


def are_equals_bt(bt1: BinaryTree, bt2: BinaryTree) -> bool:
    if not bt1 and not bt2:
        return True

    if not bt1 or not bt2 or bt1.value != bt2.value:
        return False

    return are_equals_bt(bt1.left, bt2.left) and are_equals_bt(bt1.right, bt2.right)


def generate_dot(
    bt_root: BinaryTree, dot: graphviz.Digraph = None, label: str = ""
) -> graphviz.Digraph:
    if dot is None:
        dot = graphviz.Digraph(comment=label)

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


def visualize_dot(
    original_bt: BinaryTree, result_bt: BinaryTree, filename: str
) -> None:

    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "right_sibling_tree_images"
    base_path.mkdir(parents=True, exist_ok=True)

    original_dot = generate_dot(original_bt, label="Original BT")
    result_dot = generate_dot(result_bt, label="Right Sibling BT")

    original_img = graphviz_to_image(original_dot)
    result_img = graphviz_to_image(result_dot)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(original_img)
    axes[0].axis("off")
    axes[0].set_title("Original BT")

    axes[1].imshow(result_img)
    axes[1].axis("off")
    axes[1].set_title("Right Sibling BT")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Saved to {output_file}")


def test_right_sibling_tree(visualize: bool) -> None:
    test_cases = load_test_cases("binary_trees/right_sibling_tree.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        expected = test["expected"]

        bt_root = build_bt(tree["nodes"], tree["root"])
        original_bt_root = copy.deepcopy(bt_root)
        bt_expected = build_bt(expected["nodes"], expected["root"])

        result = rightSiblingTree(bt_root)

        assert are_equals_bt(result, bt_expected), f"Test case {idx} failed"

        if visualize:
            visualize_dot(original_bt_root, result, f"right_sibling_tree_{idx}")

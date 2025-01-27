from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_trees.assets.BinaryTree import BinaryTree
from problems.binary_trees.max_path_sum_in_bt.python.max_path_sum_in_bt import \
    maxPathSum
from tests.python.binary_trees.utility import build_bt
from tests.python.utility import load_test_cases


def generate_dot(
    node: BinaryTree,
    dot: graphviz.Digraph = None,
    label: str = "",
    path_nodes: list[BinaryTree] = None,
) -> graphviz.Digraph:
    if dot is None:
        dot = graphviz.Digraph(comment=label)

    if node:
        is_in_path = path_nodes and any(path_node is node for path_node in path_nodes)
        node_color = "red" if is_in_path else "black"

        dot.node(str(id(node)), str(node.value), color=node_color)

        for child in (node.left, node.right):
            if child:
                dot.edge(str(id(node)), str(id(child)))
                generate_dot(child, dot, label, path_nodes)

    return dot


def graphviz_to_image(dot_graph: graphviz.Digraph) -> None:
    image_data = BytesIO(dot_graph.pipe(format="png"))
    return plt.imread(image_data, format="png")


def print_path(path: list[BinaryTree]) -> str:
    return " -> ".join(str(node.value) for node in path)


def visualize_tree(
    tree: BinaryTree, path_nodes: list[BinaryTree], maxValue: int, filename: str
) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "max_path_sum_in_bt_images"
    base_path.mkdir(parents=True, exist_ok=True)

    original_dot = generate_dot(tree, label="Original Tree")
    path_dot = generate_dot(tree, label="Path Tree", path_nodes=path_nodes)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(graphviz_to_image(original_dot))
    axes[0].axis("off")
    axes[0].set_title("Original BT")

    axes[1].imshow(graphviz_to_image(path_dot))
    axes[1].axis("off")
    axes[1].set_title(f"Path BT: {print_path(path_nodes)}, Max Value: {maxValue}")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Tree visualization saved at {output_file}")


def test_max_path_sum_in_bt(visualize: bool) -> None:
    test_cases = load_test_cases("binary_trees/max_path_sum_in_bt.json")

    for idx, test in enumerate(test_cases):
        tree: dict = test["tree"]
        expected: int = test["expected"]

        bt_root: BinaryTree = build_bt(tree["nodes"], tree["root"])

        result, path = maxPathSum(bt_root)

        assert result == expected, f"Test case {idx} failed"

        if visualize:
            visualize_tree(bt_root, path, result, f"max_path_sum_{idx}")

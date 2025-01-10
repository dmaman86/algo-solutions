import copy
from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_search_trees.repair_bst.python.repair_bst import (
    BST, repair_bst)
from tests.python.utility import load_test_cases


def build_bst(nodes: list[dict], root_id: str) -> BST:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BST(node["value"])

    for node in nodes:
        bst_node = id_to_node[node["id"]]
        bst_node.left = id_to_node.get(node["left"])
        bst_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]


def are_bsts_equal(bst1: BST, bst2: BST) -> bool:
    if not bst1 and not bst2:
        return True
    if not bst1 or not bst2 or bst1.value != bst2.value:
        return False
    return are_bsts_equal(bst1.left, bst2.left) and are_bsts_equal(
        bst1.right, bst2.right
    )


def generate_dot(
    bst_root: BST, dot: graphviz.Digraph = None, label: str = ""
) -> graphviz.Digraph:
    if dot is None:
        dot = graphviz.Digraph(comment=label)

    if bst_root:
        dot.node(str(bst_root.value))
        if bst_root.left:
            dot.edge(str(bst_root.value), str(bst_root.left.value))
            generate_dot(bst_root.left, dot)
        if bst_root.right:
            dot.edge(str(bst_root.value), str(bst_root.right.value))
            generate_dot(bst_root.right, dot)

    return dot


def graphviz_to_image(dot_graph: graphviz.Digraph) -> None:
    image_data = BytesIO(dot_graph.pipe(format="png"))
    return plt.imread(image_data, format="png")


def visualize_dot(original_bst: BST, result_bst: BST, filename: str) -> None:

    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "repair_bst_images"
    base_path.mkdir(parents=True, exist_ok=True)

    original_dot = generate_dot(original_bst, label="Original BST")
    result_dot = generate_dot(result_bst, label="Repaired BST")

    original_img = graphviz_to_image(original_dot)
    result_img = graphviz_to_image(result_dot)

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(original_img)
    axes[0].axis("off")
    axes[0].set_title("Original BST")

    axes[1].imshow(result_img)
    axes[1].axis("off")
    axes[1].set_title("Repaired BST")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Saved to {output_file}")


def test_repair_bst(visualize: bool) -> None:

    test_cases = load_test_cases("binary_search_trees/repair_bst.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        nodes = tree["nodes"]
        root_id = tree["root"]
        bst = build_bst(nodes, root_id)
        original_bst = copy.deepcopy(bst)
        result = repair_bst(bst)

        expected_bst = build_bst(test["expected"]["nodes"], test["expected"]["root"])

        assert are_bsts_equal(
            result, expected_bst
        ), f"Test case {idx} failed. Expected: {expected_bst}, got: {result}"

        if visualize:
            visualize_dot(original_bst, result, f"test_case_{idx}")

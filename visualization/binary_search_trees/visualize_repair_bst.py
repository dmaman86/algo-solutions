from io import BytesIO
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt

from problems.binary_search_trees.repair_bst.python.repair_bst import BST
from visualization.utility import load_json


def build_bst(nodes: list[dict], root_id: str) -> BST:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BST(node["value"])

    for node in nodes:
        bst_node = id_to_node[node["id"]]
        bst_node.left = id_to_node.get(node["left"])
        bst_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]


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


def visualize_dot(
    original_bst: BST, result_bst: BST, filename: str, output_dir: str
) -> None:

    root_dir = Path(__file__).resolve().parents[2] / "output_images"
    base_path = root_dir / "binary_search_trees" / "repair_bst"
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


def visualize_repair_bst(
    test_cases_file: str, results_file: str, output_dir: str
) -> None:
    test_cases = load_json(test_cases_file)
    results = load_json(results_file)

    for i, (test_case, result) in enumerate(zip(test_cases, results)):
        original_tree = test_case["tree"]
        repaired_tree = result["tree"]

        original_bst = build_bst(original_tree["nodes"], original_tree["root"])
        repaired_bst = build_bst(repaired_tree["nodes"], repaired_tree["root"])

        filename = f"repair_bst_result_{i}"
        visualize_dot(original_bst, repaired_bst, filename, output_dir)


def main():
    test_cases_file = "test_cases/binary_search_trees/repair_bst.json"
    results_file = "results/binary_search_trees/repair_bst.json"
    output_dir = "binary_search_trees/repair_bst/"

    visualize_repair_bst(test_cases_file, results_file, output_dir)


if __name__ == "__main__":
    main()

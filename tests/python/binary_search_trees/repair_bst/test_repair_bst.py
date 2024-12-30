import json
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from repair_bst.python.repair_bst import BST, repair_bst


def load_test_cases() -> list[dict]:
    root_dir = Path(__file__).resolve().parents[3]
    json_path = root_dir / "test_cases" / "binary_search_trees" / "repair_bst.json"
    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    with json_path.open("r") as file:
        return json.load(file)


def build_bst(nodes: list[dict], root_id: str) -> BST:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BST(node["value"])

    for node in nodes:
        bst_node = id_to_node[node["id"]]
        bst_node.left = id_to_node.get(node["left"])
        bst_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]


def bst_to_dict(bst_root: BST) -> dict:
    result: dict = {"nodes": [], "root": str(bst_root.value)}

    def traverse(node: BST | None) -> None:
        if node:
            result["nodes"].append(
                {
                    "id": str(node.value),
                    "value": node.value,
                    "left": str(node.left.value) if node.left else None,
                    "right": str(node.right.value) if node.right else None,
                }
            )
            traverse(node.left)
            traverse(node.right)

    traverse(bst_root)
    return result


def are_bsts_equal(bst1: BST, bst2: BST) -> bool:
    if not bst1 and not bst2:
        return True
    if not bst1 or not bst2 or bst1.value != bst2.value:
        return False
    return are_bsts_equal(bst1.left, bst2.left) and are_bsts_equal(
        bst1.right, bst2.right
    )


def bst_to_networkx(bst_root: BST, graph: nx.DiGraph = None) -> nx.DiGraph:
    if graph is None:
        graph = nx.DiGraph()

    if bst_root:
        graph.add_node(str(bst_root.value), label=str(bst_root.value))
        if bst_root.left:
            graph.add_edge(str(bst_root.value), str(bst_root.left.value))
            bst_to_networkx(bst_root.left, graph)
        if bst_root.right:
            graph.add_edge(str(bst_root.value), str(bst_root.right.value))
            bst_to_networkx(bst_root.right, graph)

    return graph


def visualize_bst(
    original_bst: BST, result_bst: BST, filename: str, output_dir: str = "output_images"
) -> None:
    base_path = Path(__file__).parent / output_dir
    base_path.mkdir(parents=True, exist_ok=True)

    original_graph = bst_to_networkx(original_bst)
    result_graph = bst_to_networkx(result_bst)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    nx.draw(
        original_graph,
        nx.spring_layout(original_graph),
        with_labels=True,
        ax=axes[0],
        node_size=500,
        node_color="lightblue",
    )
    axes[0].set_title("Original BST")

    nx.draw(
        result_graph,
        nx.spring_layout(result_graph),
        with_labels=True,
        ax=axes[1],
        node_size=500,
        node_color="lightgreen",
    )
    axes[1].set_title("Repaired BST")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()


def test_repair_bst() -> None:
    test_cases = load_test_cases()

    for idx, case in enumerate(test_cases):
        tree = case["tree"]
        nodes = tree["nodes"]
        root_id = tree["root"]
        bst = build_bst(nodes, root_id)

        result = repair_bst(bst)

        expected_bst = build_bst(case["expected"]["nodes"], case["expected"]["root"])
        filename = f"test_case_{idx + 1}"
        visualize_bst(bst, result, filename)
        assert are_bsts_equal(result, expected_bst), f"Test case {idx + 1} failed"

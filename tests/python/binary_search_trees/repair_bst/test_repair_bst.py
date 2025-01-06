import argparse

from problems.binary_search_trees.repair_bst.python.repair_bst import (
    BST, repair_bst)
from tests.python.utility import load_test_cases, save_results


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


def bst_to_dict(bst: BST) -> dict:
    result: dict = {"nodes": [], "root": str(bst.value)}

    def traverse(node: BST):
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

    traverse(bst)
    return {"tree": result}


def test_repair_bst(save_results_flag: bool = False) -> None:
    test_cases = load_test_cases("binary_search_trees/repair_bst.json")
    results: list[dict] = []

    for idx, case in enumerate(test_cases):
        tree = case["tree"]
        nodes = tree["nodes"]
        root_id = tree["root"]
        bst = build_bst(nodes, root_id)

        result = repair_bst(bst)

        if save_results_flag:
            results.append(bst_to_dict(result))

        expected_bst = build_bst(case["expected"]["nodes"], case["expected"]["root"])
        assert are_bsts_equal(result, expected_bst), f"Test case {idx + 1} failed"

    if save_results_flag:
        save_results("binary_search_trees/repair_bst.json", results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test repair_bst")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save the results of the test cases to a JSON file.",
    )
    args = parser.parse_args()

    test_repair_bst(save_results_flag=args.save_results)

from problems.binary_trees.flatten_binary_tree.python.flatten_binary_tree import (
    BinaryTree, flattenBinaryTree)
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


def are_bts_equal(
    bt1: BinaryTree, bt2: BinaryTree, visited: set[BinaryTree] = None
) -> bool:
    if visited is None:
        visited = set()

    if not bt1 and not bt2:
        return True

    if not bt1 or not bt2 or bt1.value != bt2.value:
        return False

    if bt1 in visited or bt2 in visited:
        return True

    visited.add(bt1)
    visited.add(bt2)

    return are_bts_equal(bt1.left, bt2.left, visited) and are_bts_equal(
        bt1.right, bt2.right, visited
    )


def test_flatten_binary_tree() -> None:
    test_cases = load_test_cases("binary_trees/flatten_binary_tree.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        expected = test["expected"]

        bt_root = build_bt(tree["nodes"], tree["root"])
        bt_expected = build_bt(expected["nodes"], expected["root"])

        result = flattenBinaryTree(bt_root)

        assert are_bts_equal(result, bt_expected), f"Test case {idx} failed"

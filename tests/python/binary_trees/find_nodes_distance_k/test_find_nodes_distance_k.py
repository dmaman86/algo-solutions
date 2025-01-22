from problems.binary_trees.find_nodes_distance_k.python.find_nodes_distance_k import (
    BinaryTree, findNodesDistanceK)
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


def test_find_nodes_distance_k() -> None:
    test_cases = load_test_cases("binary_trees/find_nodes_distance_k.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        target = test["target"]
        k = test["k"]
        root = build_bt(tree["nodes"], tree["root"])
        expected = test["expected"]

        result = findNodesDistanceK(root, target, k)

        assert (
            result.sort() == expected.sort()
        ), f"Test case {idx} failed: expected {expected}, got {result}"

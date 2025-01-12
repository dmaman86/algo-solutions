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

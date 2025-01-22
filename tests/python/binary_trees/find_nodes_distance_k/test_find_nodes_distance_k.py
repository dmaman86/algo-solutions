from problems.binary_trees.assets.BinaryTree import BinaryTree
from problems.binary_trees.find_nodes_distance_k.python.find_nodes_distance_k import \
    findNodesDistanceK
from tests.python.binary_trees.utility import build_bt
from tests.python.utility import load_test_cases


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

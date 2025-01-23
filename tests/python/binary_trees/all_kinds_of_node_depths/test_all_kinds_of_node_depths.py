from problems.binary_trees.all_kinds_of_node_depths.python.all_kinds_of_node_depths import \
    allKindsOfNodeDepths
from problems.binary_trees.assets.BinaryTree import BinaryTree
from tests.python.binary_trees.utility import build_bt
from tests.python.utility import load_test_cases


def test_all_kinds_of_node_depths() -> None:

    test_cases = load_test_cases("binary_trees/all_kinds_of_node_depths.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        expected = test["expected"]

        root: BinaryTree = build_bt(tree["nodes"], tree["root"])

        result = allKindsOfNodeDepths(root)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

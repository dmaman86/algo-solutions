from problems.binary_search_trees.assets.BST import BST
from problems.binary_search_trees.validate_three_nodes.python.validate_three_nodes import \
    validateThreeNodes
from tests.python.binary_search_trees.utility import build_bst
from tests.python.utility import load_test_cases


def find_node(root: BST, targetValue: int) -> BST:
    if not root:
        return None
    if root.value == targetValue:
        return root
    nextNode = root.right if targetValue > root.value else root.left
    return find_node(nextNode, targetValue)


def test_validate_three_nodes() -> None:
    test_cases = load_test_cases("binary_search_trees/validate_three_nodes.json")

    for idx, test in enumerate(test_cases):
        tree = test["tree"]
        root = build_bst(tree["nodes"], tree["root"])

        nodeOne = find_node(root, int(test["nodeOne"]))
        nodeTwo = find_node(root, int(test["nodeTwo"]))
        nodeThree = find_node(root, int(test["nodeThree"]))

        expected = test["expected"]
        result = validateThreeNodes(nodeOne, nodeTwo, nodeThree)

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"

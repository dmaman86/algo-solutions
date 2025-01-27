from problems.graphs.youngest_common_ancestor.python.youngest_common_ancestor import (
    AncestralTree, getYoungestCommonAncestor)
from tests.python.utility import load_test_cases


def build_map(tree_json: dict) -> dict:
    nodes = tree_json["nodes"]
    node_map = {}

    for node in nodes:
        name = node["name"]
        node_map[name] = AncestralTree(name)

    for node in nodes:
        name = node["name"]
        ancestor_name = node.get("ancestor")
        if ancestor_name:
            ancestor_node = node_map[ancestor_name]
            descendant_node = node_map[name]
            ancestor_node.add_as_ancestor([descendant_node])

    return node_map


def find_node(node_map: dict, target_name: str) -> AncestralTree:
    return node_map.get(target_name)


def test_youngest_common_ancestor() -> None:

    test_cases = load_test_cases("graphs/youngest_common_ancestor.json")

    for idx, test in enumerate(test_cases):
        ancestral_tree = test["ancestralTree"]
        top_ancestor = test["topAncestor"]
        descendant_one = test["descendantOne"]
        descendant_two = test["descendantTwo"]

        node_map = build_map(ancestral_tree)
        top_ancestor_node = find_node(node_map, top_ancestor)
        descendant_one_node = find_node(node_map, descendant_one)
        descendant_two_node = find_node(node_map, descendant_two)

        result = getYoungestCommonAncestor(
            top_ancestor_node, descendant_one_node, descendant_two_node
        )

        assert result.name == test["expected"]["nodeId"], f"Test case {idx} failed"

from problems.binary_search_trees.assets.BST import BST


def build_bst(nodes: list[dict], root_id: str) -> BST:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BST(node["value"])

    for node in nodes:
        bst_node = id_to_node[node["id"]]
        bst_node.left = id_to_node.get(node["left"])
        bst_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]

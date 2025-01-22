from problems.binary_trees.assets.BinaryTree import BinaryTree


def build_bt(nodes: list[dict], root_id: str) -> BinaryTree:
    id_to_node = {}

    for node in nodes:
        id_to_node[node["id"]] = BinaryTree(node["value"])

    for node in nodes:
        bt_node = id_to_node[node["id"]]
        bt_node.left = id_to_node.get(node["left"])
        bt_node.right = id_to_node.get(node["right"])

    return id_to_node[root_id]

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def collect_leaf_nodes(root: BinaryTree, stored_leaf: list) -> None:
    if root is None:
        return

    if root.left is None and root.right is None:
        stored_leaf.append(root.value)

    collect_leaf_nodes(root.left, stored_leaf)
    collect_leaf_nodes(root.right, stored_leaf)


def compareLeafTraversal(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    leaf_tree1: list = []
    leaf_tree2: list = []

    collect_leaf_nodes(tree1, leaf_tree1)
    collect_leaf_nodes(tree2, leaf_tree2)

    return leaf_tree1 == leaf_tree2

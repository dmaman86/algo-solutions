from problems.binary_trees.assets.BinaryTree import BinaryTree


def compareLeafTraversal(tree1: BinaryTree, tree2: BinaryTree) -> bool:

    def collect_leaf_nodes(root: BinaryTree, stored_leaf: list = None) -> list:
        if stored_leaf is None:
            stored_leaf = []

        if root is None:
            return stored_leaf

        if root.left is None and root.right is None:
            stored_leaf.append(root.value)

        collect_leaf_nodes(root.left, stored_leaf)
        collect_leaf_nodes(root.right, stored_leaf)

        return stored_leaf

    leaf_tree1 = collect_leaf_nodes(tree1)
    leaf_tree2 = collect_leaf_nodes(tree2)

    return leaf_tree1 == leaf_tree2

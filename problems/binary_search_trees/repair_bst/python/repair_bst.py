from problems.binary_search_trees.assets.BST import BST


def repair_bst(tree: BST) -> BST:
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and prev.value > node.value:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(tree)

    if first and second:
        first.value, second.value = second.value, first.value
    return tree

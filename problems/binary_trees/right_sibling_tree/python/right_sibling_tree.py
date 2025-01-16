class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helper(node: BinaryTree, parent: BinaryTree, isLeft: bool) -> None:
    if node is None:
        return

    left = node.left
    right = node.right

    helper(left, node, True)
    if parent is None:
        node.right = None
    elif isLeft:
        node.right = parent.right
    else:
        node.right = parent.right.left if parent.right and parent.right.left else None
    helper(right, node, False)


def rightSiblingTree(root: BinaryTree) -> BinaryTree:
    helper(root, None, False)
    return root

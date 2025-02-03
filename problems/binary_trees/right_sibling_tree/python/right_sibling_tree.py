from problems.binary_trees.assets.BinaryTree import BinaryTree


def rightSiblingTree(root: BinaryTree) -> BinaryTree:

    def helper(
        node: BinaryTree, parent: BinaryTree = None, isLeft: bool = False
    ) -> None:
        if not node:
            return

        left = node.left
        right = node.right
        helper(left, node, True)

        if not parent:
            node.right = None
        elif isLeft:
            node.right = parent.right
        else:
            node.right = (
                parent.right.left if parent.right and parent.right.left else None
            )
        helper(right, node, False)

    helper(root)
    return root

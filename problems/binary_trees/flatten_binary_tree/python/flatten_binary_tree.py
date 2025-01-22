from problems.binary_trees.assets.BinaryTree import BinaryTree


def flattenInOrder(node: BinaryTree, state: dict) -> None:
    if node is None:
        return

    # traverse the left subtree
    flattenInOrder(node.left, state)

    # link the previous node with the current node
    if state["prev"] is not None:
        state["prev"].right = node
        node.left = state["prev"]

    state["prev"] = node  # update the previous node
    # traverse the right subtree
    flattenInOrder(node.right, state)


def flattenBinaryTree(root: BinaryTree) -> BinaryTree:
    state: dict = {"prev": None}  # shared state as a dictionary
    flattenInOrder(root, state)

    # fint the leftmost node
    leftMost = root
    while leftMost.left is not None:
        leftMost = leftMost.left

    return leftMost

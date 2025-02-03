from problems.binary_trees.assets.BinaryTree import BinaryTree


def flattenBinaryTree(root: BinaryTree) -> BinaryTree:

    def flattenInOrder(node: BinaryTree, state: dict) -> None:
        if not node:
            return

        flattenInOrder(node.left, state)

        if not state["head"]:
            state["head"] = node

        if state["prev"]:
            state["prev"].right = node
            node.left = state["prev"]

        state["prev"] = node

        flattenInOrder(node.right, state)

    state: dict = {"prev": None, "head": None}
    flattenInOrder(root, state)

    return state["head"]

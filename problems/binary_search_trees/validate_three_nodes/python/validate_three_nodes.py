from problems.binary_search_trees.assets.BST import BST


def validateThreeNodes(nodeOne: BST, nodeTwo: BST, nodeThree: BST) -> bool:

    def is_ancestor(ancestor: BST, node: BST) -> bool:
        if ancestor is None:
            return False
        if ancestor == node:
            return True
        nextNode = ancestor.left if node.value < ancestor.value else ancestor.right
        return is_ancestor(nextNode, node)

    isNodeOneAncestorOfTwo: bool = is_ancestor(nodeOne, nodeTwo)
    isNodeThreeAncestorOfTwo: bool = is_ancestor(nodeThree, nodeTwo)

    if not (isNodeOneAncestorOfTwo or isNodeThreeAncestorOfTwo):
        return False

    nextPair: tuple[BST, BST] = (
        (nodeTwo, nodeThree) if isNodeOneAncestorOfTwo else (nodeTwo, nodeOne)
    )

    return is_ancestor(*nextPair)

from problems.binary_search_trees.assets.BST import BST


def validateThreeNodes(nodeOne: BST, nodeTwo: BST, nodeThree: BST) -> bool:

    def is_ancestor(ancestor: BST, node: BST) -> bool:
        if ancestor is None:
            return False
        if ancestor == node:
            return True
        nextNode = ancestor.left if node.value < ancestor.value else ancestor.right
        return is_ancestor(nextNode, node)

    def is_descendant(node: BST, descendant: BST) -> bool:
        return is_ancestor(node, descendant)

    isNodeOneAncestorOfTwo = is_ancestor(nodeOne, nodeTwo)
    isNodeThreeAncestorOfTwo = is_ancestor(nodeThree, nodeTwo)

    if isNodeOneAncestorOfTwo:
        return is_descendant(nodeTwo, nodeThree)
    elif isNodeThreeAncestorOfTwo:
        return is_descendant(nodeTwo, nodeOne)
    return False

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def add_as_ancestor(self, descendants: list) -> None:
        for descendant in descendants:
            descendant.ancestor = self


def getYoungestCommonAncestor(
    topAncestor: AncestralTree,
    descendantOne: AncestralTree,
    descendantTwo: AncestralTree,
) -> AncestralTree:

    def get_depth(node: AncestralTree, topAncestor: AncestralTree) -> int:
        depth = 0
        while node != topAncestor:
            depth += 1
            node = node.ancestor
        return depth

    def backtrack_ancestor(
        node: AncestralTree, currentDepth: int, targetDepth: int
    ) -> AncestralTree:
        while currentDepth > targetDepth:
            node = node.ancestor
            currentDepth -= 1
        return node

    depthOne: int = get_depth(descendantOne, topAncestor)
    depthTwo: int = get_depth(descendantTwo, topAncestor)

    descendantOne = backtrack_ancestor(descendantOne, depthOne, depthTwo)
    descendantTwo = backtrack_ancestor(descendantTwo, depthTwo, depthOne)

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne

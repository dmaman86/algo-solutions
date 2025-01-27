from problems.binary_trees.assets.BinaryTree import BinaryTree


def maxPathSumHelper(
    node: BinaryTree, globalMax: dict[str, float], globalPath: list[BinaryTree]
) -> tuple[int, list[BinaryTree]]:
    if not node:
        return 0, []

    leftMax, leftPath = maxPathSumHelper(node.left, globalMax, globalPath)
    leftMax = max(leftMax, 0)

    rightMax, rightPath = maxPathSumHelper(node.right, globalMax, globalPath)
    rightMax = max(rightMax, 0)

    localMax = node.value + leftMax + rightMax

    if localMax > globalMax["max"]:
        globalMax["max"] = localMax
        globalPath.clear()
        if leftMax > 0:
            globalPath.extend(leftPath)
        globalPath.append(node)
        if rightMax > 0:
            globalPath.extend(rightPath[::-1])

    if leftMax > rightMax:
        return node.value + leftMax, leftPath + [node]
    else:
        return node.value + rightMax, rightPath + [node]


def maxPathSum(tree: BinaryTree) -> tuple[int, list[BinaryTree]]:
    globalMax = {"max": float("-inf")}
    globalPath: list[BinaryTree] = []
    maxPathSumHelper(tree, globalMax, globalPath)
    return globalMax["max"], globalPath

from problems.binary_trees.assets.BinaryTree import BinaryTree


def maxPathSum(tree: BinaryTree) -> tuple[int, list[BinaryTree]]:
    result: dict = {"max_sum": float("-inf"), "max_path": []}

    def max_gain(node: BinaryTree) -> int:
        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        current_path_sum = node.value + left_gain + right_gain

        if current_path_sum > result["max_sum"]:
            result["max_sum"] = current_path_sum
            result["max_path"] = (
                get_path(node.left, left_gain)
                + [node]
                + get_path(node.right, right_gain)
            )

        return node.value + max(left_gain, right_gain)

    def get_path(node: BinaryTree, gain: int) -> list[BinaryTree]:
        if not node or gain == 0:
            return []
        return [node] + get_path(
            (node.left if max_gain(node.left) > max_gain(node.right) else node.right),
            gain - node.value,
        )

    max_gain(tree)
    return result["max_sum"], result["max_path"]

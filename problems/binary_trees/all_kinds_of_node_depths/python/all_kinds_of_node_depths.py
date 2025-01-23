from problems.binary_trees.assets.BinaryTree import BinaryTree


def allKindsOfNodeDepths(root: BinaryTree) -> int:
    result = 0

    def preorderTraversal(node: BinaryTree) -> dict:
        nonlocal result
        if node is None:
            return {"depth_sum": 0, "size": 0}  # base case for null nodes

        left = preorderTraversal(node.left)
        right = preorderTraversal(node.right)

        # calculate depth sum and size for the current node
        depth_sum = left["depth_sum"] + right["depth_sum"]
        size = left["size"] + right["size"] + 1

        # update the global result with the depth sum for this subtree
        result += depth_sum

        # return the depth sum including the current node and its size
        return {"depth_sum": depth_sum + size, "size": size}

    preorderTraversal(root)
    return result

class Node:
    """BST Node that keeps track of the number of elements in the left subtree."""

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.left_size = 0  # Keeps track of the number of nodes in the left subtree.


class BST:
    """BST that efficiently tracks the number of elements smaller than given value."""

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> int:
        """Inserts a value into the BST and returns the count of smaller elements to its right."""
        if self.root is None:
            self.root = Node(value)
            return 0
        return self._insert(self.root, value)

    def _insert(self, node: Node, value: int) -> int:
        """Recursive function to insert a node and compute the count of smaller elements."""
        if value <= node.value:
            node.left_size += 1
            if node.left is None:
                node.left = Node(value)
                return 0
            return self._insert(node.left, value)
        else:
            right_count = node.left_size + 1
            if node.right is None:
                node.right = Node(value)
                return right_count
            return right_count + self._insert(node.right, value)


def right_smaller_than(array: list[int]) -> tuple[list[int], BST]:
    """Computes how many numbers are smaller to the right for each element in the array."""
    bst = BST()
    result: list[int] = []

    # traverse the array in reverse order
    for value in reversed(array):
        count = bst.insert(value)
        result.append(count)

    # reverse result to match original order
    return result[::-1], bst

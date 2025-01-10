class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_size = 0


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return 0
        return self._insert(self.root, value)

    def _insert(self, node, value):
        if value <= node.value:
            node.left_size += 1
            if node.left is None:
                node.left = Node(value)
                return 0
            else:
                return self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return node.left_size + 1
            else:
                return node.left_size + 1 + self._insert(node.right, value)


def right_smaller_than(array: list[int]) -> tuple[list[int], BST]:
    bst = BST()
    result: list[int] = []

    for value in reversed(array):
        count = bst.insert(value)
        result.append(count)

    return result[::-1], bst

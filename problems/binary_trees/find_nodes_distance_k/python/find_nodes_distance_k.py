from problems.binary_trees.assets.BinaryTree import BinaryTree


def findNodesDistanceK(tree: BinaryTree, target: int, k: int) -> list[int]:

    def find_parents(
        node: BinaryTree, parent_map: dict = None, parent: BinaryTree = None
    ) -> dict[BinaryTree, BinaryTree]:
        if not parent_map:
            parent_map = {}

        if not node:
            return parent_map

        parent_map[node] = parent
        find_parents(node.left, parent_map, node)
        find_parents(node.right, parent_map, node)
        return parent_map

    def find_target(node: BinaryTree, target_value: int) -> BinaryTree:
        if not node:
            return None
        if node.value == target_value:
            return node

        left_result = find_target(node.left, target_value)
        if left_result:
            return left_result
        return find_target(node.right, target_value)

    if not tree or k < 0:
        return []

    parent_map = find_parents(tree)

    target_node = find_target(tree, target)
    if not target_node:
        return []

    visited = set()
    queue = [(target_node, 0)]
    visited.add(target_node)

    result = []

    while queue:
        current_node, current_distance = queue.pop(0)

        if current_distance == k:
            result.append(current_node.value)

        def add_to_queue(node: BinaryTree) -> None:
            if node and node not in visited:
                visited.add(node)
                queue.append((node, current_distance + 1))

        add_to_queue(current_node.left)
        add_to_queue(current_node.right)
        add_to_queue(parent_map.get(current_node))

    return result

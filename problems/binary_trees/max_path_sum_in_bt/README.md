# Max Path Sum In Binary Tree

Write a function that takes in a Binary Tree and returns its max path sum.

A path is a collection of connected nodes in a tree, where no node is connected
to more than two other nodes; a path sum is the sum of the values of the nodes
in a particular path.

Each `BinaryTree` node has an integer `value`, a `left` child node, and a `right`
child node. Children nodes can either be `BinaryTree` nodes themselves or `None` /
`null`.

### Sample Input

```python
tree =           1
              /     \
            2         3
          /   \     /   \
         4     5   6     7
```

### Sample Output

```python
18  # 5 + 2 + 1 + 3 + 7
```

### Optimal Space & Time Complexity

`O(n) time | O(log(n)) space` - where `n` is the number of nodes in the Binary Tree.

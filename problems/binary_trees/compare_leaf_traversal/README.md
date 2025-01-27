# Compare Leaf Traversal

Write a function that takes in the root nodes of two Binary Trees
and returns a boolean representing whether their leaf traversals
are the same.

The leaf traversal of Binary Tree traverses only its leaf nodes from
left to right. A leaf node is any node that has no `left` or `right`
children.

For example, the leaf traversal of the following Binary Tree is `1, 2, 3`.

```
       4
      / \
     1   5
        / \
        3  2
```

Each `BinaryTree` node has an integer `value`, a `left` child node, and a
`right` child node. Children nodes can either be `BinaryTree` nodes
themselves or `None` / `null`.

### Sample Input

```python
tree1 =
       1
      / \
     2   3
    / \   \
   4  5    6
     / \
    7   8

tree2 =
       1
      / \
     2   3
    / \   \
   4   7   5
          / \
         8   6

```

### Sample Output

```python
true
```

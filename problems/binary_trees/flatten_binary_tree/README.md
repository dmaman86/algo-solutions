# Flatten Binary Tree

Write a function that takes in a Binary Tree, flattens it, and returns its leftmost node.

A flattened Binary Tree is a structure that's nearly identical to a Doubly Linked List
(except that nodes have `left` and `right` pointers instead of `prev` and `next` pointers),
where nodes follow the original tree's left-to-right order.

Note that if the input Binary Tree happens to be valid Binary Tree, the nodes in the
flattened tree will be sorted.

The flattening should be done in place, meaning that the original data structure should
be mutated (no new structure should be created).

Each `BinaryTree` node has an integer `value`, a `left` child node, and a `right` child node.
Children nodes can either be `BinaryTree` nodes themselves or `None` / `null`.

### Sample Input

```python
tree =
        1
      /   \
     2     3
    / \   /
   4   5 6
      / \
     7   8
```

### Sample Output

```
4 <-> 2 <-> 7 <-> 5 <-> 8 <-> 1 <-> 6 <-> 3 // the leftmost node with value 4
```

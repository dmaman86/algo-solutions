#All kinds Of Node Depths

The distance between a node in a Binary Tree and tree's root is called
the node's depth.

Write a function that takes in a Binary Tree and returns the sum of all
of its subtrees' nodes' depths.

Each `BinaryTree` node has an integer `value`, a `left` child node, and
a `right` child node. Children nodes can either be `BinaryTree` nodes
themselves or `None` / `null`.

### Sample Input

```python
tree =      1
        /       \
       2         3
     /   \     /   \
    4     5   6     7
  /   \
 8     9
```

### Sample Output

```
26
// The sum of the root tree's node depths is 16.
// The sum of the tree rooted at 2's node depths is 6.
// The sum of the tree rooted at 3's node depths is 2.
// The sum of the tree rooted at 4's node depths is 2.
// Summing all of these sums yields 26.
```

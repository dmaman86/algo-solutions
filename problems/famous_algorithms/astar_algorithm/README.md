# A<sup>\*</sup> Algorithm

Your're given a two-dimensional array containing `0`s and `1`s, where each `0` represents a free space and each `1` represents an obstacle (a space that cannot be passed through). You can think of this array as a grid-shaped graph. You're also given four integers `startRow`, `startCol`, `endRow`, and `endCol`, representing the positions of a start node and an end node in the graph.

Write a function that finds the shortest path between the start node and the end node using the A<sup>\*</sup> search algorithm and returns it.

The shortest path should be returned as an array of node positions, where each node position is an array of two elements; the `[row, col]` of the respective node in the graph. The output array should contain the start node's position, the end node's position, and all of the positions of the remaining nodes in the shortest path, and these node positions should be ordered from start node to end node.

If there is no path from the start node to the end node, your function should return an empty array.

Note that:

- From each node in the graph, you can only travel in four directions; up, left, down and right; you can't travel diagonally.
- The distance between all neighboring nodes in the graph is the same; you can treat it as a distance of 1.
- The start node and end node are guaranteed to be located in empty spaces (cells containing `0`).
- The start node and end node will never be out of bounds and will never overlap.
- There will be at most one shortest path from the start node to the end node.

### Sample Input

```python
startRow = 0
startCol = 1
endRow = 4
endCol = 3
graph = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0]
]
```

### Sample Output

```python
[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

# The shortest path can be clearly seen here:
# [
#    [., ., 0, 0, 0],
#    [., 1, 1, 1, 0],
#    [., ., 0, 0, 0],
#    [1, ., 1, 1, 1],
#    [0, ., ., ., 0],
# ]
```

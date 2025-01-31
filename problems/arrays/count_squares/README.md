# Count Squares

Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and
returns the number of squares that can be formed by these coordinates.

A square must have four corners amongst the coordinates in order to be counted. A single
coordinate can be used as a corner for multiple different squares.

You can also assume that no coordinate will be farther than 100 units from the origin.

### Sample Input

```python
points = [
  [1, 1],
  [0, 0],
  [-4, 2],
  [-2, -1],
  [0, 1],
  [1, 0],
  [-1, 4]
]
```

### Sample Output

```python
    # [1, 1], [0, 0], [0, 1], and [1, 0] makes a square
2   # as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]
```

### Optimal Space & Time Complexity

`O(n^2) time | O(n) space` - where `n` is the number of points

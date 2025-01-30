# Line Through Points

You're given an array of points plotted on a 2D graph (the xy-plane). Write a function that returns
the maximum number of points that a single line (or potentially multiple lines) on the graph passes
through.

The input array will contain points represented by an array of two integers `[x, y]`. The input array
will never contain duplicate points and will always contain at least one point.

### Sample Input

```python
points = [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1]
]
```

### Sample Output

```python
4   # A line passes through points: [-2, 6], [0, 4], [2, 2], [4, 0].
```

### Optimal Space & Time Complexity

`O(n^2) time | O(n) space` - where `n` is the number of points

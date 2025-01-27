# Maximum Sum Submatrix

You're given a two-dimensional array (a matrix) of potentially unequal height and width
that's filled with integers. You're also given a positive integer `size`. Write a function
that returns the maximum sum that can be generated from a submatrix with dimensions `size * size`.

For example, consider the following matrix:

```
[
  [2, 4],
  [5, 6],
  [-3, 2],
]
```

If `size = 2`, then the 2x2 submatrices to consider are:

```
[2, 4]
[5, 6]
--------
[5, 6]
[-3, 2]
```

The sum of the elements in the first submatrix is `17`, and the sum of the elements in the
second submatrix is `10`. In this example, your function should return `17`.

Node: `size` will always be at least `1`, and the dimensions of the input `matrix` will
always be at least `size * size`.

### Sample Input

```python
matrix =
[
  [5, 3, -1, 5],
  [-7, 3, 7, 4],
  [12, 8, 0, 0],
  [1, -8, -8, 2],
]
size = 2
```

### Sample Output

```python
18

# [
#  [., ., ., .],
#  [., 3, 7, .],
#  [., 8, 0, .],
#  [., ., ., .],
# ]
```

### Optimal Space & Time Complexity

`O(w * h) time | O(w * h) space` - where w is the width of the matrix and h is the height.

# Zigzag Traverse

Write a function that takes in an n x m two-dimensional array (that can be
square-shaped when n == m) and returns a one-dimensional array of all
the array's elements in zigzag order.

Zigzag order starts at the top left corner of the two-dimensional array, goes
down by one element, and proceeds in a zigzag pattern all the way to the bottom
right corner.

### Sample Input

```python
array = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16],
]
```

### Sample Output

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

### Optimal Space & Time Complexity

`O(n) time | O(n) space` - where `n` is the total number of elements
in the two-dimensional array.

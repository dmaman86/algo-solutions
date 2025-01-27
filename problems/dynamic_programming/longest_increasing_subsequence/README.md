# Longest Increasing Subsequence

Given a non-empty array of integers, write a function that returns the longest
strictly-increasing subsequence of the array.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`,
and so do the numbers `[2, 4]`. Note that a single number in an array and the
array itself are both valid subsequences of the array.

You can assume that there will only be one longest increasing subsequence.

### Sample Input

```python
array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
```

### Sample Output

```python
[-24, 2, 3, 5, 6, 35]
```

### Optimal Space & Time Complexity

`O(nlogn) time | O(n) space` - where `n` is the length of the input array

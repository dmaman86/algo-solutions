# Apartment Hunting

You're looking to move into a new apartment on specific street, and you're given a list of
contiguous blocks on that street where each block contains an apartment that you could move into.

You also have a list of requirements: a lost of buildings that are important to you. For instance,
you might value having a school and a gym near your apartment. The list of blocks that you have
contains information at every block about all of the buildings that are present and absent at the block
in question. For instance, for every block, you might know whether a school, a pool, an office, and a gym
are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the
farthest distance you'd have to walk to reach all of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your
required buildings and returns the location (the index) of the block that is most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.

### Sample Input

```python
blocks = [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  }
]
reqs = ["gym", "school", "store"]
```

### Sample Output

```python
3   # at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther
```

### Optimal Space & Time Complexity

`O(br) time | O(br) space` - where `b` is the number of blocks and `r` is the number of requirements

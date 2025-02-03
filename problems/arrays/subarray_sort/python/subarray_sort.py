def subarray_sort(array: list[int]) -> list[int]:
    """Finds the smallest subarray that need to be sorted for the entire array to be sorted."""
    if len(array) <= 1:
        return [-1, -1]

    def find_boundary(init: int, condition: callable, step: int):
        """Finds the boundary index where the condition stops being true."""
        while condition(init):
            init += step
        return init

    # Find first out-of-order element from the left
    left: int = find_boundary(
        0,
        lambda i: i < len(array) - 1 and array[i] <= array[i + 1],
        1,
    )

    # If no disorder is found, the array is already sorted
    if left == len(array) - 1:
        return [-1, -1]

    # Find first out-of-order element from the right
    right: int = find_boundary(
        len(array) - 1,
        lambda i: i > 0 and array[i] >= array[i - 1],
        -1,
    )

    # Find the min and max in the unordered subarray
    subarray: list[int] = array[left : right + 1]
    min_val: int = min(subarray)
    max_val: int = max(subarray)

    # Expand left boundary
    left = find_boundary(left, lambda i: i > 0 and array[i - 1] > min_val, -1)

    # Expand right boundary
    right = find_boundary(
        right,
        lambda i: i < len(array) - 1 and array[i + 1] < max_val,
        1,
    )

    return [left, right]

def find_boundary(array: list[int], init: int, condition: callable, step: int):
    index: int = init
    while condition(index, array):
        index += step
    return index


def subarray_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return [-1, -1]

    left: int = find_boundary(
        array,
        0,
        lambda index, arr: index < len(arr) - 1 and arr[index] <= arr[index + 1],
        1,
    )

    if left == len(array) - 1:
        return [-1, -1]

    right: int = find_boundary(
        array,
        len(array) - 1,
        lambda index, arr: index > 0 and arr[index] >= arr[index - 1],
        -1,
    )

    subarray: list[int] = array[left : right + 1]
    min_val: int = min(subarray)
    max_val: int = max(subarray)

    left = find_boundary(
        array, left, lambda index, arr: index > 0 and arr[index - 1] > min_val, -1
    )
    right = find_boundary(
        array,
        right,
        lambda index, arr: index < len(arr) - 1 and arr[index + 1] < max_val,
        1,
    )

    return [left, right]

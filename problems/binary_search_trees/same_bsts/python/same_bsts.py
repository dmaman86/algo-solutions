def get_children(array: list[int]) -> tuple[list[int], list[int]]:
    smaller: list[int] = []
    greater_or_equal: list[int] = []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
        else:
            greater_or_equal.append(array[i])

    return smaller, greater_or_equal


def sameBsts(arrayOne: list[int], arrayTwo: list[int]) -> bool:
    if not len(arrayOne) and not len(arrayTwo):
        return True

    if (len(arrayOne) != len(arrayTwo)) or (arrayOne[0] != arrayTwo[0]):
        return False

    left_one, right_one = get_children(arrayOne)
    left_two, right_two = get_children(arrayTwo)

    return sameBsts(left_one, left_two) and sameBsts(right_one, right_two)
